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
        super().__init__(header=header, parent=parent)

        info = parent.db.execute(f"select * from {parent.source} order by `Дата покупки` desc limit 1")
        info = list(info.fetchall()[0])  # из курсора возрващаются tuple, имутабельный
        info[0] = ""  # Номер авто пользователь должен задать
        info[-1] = "0"  # у нового авто пробег будет равен нулю
        # да, при изменении конфигурации таблицы может отвалиться
        for cell_name, cell_pre_value in zip(header, info):
            cell = self.cell_index[cell_name]
            edit = cell.itemAt(1).widget()
            edit.setText(str(cell_pre_value))
            self.changed_cells[cell_name] = cell_pre_value

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
    def __init__(self):
        super().__init__("`автомобиль`", ["Номер автомобиля"])
        self.record_adder = AutoRecordAdder
        self.record_editor = AutoEditor
        self.record_editor.combo_config = auto_combo_config
        self.record_adder.combo_config = auto_combo_config


class AutoUi(AutoTableShower):

    def __init__(self):
        super().__init__()
        self.show()

