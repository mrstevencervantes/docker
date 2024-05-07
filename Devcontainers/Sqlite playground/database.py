import sqlalchemy

engine = sqlalchemy.create_engine("sqlite:///movies.db", echo=True)

# with engine.connect() as conn:
#     result = conn.execute(sqlalchemy.text('''SELECT * FROM Movies;'''))
#     for row in result:
#         print(row)

metadata = sqlalchemy.MetaData()

movies_table = sqlalchemy.Table("Movies", metadata,
    sqlalchemy.Column("Title", sqlalchemy.Text),
    sqlalchemy.Column("Director", sqlalchemy.Text),
    sqlalchemy.Column("Year", sqlalchemy.Integer),
)

metadata.create_all(engine)

with engine.connect() as conn:
    for row in conn.execute(sqlalchemy.select(movies_table)):
        print(row)
