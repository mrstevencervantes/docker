import sqlite3

conn = sqlite3.connect('movies.db')

cursor = conn.cursor()

# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS Movies (Title TEXT, Director TEXT, Year INT);'''
#             )

# cursor.execute('''INSERT INTO Movies VALUES('Aliens', 'Scott Ripley', 1986);''')
# cursor.execute('''INSERT INTO Movies (Title, Director, Year) VALUES (?,?,?);''', ("God Father", "Martin Scoresce", 1972))

# famous_movies = [("Nightmare Before Christmas", "Tim Burton", 1993),
    #                 ("The Cat in the Hat", "David Green", 2000),
    #                 ("The Lion King", "William Green", 2000)
#                 ]
# cursor.executemany('''INSERT INTO Movies (Title, Director, Year) VALUES (?,?,?);''', famous_movies)
# cursor.execute('''SELECT * FROM Movies;''')

release_year = (2000,)
cursor.execute('''SELECT * FROM Movies WHERE Year =?;''', release_year)

# print(cursor.fetchone())
# print(cursor.fetchall())
for row in cursor.fetchmany(size=5):
    print(row)

conn.commit()
conn.close()