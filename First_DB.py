from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Person(Base):
    __tablename__ = "people"
    
    ssn = Column("ssn", Integer, primary_key = True)
    firstname = Column("firstname", String)
    lastname = Column("lastname", String)
    gender = Column("gender", CHAR)
    age = Column("age", Integer)

    def __init__(self, ssn, first, last, gender, age):
        self.snn = ssn
        self.firstname = first
        self.lastname = last
        self.gender = gender
        self.age = age

    def __repr__(self):
        return f"({self.ssn}){self.firstname}{self.lastname}({self.gender},{self.age})"
    
engine = create_engine("sqlite:///mydb.db", echo = True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

p1 = Person(12312, "Mike", "Smith", "m", 35)
p2 = Person(12848, "Bob", "Roman", "m", 33)
session.add(p1)
session.add(p2)
session.commit()