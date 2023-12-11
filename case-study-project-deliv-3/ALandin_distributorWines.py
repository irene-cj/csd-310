from datetime import datetime
from collections import defaultdict
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

    cursor.execute("SELECT DISTINCT distributer.name, wines.name from sales "
                   "join distributer on distributer.distributer_id = sales.distributer_id "
                   "join wines on wines.wine_id = sales.wine_id")

    rows = cursor.fetchall()
    fieldNameArray = ['Name', 'Wine Name']
    now = datetime.now()
    print("\n --Distributer's Wine's Report ran on {}--".format(now.ctime()))
    
    # dictionary to identify indices of duplicates of distributors
    DistributerDuplicates = defaultdict(list)
    for i, item in enumerate(rows):
        DistributerDuplicates[item[0]].append(i)
    DistributerDuplicates = {k:v for k,v in DistributerDuplicates.items() if len(v)>1}

    for row in rows:
        if row[0] in DistributerDuplicates: # iterates through distributor with multiple wines
            entryArray = []
            for index in DistributerDuplicates[row[0]]:
                for entry in rows[index]:
                    entryArray.append(entry)
            print(" ")    
            print(fieldNameArray[0] +  ": " + row[0])    
            wines = fieldNameArray[1] + ": "
            for entry in entryArray[1::2]:
                wines = wines + entry + ", "
            print(wines[:-2])

            # removes duplicates
            for index in DistributerDuplicates[row[0]][1::]:
                rows.remove(rows[index])
                
        else:    
            entryArray = []
            for entry in row:
                entryArray.append(entry)
            i = 0
            print(" ")
            
            for entry in entryArray:
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
