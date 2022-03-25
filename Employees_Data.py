import sqlite3

from prettytable import PrettyTable

connection = sqlite3.connect("employee.db")

List_of_Tables = connection.execute("Select name from sqlite_master Where type='table' And name='Employee_Details'").fetchall()

if List_of_Tables != []:

    print("Table not found!  ")

else:

    connection.execute('''Create Table Employee_Details(
                          Employee_ID Integer Primary Key Autoincrement,
                          Employee_Code,
                          Employee_Name,
                          Employee_Salary,
                          Employee_Designation
                                   
    );     ''')

    print("Table Created Successfully")

while True:
    print("Select an OPTION from the MENU: ? ")

    print("1. ADD an Employee ")
    print("2. VIEW all the Employee ")
    print("3. Exit ")

    choice = int(input("Enter any Choice to Selected ? "))

    if choice == 1:

        get_emp_code = input("Enter an Employee Code: ? ")
        get_emp_name = input("Enter an Employee Name: ? ")
        get_emp_salary = input("Enter an Employee Salary: ? ")
        get_emp_desig = input("Enter an Employee Designation: ? ")



        connection.execute("Insert into Employee_Details(Employee_Code, Employee_Name, \
        Employee_Salary, Employee_Designation) \
        Values ("+get_emp_code+", '"+get_emp_name+"', "+get_emp_salary+", \
        '"+get_emp_desig+"')")

        connection.commit()

        print("Data Inserted Successfully !!! ")


    elif choice == 2:

        result = connection.execute("Select * from Employee_Details")

        table = PrettyTable(["Employee ID", "Employee Code", "Employee Name", "Employee Salary", "Employee Designation"])

        for i in result:

            table.add_row([i[0], i[1], i[2], i[3], i[4]])

        print(table)

    elif choice == 3:

        connection.close()

        break


    else:

        print("INVALID Choice ! Please Re-Enter the CHOICE !!!")