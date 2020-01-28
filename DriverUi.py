from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout
from TableShower import TableShower


class DriverUi(QWidget):

    def __init__(self):
        super().__init__()

        self.show_all_btn = QPushButton("Отобразить всех водителей")
        self.replacement_btn = QPushButton("Замены водителей")

        self.show_all_btn.clicked.connect(lambda: TableShower("`водитель`", ["Табельный номер"]).show())
        self.replacement_btn.clicked.connect(lambda: TableShower("`замена водителя`", ["Номер наряда"]).show())

        self.box = QVBoxLayout()
        self.box.addWidget(self.show_all_btn)
        self.box.addWidget(self.replacement_btn)

        self.setLayout(self.box)

        self.show()

