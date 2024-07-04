# db/DBconnection.py

import psycopg2

class Database:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.cursor = self.connection.cursor()
            print("Database connection established.")
        except Exception as e:
            print(f"Error connecting to database: {e}")

    def disconnect(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Database connection closed.")

    def execute_query(self, query, params=None):
        try:
            if not self.connection or self.connection.closed != 0:
                self.connect()

            self.cursor.execute(query, params)
            self.connection.commit()
            print("Query executed successfully.")
        except Exception as e:
            print(f"Error executing query: {e}")
            if self.connection:
                self.connection.rollback()

    def fetch_results(self, query, params=None):
        try:
            if not self.connection or self.connection.closed != 0:
                self.connect()

            self.cursor.execute(query, params)
            results = self.cursor.fetchall()
            return results
        except Exception as e:
            print(f"Error fetching results: {e}")
            return None
