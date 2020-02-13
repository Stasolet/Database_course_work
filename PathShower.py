from PathAdder import PathAdder
from PathEditor import PathEditor
from ViewShower import ViewShower

path_combo_config = {"Станция отправления": ("станция_view", "*", "`Населённый пункт`", "Станция отправления"),
                     "Станция прибытия": ("станция_view", "*", "`Населённый пункт`", "Станция прибытия")}


class PathShower(ViewShower):
    def __init__(self):
        super().__init__("`маршрут_view`", ["Номер маршрута"], "`маршрут`")

        self.record_editor = PathEditor
        self.record_adder = PathAdder


