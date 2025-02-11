import sqlite3

#Connection to database
def dbconnect():

    try:
        connection = sqlite3.connect('database/RPG_Database.db')
        cursor = connection.cursor()

    except Exception as error:
        print("Error ", error)
        connection.rollback()

    finally:
        connection.close()

    return connection, cursor