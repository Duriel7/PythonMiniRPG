import sqlite3
        
#Connection to database
def dbconnect():
    connection = sqlite3.connect('database/RPG_Database.db')
    return connection

#Cursor declaration to feed database
def dbcursor():
    connection = dbconnect()
    return connection.cursor()

#In case of error in the except block
def dberror(error):
    print("Error ", error)
    dbConnect = dbconnect()
    dbCursor = dbconnect()
    dbConnect.rollback()
    dbCursor.rollback()

#And finally close all when done
def dbclose():
    connection = dbconnect()
    cursor = dbcursor()
    connection.close()
    cursor.close()