import sqlalchemy
from faker import Faker

fake = Faker(['en_US', 'en_GB', 'en_CA', 'es_MX'])

users = []

for _ in range(5):
    users.append({'first_name': fake.first_name(), 'last_name': fake.last_name(), 'email': fake.free_email()})

engine = sqlalchemy.create_engine('sqlite:///users.db', echo=True)

metadata = sqlalchemy.MetaData()

with engine.connect() as conn:
    conn.execute(sqlalchemy.text('''CREATE TABLE IF NOT EXISTS users_v2 
                                    (user_id integer primary key autoincrement,
                                    first_name text,
                                    last_name text,
                                    email text);
                                '''))

    conn.execute(sqlalchemy.text('''INSERT INTO users_v2(first_name, last_name, email) VALUES (:first_name, :last_name, :email);'''), users)

    result = conn.execute(sqlalchemy.text('''SELECT * FROM users_v2;'''))
    conn.commit()

for row in result:
    print(row)

