

import pyodbc
from .dbproperty import PropertyUtil 

class DBConnection:
    def __init__(self):
        self.conn_str = PropertyUtil.getpropertystring()  

    def get_connection(self):
        try:
            conn = pyodbc.connect(self.conn_str)
            return conn 
        except pyodbc.Error as e:
            print("Error connecting to database:", e)
            return None 

if __name__ == "__main__":
    dbconnection = DBConnection()
    conn = dbconnection.get_connection()
    if conn:
        print("Connected to database")
        conn.close()