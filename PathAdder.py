from PyQt5.QtWidgets import QVBoxLayout, QPushButton

from PathEditor import PathEditor
from PathShower import path_combo_config
from ViewShower import ViewRecordAdder, ViewShower


class PathAdder(ViewRecordAdder):
    combo_config = path_combo_config
    add_cell = PathEditor.add_cell
    del_cell = PathEditor.del_cell
    move_cell_up = PathEditor.move_cell_up
    move_cell_down = PathEditor.move_cell_down
    push_point_changes = PathEditor.push_point_changes

    def __init__(self, header, parent: ViewShower):
        super().__init__(header, parent)
        self.path_id = None
        self.way_layout = QVBoxLayout()
        push_btn = self.main_layout.takeAt(self.main_layout.count() - 1).widget()

        add_btn = QPushButton("Добавить")
        add_btn.clicked.connect(lambda e: self.add_cell(-1))
        self.main_layout.addWidget(add_btn)

        self.main_layout.addLayout(self.way_layout)
        self.main_layout.addWidget(push_btn)

    def push_changes(self):
        super().push_changes()
        self.path_id = self.changed_cells["Номер маршрута"]
        self.push_point_changes()