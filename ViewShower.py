from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QComboBox, QLineEdit, QSizePolicy

from TableShower import TableShower, TableRecordAdder, TableInfoChanger


class ViewShower(TableShower):
    """Класс для визуализации View, с возможностью изменения исходной таблицы с использованием выпадающих списков"""
    def __init__(self, view_source: str, key_field: list, data_source: str, parent=None):
        super().__init__(view_source, key_field, parent)
        self.data_source = data_source


class ViewInfoChanger(TableInfoChanger):
    """Виджет для визуализации отображений с возможностью редакирование содержимого,
     с использованием выпадающих списков

     Для использования необходимо отнаследоваться от него и присвоить атрибут combo_config"""

    combo_config: dict  # словарь -- ключи названия столбцов отображения куда приделается комбобокс элементы кортежи,
    # нулевым элементом является таблица источник этого поля, первым строка в которой указаны столбцы данной таблицы,
    # сначала внешний ключ таблицы источника, остальные это атрибуты для визуализации, вторым элементом поле для поиска
    # по шаблону LIKE, третьим элементом поле, на которое ссылается внешний ключ(основе view)
    # combo_config = {"Станция отправления": ("станция_view", "*", "`Населённый пункт`", "Станция отправления")}

    @classmethod
    def combo_config_getter(cls):
        return cls.combo_config

    def __init__(self, header, info, parent: ViewShower):
        """виджеты ввода текста для станций заменяются на комбобоксы с возможностью поиска"""
        super().__init__(header, info, parent)
        self.combo_config = self.combo_config_getter()
        self.source = parent.data_source
        self.combo_change_idx = {}  # структура для отображения данных комбобокса в значения атрибутов таблиы данных
        for box_name in self.combo_config.keys():
            self.combo_change_idx[box_name] = {}
            self.old_data[self.combo_config[box_name][3]] = self.old_data[box_name]
            cell = self.cell_index[box_name]
            edit = cell.itemAt(1).widget()
            edit.disconnect()
            combo = QComboBox()
            combo.addItem(edit.text())
            edit.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
            combo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            cell.addWidget(combo)
            edit.editingFinished.connect(lambda c_name=box_name, c=combo, t=edit.text:
                                         self.combo_update(c_name, c, t()))
            combo.activated[str].connect(lambda text, c_name=box_name, cell_name=self.combo_config[box_name][3]:
                                         self.changed_cells.__setitem__(cell_name, self.combo_change_idx[c_name][text]))

    def combo_update(self, c_name: str, c: QComboBox, text: str):
        if text:
            results = self.db.execute(f"""SELECT {self.combo_config[c_name][1]}
                                            from {self.combo_config[c_name][0]} where {self.combo_config[c_name][2]} LIKE '%{text}%';""")
            c.clear()
            for i in results:
                combo_text = " ".join(i[1:])  # за счёт этой части можно кидать несколько полей
                self.combo_change_idx[c_name][combo_text] = i[0]
                c.addItem(combo_text)


class ViewRecordAdder(ViewInfoChanger):
    push_changes = TableRecordAdder.push_changes

    def __init__(self, header, parent: ViewShower):
        super().__init__(header=header, info=[""] * len(header), parent=parent)

