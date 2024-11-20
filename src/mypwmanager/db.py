from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Datenbank und Basisklasse
engine = create_engine('sqlite:///example.db')
Base = declarative_base()

# Tabelle als Klasse definieren
class DB(Base):
    __tablename__ = 'pw'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)

# Tabelle erstellen
Base.metadata.create_all(engine)

# Session einrichten
Session = sessionmaker(bind=engine)
session = Session()

# Daten einfügen
new_user = DB(name="Anna", age=25)
session.add(new_user)
session.commit()

# Daten abrufen
users = session.query(DB).all()
for user in users:
    print(user.name, user.age)