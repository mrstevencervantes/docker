import sqlite3
from faker import Faker

fake = Faker(['en_US', 'en_GB', 'en_CA', 'es_MX'])

users = []

for _ in range(5):
    users.append((fake.first_name(), fake.last_name(), fake.free_email()))

conn = sqlite3.connect('users.db')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                (user_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                first_name TEXT, 
                last_name TEXT, 
                email TEXT);
            ''')

cursor.executemany('''INSERT INTO users(first_name, last_name, email) VALUES (?, ?, ?);''', users)

cursor.execute('''SELECT * FROM users;''')

print(cursor.fetchall())

conn.commit()

conn.close()