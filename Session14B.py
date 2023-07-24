import mysql.connector as db


class DBHelper:

    def __init__(self):
        self.connection = db.connect(user='root',
                                     password='12345678',
                                     host='127.0.0.1',
                                     database='gwpds')

        self.cursor = self.connection.cursor()

        print("[DBHelper] Connection Created and cursor obtained")

    def execute_sql(self, sql):
        print("[DBHelper] Executing SQL", sql)

        self.cursor.execute(sql)
        self.connection.commit()
        print("[DBHelper] SQL Statement executed")
