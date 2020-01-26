from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout
from TableShower import TableShower




class DriverUi(QWidget):

    def __init__(self):
        super().__init__()

        self.show_all_btn = QPushButton("Отобразить всех водителей")
        self.add_new_btn = QPushButton("Найм водителя")
        self.change_info_btn = QPushButton("Изменение информации о водителе")
        self.zamena_btn = QPushButton("Замены водителей")

        self.show_all_btn.clicked.connect(lambda: TableShower("`водитель`", ["Табельный номер"]).show())
        self.zamena_btn.clicked.connect(lambda: TableShower("`замена водителя`", ["Номер наряда"]).show())

        self.box = QVBoxLayout()
        self.box.addWidget(self.show_all_btn)
        self.box.addWidget(self.add_new_btn)
        self.box.addWidget(self.change_info_btn)

        self.setLayout(self.box)

        self.show()

