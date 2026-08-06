import random, math, sys
from database_connection import *

try:

    #Database tables creation functions
    def databaseSaves():
        
        #Calling needed variables from databse connection file
        connection = dbconnect()
        cursor = dbcursor()
        
        #Create saves table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS saves(
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                characterName TEXT,
                characterLevel INTEGER,
                characterXP INTEGER
            )
        """)
        connection.commit()

    def databaseItems():
        pass

    def databaseWeapons():
        
        #Calling needed variables from databse connection file
        connection = dbconnect()
        cursor = dbcursor()
        
        #Create weapons table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS weapons(
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                weaponName TEXT,
                weaponType TEXT,
                weaponRank TEXT,
                weaponLevel INTEGER,
                weaponPrice INTEGER
            )
        """)
        connection.commit()
        
    def databaseArmors():
        
        #Calling needed variables from databse connection file
        connection = dbconnect()
        cursor = dbcursor()
        
        #Create armors table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS armors(
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                armorName TEXT,
                armorType TEXT,
                armorRank TEXT,
                armorLevel INTEGER,
                armorPrice INTEGER
            )
        """)
        connection.commit()

    def databasePotions():
        pass

    def databaseIngredients():
        pass

    def databaseMonsters():
        pass

    #Database tables update functions
    def databaseSaveCreation():
        pass

except Exception as error:
    print("Error ", error)

finally:
    pass