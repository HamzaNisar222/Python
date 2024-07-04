# usertable.py

from db import DBconnection

database = DBconnection.Database("Users","postgres","12345","localhost","5432")
database.connect()




createtable = """
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

database.execute_query(createtable)

# Sample data for insertion (you can modify these values as per your data structure)
username = "john_doe"
email = "john.doe@example.com"

# SQL query to insert into the users table
insert_query = """
INSERT INTO users (username, email)
VALUES (%s, %s)
"""

database.execute_query(insert_query,(username,email))

user_id=1
delete_query="""
DELETE FROM users
WHERE id=%s 
"""
database.execute_query(delete_query,(user_id,))

database.fetch_results()
database.disconnect()
