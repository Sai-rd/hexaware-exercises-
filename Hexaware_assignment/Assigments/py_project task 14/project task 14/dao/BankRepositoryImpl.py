import pyodbc
from dao.IBankRepository import IBankRepository
from entity.Customer import Customer
from entity.SavingsAccount import SavingsAccount
from entity.CurrentAccount import CurrentAccount
from entity.ZeroBalanceAccount import ZeroBalanceAccount
from entity.transaction import *
from exception import *

class BankRepositoryImpl(IBankRepository):
    def __init__(self):
        self.conn = self.get_db_conn()
        self.cursor = self.conn.cursor()

    def get_db_conn(self):
        try:
            # Modify with your actual database connection string
            conn_str = (
                'Driver={SQL Server};'
                'Server=Xiaomi_AG;'
                'Database=BankDB;'
                'Trusted_Connection=yes;')
            conn = pyodbc.connect(conn_str)
            return conn
        except pyodbc.DatabaseError as e:
            print(f"Error connecting to database: {e}")
            return None

    def create_account(self, customer, accType, balance, accNo=None):
        try:
            if accType.lower() == "savings":
                acc = SavingsAccount(customer, balance)
            elif accType.lower() == "current":
                acc = CurrentAccount(customer, balance)
            elif accType.lower() == "zerobalance":
                acc = ZeroBalanceAccount(customer)
            else:
                raise invalidAccountException("Invalid account type!")
            self.cursor.execute("select count(customer_id) from customers where first_name=? and last_name=?",customer.first_name,customer.last_name)
            data=self.cursor.fetchall()
            if(data[0][0]==0):
                self.cursor.execute("insert into customers values(?,?,?,?,?)",customer.first_name,customer.last_name,customer.email,customer.phone,customer.address)
                self.cursor.commit()
            self.cursor.execute("select customer_id from customers where first_name=? and last_name=?",customer.first_name,customer.last_name)
            data=int(self.cursor.fetchall()[0][0])
            customer.customer_id=data
            customer.account_number=data
            # Insert the new account into the database
            query = "INSERT INTO accounts VALUES (?, ?, ?)"
            self.cursor.execute(query, ( accType, balance, customer.customer_id))
            self.conn.commit()

            self.cursor.execute("select account_number from accounts where customer_id=?",customer.customer_id)
            data=self.cursor.fetchall()
            return acc
        except pyodbc.DatabaseError as e:
            print(f"Error creating account: {e}")
            return None

    def list_accounts(self):
        try:
            query = "SELECT * FROM accounts"
            self.cursor.execute(query)
            rows = self.cursor.fetchall()

            accounts = []
            for row in rows:
                account = self._map_account(row)
                accounts.append(account)

            return accounts
        except pyodbc.DatabaseError as e:
            print(f"Error listing accounts: {e}")
            return []

    def calculate_interest(self):
        try:
            query = "SELECT * FROM accounts WHERE account_type = 'savings'"
            self.cursor.execute(query)
            rows = self.cursor.fetchall()

            for row in rows:
                account = self._map_account(row)
                if isinstance(account, SavingsAccount):
                    account.calculate_interest()
                    # Update the balance with interest applied
                    self._update_balance(account)
        except pyodbc.DatabaseError as e:
            print(f"Error calculating interest: {e}")

    def get_account_balance(self, account_number):
        try:
            query = "SELECT balance FROM accounts WHERE account_number = ?"
            self.cursor.execute(query, (account_number,))
            result = self.cursor.fetchone()
            return int(result[0]) if result else None
        except pyodbc.DatabaseError as e:
            print(f"Error retrieving account balance: {e}")
            return None

    def deposit(self, account_number, amount):
        try:
            balance = self.get_account_balance(account_number)
            if balance is None:
                raise invalidAccountException("Account not found.")
            new_balance = int(balance) + amount
            query = "UPDATE accounts SET balance = ? WHERE account_number = ?"
            self.cursor.execute(query, (new_balance, account_number))
            self.record_transaction("Deposit",amount,datetime.datetime.now(),new_balance,account_number,"no")
            self.conn.commit()
            return new_balance
        except pyodbc.DatabaseError as e:
            print(f"Error depositing amount: {e}")
            return None

    def withdraw(self, account_number, amount):
        try:
            balance = self.get_account_balance(account_number)
            if balance is None:
                raise invalidAccountException("Account not found.")

            account = self._get_account_by_number(account_number)
            if isinstance(account, SavingsAccount):
                if balance - amount < account.min_balance:
                    raise insufficientFundException("Withdrawal exceeds minimum balance.")
            
            elif isinstance(account, CurrentAccount):
                overdraft_limit = account.OVERDRAFT_LIMIT
                if balance - amount < -overdraft_limit:
                    raise insufficientFundException("Withdrawal exceeds overdraft limit.")

            new_balance = balance - amount
            query = "UPDATE accounts SET balance = ? WHERE account_number = ?"
            self.cursor.execute(query, (new_balance, account_number))
            self.conn.commit()
            self.record_transaction("Withdraw",amount,datetime.datetime.now(),new_balance,account_number,"no")
            return new_balance
        except pyodbc.DatabaseError as e:
            print(f"Error withdrawing amount: {e}")
            return None

    def transfer(self, from_account_number, to_account_number, amount):
        try:
            from_balance = self.get_account_balance(from_account_number)
            to_balance = self.get_account_balance(to_account_number)

            if from_balance is None or to_balance is None:
                raise invalidAccountException("One or both accounts not found.")
            
            new_from_balance = from_balance - amount
            new_to_balance = to_balance + amount

            query = "UPDATE accounts SET balance = ? WHERE account_number = ?"
            self.cursor.execute(query, (new_from_balance, from_account_number))
            self.cursor.execute(query, (new_to_balance, to_account_number))
            self.record_transaction("Transfer",amount,datetime.datetime.now(),new_from_balance,from_account_number,"no")
            self.conn.commit()
            return True
        except pyodbc.DatabaseError as e:
            print(f"Error transferring amount: {e}")
            return False

    def get_account_details(self, account_number):
        try:
            query = "SELECT * FROM accounts WHERE account_number = ?"
            self.cursor.execute(query, (account_number,))
            row = self.cursor.fetchone()
            if row:
                account = self._map_account(row)
                customer = account.customer
                account_details = {
                    "customer_id": customer.customer_id,
                    "first name": customer.first_name,
                    "last name": customer.last_name,
                    "email": customer.email,
                    "phone": customer.phone,
                    "address": customer.address,
                    "account number": account.account_number,
                    "account type": account.account_type,
                    "balance": account.balance
                }
                return account_details
            else:
                raise invalidAccountException("Account not found.")
        except pyodbc.DatabaseError as e:
            print(f"Error getting account details: {e}")
            return None

    def get_transactions(self, account_number, from_date, to_date):
        try:
            query = "SELECT * FROM transactions WHERE account_number_from = ? or account_number_to = ?  AND transaction_date BETWEEN ? AND ?"
            self.cursor.execute(query, (account_number,account_number, from_date, to_date))
            rows = self.cursor.fetchall()

            transactions = []
            for row in rows:
                transaction = self._map_transaction(row)
                transactions.append(transaction)

            return transactions
        except pyodbc.DatabaseError as e:
            print(f"Error retrieving transactions: {e}")
            return []

    # Helper methods to map database rows to account and transaction objects
    def _map_account(self, row):
        account_number, account_type, balance, customer_id = row
    
        # Fetch customer details using customer_id
        self.cursor.execute("SELECT * FROM customers WHERE customer_id = ?", (customer_id,))
        cust_row = self.cursor.fetchone()
    
        if not cust_row:
            print(f"Warning: No customer found for account {account_number}")
            return None
    
        try:
            customer_id_db=cust_row[0]
            first_name=cust_row[1] 
            last_name=cust_row[2]
            email=cust_row[3]
            phone=cust_row[4]
            address=cust_row[5]
    
            # Create customer object
            customer = Customer(customer_id_db,first_name,last_name, email, phone, address)
            customer.customer_id = customer_id
            customer.account_number = account_number
    
            # Create appropriate account object
            account_type = account_type.lower()
            if account_type == "savings":
                return SavingsAccount(customer, balance)
            elif account_type == "current":
                return CurrentAccount(customer, balance)
            elif account_type == "zerobalance":
                return ZeroBalanceAccount(customer)
            else:
                print(f"Unknown account type: {account_type}")
                return None
        except Exception as e:
            print(f"Error mapping account: {e}")
            return None




    def _map_transaction(self, row):
        transaction_id, account_number, transaction_date, transaction_type, amount, balance_after, description = row
        return Transaction(
            transaction_id=transaction_id,
            account_number=account_number,
            transaction_type=transaction_type,
            amount=amount,
            balance_after=balance_after,
            transaction_date=transaction_date,
            description=description
        )


    def _get_account_by_number(self, account_number):
        query = "SELECT * FROM accounts WHERE account_number = ?"
        self.cursor.execute(query, (account_number,))
        row = self.cursor.fetchone()
        return self._map_account(row) if row else None

    def _update_balance(self, account):
        query = "UPDATE accounts SET balance = ? WHERE account_number = ?"
        self.cursor.execute(query, (account.balance, account.account_number))
        self.conn.commit()

    def record_transaction(self, transaction_type, amount,transaction_date, balance_after,account_number, description="no"):
        try:
            query = query = """
                INSERT INTO transactions (account_number, transaction_date, transaction_type, amount, balance_after, description)
                VALUES (?, ?, ?, ?, ?, ?)
            """

            self.cursor.execute(query, (account_number,transaction_date, transaction_type, amount, balance_after, description))
            self.conn.commit()
            print(f"[Transaction Logged] {transaction_type} {amount:.2f} for A/C {account_number} | Balance: {balance_after:.2f}")
        except pyodbc.DatabaseError as e:
            print(f"Failed to log transaction: {e}")

