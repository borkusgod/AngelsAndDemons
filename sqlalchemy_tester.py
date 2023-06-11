# https://www.datacamp.com/tutorial/sqlalchemy-tutorial-examples
import sqlalchemy as sqa

engine = sqa.create_engine('sqlite:///datacamp.sqlite')
conn = engine.connect()
metadata = sqa.MetaData()

Student = sqa.Table('Student', metadata,
                    sqa.Column('Id', sqa.Integer(), primary_key=True),
                    sqa.Column('Name', sqa.String(255), nullable=False),
                    sqa.Column('Major', sqa.String(255), default="Math"),
                    sqa.Column('Pass', sqa.Boolean(), default=True)
                    )

metadata.create_all(engine)

query = sqa.insert(Student).values(Id=1, Name='Matthew', Major="English",
                                   Pass=True)
Result = conn.execute(query)

output = conn.execute(Student.select()).fetchall()
print(output)

# metadata = sqa.MetaData()  # extracting the metadata
# division = sqa.Table('divisions', metadata, autoload=True,
#                      autoload_with=engine)  # Table object
