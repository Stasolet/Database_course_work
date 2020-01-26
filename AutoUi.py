from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout

from TableShower import TableShower


class AutoUi(QWidget):

    def __init__(self):
        super().__init__()

        self.box = QVBoxLayout()
        self.show_all_btn = QPushButton("Отобразить весь автопарк")
        self.add_new_btn = QPushButton("Добавить авто")

        self.show_all_btn.clicked.connect(lambda: TableShower("`автомобиль`", ["Номер автомобиля"]).show())

        self.box.addWidget(self.show_all_btn)
        self.box.addWidget(self.add_new_btn)

        self.setLayout(self.box)

        self.show()

