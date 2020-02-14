from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout

from AutoEditor import AutoEditor
from TableShower import TableShower, TableRecordAdder


auto_combo_config = {"Водитель":
                       ("водитель",
                        "`Табельный номер`, CONCAT(`Фамилия`,' ', `Имя`,' ',`Отчество`)",
                        "CONCAT(`Фамилия`,`Имя`,`Отчество`)",
                        "Табельный номер")}


class AutoRecordAdder(TableRecordAdder):
    add_cell = AutoEditor.add_cell
    del_cell = AutoEditor.del_cell
    push_point_changes = AutoEditor.push_point_changes
    combo_update = AutoEditor.combo_update

    def __init__(self, header, parent: TableShower):
        """Преподготовленная форма, облегчающая добавление сразу нескольких авто"""

        info = parent.db.execute(f"select * from {parent.source} order by `Дата покупки` desc limit 1")
        info = list(info.fetchall()[0])  # из курсора возрващаются tuple, имутабельный
        info[0] = ""  # Номер авто пользователь должен задать
        info[-1] = "0"  # у нового авто пробег будет равен нулю
        # да, при изменении конфигурации таблицы может отвалиться
        super(TableRecordAdder, self).__init__(header=header, info=info, parent=parent)
        # В данном месте вызывается конструктор родителя родителя -- TableInfoChanger,
        # для того, чтобы передать ему заполнение ячеек
        # todo такое говно, лучше вручную всё заполнить
        self.changed_cells.update(zip(header, info))
        self.old_data.update(zip(header, [""] * len(header)))
        self.combo_change_idx = {"Водитель": {}}
        self.auto_id = None
        self.slave_drivers_layout = QVBoxLayout()
        push_btn = self.main_layout.takeAt(self.main_layout.count() - 1).widget()

        add_btn = QPushButton("Добавить")
        add_btn.clicked.connect(lambda e: self.add_cell(-1))
        self.main_layout.addWidget(add_btn)

        self.main_layout.addLayout(self.slave_drivers_layout)
        self.main_layout.addWidget(push_btn)

    def push_changes(self):
        super().push_changes()
        self.auto_id = self.changed_cells["Номер автомобиля"]
        self.push_point_changes()


class AutoTableShower(TableShower):
    # todo отображение водителей, привязанных к автомобилю как у маршрутов работающее при добавлении автомобиля
    def __init__(self, source: str, key_fields: list, parent=None):
        super().__init__(source, key_fields, parent=parent)
        self.record_adder = AutoRecordAdder
        self.record_editor = AutoEditor
        self.record_editor.combo_config = auto_combo_config
        self.record_adder.combo_config = auto_combo_config


class AutoUi(QWidget):

    def __init__(self):
        super().__init__()

        self.box = QVBoxLayout()
        self.show_all_btn = QPushButton("Отобразить весь автопарк")

        self.show_all_btn.clicked.connect(lambda: AutoTableShower("`автомобиль`", ["Номер автомобиля"]).show())

        self.box.addWidget(self.show_all_btn)

        self.setLayout(self.box)

        self.show()

