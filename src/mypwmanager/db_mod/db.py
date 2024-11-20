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
                    name TEXT NOT NULL,
                    website TEXT NOT NULL,
                    password TEXT NOT NULL
                )"""
        )
        self.con.commit()

    def add_data(self, name, website, password):
        self.cursor.execute(
            f"INSTER INTO {self.tablename} (?, ?, ?)", (name, website, password)
        )
        self.con.commit()

    def get_all_data(self):
        return self.cursor.execute(
            f"SELECT id, name, age FROM {self.tablename}"
        ).fetchall()

    def close(self):
        self.con.close()


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
                            column.id,
                            column.name,
                            column.name,
                            column.password,
                            column.website,
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
