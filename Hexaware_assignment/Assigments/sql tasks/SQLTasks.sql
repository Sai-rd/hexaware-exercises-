Create table customers(
Customer_id  int  primary key,
First_name  varchar(20) not null,
Last_name varchar(20),
DOB date,
Email varchar(40) not null,
Phone_number varchar(15) not null,
Address varchar(100) 
);

Create table accounts(
Account_id int primary key,
Customer_id int,
Account_type varchar(20),
Balance int,
Foreign key(customer_id) references customers(customer_id)
);

Create table transactions(
Transaction_id int primary key,
Account_id int,
Transaction_type varchar(20),
Amount int,
Transaction_date date,
Foreign key(account_id) references accounts(account_id)
);

INSERT INTO customers VALUES (1001, 'Aakash', 'Gupta', '2003-11-29', 'aakash@gmail.com', 987654321, '21, new street, ramapuram, chennai');
INSERT INTO customers VALUES (1002, 'sai', 'riteshvar', '2003-03-30', 'sai@gmail.com', 9878363728, '10, andavar nagar, villivakkam, Chennai');
INSERT INTO customers VALUES (1003, 'varshini', 'sankar', '2004-08-24', 'varshini@gmail.com', 6373828288, '23, church street, Bangalore');
INSERT INTO customers VALUES (1004, 'Priyanka', 'Mohan', '2003-10-25', 'priyankamohan@gmail.com', 8972627828, '2, st thomas mount, Chennai');
INSERT INTO customers VALUES (1005, 'Maya', 'Krishnan', '2004-12-04', 'mayakrishnan@gmail.com', 7894523567, '21, royapettah, Chennai');
INSERT INTO customers VALUES (1006, 'Abishek', 'Nirmal', '2002-08-07', 'abisheknirmal@gmail.com', 9872527167, '23, Krishna Street, Royapuram, Chennai');
INSERT INTO customers VALUES (1007, 'Vishwa', 'Vajendra', '2003-10-09', 'vishwavajendra@gmail.com', 9282982873, '12, Maya street, anna nagar, Chennai');
INSERT INTO customers VALUES (1008, 'Haniya', 'Hameed', '2004-06-11', 'haniyahameed@gmail.com', 9282782292, '16, mark antony street, besant bagar, Chennai');
INSERT INTO customers VALUES (1009, 'Viyanna', 'Koul', '2001-05-23', 'viyannakoul@gmail.com', 9832738383, '9, kumbakonam street, Chennai');
INSERT INTO customers VALUES (1010, 'Miyanna', 'Nigar', '2004-06-11', 'miyannanigar@gmail.com', 7282973897, '8, old street, T nagar, Chennai');

INSERT INTO customers (customer_id, first_name, last_name, dob, email, phone_number, address)
VALUES 
(1011, 'John', 'Doe', '1990-01-01', 'john.doe@example.com', '1234567890', '123 Main St'),
(1012, 'Jane', 'Smith', '1992-05-15', 'jane.smith@example.com', '9876543210', '456 Park Ave'),
(1013, 'Mark', 'Lee', '1985-08-20', 'mark.lee@example.com', '9991112222', '789 River Rd');

select * from customers;


INSERT INTO accounts (account_id, customer_id, account_type, balance)
VALUES 
(1240, 1011, 'Savings', 5000),
(1241, 1011, 'Checking', 3000), 
(1242, 1012, 'Savings', 4000),
(1243, 1013, 'Checking', 6000),
(1244, 1013, 'Savings', 2000);

INSERT INTO accounts VALUES (1230, 1001, 'savings', 20000);
INSERT INTO accounts VALUES (1231, 1002, 'zero_balance', 25000);
INSERT INTO accounts VALUES (1232, 1003, 'current', 30000);
INSERT INTO accounts VALUES (1233, 1004, 'savings', 35000);
INSERT INTO accounts VALUES (1234, 1005, 'zero_balance', 15000);
INSERT INTO accounts VALUES (1235, 1006, 'current', 40000);
INSERT INTO accounts VALUES (1236, 1007, 'savings', 45000);
INSERT INTO accounts VALUES (1237, 1008, 'zero_balance', 42500);
INSERT INTO accounts VALUES (1238, 1009, 'savings', 33000);
INSERT INTO accounts VALUES (1239, 1010, 'current', 37500);

INSERT INTO transactions VALUES (0034, 1230, 'deposit', 20000, '2025-03-16');
INSERT INTO transactions VALUES (0035, 1231, 'withdrawal', 15000, '2025-02-12');
INSERT INTO transactions VALUES (0036, 1232, 'transfer', 5000, '2025-01-13');
INSERT INTO transactions VALUES (0037, 1233, 'transfer', 2500, '2025-02-25');
INSERT INTO transactions VALUES (0038, 1234, 'withdrawal', 1500, '2025-01-20');
INSERT INTO transactions VALUES (0039, 1235, 'deposit', 20000, '2025-03-01');
INSERT INTO transactions VALUES (0040, 1236, 'withdrawal', 4000, '2025-03-03');
INSERT INTO transactions VALUES (0041, 1237, 'deposit', 3500, '2025-02-18');
INSERT INTO transactions VALUES (0042, 1238, 'withdrawal', 500, '2025-01-29');
INSERT INTO transactions VALUES (0043, 1239, 'deposit', 15000, '2025-02-28');


