from mysql.connector import errorcode
import mysql.connector.conversion
from datetime import datetime


#Question #3: Employee time. During the last four quarters, how many hours did each employee work?
#A report on the hours each employee worked during the last four quarters.

conn = {
    "user": "bacchusWinery",
    "password": "password",
    "host": "127.0.0.1",
    "database": "bacchus",
    "raise_on_warnings": True
}
try:
    db = mysql.connector.connect(**conn)
    cursor = db.cursor()

    print("Connected...")
    input("Press any key to continue...")

    cursor.execute("SELECT  employees.employees_id, employees.f_name, employees.l_name, hours.hours from hours "
                   "join employees on employees.employees_id = hours.employee_id order by hours.employee_id")

    results = cursor.fetchall()

    employeeArray = ['Employee Id', 'Employee Name', 'Hours Worked']
    current = datetime.now()

    print(" -- Hours Worked Report --")
    print("Pulled on: {}".format(current.ctime()))
    entryArray = []
    for row in results:
        i = 0

        if len(entryArray) == 0:
            entryArray.append([row[0], row[1] + " " + row[2], row[3]])
        else:
            while i < len(entryArray):
                alreadyAdded = False
                if entryArray[i][0] == row[0]:
                    entryArray[i][2] += row[3]
                    alreadyAdded = True
                i += 1

            if not alreadyAdded:
                entryArray.append([row[0], row[1] + " " + row[2], row[3]])

    for array in entryArray:
        n = 0
        print(" ")
        for entry in array:
            print(employeeArray[n] + ": " + str(entry))
            n += 1


except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password is invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")

    else:
        print(err)
