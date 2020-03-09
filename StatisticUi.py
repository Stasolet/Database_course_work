from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout

from TableShower import TableShower
from ProcedureShower import ProcedureShower

driver_statistic_args = [("Водитель",
                          {"src": "водитель",
                              "comb_info": "CONCAT(`Фамилия`, ' ',`Имя`, ' ',`Отчество`)",
                              "substitution": "`Табельный номер`"})]

auto_statistic_args = [("Автомобиль",
                        {"src": "автомобиль",
                                "comb_info": """CONCAT(`Номер автомобиля`, ' ', `Производитель`, ' ', `Модель`,
                                                ' ', `Вместимость`, ' мест')""",
                                "substitution": "`Номер автомобиля`"})]

path_statistic_args = [("Маршрут",
                        {"src": "маршрут_view",
                         "comb_info": "CONCAT(`Станция отправления`, ' - ', `Станция прибытия`)",
                         "substitution": "`Номер маршрута`"})]


class StatisticUi(QWidget):
    def add_slave(self, widget: QWidget):
        self.slave_widgets.append(widget)
        widget.show()

    def __init__(self):
        super().__init__()
        self.slave_widgets = []
        self.full_stat = QPushButton("Общая статистика")
        self.full_auto_stat = QPushButton("Статистика по автомобилям")
        self.full_drivers_stat = QPushButton("Статистика по водителям")
        self.full_path_stat = QPushButton("Статистика по маршрутам")

        self.one_auto_stat = QPushButton("Статистика по одному автомобилям")
        self.one_drive_stat = QPushButton("Статистика по одному водителю")
        self.one_path_stat = QPushButton("Статистика по одному маршруту")

        self.full_stat.clicked.connect(lambda: self.add_slave(TableShower("`общая статистика помесячно`",
                                                                          editable=False, deletable=False)))
        self.full_auto_stat.clicked.connect(lambda: self.add_slave(TableShower("`общая статистика по автомобилям`",
                                                                               editable=False, deletable=False)))
        self.full_drivers_stat.clicked.connect(lambda: self.add_slave(TableShower("`общая статистика по водителям`",
                                                                                  editable=False, deletable=False)))
        self.full_path_stat.clicked.connect(lambda: self.add_slave(TableShower("`общая статистика по маршрутам`",
                                                                               editable=False, deletable=False)))

        self.one_auto_stat.clicked.connect(lambda: self.add_slave(ProcedureShower("auto_statistic",
                                                                                  arg=auto_statistic_args)))
        self.one_drive_stat.clicked.connect(lambda: self.add_slave(ProcedureShower("driver_statistic",
                                                                                   arg=driver_statistic_args)))
        self.one_path_stat.clicked.connect(lambda: self.add_slave(ProcedureShower("path_statistic",
                                                                                  arg=path_statistic_args)))

        self.box = QVBoxLayout()
        self.box.addWidget(self.full_stat)
        self.box.addWidget(self.full_auto_stat)
        self.box.addWidget(self.full_drivers_stat)
        self.box.addWidget(self.full_path_stat)
        self.box.addWidget(self.one_auto_stat)
        self.box.addWidget(self.one_drive_stat)
        self.box.addWidget(self.one_path_stat)

        self.setLayout(self.box)

        self.show()

