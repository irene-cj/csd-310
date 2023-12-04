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
    cursor.execute("show tables")
    tables = cursor.fetchall()

    tables = str(tables).replace("(", "", -1).replace(")", "", -1) \
        .replace(",,", ",", -1).replace("'", "", -1) \
        .replace(" ", "", -1).removeprefix("[") \
        .removesuffix(",]").split(",")

    for table in tables:
        cursor.execute("select * from " + table)
        rows = cursor.fetchall()
        cursor.execute("select Column_Name from information_schema.COLUMNS where TABLE_NAME='" + table + "'")
        fieldName = cursor.fetchall()

        fieldNameArray = str(fieldName).replace("(", "", -1). \
            replace(")", "", -1).replace("'", "", -1) \
            .replace(",,", ",", -1).removeprefix("[").split(",")

        print("\n --{} Results--".format(table.replace(table[0], table[0].upper(), 1)))

        for row in rows:
            entryArray = []
            for entry in row:
                entryArray.append(entry)
            i = 0

            print(" ")
            for entry in entryArray:
                print(fieldNameArray[i].removeprefix(" ") + ":" + str(entry))
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
