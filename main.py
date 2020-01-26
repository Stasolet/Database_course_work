import sys
from PyQt5.QtWidgets import QApplication

from DbWrapper import db_wrapper
from MainUi import MainUi

if __name__ == '__main__':
    db_wrapper.connect(host="localhost",
                       user="root",
                       passwd="111222333",
                       database="пассажироперевозочная",
                       use_pure=True)
    app = QApplication(sys.argv)
    w = MainUi()

    sys.exit((app.exec_()))

