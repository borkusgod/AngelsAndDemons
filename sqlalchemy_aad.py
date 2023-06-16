# https://www.datacamp.com/tutorial/sqlalchemy-tutorial-examples
import sqlalchemy as sqa

engine = sqa.create_engine('sqlite:///ars_goetia_demons.sqlite')
conn = engine.connect()
metadata = sqa.MetaData()

Ars_Goetia_demons = sqa.Table('Ars_Goetia_demons', metadata,
                              sqa.Column('Name', sqa.String(255),
                                         default="Placeholder",
                                         primary_key=True),
                              sqa.Column('Number', sqa.String(255),
                                         default="Placeholder",
                                         nullable=False),
                              sqa.Column('Type', sqa.String(255),
                                         default="Placeholder",
                                         nullable=False),
                              sqa.Column('Alt_Names', sqa.String(255),
                                         default="Placeholder",
                                         nullable=False),
                              sqa.Column('Angel_Equivalent', sqa.String(255),
                                         default="Placeholder",
                                         nullable=False)
                              )

metadata.create_all(engine)

add_sing_entry = sqa.insert(Ars_Goetia_demons).values(Name='Eligos',
                                             # Number='24',
                                             Type='Duke',
                                             Alt_Names='Eligor',
                                             Angel_Equivalent='habuiah'
                                             )
Result = conn.execute(add_sing_entry)
output = conn.execute(Ars_Goetia_demons.select()).fetchall()
print(output)

# create a function that will insert the variables into the database
