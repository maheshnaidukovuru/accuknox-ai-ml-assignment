import sqlite3

conn = sqlite3.connect(':memory:')
cur = conn.cursor()

cur.execute(
    '''
    CREATE TABLE employees (
        employee_id INTEGER PRIMARY KEY,
        employee_name VARCHAR(100) NOT NULL,
        department VARCHAR(50) NOT NULL,
        salary DECIMAL(10, 2) NOT NULL CHECK (salary >= 0)
    )
    '''
)

cur.executemany(
    'INSERT INTO employees (employee_name, department, salary) VALUES (?, ?, ?)',
    [
        ('Ravi Kumar', 'IT', 45000.00),
        ('Priya Sharma', 'HR', 40000.00),
        ('Arjun Reddy', 'IT', 55000.00),
        ('Sneha Patel', 'Finance', 48000.00),
    ]
)

cur.execute('UPDATE employees SET salary = salary * 1.05 WHERE department = "IT"')

print('--- All employees ---')
for row in cur.execute('SELECT * FROM employees'):
    print(row)

print('--- IT employees ---')
for row in cur.execute("SELECT employee_name, salary FROM employees WHERE department = 'IT'"):
    print(row)

print('--- Average salary by department ---')
for row in cur.execute('SELECT department, AVG(salary) AS average_salary FROM employees GROUP BY department'):
    print(row)

print('--- Highest paid employee ---')
for row in cur.execute('SELECT employee_name, department, salary FROM employees ORDER BY salary DESC LIMIT 1'):
    print(row)

conn.close()
