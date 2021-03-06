from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout

from DbWrapper import db_wrapper
from PathShower import PathShower
from TableShower import TableShower

from ViewShower import ViewShower, ViewInfoChanger, ViewRecordAdder
from ProcedureShower import ProcedureShower

path_through_point_args = [("Станция",
                            {"src": "`станция_view`",
                             "comb_info": """CONCAT(`Населённый пункт`, ' ', `Адрес`, ' ', `Описание`)""",
                             "substitution": "`Код станции`"
                             })]

path_between_points_args = [("Первая станция",
           {"src": "`станция_view`",
               "comb_info": """CONCAT(`Населённый пункт`, ' ', `Адрес`, ' ', `Описание`)""",
               "substitution": "`Код станции`"
            }
           ),
          ("Вторая станция",
           {"src": "`станция_view`",
               "comb_info": """CONCAT(`Населённый пункт`, ' ', `Адрес`, ' ', `Описание`)""",
               "substitution": "`Код станции`"
            }
           )
          ]


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

        self.way_through_station_btn = QPushButton("Маршруты через станцию")
        self.way_between_stations_btn = QPushButton("Маршруты проходящие на участке между двумя станцями")

        self.show_all_btn.clicked.connect(lambda: PathShower().show())
        self.station_btn.clicked.connect(lambda: StationShower().show())
        self.town_btn.clicked.connect(lambda: TownShower().show())
        self.region_btn.clicked.connect(lambda: TableShower("`регион`", ["Код региона"]).show())

        self.way_through_station_btn.clicked.connect(lambda: ProcedureShower("path_through_point",
                                                                             path_through_point_args).show())
        self.way_between_stations_btn.clicked.connect(lambda: ProcedureShower("path_between_point",
                                                                              path_between_points_args).show())

        self.box = QVBoxLayout()
        self.box.addWidget(self.show_all_btn)
        self.box.addWidget(self.station_btn)
        self.box.addWidget(self.town_btn)
        self.box.addWidget(self.region_btn)
        self.box.addWidget(self.way_through_station_btn)
        self.box.addWidget(self.way_between_stations_btn)
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


