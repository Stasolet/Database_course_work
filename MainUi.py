from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout

from AutoUi import AutoUi
from DriverUi import DriverUi
from OrdersUi import OrdersUi
from PathUi import PathUi



class MainUi(QWidget):
    def __init__(self):
        super().__init__()
        self.slave_widgets = []

        self.resize(500, 500)

        self.drive_btn = QPushButton("Управление персоналом")  # это должно как-то обобщится, а не писаться раз за разом
        self.auto_btn = QPushButton("Управление автопарком")
        self.orders_btn = QPushButton("Управление рейсами")
        self.path_btn = QPushButton("Управлнение маршрутами")

        self.drive_btn.clicked.connect(lambda: self.slave_widgets.append(DriverUi()))
        self.auto_btn.clicked.connect(lambda: self.slave_widgets.append(AutoUi()))
        self.orders_btn.clicked.connect(lambda: self.slave_widgets.append(OrdersUi()))
        self.path_btn.clicked.connect(lambda: self.slave_widgets.append(PathUi()))

        self.bx = QVBoxLayout()
        self.bx.addWidget(self.drive_btn)
        self.bx.addWidget(self.auto_btn)
        self.bx.addWidget(self.orders_btn)
        self.bx.addWidget(self.path_btn)

        self.setLayout(self.bx)

        self.show()

    # Главное окно тоже можно вынести в отдельный класс