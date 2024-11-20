import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import locale
from mylocale.TR import tr
import sqlite3

platform = toga.platform.current_platform


class MyPWManager(toga.App):
    def startup(self):
        self.db = f"{self.paths.app.absolute()}/db/pw.sqlite"
        self.db_con = sqlite3.connect(self.db)
        self.cur = self.db_con.cursor()
        self.cur.execute("CREATE TABLE movie(title, uris, otp)")
        
        self.file = f"{self.paths.app.absolute()}/resources/localisation.csv"
        if platform == "android":
            self.lang = str(
                self._impl.native.getResources().getConfiguration().getLocales().get(0)
            ).split("_")[0]
        else:
            self.lang = locale.getlocale()[0].split("_")[0]
        main_box = toga.Box()

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.style = COLUMN
        self.main_window.show()


def main():
    return MyPWManager()
