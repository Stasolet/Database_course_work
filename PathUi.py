from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QComboBox, QLineEdit, QSizePolicy

from DbWrapper import db_wrapper
from TableShower import TableShower, TableRecordAdder, TableInfoChanger

# todo  Где-то должен отображаться состав маршрута
#  также должно реализовано возможность изменения и добавления вместе с составом


class PathRecordInfoChanger(TableInfoChanger):
    def __init__(self, header, info, parent: TableShower):
        """виджеты ввода текста для станций заменяются на комбобоксы с возможностью поиска

            можно пробовать наследоваться от ViewShower с переопределение combo_update"""
        super().__init__(header, info, parent)
        self.source = "`маршрут`"
        self.combo_change_idx = {}
        for box_name in ["Станция отправления", "Станция прибытия"]:
            cell = self.cell_index[box_name]
            edit = cell.itemAt(1).widget()
            edit.disconnect()
            combo = QComboBox()
            combo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)  # это не работает todo исправить размер
            cell.addWidget(combo)
            edit.editingFinished.connect(lambda c=combo, t=edit.text: self.combo_update(c, t()))
            combo.activated[str].connect(lambda text, cell_name=box_name:
                                         self.changed_cells.__setitem__(cell_name, self.combo_change_idx[text]))

    def combo_update(self, c: QComboBox, text: str):
        if text:
            # я это ненавижу
            station_list = self.db.execute(f"""SELECT 
                                                станция.`Код станции`,
                                                регион.`Наименование региона`,
                                                `населённый пункт`.`Название пункта`,
                                                станция.`Описание`,
                                                станция.`Адрес`
                                                FROM
                                                    `населённый пункт`
                                                    JOIN
                                                        станция ON станция.`Код пункта` = `населённый пункт`.`Код пункта`
                                                    JOIN
                                                        регион ON регион.`Код региона` = `населённый пункт`.`Код региона`
                                                WHERE
                                                    `Название пункта` LIKE '%{text}%';""")
            c.clear()
            for i in station_list:
                station_info = " ".join(i[1:])
                self.combo_change_idx[station_info] = i[0]
                c.addItem(station_info)


class PathRecordAdder(PathRecordInfoChanger):

    def __init__(self, header, parent: TableShower):
        super().__init__(header=header, info=[""] * len(header), parent=parent)


class PathShower(TableShower):
    def __init__(self, parent=None):
        super().__init__("`маршрут с названиям`", ["Номер маршрута"], parent)
        self.record_editor = PathRecordInfoChanger
        self.record_adder = PathRecordAdder


class PathUi(QWidget):

    def __init__(self):
        super().__init__()

        self.slave_widgets = []
        self.show_all_btn = QPushButton("Отобразить все маршруты")
        self.station_btn = QPushButton("Станции")  # todo здесь тоже надо прикрутить комбобоксов:( на 2 виджета
        self.town_btn = QPushButton("Населённые пункты")  # можно сделать класс, который будет принимать массив для комбо
        self.region_btn = QPushButton("Регионы")

        self.show_all_btn.clicked.connect(lambda: PathShower().show())
        self.station_btn.clicked.connect(lambda: TableShower("`станция`", ["Код станции"]).show())
        self.town_btn.clicked.connect(lambda: TableShower("`населённый пункт`", ["Код пункта"]).show())
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


