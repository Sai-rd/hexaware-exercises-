class PropertyUtil:
    @staticmethod
    def getpropertystring():
        servername='SAI\\SQLEXPRESS'
        database='Assignment'
        connstr=(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            f"Server={servername};"
            f"Database={database};"
            f"Trusted_Connection=yes;"
        )
        return connstr 