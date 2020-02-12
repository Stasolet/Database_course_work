from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QComboBox, QLineEdit, QSizePolicy, QLabel

from ViewShower import ViewShower, ViewInfoChanger, ViewRecordAdder
# todo  Где-то должен отображаться состав маршрута
#  также должно реализовано возможность изменения и добавления вместе с составом
#  какая-то жопная это часть, но ладно

# вывести состав маршрута
# кнопка добавления пункта
# учёт где начало где конец
# чуть накрученный push

path_combo_config = {"Станция отправления": ("станция_view", "*", "`Населённый пункт`", "Станция отправления"),
                     "Станция прибытия": ("станция_view", "*", "`Населённый пункт`", "Станция прибытия")}


class PathEditor(ViewInfoChanger):
    combo_config = path_combo_config

    def __init__(self, header, info, parent: ViewShower):
        super().__init__(header, info, parent)
        self.way_layout = QVBoxLayout()
        self.path_idx = info[0]
        self.way_change_idx = {}
        self.point_positions = []

        way = self.db.execute(f"SELECT Станция, `Код станции` FROM `состав_маршрута_view` where `Номер маршрута` = {self.path_idx}")
        for pos, point in enumerate(way):
            # можно обернуть в функцию
            station_info = str(point[0])
            self.point_positions.append(pos)
            self.combo_change_idx["Станция отправления"][station_info] = point[1]
            cell = QHBoxLayout()
            edi = QLineEdit()
            edi.setText(station_info)

            add_btn = QPushButton("Добавить")
            down_btn = QPushButton("Вниз")
            up_btn = QPushButton("Вверх")

            cmb = QComboBox()
            cmb.addItem(station_info)

            up_btn.clicked.connect(lambda e, p=pos, c=cell: self.move_cell_up(c))
            down_btn.clicked.connect(lambda e, p=pos, c=cell: self.move_cell_down(c))
            add_btn.clicked.connect(lambda e, c=cell: self.add_cell(cell.pos))

            edi.editingFinished.connect(lambda c=cmb, t=edi.text:
                                        self.combo_update("Станция отправления", c, t()))  # le-kostyl
            cell.pos = pos
            cell.addWidget(edi)
            cell.addWidget(cmb)
            cell.addWidget(add_btn)
            cell.addWidget(down_btn)
            cell.addWidget(up_btn)
            self.way_layout.addLayout(cell)
        self.main_layout.addLayout(self.way_layout)

    def add_cell(self, idx: int):
        pass

    def move_cell_up(self, cell):
        if cell.pos > 0:
            old_cell = self.way_layout.itemAt(cell.pos - 1)
            self.way_layout.takeAt(cell.pos)
            self.way_layout.insertLayout(cell.pos - 1, cell)
            old_cell.pos += 1
            cell.pos -= 1

    def move_cell_down(self, cell):
        if cell.pos < self.way_layout.count() - 1:
            old_cell = self.way_layout.itemAt(cell.pos + 1)
            self.way_layout.takeAt(cell.pos)
            self.way_layout.insertLayout(cell.pos + 1, cell)
            old_cell.pos -= 1
            cell.pos += 1

    def push_all(self):
        params = []
        for i in range(self.way_layout.count()):
            cell = self.way_layout.itemAt(i)
            w = cell.itemAt(1).widget()
            station = w.currentText()
            if station:
                idx = self.combo_change_idx["Станция отправления"][station]
                params.append((self.path_idx, i, idx))

        query = f" insert into `состав маршрута` values(%s, %s, %s)"
        self.db.execute("delete from `состав маршрута` where `Номер маршрута` = %s", (self.path_idx,))
        self.db.executemany(query, params)


class PathShower(ViewShower):
    def __init__(self):
        super().__init__("`маршрут_view`", ["Номер маршрута"], "`маршрут`")

        self.record_editor = PathEditor
        self.record_adder = type("PathEditor", (ViewRecordAdder,), {"combo_config": path_combo_config})


