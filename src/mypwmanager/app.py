import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import locale
from mylocale.TR import tr
import os


platform = toga.platform.current_platform


class MyPWManager(toga.App):
    def startup(self):
        self.db = f"{self.paths.app.absolute()}"
        #for i in os.listdir(self.app.paths.app):
        #    print(i)
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