1.select c.first_name, c.last_name, a.account_type, c.email
From customers c inner join accounts a
on c.customer_id = a.customer_id ;
2. select * from transactions
Where account_id in (select account_id from accounts where customer_id=1002);

3) update accounts
Set balance=25000
Where account_id=1238;

4)select First_name + ' ' + Last_Name as FullName from customers;

5)delete from accounts 
Where balance=0 and account_type='savings';

6)select * from customers
Where address like '%chennai%';

7)select balance from accounts
Where account_id=1234;

8)select * from accounts
Where balance>1000;

9) select *
From transactions 
Where account_id = 1232;

10) select account_id, account_type, balance*1*10/100 as 'simple interest'
From accounts 
Where account_type='savings';

11) select * from accounts 
Where balance<20000;

12)select * from customers
Where address not like '%chennai%';

Task 3:
1)select avg(balance) 'average balance' from accounts;
2)select top 10 balance from accounts
Order by balance desc;

3)select sum(amount) 'sum'
From transactions 
Where transaction_type = 'deposit'
And Transaction_date = '2025-3-16';

4))select top 1 * from customers
Order by DOB desc
Select top 1 * from customers 
Order by DOB asc;

5)select t.transaction_id, t.account_id, t.transaction_type, t.amount, t.transaction_date, a.account_type
From transactions t inner join accounts a
On t.transaction_id = a.account_id;

6)select * from customers inner join accounts
On customers.customer_id = accounts.customer_id;

7) select * from customers, accounts, transactions 
Where customers.customer_id=accounts.customer_id 
And accounts.account_id = transactions.account_id;

8) select c.customer_id 
From customers c inner join accounts a
On c.customer_id = a.customer_id
Group by c.customer_id 
Having count(*)>1;

9) select a.account_id,
(select sum(amount) from transactions where transaction_type='deposit') 
- (select sum(amount) from transactions where transaction_type='withdrawal') 
As 'difference'
From accounts a;

10)select account_id, avg(balance)
From accounts
Where account_id in 
(select distinct account_id 
From transactions
Where transactions.Transaction_date between '2025-01-01' and '2025-02-01')
Group by account_id;

11)select account_type, sum(balance)
From accounts 
Group by account_type;

12) select a.account_id 
From accounts a inner join transactions t 
On a.account_id = t.account_id 
Group by a.account_id ;

13) select c.customer_id, sum(a.balance)
From customers c inner join accounts a
On c.customer_id=a.customer_id 
Group by c.customer_id
Order by sum(a.balance) desc;

14) select t.*
from transactions t
join(
select account_id,amount,transaction_date
from transactions
group by account_id,Amount,Transaction_date
having count(*)>1) dup on t.Account_id=dup.Account_id and t.Amount=dup.Amount and t.Transaction_date=dup.Transaction_date;

Task 4:
1)select c.customer_id, c.first_name, c.last_name, a.balance
From customers c inner join accounts a
On c.customer_id=a.customer_id
Where a.balance=(select max(balance) from accounts);

2)SELECT AVG(a.balance) AS 'average balance'
FROM accounts a
WHERE a.customer_id IN (
    SELECT customer_id
    FROM accounts
    GROUP BY customer_id
    HAVING COUNT(account_id) > 1
);

3)SELECT a.account_id, a.balance
FROM accounts a 
INNER JOIN transactions t ON a.account_id = t.account_id 
WHERE t.amount > (SELECT AVG(amount) FROM transactions); 

4)SELECT * FROM customers
WHERE customer_id IN (
    SELECT a.customer_id
    FROM accounts a
    LEFT JOIN transactions t ON a.account_id = t.account_id
    WHERE t.transaction_id IS NULL
);

5)SELECT account_id, balance
FROM accounts
WHERE account_id IN (
    SELECT a.account_id
    FROM accounts a
    LEFT JOIN transactions t ON a.account_id = t.account_id
    WHERE t.transaction_id IS NULL
);

6)SELECT * FROM transactions
WHERE account_id IN (
    SELECT account_id
    FROM accounts
    WHERE balance = (SELECT MIN(balance) FROM accounts)
);

7)SELECT * FROM customers
WHERE customer_id IN (
    SELECT customer_id
    FROM accounts
    GROUP BY customer_id
    HAVING COUNT(DISTINCT account_type) > 1
);

8)SELECT account_type, 
       COUNT(*) * 100.0 / (SELECT COUNT(*) FROM accounts) AS 'total_percentage'
FROM accounts
GROUP BY account_type; 

9)SELECT * FROM transactions
WHERE account_id IN (
    SELECT account_id
    FROM accounts
    WHERE customer_id = 1002
);


10)SELECT a.account_type,
SUM(a.balance) AS 'total balance'
FROM accounts a
GROUP BY a.account_type;





























