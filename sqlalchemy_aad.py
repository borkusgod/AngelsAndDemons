# https://www.datacamp.com/tutorial/sqlalchemy-tutorial-examples
import sqlalchemy as sqa

engine = sqa.create_engine('sqlite:///ars_goetia_demons.sqlite')
conn = engine.connect()
metadata = sqa.MetaData()

Demons = sqa.Table('Ars_Goetia_demons', metadata,
                   sqa.Column('Name', sqa.String(255), primary_key=True),
                   sqa.Column('Number', sqa.String(255), nullable=False),
                   sqa.Column('Type', sqa.String(255), nullable=False),
                   sqa.Column('Alt_Names', sqa.String(255), nullable=False),
                   sqa.Column('Angel Equivalent', sqa.String(255),
                              nullable=False)
                   )

metadata.create_all(engine)

query = sqa.insert(Demons).values(Name='Eligos',
                                  Number='24',
                                  Type='Duke',
                                  Alt_Names='Eligor',
                                  Angel_Equiv='habuiah'
                                  )
Result = conn.execute(query)
output = conn.execute(Demons.select()).fetchall()
print(output)
