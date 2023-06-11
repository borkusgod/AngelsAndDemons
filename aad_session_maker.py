from sqlalchemy import Column, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Demon(Base):
    __tablename__ = "demons"
    name = Column("Name", String(255), primary_key=True)
    number = Column("Number", String(255), default="Placeholder",
                    nullable=False)
    type_of = Column("Type", String(255), default="Placeholder", nullable=False)
    alt_names = Column("Alt_Names", String(255), default="Placeholder",
                       nullable=False)
    ang_equiv = Column("Angel_Equivalent", String(255),
                       default="Placeholder", nullable=False)

    def __init__(self, name, number, type_of, alt_names, ang_equiv):
        self.name = name
        self.number = number
        self.type_of = type_of
        self.alt_names = alt_names
        self.ang_equiv = ang_equiv

    def __repr__(self):
        return f"({self.name} is number {self.number} of the {self.type_of} " \
               f"type. Alt names are {self.alt_names} and the equivalent " \
               f"angel is {self.ang_equiv})"


engine = create_engine("sqlite:///ars_draft2.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

demon1 = Demon("Eligos", "24", "Duke", "Eligor", "habuiah")
session.add(demon1)
session.commit()

demon2 = Demon("Kimaris", "36", "Marquis", "Cimeies", "mavakel")
session.add(demon2)
session.commit()
