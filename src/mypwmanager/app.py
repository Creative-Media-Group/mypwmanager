import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import locale
from mylocale.TR import tr
from mypwmanager.db_mod.db import *

platform = toga.platform.current_platform


class MyPWManager(toga.App):  # App
    def startup(self):
        self.db = DB(
            tablename="pwmanager", db_url=f"sqlite:///{self.paths.app.absolute()}/db/pw.db"
        )
        self.file = f"{self.paths.app.absolute()}/resources/localisation.csv"
        if platform == "android":
            self.lang = str(
                self._impl.native.getResources().getConfiguration().getLocales().get(0)
            ).split("_")[0]
        else:
            self.lang = locale.getlocale()[0].split("_")[0]
        main_box = toga.Box(children=[
            toga.ScrollContainer(content=toga.Box(children=[toga.Label("test"),toga.Label("test"),toga.Label("test"),toga.Label("test"),toga.Label("test"),toga.Label("test"),toga.Label("test"),toga.Label("test"),toga.Label("test"),toga.Label("test"),toga.Label("test"),toga.Label("test"),toga.Label("test"),toga.Label("test"),]),vertical=True,horizontal=False)
        ])

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.style = COLUMN
        self.main_window.show()


def main():
    return MyPWManager()
