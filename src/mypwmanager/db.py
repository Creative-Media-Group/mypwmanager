from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Datenbank und Basisklasse
engine = create_engine("sqlite:///example.db")
Base = declarative_base()
Base.metadata.create_all(engine)

# Session einrichten
Session = sessionmaker(bind=engine)
session = Session()


# Tabelle als Klasse definieren
class DB(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)


if __name__ == "__main__":
    # Daten einfügen
    new_user = DB(name="Anna", age=25)
    session.add(new_user)
    session.commit()

    # Daten abrufen
    users = session.query(DB).all()
    for user in users:
        print(user.name, user.age)
