from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QComboBox, QLineEdit, QSizePolicy

from TableShower import TableShower, TableRecordAdder, TableInfoChanger


class ViewShower(TableShower):
    """Класс для визуализации View, с возможностью изменения исходной таблицы с использованием выпадающих списков"""
    def __init__(self, view_source: str, key_field: list, data_source: str, parent=None):
        super().__init__(view_source, key_field, parent)
        self.data_source = data_source


class ViewInfoChanger(TableInfoChanger):  # походу не покатит, либо надо делать фабрику классов
    """В что-то можно словарь положить ключ -- имя поля для приделывания комбобокса, а в значениях источник и имя в
    таблице источнике кладётся при помощи наследования"""

    что_то: dict  # словарь -- ключи названия столбцов отображения куда приделается комбобокс элементы кортежи, нулевым
    # элементом является таблица источник для этого поля, первым строка в которой указаны столбцы данной таблицы,
    # сначала внешний ключ таблицы источника, остальные это атрибуты для визуализации, вторым элементом поле для поиска
    # по шаблону LIKE, третьим элементом поле, на которое ссылается внешний ключ(основе view)
    # что_то = {"Станция отправления": ("станция_view", "*", "`Населённый пункт`", "Станция отправления")}

    @classmethod
    def combo_source_info_getter(cls):
        return cls.что_то

    def __init__(self, header, info, parent: ViewShower):
        """виджеты ввода текста для станций заменяются на комбобоксы с возможностью поиска"""
        # todo конструктор принимает поля для выпадающего списка, таблицы откуда они будут браться, и названия поля в т
        #  и имя поле в этой таблице
        super().__init__(header, info, parent)
        self.что_то = self.combo_source_info_getter()
        self.source = parent.data_source
        self.combo_change_idx = {}  # структура для отображения данных комбобокса в значения атрибутов таблиы данных
        for box_name in self.что_то.keys():
            self.combo_change_idx[box_name] = {}
            self.old_data[self.что_то[box_name][3]] = self.old_data[box_name]
            cell = self.cell_index[box_name]
            edit = cell.itemAt(1).widget()
            edit.disconnect()
            combo = QComboBox()
            combo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)  # это не работает todo исправить размер
            cell.addWidget(combo)
            edit.editingFinished.connect(lambda c_name=box_name, c=combo, t=edit.text:
                                         self.combo_update(c_name, c, t()))
            combo.activated[str].connect(lambda text, c_name=box_name, cell_name=self.что_то[box_name][3]:
                                         self.changed_cells.__setitem__(cell_name, self.combo_change_idx[c_name][text]))

    def combo_update(self, c_name: str, c: QComboBox, text: str):
        if text:
            results = self.db.execute(f"""SELECT {self.что_то[c_name][1]}
                                            from {self.что_то[c_name][0]} where {self.что_то[c_name][2]} LIKE '%{text}%';""")
            c.clear()
            for i in results:
                combo_text = " ".join(i[1:])  # за счёт этой части можно кидать несколько полей
                self.combo_change_idx[c_name][combo_text] = i[0]
                c.addItem(combo_text)


class ViewRecordAdder(ViewInfoChanger):
    push_changes = TableRecordAdder.push_changes

    def __init__(self, header, parent: ViewShower):
        super().__init__(header=header, info=[""] * len(header), parent=parent)



