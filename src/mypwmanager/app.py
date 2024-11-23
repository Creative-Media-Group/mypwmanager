import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import locale
from mylocale.TR import tr
from mypwmanager.db_mod.db import DB

platform = toga.platform.current_platform

#
class MyPWManager(toga.App):  # App
    def startup(self):
        self.paths.data.mkdir(exist_ok=True, parents=True)
        self.db_path = str(self.paths.data)
        print(self.db_path)  # create path for db
        self.db = DB(
            tablename="pwmanager",
            db_url=f"{self.db_path}/pw.db",
        )
        self.file = f"{self.paths.app.absolute()}/resources/localisation.csv"
        if platform == "android":
            self.lang = str(
                self._impl.native.getResources().getConfiguration().getLocales().get(0)
            ).split("_")[0]
        else:
            self.lang = locale.getlocale()[0].split("_")[0]
        # self.td = text_direction(lang=self.lang, fp=self.file)
        rows = []
        for row in self.db.get_all_data():
            rows.append(
                {
                    "icon": toga.Icon(""),
                    "title": row["name"],
                    "subtitle": row["username"],
                }
            )
        self.mylist = toga.DetailedList(
            #accessors=("name", "username",""),
            data=rows,
            style=Pack(alignment="center", direction="column", flex=1),
        )
        self.main_box = toga.Box(
            children=[
                toga.ScrollContainer(
                    content=self.mylist,
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
        newbox = toga.Box(
            style=Pack(direction="column", alignment="center", padding=10)
        )
        self.myname = toga.TextInput(placeholder="Name")
        self.username = toga.TextInput(placeholder="Username")
        self.password = toga.PasswordInput(placeholder="Password")
        self.website = toga.TextInput(placeholder="Website")
        self.backbtn = toga.Button(text="Save & Back", on_press=self.save_pw)
        newbox.add(self.myname)
        newbox.add(self.username)
        newbox.add(self.password)
        newbox.add(self.website)
        newbox.add(self.backbtn)
        self.main_window.content = newbox

    def save_pw(self, widget):
        self.db.add_data(
            name=self.myname.value,
            username=self.username.value,
            password=self.password.value,
            website=self.website.value,
        )
        self.go_home()

    def go_home(self):
        self.main_window.content = self.main_box


def main():
    return MyPWManager()
