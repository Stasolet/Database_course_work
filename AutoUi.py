from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout

from TableShower import TableShower, TableRecordAdder


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
    def __init__(self, source: str, key_fields: list, parent=None):
        super().__init__(source, key_fields, parent=parent)
        self.record_adder = AutoRecordAdder


class AutoUi(QWidget):

    def __init__(self):
        super().__init__()

        self.box = QVBoxLayout()
        self.show_all_btn = QPushButton("Отобразить весь автопарк")

        self.show_all_btn.clicked.connect(lambda: AutoTableShower("`автомобиль`", ["Номер автомобиля"]).show())

        self.box.addWidget(self.show_all_btn)

        self.setLayout(self.box)

        self.show()

