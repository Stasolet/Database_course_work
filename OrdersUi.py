from ViewShower import ViewShower, ViewRecordAdder, ViewInfoChanger


class OrderShower(ViewShower):
    def __init__(self):
        super().__init__("`наряд_view`", ["Номер наряда"], "`наряд`")
        q = {"Маршрут":
                 ("`маршрут_view`",
                  "`Номер маршрута`, CONCAT(`Станция отправления`, ' - ', `Станция прибытия`)",
                  "CONCAT(`Станция отправления`, ' - ', `Станция прибытия`)",
                  "Номер маршрута"),
             "Водитель":
                 ("водитель",
                  "`Табельный номер`, CONCAT(`Фамилия`,' ', `Имя`,' ',`Отчество`)",
                  "CONCAT(`Фамилия`,`Имя`,`Отчество`)",
                  "Табельный номер"),
             "Автомобиль":
                 ("автомобиль",
                  """`Номер автомобиля`, CONCAT(`Номер автомобиля`, ' ', `Производитель`, ' ', `Модель`,
                                                ' ', `Вместимость`, ' мест')""",
                  """CONCAT(`Производитель`,`Модель`,`Вместимость`)""",
                  "Номер автомобиля"
                  )
             }
        self.record_editor = type("OrderEditor", (ViewInfoChanger,), {"combo_config": q})
        self.record_adder = type("OrderAdder", (ViewRecordAdder,), {"combo_config": q})
        self.resize(1500, 300)


class OrdersUi(OrderShower):

    def __init__(self):
        super().__init__()
        self.show()

