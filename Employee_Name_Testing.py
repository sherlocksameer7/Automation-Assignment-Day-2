import unittest

import sqlite3

class Testing_Employee_Name(unittest.TestCase):

    def setUp(self):

        self.Name = "John"
        self.Code = "1102"

        self.connection = sqlite3.connect("employee.db")


    def tearDown(self):

        self.Name = " "
        self.Code = " "

        self.connection.close()


    def test_verify_employee_name(self):

        result = self.connection.execute("Select Employee_Name from Employee_Details Where Employee_Code=" + self.Code)

        for i in result:
            fetch_employees_name = i[0]

        self.assertEqual(self.Name, fetch_employees_name)


if __name__ == "__main__":
    unittest.main()