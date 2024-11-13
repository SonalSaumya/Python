import sqlite3


try:
    conn = sqlite3.connect('company.db')
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS departments (departments_id INTEGER PRIMARY KEY,
    department_name TEXT NOT NULL)''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (employees_id INTEGER PRIMARY KEY,
    employee_name TEXT NOT NULL, department_id INTEGER,
    FOREIGN KEY (department_id) REFERENCES departments (department_id)''')

    cursor.execute ('CREATE INDEX IF NOT EXISTS idx_employee_name ON employees (employee_name)')
    cursor.execute ('CREATE INDEX IF NOT EXISTS idx_department_name ON departments (department_names')

    cursor.execute("INSERT INTO departments (department_name) VALUES ('Human Resourses')")
    cursor.execute("INSERT INTO departments (department_name) VALUES ('Engineering')")
    cursor.execute("INSERT INTO departments (department_name) VALUES ('Sales')")

    cursor.execute("INSERT INTO employees (employee_name, department_id) VALUES ('Mayura', 1)")
    cursor.execute("INSERT INTO employees (employee_name, department_id) VALUES ('Mayuresh', 2)")
    cursor.execute("INSERT INTO employees (employee_name, department_id) VALUES ('Sugandha', 3)")
    cursor.execute("INSERT INTO employees (employee_name, department_id) VALUES ('Srujan', 4)")

    conn.commit()
    print("Employees and their departments: ")
    cursor.execute('''SELECT employee_id, employee_name, department_id FROM employees''')
    results = cursor.fetchall()
    for row in results:
        print(row)

    print("Employees and their departments: ")
    cursor.execute('''SELECT employees.employee_name, departments.department_name FROm employees
    JOIN departments ON employees.department_id = departments.department_id
    ''')

    results = cursor.fetchall()
    for row in results:
        print(row)

except sqlite3.Error as e:
    print(f"SQLite error: {e}")


finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()


        