from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QComboBox, QSizePolicy

from TableShower import TableShower, TableRecordAdder, TableInfoChanger
from ViewShower import ViewInfoChanger


class AutoEditor(TableInfoChanger):
    """Ух, шайтан
    класс, в которых запихнули кишки из PathEditor, который основан на ViewShower,
     со всеми вытекающими для совместимости"""
    combo_update = ViewInfoChanger.combo_update
    combo_config = {"Водитель":
                        ("водитель",
                         "`Табельный номер`, CONCAT(`Фамилия`,' ', `Имя`,' ',`Отчество`)",
                         "CONCAT(`Фамилия`,`Имя`,`Отчество`)",
                         "Табельный номер")}

    def __init__(self, header, info, parent):
        super().__init__(header, info, parent)
        self.combo_change_idx ={"Водитель": {}}
        self.slave_drivers = QVBoxLayout()
        push_btn = self.main_layout.takeAt(self.main_layout.count() - 1).widget()

        self.auto_id = info[0]
        add_btn = QPushButton("Добавить")
        add_btn.clicked.connect(lambda e: self.add_cell(-1))
        self.main_layout.addWidget(add_btn)

        way = self.db.execute(f"SELECT CONCAT(`Фамилия`,' ', `Имя`,' ',`Отчество`), `назначение автомобиля водителю`.`Табельный номер` FROM `назначение автомобиля водителю` join `водитель` on `водитель`.`Табельный номер` = `назначение автомобиля водителю`.`Табельный номер` where `Номер автомобиля` = '{self.auto_id}'")
        for pos, point in enumerate(way, start=-1):
            auto_info = str(point[0])
            self.combo_change_idx["Водитель"][auto_info] = point[1]
            self.add_cell(pos, auto_info)

        self.main_layout.addLayout(self.slave_drivers)
        self.main_layout.addWidget(push_btn)

    def add_cell(self, pos: int, txt=""):
        """Вставляет ячейку ниже активирующей кнопки для вставки на уровне надо передать ::pos:: = -1"""

        cell = QHBoxLayout()
        edi = QLineEdit()
        edi.setText(txt)

        add_btn = QPushButton("Добавить")
        del_btn = QPushButton("Удалить")

        cmb = QComboBox()
        cmb.addItem(txt)

        edi.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        cmb.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        add_btn.clicked.connect(lambda e, c=cell: self.add_cell(c.pos))
        del_btn.clicked.connect(lambda e, c=cell: self.del_cell(c.pos))

        edi.editingFinished.connect(lambda c=cmb, t=edi.text:
                                    self.combo_update("Водитель", c, t()))  # le-kostyl
        cell.pos = pos
        cell.addWidget(edi)
        cell.addWidget(cmb)
        cell.addWidget(add_btn)
        cell.addWidget(del_btn)
        for i in range(pos + 1, self.slave_drivers.count()):
            cell_to_move = self.slave_drivers.itemAt(i)
            cell_to_move.pos += 1
        cell.pos += 1  # для вставки ниже активированной кнопки

        self.slave_drivers.insertLayout(cell.pos, cell)

    def del_cell(self, pos):
        cell: QVBoxLayout
        cell = self.slave_drivers.takeAt(pos)
        for i in range(cell.count()):
            w = cell.takeAt(0).widget()
            w.deleteLater()
        cell.deleteLater()

        for i in range(pos, self.slave_drivers.count()):
            cell_to_move = self.slave_drivers.itemAt(i)
            cell_to_move.pos -= 1

    def push_point_changes(self):
        params = []
        for i in range(self.slave_drivers.count()):
            cell = self.slave_drivers.itemAt(i)
            w = cell.itemAt(1).widget()
            driver = w.currentText()
            if driver:
                driver_id = self.combo_change_idx["Водитель"][driver]
                params.append((driver_id, self.auto_id))

        query = f" insert into `назначение автомобиля водителю` values(%s, %s)"
        self.db.execute("delete from `назначение автомобиля водителю` where `Номер автомобиля` = %s", (self.auto_id,))
        self.db.executemany(query, params)
        self.db.commit()

    def push_changes(self):
        self.push_point_changes()
        super().push_changes()


class AutoRecordAdder(TableRecordAdder):
    def __init__(self, header, parent: TableShower):
        """Преподготовленная форма, облегчающая добавление сразу нескольких авто"""

        info = parent.db.execute(f"select * from {parent.source} order by `Дата покупки` desc limit 1")
        info = list(info.fetchall()[0])  # из курсора возрващаются tuple, имутабельный
        info[0] = ""  # Номер авто пользователь должен задать
        info[-1] = "0"  # у нового авто пробег будет равен нулю
        # да, при изменении конфигурации таблицы может отвалиться
        super(TableRecordAdder, self).__init__(header=header, info=info, parent=parent)


class AutoTableShower(TableShower):
    # todo отображение водителей, привязанных к автомобилю как у маршрутов работающее при добавлении автомобиля
    def __init__(self, source: str, key_fields: list, parent=None):
        super().__init__(source, key_fields, parent=parent)
        self.record_adder = AutoRecordAdder
        self.record_editor = AutoEditor


class AutoUi(QWidget):

    def __init__(self):
        super().__init__()

        self.box = QVBoxLayout()
        self.show_all_btn = QPushButton("Отобразить весь автопарк")

        self.show_all_btn.clicked.connect(lambda: AutoTableShower("`автомобиль`", ["Номер автомобиля"]).show())

        self.box.addWidget(self.show_all_btn)

        self.setLayout(self.box)

        self.show()

