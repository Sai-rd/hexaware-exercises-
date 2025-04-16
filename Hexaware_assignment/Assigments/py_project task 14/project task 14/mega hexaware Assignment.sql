-- Create the database
CREATE DATABASE BankDB;

USE BankDB;


CREATE TABLE customers (
    customer_id INT PRIMARY KEY IDENTITY(1,1),
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    address VARCHAR(255)
);

CREATE TABLE accounts (
    account_number BIGINT PRIMARY KEY identity(1000,1),
    account_type VARCHAR(50) NOT NULL,
    balance DECIMAL(18, 2) NOT NULL,
    customer_id INT FOREIGN KEY REFERENCES customers(customer_id),
    CONSTRAINT CHK_Account_Type CHECK (account_type IN ('Savings', 'Current', 'ZeroBalance'))
);

CREATE TABLE transactions (
    transaction_id INT PRIMARY KEY IDENTITY(1,1),
    account_number_from BIGINT NULL  FOREIGN KEY REFERENCES accounts(account_number),
	account_number_to BIGINT NULL  FOREIGN KEY REFERENCES accounts(account_number),
    transaction_date DATETIME NOT NULL DEFAULT GETDATE(),
    transaction_type VARCHAR(50) NOT NULL, -- 'Deposit', 'Withdraw', 'Transfer'
    amount DECIMAL(18, 2) NOT NULL,
    balance_after DECIMAL(18, 2) NOT NULL, -- The balance after the transaction
    description VARCHAR(255)
);

drop table transactions;

select * from customers;
select * from accounts;
select * from transactions;

update transactions set description='Nill';
use master;
drop database BankDB;
