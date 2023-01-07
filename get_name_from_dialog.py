import sqlite3

from PyQt5.QtWidgets import QInputDialog
from PyQt5.QtWidgets import QWidget


class GetName(QWidget):
    def __init__(self):
        super().__init__()
        # self.initUI()
    
    def get_name(self):
        name = ""
        ok_pressed = False
        con = sqlite3.connect("data.sqlite")
        cur = con.cursor()
        data = cur.execute("""SELECT name FROM data ORDER BY -id""").fetchone()
        while not name or not ok_pressed:
            name, ok_pressed = QInputDialog.getText(self, "Введите имя",
                                                    "Как Вас зовут?", text=data[0])
        return name
