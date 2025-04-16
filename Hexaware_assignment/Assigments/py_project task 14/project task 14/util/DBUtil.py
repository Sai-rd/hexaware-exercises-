
import pyodbc

class DBUtil():
    @staticmethod
    def getDBConn():
        try:
            connection=pyodbc.connect(
                'Driver={SQL Server};'
                'Server=Assignment;'
                'Database=BankDB;'
                'Trusted_Connection=yes;')
            #print("Connection To Database Successfull")
            return connection
        except Exception as e:
            print(f"Following Error Occured Connection to Database : \n{e}")
            return None
DBUtil().getDBConn()

