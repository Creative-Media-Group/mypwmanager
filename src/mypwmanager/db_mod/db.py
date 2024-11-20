import sqlite3


class DB:
    def __init__(self, tablename, db_url):
        self.tablename = tablename
        self.db_url = db_url
        self.con = sqlite3.connect(self.db_url)
        self.cursor = self.con.cursor()
        self.cursor.execute(
            f"""
                CREATE TABLE IF NOT EXISTS {self.tablename} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    name TEXT NOT NULL,
                    website TEXT NOT NULL,
                    password TEXT NOT NULL
                )"""
        )
        self.con.commit()

    def add_data(self, name, username, website, password):
        self.cursor.execute(
            f"INSERT INTO {self.tablename} (name, username, website, password) VALUES (?, ?, ?, ?)",
            (name, username, website, password),
        )
        self.con.commit()

    def get_all_data(self):
        self.cursor.execute(
            f"SELECT id, name, username, website, password FROM {self.tablename}"
        )
        columns = [col[0] for col in self.cursor.description]  # Spaltennamen abrufen
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def delete_user_by_id(self, user_id):
        self.cursor.execute(f"DELETE FROM {self.tablename} WHERE id = ?", (user_id,))
        self.con.commit()

    def close(self):
        self.con.close()


# Beispielverwendung
if __name__ == "__main__":
    db = DB(tablename="data", db_url="example.db")
    while True:
        data = db.get_all_data()
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
                print(data)
            if cmd == "r":
                user_id = int(input("ID des Benutzers, der gelöscht werden soll: "))
                db.delete_user_by_id(user_id)
            if cmd == "ra":
                ids = [row[0] for row in data]  # Alle IDs extrahieren
                for user_id in ids:
                    db.delete_user_by_id(user_id)
            if cmd == "e":
                db.close()
                exit()
