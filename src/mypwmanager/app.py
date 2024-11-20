import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import locale
from mylocale.TR import tr
from mypwmanager.db_mod.db import *
from mypwmanager.direction.direction import text_direction

platform = toga.platform.current_platform


class MyPWManager(toga.App):  # App
    def startup(self):
        self.paths.data.mkdir(exist_ok=True, parents=True)
        self.db_path = str(self.paths.data)
        print(self.db_path)  # create path for db
        self.db = DB(
            tablename="pwmanager",
            db_url=f"sqlite:///{self.db_path}/pw.db",
        )
        self.file = f"{self.paths.app.absolute()}/resources/localisation.csv"
        if platform == "android":
            self.lang = str(
                self._impl.native.getResources().getConfiguration().getLocales().get(0)
            ).split("_")[0]
        else:
            self.lang = locale.getlocale()[0].split("_")[0]
        self.td = text_direction(lang=self.lang, fp=self.file)
        self.main_box = toga.Box(
            children=[
                toga.ScrollContainer(
                    content=toga.Box(
                        children=[
                            toga.Label(i.name, i.username, i.password, i.website)
                            for i in self.db.get_all_data()
                        ],
                        style=Pack(alignment="center", direction="column", flex=1),
                    ),
                    vertical=True,
                    horizontal=False,
                ),
                toga.Button("New Window", on_press=self.addcontentwin),
            ],
            style=Pack(alignment="center", direction="column", flex=1),
        )

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.main_box
        self.main_window.style = COLUMN
        self.main_window.show()

    def addcontentwin(self, widget):
        newbox = toga.Box(style=Pack(direction=COLUMN, alignment="center", padding=10))
        username = toga.TextInput(placeholder="Username")
        password = toga.PasswordInput(placeholder="Password")
        website = toga.TextInput(placeholder="Username")
        backbtn = toga.Button(text="Save & Back", on_press=self.go_home)
        newbox.add(username)
        newbox.add(password)
        newbox.add(website)
        newbox.add(backbtn)
        self.main_window.content = newbox

    def go_home(self, widget):
        self.main_window.content = self.main_box


def main():
    return MyPWManager()
