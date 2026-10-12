CREATE DATABASE IF NOT EXISTS employee_management;
USE employee_management;

CREATE TABLE IF NOT EXISTS employees (
    employee_id INT PRIMARY KEY AUTO_INCREMENT,
    employee_name VARCHAR(100) NOT NULL,
    department VARCHAR(50) NOT NULL,
    salary DECIMAL(10, 2) NOT NULL CHECK (salary >= 0)
);

INSERT INTO employees (employee_name, department, salary)
VALUES
('Ravi Kumar', 'IT', 45000.00),
('Priya Sharma', 'HR', 40000.00),
('Arjun Reddy', 'IT', 55000.00),
('Sneha Patel', 'Finance', 48000.00);

-- View all employees
SELECT * FROM employees;

-- Find employees in IT
SELECT employee_name, salary
FROM employees
WHERE department = 'IT';

-- Average salary by department
SELECT department, AVG(salary) AS average_salary
FROM employees
GROUP BY department;

-- Highest-paid employee
SELECT employee_name, department, salary
FROM employees
ORDER BY salary DESC
LIMIT 1;

-- Give IT employees a 5% raise
UPDATE employees
SET salary = salary * 1.05
WHERE department = 'IT';

SELECT * FROM employees;