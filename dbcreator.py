import sqlite3


def create_database():
    # Connect to the database (or create it if it doesn't exist)
    conn = sqlite3.connect('employees.db')
    cur = conn.cursor()

    # Drop existing tables if they exist
    cur.execute('DROP TABLE IF EXISTS Employees')
    cur.execute('DROP TABLE IF EXISTS Departments')
    cur.execute('DROP TABLE IF EXISTS Locations')

    # Create the Departments table
    cur.execute('''
    CREATE TABLE Departments (
        DepartmentID INTEGER PRIMARY KEY,
        DepartmentName TEXT NOT NULL
    )
    ''')

    # Create the Locations table
    cur.execute('''
    CREATE TABLE Locations (
        LocationID INTEGER PRIMARY KEY,
        City TEXT NOT NULL
    )
    ''')

    # Create the Employees table
    cur.execute('''
    CREATE TABLE Employees (
        EmployeeID INTEGER PRIMARY KEY,
        Name TEXT NOT NULL,
        Position TEXT NOT NULL,
        Salary REAL NOT NULL,
        DepartmentID INTEGER NOT NULL,
        LocationID INTEGER NOT NULL,
        FOREIGN KEY (DepartmentID) REFERENCES Departments (DepartmentID),
        FOREIGN KEY (LocationID) REFERENCES Locations (LocationID)
    )
    ''')

    # Insert sample data into Departments table
    cur.execute("INSERT INTO Departments (DepartmentName) VALUES ('HR')")
    cur.execute("INSERT INTO Departments (DepartmentName) VALUES ('IT')")
    cur.execute("INSERT INTO Departments (DepartmentName) VALUES ('Finance')")

    # Insert sample data into Locations table
    cur.execute("INSERT INTO Locations (City) VALUES ('New York')")
    cur.execute("INSERT INTO Locations (City) VALUES ('Los Angeles')")
    cur.execute("INSERT INTO Locations (City) VALUES ('Chicago')")

    # Insert sample data into Employees table
    employees = [
        ('Alice Smith', 'HR Manager', 75000, 1, 1),
        ('Bob Johnson', 'Software Engineer', 85000, 2, 2),
        ('Carol Williams', 'Accountant', 65000, 3, 3),
        ('David Brown', 'IT Support', 55000, 2, 1),
        ('Eve Davis', 'HR Specialist', 60000, 1, 2),
        ('Frank Miller', 'Systems Analyst', 90000, 2, 3),
        ('Grace Wilson', 'Finance Analyst', 70000, 3, 1),
        ('Hank Moore', 'Software Developer', 80000, 2, 2),
        ('Ivy Taylor', 'HR Coordinator', 58000, 1, 3),
        ('Jack Anderson', 'Network Administrator', 87000, 2, 1),
        ('Katie Thomas', 'Data Scientist', 95000, 2, 2),
        ('Liam Jackson', 'Payroll Specialist', 62000, 3, 3),
        ('Mia White', 'Recruiter', 60000, 1, 1),
        ('Noah Harris', 'DevOps Engineer', 92000, 2, 3)
    ]

    cur.executemany('''
    INSERT INTO Employees (Name, Position, Salary, DepartmentID, LocationID)
    VALUES (?, ?, ?, ?, ?)
    ''', employees)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()


# Run the function to create the database and tables
create_database()
