from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout

from TableShower import TableShower


class OrdersUi(QWidget):
    def __init__(self):
        super().__init__()

        self.box = QVBoxLayout()
        self.show_all_btn = QPushButton("Отобразить все рейсы")
        self.add_new_btn = QPushButton("Отправить в рейс")

        self.show_all_btn.clicked.connect(lambda: TableShower("`наряд`", ["Номер наряда"]).show())

        self.box.addWidget(self.show_all_btn)
        self.box.addWidget(self.add_new_btn)

        self.setLayout(self.box)

        self.show()


