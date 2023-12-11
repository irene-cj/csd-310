from datetime import datetime

from mysql.connector import errorcode
import mysql.connector.conversion

config = {
    "user": "bacchusWinery",
    "password": "password",
    "host": "127.0.0.1",
    "database": "bacchus",
    "raise_on_warnings": True
}
try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    print("\n Database user {} connected to MySQL on host "
          "{} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n Press any key to continue...")

    cursor.execute("SELECT suppliers.name, expected_date, actual_date, "
                   "IF(actual_date = expected_date, 'Yes', 'No'), actual_date - expected_date  "
                   "from shipments "
                   "join suppliers on suppliers.suppliers_id = shipments.supplier_id "
                   "where week(expected_date) < week(actual_date)")
    rows = cursor.fetchall()

    fieldNameArray = ['Name', 'Expected Date', 'Actual Date', 'On Time', "Late By"]
    now = datetime.now()
    print("\n --Late Shipment's Report ran on {}--".format(now.ctime()))

    for row in rows:
        entryArray = []
        for entry in row:
            entryArray.append(entry)
        i = 0
        print(" ")
        for entry in entryArray:
            if i == 4:
                print(fieldNameArray[i] + ": " + str(entry) + " days")
            else:
                print(fieldNameArray[i] + ": " + str(entry))
            i += 1

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password is invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)
finally:
    db.close()
