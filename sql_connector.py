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


output = conn.execute(Ars_Goetia_demons.select()).fetchall()
print(output)
