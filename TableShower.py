from PyQt5.QtWidgets import QScrollArea, QWidget, QHBoxLayout, QVBoxLayout,\
    QLabel, QLineEdit, QPushButton, QGridLayout, QSizePolicy


from DbWrapper import db_wrapper


class TableShower(QWidget):
    def __init__(self, source: str, key_fields: list, parent=None):
        super().__init__(parent=parent)
        self.slave_widgets = []
        self.source = source
        self.key_fields = key_fields
        self.db = db_wrapper
        self.record_editor = TableInfoChanger
        self.record_adder = TableRecordAdder

        self.content_widget = QWidget()
        self.table = QScrollArea()
        self.table.setWidget(self.content_widget)
        self.table.setWidgetResizable(True)
        self.table.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.content_layout = QGridLayout()
        self.content_widget.setLayout(self.content_layout)

        self.head_layout = QVBoxLayout()
        self.footer_layout = QVBoxLayout()
        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.head_layout)
        self.main_layout.addWidget(self.table)
        self.main_layout.addLayout(self.footer_layout)

        self.add_record_btn = QPushButton("ДОБАВИТЬ")
        self.footer_layout.addWidget(self.add_record_btn)

        self.setLayout(self.main_layout)
        self.content()
        self.resize(1000, 100)  # потому что я так хочу иначе слишком узко получается some magic
        # я не знаю почему но при таких числах всё хорошо выглядит

    def content(self) -> None:
        """Отображение непосредственно данных"""
        all_path = self.db.execute(f"SELECT * FROM {self.source}")
        data = [all_path.column_names] + all_path.fetchall()  # если отделить заголовок сложно верстать
        width = len(data[0])
        for i in range(len(data)):
            for j in range(width):
                lbl = QLabel(str(data[i][j]))
                self.content_layout.addWidget(lbl, i, j)

            if i:  # чтобы не было кнопки на заголовке
                btn = QPushButton("Изменить запись")
                btn.clicked.connect(lambda state, num=i: self.record_editor(data[0], data[num], self).show())
                self.content_layout.addWidget(btn, i, width)

        self.add_record_btn.clicked.connect(lambda state: self.record_adder(data[0], self).show())

    def content_update(self) -> None:
        """Обновление данных при принятии изменений"""
        for i in reversed(range(self.content_layout.count())):  # Скопипасченное шайтан колдунство для очистки
            widget_to_remove = self.content_layout.itemAt(i).widget()
            widget_to_remove.setParent(None)
            widget_to_remove.deleteLater()
        self.content()


class TableInfoChanger(QWidget):
    """Класс для изменения записей в таблице, визуализированной TableShower

    исходные значения полей берёт из родительского TableShower, после изменений вызывает обновление родителя
    каждая ячейка представленна в виде Layout, информация о которых хранится в cell_index"""
    def __init__(self, header, info, parent: TableShower):
        super().__init__()
        parent.slave_widgets.append(self)
        self.source = parent.source
        self.db = parent.db
        self.key_fields = parent.key_fields
        self.p_content_up = parent.content_update
        self.changed_cells = {}
        self.old_data = dict(zip(header, info))
        self.main_layout = QVBoxLayout()
        self.cell_index = {}
        for h, i in zip(header, info):
            cell_layout = QHBoxLayout()
            cell_head = QLabel(str(h))
            cell_info = QLineEdit()
            cell_info.setText(str(i))
            cell_info.editingFinished.connect(lambda name=h, new_info_func=cell_info.text:
                                              self.changed_cells.__setitem__(name, new_info_func()))
            cell_layout.addWidget(cell_head)
            cell_layout.addWidget(cell_info)
            self.cell_index[str(h)] = cell_layout
            self.main_layout.addLayout(cell_layout)
        accept_btn = QPushButton("Подтвердить изменения")
        accept_btn.clicked.connect(self.push_changes)
        self.main_layout.addWidget(accept_btn)
        self.setLayout(self.main_layout)

    def push_changes(self):
        """отправляет изменения обратно в базу данных

        собирает запрос, поочерёдно сравнивая значения в изменённых ячейках и собриает в единый запрос"""
        params, query = self.get_set_query()

        # формирование части запроса для определения изменяемого кортежа
        query += " WHERE "
        key_fields_values = [self.old_data[field] for field in self.key_fields]
        key_query = [f"`{k}` = {v}" for k, v in zip(self.key_fields, key_fields_values)]
        query += " and ".join(key_query)
        if params:
            self.db.execute(f"UPDATE {self.source} SET {query} ", params=params)
            self.db.commit()
            self.p_content_up()
            self.close()

    def get_set_query(self):
        """формирует последовательность вида: поле1 = значение1, полеN = значениеN, ... на основе изменённых полей"""
        query = []
        params = []
        for field_name in self.changed_cells.keys():
            if self.changed_cells[field_name] != str(self.old_data[field_name]):
                query.append(f" `{field_name}` = %s")
                params.append(self.changed_cells[field_name])
        query = ",".join(query)
        return params, query


class TableRecordAdder(TableInfoChanger):
    def __init__(self, header, parent: TableShower):
        super().__init__(header=header, info=[""] * len(header), parent=parent)

    def push_changes(self):
        params, query = self.get_set_query()
        if params:
            self.db.execute(f"insert into {self.source} SET {query} ", params=params)
            self.db.commit()
            self.p_content_up()
            self.close()


if __name__ == '__main__':
    db_wrapper.connect(host="localhost",
                       user="root",
                       passwd="111222333",
                       database="пассажироперевозочная",
                       use_pure=True)

    from PyQt5.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)
    path = TableShower("`маршрут с названиям`", ["Номер маршрута"])
    drive = TableShower("`водитель`", ["Табельный номер"])
    path.show()
    drive.show()
    sys.exit((app.exec_()))
