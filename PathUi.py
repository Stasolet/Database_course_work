from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout

from DbWrapper import db_wrapper
from TableShower import TableShower


class PathUi(QWidget):

    def __init__(self):
        super().__init__()

        self.slave_widgets = []
        self.show_all_btn = QPushButton("Отобразить все маршруты")
        self.get_path_btn = QPushButton("Проложить маршрут")

        self.show_all_btn.clicked.connect(lambda: TableShower("`маршрут с названиям`", ["Номер маршрута"]).show())

        self.box = QVBoxLayout()
        self.box.addWidget(self.show_all_btn)
        self.box.addWidget(self.get_path_btn)

        self.setLayout(self.box)

        self.show()


if __name__ == '__main__':
    db_wrapper.connect(host="localhost",
                       user="root",
                       passwd="111222333",
                       database="пассажироперевозочная",
                       use_pure=True)
    from PyQt5.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)
    w = PathUi()

    sys.exit((app.exec_()))


