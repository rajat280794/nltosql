import sqlite3

# Connection to sqlite3
connection = sqlite3.connect("sqlite-sakila.db")

# Create a curson to add or delete records, create table and retrieve
cursor = connection.cursor()

# Close the connection
connection.close()

