create database Assignment;
use Assignment;
CREATE TABLE Customer (
    customer_id INT PRIMARY KEY,  
    name VARCHAR(100),
    email VARCHAR(100),
    phone_number VARCHAR(15),
    address VARCHAR(255),
    credit_score INT
);

CREATE TABLE Loan (
    loan_id INT PRIMARY KEY,  
    customer_id INT,
    principal_amount DECIMAL(18,2),
    interest_rate DECIMAL(5,2),
    loan_term INT,  
    loan_type VARCHAR(50),
    loan_status VARCHAR(50),
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
);

CREATE TABLE HomeLoan (
    loan_id INT PRIMARY KEY,
    property_address VARCHAR(255),
    property_value DECIMAL(18,2),
    FOREIGN KEY (loan_id) REFERENCES Loan(loan_id)
);

CREATE TABLE CarLoan (
    loan_id INT PRIMARY KEY,
    car_model VARCHAR(100),
    car_value DECIMAL(18,2),
    FOREIGN KEY (loan_id) REFERENCES Loan(loan_id)
);

select * from Customer;
select * from Loan;
select * from HomeLoan;
select * from CarLoan;
