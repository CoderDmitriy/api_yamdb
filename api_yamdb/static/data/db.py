import csv
import sqlite3

con = sqlite3.connect('db.sqlite3')  # change to 'sqlite:///your_filename.db'
cur = con.cursor()
cur.execute("CREATE TABLE users (username, email, role, bio, first_name, last_name);")  # use your column names here

with open('users.csv', 'r', encoding="utf8") as fin:  # `with` statement 
        available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin)  # comma is default delimiter
    to_db = [(i['username'], i['email'], i['role'], i['bio'], i['first_name'], i['last_name'],) for i in dr]

cur.executemany("INSERT INTO users (username, email, role, bio, first_name, last_name) VALUES (?, ?, ?, ?, ?, ?);", to_db)
con.commit()
con.close()

# id,username,email,role,bio,first_name,last_name