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

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\nPress any key to continue...")


    cursor.execute("SELECT wines.name, sales.quantity from sales join wines on wines.wine_id = sales.wine_id")

    rows = cursor.fetchall()

    fieldNameArray = ['Name', 'Sales Quantity', 'Results']
    now = datetime.now()
    print("\n--Wine Sales Report on {}--".format(str(now.ctime())))
    entryArray = [["Merlot", 0, ""], ["Chablis", 0, ""], ["Cabernet", 0, ""], ["Chardonnay", 0, ""]]
    for row in rows:
        for entry in entryArray:
            if row[0] == "Merlot":
                entryArray[0][1] += row[1]
            elif row[0] == "Chablis":
                entryArray[1][1] += row[1]
            elif row[0] == "Cabernet":
                entryArray[2][1] += row[1]
            elif row[0] == "Chardonnay":
                entryArray[3][1] += row[1]
    totalQuantity = 0
    for entry in entryArray:
        i = 0
        print(" ")
        totalQuantity += entry[1]
        avg = totalQuantity/4
        if entry[1] >= avg:
            entry[2] = "Selling Well"

        else:
            entry[2] = "Not Selling Well"

        for field in entry:
            print(fieldNameArray[i].removeprefix(" ") + ":" + str(field))
            i += 1
    print("\nThe Average of all wine sales is " + str(round(totalQuantity/4)))
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password is invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")

    else:
        print(err)
finally:
    db.close()
