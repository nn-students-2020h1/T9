import sqlite3


class SqlDataBase():
    '''Set db file name\n
    Example:\n
    dataBase = SqlDataBase("dataBase.db")
    '''

    def __init__(self, fileName: str, check_thread: bool = True):
        self.dataBase = sqlite3.connect(
            fileName, check_same_thread=check_thread)
        self.cursor = self.dataBase.cursor()
        self.tables = [table[0] for table in self.cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table'").fetchall()]

    def createTable(self, tableName: str, fields: str):
        '''Create a table with your fields\n
        Example:\n
        dataBase = SqlDataBase("dataBase.db")\n
        fields = "userId integer, call text, message text, time text"\n
        # field type can be null, integer, real, text or blob only\n
        dataBase.createTable("log", fields)
        '''
        self.cursor.execute(f"""CREATE TABLE {tableName}({fields})""")

    def addRecord(self, tableName: str, data: dict):
        '''Insert the data record in the table\n
        Example:\n
        dataBase = SqlDataBase("dataBase.db")\n
        fields = "userId integer, call text, message text, time text"\n
        # field type can be null, integer, real, text or blob only\n
        dataBase.createTable("log", fields)\n
        data = {
            "userId": 123,
            "call": "history",
            "message": "/history",
            "time": "15/03/2020"
        }\n
        dataBase.addRecord("log", data)
        '''
        self.cursor.execute(f"""INSERT INTO {tableName}
        VALUES({','.join([f"'{data[key]}'" for key in data])})""")

        self.dataBase.commit()

    def getRecords(self, tableName: str, SQL: str, count: int = 0):
        '''Get records from the table\n
        Example:\n
        dataBase = SqlDataBase("dataBase.db")\n
        fields = "userId integer, call text, message text, time text"\n
        # field type can be null, integer, real, text or blob only\n
        dataBase.createTable("log", fields)\n
        data = {
            "userId": 123,
            "call": "history",
            "message": "/history",
            "time": "15/03/2020"
        }\n
        dataBase.addRecord("log", data)\n
        # Get all record from "log" table\n
        dataBase.getRecords("log")\n
        # Get 5 last records containing a "call" field equal to "help" from "log" table\n
        dataBase.getRecords("log", "SELECT * FROM log WHERE call='help' ORDER BY time DESC", 5)
        '''
        self.cursor.execute(SQL)

        if count:
            return self.cursor.fetchmany(count)
        return self.cursor.fetchall()

    def delete_all_records(self, tableName: str):
        self.cursor.execute(f"DELETE FROM {tableName}")
