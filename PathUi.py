from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QComboBox, QLineEdit, QSizePolicy

from DbWrapper import db_wrapper
from TableShower import TableShower, TableRecordAdder, TableInfoChanger

from ViewShower import ViewShower, ViewInfoChanger, ViewRecordAdder

# todo  Где-то должен отображаться состав маршрута
#  также должно реализовано возможность изменения и добавления вместе с составом
#  какая-то жопная это часть, но ладно

# вывести состав маршрута
# кнопка добавления пункта
# учёт где начало где конец
# чуть накрученный push


class PathShower(ViewShower):
    def __init__(self):
        super().__init__("`маршрут_view`", ["Номер маршрута"], "`маршрут`")
        q = {"Станция отправления": ("станция_view", "*", "`Населённый пункт`", "Станция отправления"),
             "Станция прибытия": ("станция_view", "*", "`Населённый пункт`", "Станция прибытия")}
        self.record_editor = type("PathEditor", (ViewInfoChanger,), {"combo_config": q})
        self.record_adder = type("PathEditor", (ViewRecordAdder,), {"combo_config": q})


class StationShower(ViewShower):
    def __init__(self):
        super().__init__("`станция_view`", ["Код станции"], "`станция`")
        q = {"Населённый пункт":
                  ("`населённый_пункт_view`",
                   "`Код пункта`, `Название пункта`, `Наименование региона`",
                   "`Название пункта`",
                   "Код пункта")}
        self.record_editor = type("StationEditor", (ViewInfoChanger,), {"combo_config": q})
        self.record_adder = type("StationAdder", (ViewRecordAdder,), {"combo_config": q})


class TownShower(ViewShower):
    def __init__(self):
        super().__init__("`населённый_пункт_view`", ["Код пункта"], "`населённый пункт`")
        q = {"Наименование региона":
                 ("регион",
                  "`Код региона`, `Наименование региона`",
                  "`Наименование региона`",
                  "Код региона")}
        self.record_editor = type("TownEditor", (ViewInfoChanger,), {"combo_config": q})
        self.record_adder = type("TownAdder", (ViewRecordAdder,), {"combo_config": q})


class PathUi(QWidget):

    def __init__(self):
        super().__init__()

        self.slave_widgets = []
        self.show_all_btn = QPushButton("Отобразить все маршруты")
        self.station_btn = QPushButton("Станции")
        self.town_btn = QPushButton("Населённые пункты")
        self.region_btn = QPushButton("Регионы")

        self.show_all_btn.clicked.connect(lambda: PathShower().show())
        self.station_btn.clicked.connect(lambda: StationShower().show())
        self.town_btn.clicked.connect(lambda: TownShower().show())
        self.region_btn.clicked.connect(lambda: TableShower("`регион`", ["Код региона"]).show())

        self.box = QVBoxLayout()
        self.box.addWidget(self.show_all_btn)
        self.box.addWidget(self.station_btn)
        self.box.addWidget(self.town_btn)
        self.box.addWidget(self.region_btn)

        self.setLayout(self.box)

        self.show()


if __name__ == '__main__':
    db_wrapper.connect(host="localhost",
                       user="root",
                       passwd="111222333",
                       database="пассажироперевозочная",
                       use_pure=True)
    from PyQt5.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)
    w = PathUi()

    sys.exit((app.exec_()))


