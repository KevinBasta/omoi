import mysql.connector
from mysql.connector import Error
import pandas as pd

def createServerConnection(hostName, userName, userPassword): 
    connection = None
    try: 
        connection = mysql.connector.connect( 
            host = hostName,
            user = userName,
            password = userPassword
        )
        print('connected to database')
    except Error as err: 
        print(f'Error: {err}')
    
    return connection

connection = createServerConnection("localhost", "root", "mysqlpass")


# creating a local database to learn sql for now. Will move to azure sql later
def createDatabase(connection, query): 
    cursor = connection.cursor()
    try: 
        cursor.execute(query)
        print('database created')
    except Error as err: 
        print(f'Error: {err}')
        
        