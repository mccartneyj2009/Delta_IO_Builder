import pyodbc

class Delta_Connection():
    def __init__(self, sql_statement):
        self.dsn = 'DSN=Delta ODBC 4'
        self.autocommit = True
        self.conn = pyodbc.connect(self.dsn, autocommit=self.autocommit)
        self.cursor = self.conn.cursor()
        self.cursor.execute(sql_statement)
        self.fetched_list = self.cursor.fetchall()

    
    def close_conn_cursor(self):
        self.cursor.close()
        self.conn.close()