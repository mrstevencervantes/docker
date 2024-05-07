import sqlalchemy
from faker import Faker

fake = Faker(['en_US', 'en_GB', 'en_CA', 'es_MX'])

users = []

for _ in range(5):
    users.append({'first_name': fake.first_name(), 'last_name': fake.last_name(), 'email': fake.free_email()})

engine = sqlalchemy.create_engine('sqlite:///users.db', echo=True)

metadata = sqlalchemy.MetaData()

users_table = sqlalchemy.Table("users_v3", metadata,
                                sqlalchemy.Column("user_id", sqlalchemy.Integer, primary_key=True),
                                sqlalchemy.Column("first_name", sqlalchemy.String),
                                sqlalchemy.Column("last_name", sqlalchemy.String),
                                sqlalchemy.Column("email", sqlalchemy.String)
                            )

metadata.create_all(engine)

with engine.connect() as conn:
    conn.execute(sqlalchemy.insert(users_table).values(users))
    for row in conn.execute(sqlalchemy.select(users_table)):
        print(row)
    conn.commit()
    