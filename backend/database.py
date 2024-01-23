import pymysql
from flask_sqlalchemy import SQLAlchemy

HOSTNAME = 'localhost'
USER = 'root'
PASSWORD = 'sql123'

#db = SQLAlchemy()
# def initDB(app):
#     return db 


#Initializing DB 
database = pymysql.connections.Connection(
    host = HOSTNAME,
    user = USER,
    password = PASSWORD
)

#Creating cursor object
cursor = database.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS users")
cursor.execute("SHOW DATABASES")



for databases in cursor:
    print(databases)


cursor.close()
database.close()