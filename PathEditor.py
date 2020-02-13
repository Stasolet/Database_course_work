from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QHBoxLayout, QLineEdit, QComboBox, QSizePolicy

from PathShower import path_combo_config
from ViewShower import ViewInfoChanger, ViewShower


class PathEditor(ViewInfoChanger):
    combo_config = path_combo_config

    def __init__(self, header, info, parent: ViewShower):
        super().__init__(header, info, parent)
        self.way_layout = QVBoxLayout()
        push_btn = self.main_layout.takeAt(self.main_layout.count() - 1).widget()

        self.path_id = info[0]

        add_btn = QPushButton("Добавить")
        add_btn.clicked.connect(lambda e: self.add_cell(-1))
        self.main_layout.addWidget(add_btn)

        way = self.db.execute(f"SELECT Станция, `Код станции` FROM `состав_маршрута_view` where `Номер маршрута` = {self.path_id}")
        for pos, point in enumerate(way, start=-1):
            station_info = str(point[0])
            self.combo_change_idx["Станция отправления"][station_info] = point[1]
            self.add_cell(pos, station_info)

        self.main_layout.addLayout(self.way_layout)
        self.main_layout.addWidget(push_btn)

    def add_cell(self, pos: int, txt=""):
        """Вставляет ячейку ниже активирующей кнопки для вставки на уровне надо передать ::pos:: = -1"""

        cell = QHBoxLayout()
        edi = QLineEdit()
        edi.setText(txt)

        add_btn = QPushButton("Добавить")
        down_btn = QPushButton("Вниз")
        up_btn = QPushButton("Вверх")
        del_btn = QPushButton("Удалить")

        cmb = QComboBox()
        cmb.addItem(txt)

        edi.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        cmb.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        up_btn.clicked.connect(lambda e, p=pos, c=cell: self.move_cell_up(c))
        down_btn.clicked.connect(lambda e, p=pos, c=cell: self.move_cell_down(c))

        add_btn.clicked.connect(lambda e, c=cell: self.add_cell(c.pos))
        del_btn.clicked.connect(lambda e, c=cell: self.del_cell(c.pos))

        edi.editingFinished.connect(lambda c=cmb, t=edi.text:
                                    self.combo_update("Станция отправления", c, t()))  # le-kostyl
        cell.pos = pos
        cell.addWidget(edi)
        cell.addWidget(cmb)
        cell.addWidget(add_btn)
        cell.addWidget(down_btn)
        cell.addWidget(up_btn)
        cell.addWidget(del_btn)
        for i in range(pos + 1, self.way_layout.count()):
            cell_to_move = self.way_layout.itemAt(i)
            cell_to_move.pos += 1
        cell.pos += 1  # для вставки ниже активированной кнопки

        self.way_layout.insertLayout(cell.pos, cell)

    def del_cell(self, pos):
        cell: QVBoxLayout
        cell = self.way_layout.takeAt(pos)
        for i in range(cell.count()):
            w = cell.takeAt(0).widget()
            w.deleteLater()
        cell.deleteLater()

        for i in range(pos, self.way_layout.count()):
            cell_to_move = self.way_layout.itemAt(i)
            cell_to_move.pos -= 1

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

    def push_point_changes(self):
        params = []
        station_ord_numb_in_path = 0
        for i in range(self.way_layout.count()):
            cell = self.way_layout.itemAt(i)
            w = cell.itemAt(1).widget()
            station = w.currentText()
            if station:
                station_id = self.combo_change_idx["Станция отправления"][station]
                params.append((self.path_id, station_ord_numb_in_path, station_id))
                station_ord_numb_in_path += 1

        query = f" insert into `состав маршрута` values(%s, %s, %s)"
        self.db.execute("delete from `состав маршрута` where `Номер маршрута` = %s", (self.path_id,))
        self.db.executemany(query, params)
        self.db.commit()

    def push_changes(self):
        self.push_point_changes()
        super().push_changes()