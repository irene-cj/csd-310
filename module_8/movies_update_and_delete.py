import mysql.connector

def films(cursor, label):
    # Displaying selected fields and labels
    print(f"-- {label} --")
    query = """
    SELECT film.film_name, film.film_director, genre.genre_name, studio.studio_name
    FROM film
    JOIN genre ON film.genre_id = genre.genre_id
    JOIN studio ON film.studio_id = studio.studio_id;
    """
    cursor.execute(query)
    films = cursor.fetchall()

    for film in films:
        print(f"Film Name: {film[0]}\nDirector: {film[1]}\nGenre Name ID: {film[2]}\nStudio Name: {film[3]}\n")

# Establishing connection to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="!Lemonpeppa05.01",
    database="movies"
)

# Creating a cursor object to execute queries
cursor = db.cursor()

# Show films before the insert operation
films(cursor, "DISPLAYING FILMS")

# Insert a new record into the film table
insert_query = """
INSERT INTO film (film_name, film_director, genre_id, studio_id)
VALUES ('Alien', 'Ridley Scott', 'SciFi', '20th Century Fox');
"""
insert_query = """
INSERT INTO film (film_name, film_director, genre_id, studio_id)
VALUES ('Alien', 'Ridley Scott', 'SciFi', '20th Century Fox');
"""
insert_query = """
INSERT INTO film (film_name, film_director, genre_id, studio_id)
VALUES ('The Purge', 'James DeMonaco', 
    (SELECT genre_id FROM genre WHERE genre_name = 'Horror'), 
    (SELECT studio_id FROM studio WHERE studio_name = 'Blumhouse Productions'));
"""

db.commit()

# Show films after the insert operation
films(cursor, "DISPLAYING FILMS AFTER INSERT")

# Closing cursor and database connection
cursor.close()
db.close()



def films(cursor, label):
    # Displaying selected fields and labels
    print(f"-- {label} --")
    query = """
    SELECT film.film_name, film.film_director, genre.genre_name, studio.studio_name
    FROM film
    JOIN genre ON film.genre_id = genre.genre_id
    JOIN studio ON film.studio_id = studio.studio_id;
    """
    cursor.execute(query)
    films = cursor.fetchall()

    for film in films:
        print(f"Film Name: {film[0]}\nDirector: {film[1]}\nGenre Name ID: {film[2]}\nStudio Name: {film[3]}\n")

# Establishing connection to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="!Lemonpeppa05.01",
    database="movies"
)

# Creating a cursor object to execute queries
cursor = db.cursor()

# Show films after the update and delete operations
films(cursor, "DISPLAYING FILMS AFTER UPDATE - Changed Alien to Horror")

# Delete the movie "Gladiator"
delete_query = """
DELETE FROM film
WHERE film_name = 'Gladiator';
"""
cursor.execute(delete_query)
db.commit()

# Show films after the delete operation
films(cursor, "DISPLAYING FILMS AFTER DELETE")

# Closing cursor and database connection
cursor.close()
db.close()

