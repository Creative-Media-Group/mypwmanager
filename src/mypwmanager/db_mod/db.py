from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


class DB:
    # Initialisierung der Datenbank
    def __init__(self, tablename, db_url="sqlite:///example.db"):
        self.engine = create_engine(db_url)
        self.Base = declarative_base()
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

        # Definiere die Tabelle
        class Data(self.Base):
            __tablename__ = tablename
            id = Column(Integer, primary_key=True)
            name = Column(String, nullable=False)
            website = Column(Integer, nullable=False)
            username = Column(String, nullable=False)
            password = Column(String, nullable=False)

        self.Data = Data

        # Tabelle erstellen
        self.Base.metadata.create_all(self.engine)

    # Daten einfügen
    def add_data(self, name, website, username, password):
        new_data = self.Data(
            name=name, website=website, username=username, password=password
        )
        self.session.add(new_data)
        self.session.commit()

    # Daten abrufen
    def get_all_data(self):
        return self.session.query(self.Data).all()

    # Benutzer löschen (optional)
    def delete_data_by_id(self, data_id):
        data = self.session.query(self.Data).filter_by(id=data_id).first()
        if data:
            self.session.delete(data)
            self.session.commit()


# Beispielverwendung
if __name__ == "__main__":
    db = DB(tablename="data")
    while True:
        data = db.get_all_data()
        try:
            cmd = input("a: add, l: list, r: remove, ra: remove all, e: exit: ")
            if cmd:
                if cmd == "a":
                    db.add_data(
                        name=input("Name: "),
                        username=input("Username: "),
                        password=input("Password: "),
                        website=input("Website: "),
                    )
                if cmd == "l":
                    for column in data:
                        print(
                            column.id, column.name, column.name, column.password, column.website
                        )
                if cmd == "r":
                    pass
                if cmd == "ra":
                    rang = len(data)
                    for id in range(rang):
                        db.delete_user_by_id(id)
                if cmd == "e":
                    exit()
        except:
            exit()
