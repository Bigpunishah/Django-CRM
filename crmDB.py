import mysql.connector

# Connect the db
database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'admin',
)

# prepare the cursor object
cursorObject = database.cursor()

#Create the DB
cursorObject.execute("CREATE DATABASE crmDB")