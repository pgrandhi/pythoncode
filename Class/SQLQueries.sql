CREATE DATABASE employeedb;
CREATE TABLE employees(
   Id INT PRIMARY KEY auto_increment,
   FirstName VARCHAR(30) NOT NULL,
   LastName VARCHAR(30) NOT NULL,
   Age INT,
   Gender CHAR(1),
   Income FLOAT
)
