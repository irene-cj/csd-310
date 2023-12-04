import mysql.connector

# Establishing connection to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="!Lemonpeppa05.01",
    database="movies"
)

# Creating a cursor object to execute queries
cursor = db.cursor()

# Query 1: Selecting all fields for the studio table
cursor.execute("SELECT * FROM studio")
studios = cursor.fetchall()

# Printing studio records
print("-- DISPLAYING Studio RECORDS -–")
for studio in studios:
    print(f"Studio ID: {studio[0]}\nStudio Name: {studio[1]}\n")

# Query 2: Selecting all fields for the genre table
cursor.execute("SELECT * FROM genre")
genres = cursor.fetchall()

# Printing genre records
print("-- DISPLAYING Genre RECORDS -–")
for genre in genres:
    print(f"Genre ID: {genre[0]}\nGenre Name: {genre[1]}\n")

# Query 3 Short film Records

query_3 = "SELECT film_name, film_runtime FROM film WHERE film_runtime < 120;"
cursor.execute(query_3)
short_movies = cursor.fetchall()

# Displaying Short Film Records
print("-- DISPLAYING Short Film RECORDS --")
for movie in short_movies:
    print("Film Name: {}\nRuntime: {}\n".format(movie[0], movie[1]))

# Query 4: Get a list of film names and directors ordered by director
query_4 = "SELECT film_name, film_director FROM film ORDER BY film_director;"
cursor.execute(query_4)
film_directors = cursor.fetchall()

# Displaying director records
print("-- DISPLAYING Director RECORDS in Order --")
prev_director = None
for film_dir in film_directors:
    if prev_director != film_dir[1]:
        print("Film Name: {}\nDirector: {}\n".format(film_dir[0], film_dir[1]))
    else:
        print("Film Name: {}\nDirector: {}\n".format(film_dir[0], film_dir[1]))
    prev_director = film_dir[1]


# Closing cursor and database connection
cursor.close()
db.close()
