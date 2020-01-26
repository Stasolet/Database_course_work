from PyQt5.QtWidgets import QScrollArea, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton, QGridLayout

from DbWrapper import db_wrapper


class TableShower(QScrollArea):
    # todo отдлеьный контейнер для содержимого, логическое разделение на заголовок, контент, подвал
    def content_update(self) -> None:
        """Обновление данных при принятии изменений"""
        for i in reversed(range(self.path_table_widget_layout.count())):  # Скопипасченное шайтан колдунство для очистки
            widget_to_remove = self.path_table_widget_layout.itemAt(i).widget()
            widget_to_remove.setParent(None)
            widget_to_remove.deleteLater()
        self.content()

    def __init__(self, source: str, key_fields: list, parent=None):
        super().__init__(parent=parent)
        self.slave_widgets = []
        self.source = source
        self.key_fields = key_fields
        self.db = db_wrapper
        self.path_table_widget = QWidget()
        self.path_table_widget_layout = QGridLayout()

        self.path_table_scroll_layout = QVBoxLayout()
        self.path_table_scroll_layout.addLayout(self.path_table_widget_layout)

        self.setLayout(self.path_table_scroll_layout)
        self.setWidget(self.path_table_widget)
        # Может стоит Qscroll завернуть только как нонтент, и в контейнер и кнопки
        self.content()

    def content(self) -> None:
        """Отображение непосредственно данных"""
        all_path = self.db.execute(f"SELECT * FROM {self.source}")
        data = [all_path.column_names] + all_path.fetchall()  # возможно стоит отделить заоголовок.
        width = len(data[0])
        for i in range(len(data)):
            for j in range(width):
                lbl = QLabel(str(data[i][j]))

                self.path_table_widget_layout.addWidget(lbl, i, j)
            if i:
                btn = QPushButton("Изменить маршрут")
                btn.clicked.connect(lambda state, num=i: TableInfoChanger(data[0], data[num], self).show())
                self.path_table_widget_layout.addWidget(btn, i, width)

        qwe = QPushButton("ДОБАВИТЬ")
        qwe.clicked.connect(lambda state: TableRecordAdder(data[0], self).show())
        self.path_table_scroll_layout.addWidget(qwe)


class TableInfoChanger(QWidget):
    # todo отдлеьный контейнер для содержимого, логическое разделение на заголовок, контент, подвал
    def __init__(self, header, info, parent: TableShower):
        super().__init__()

        parent.slave_widgets.append(self)  # пока что пусть будет так виджет изменения записи сам регистрируется в родителе
        self.source = parent.source
        self.db = parent.db
        self.key_fields = parent.key_fields
        self.p_content_up = parent.content_update
        self.changed_cells = {}
        self.old_data = dict(zip(header, info))
        main_layout = QHBoxLayout()
        for h, i in zip(header, info):
            cell_layout = QVBoxLayout()

            cell_head = QLabel(str(h))
            cell_info = QLineEdit()
            cell_info.setText(str(i))
            cell_info.editingFinished.connect(lambda name=h, new_info_func=cell_info.text:
                                              self.changed_cells.__setitem__(name, new_info_func()))

            cell_layout.addWidget(cell_head)
            cell_layout.addWidget(cell_info)
            main_layout.addLayout(cell_layout)
        accept_btn = QPushButton("Подтвердить изменения")
        accept_btn.clicked.connect(self.push_changes)
        main_layout.addWidget(accept_btn)
        self.setLayout(main_layout)

    def push_changes(self):
        """отправляет изменения обратно в базу данных

        собирает запрос, поочерёдно сравнивая значения в изменённых ячейках и собриает в единый запрос"""
        query = []
        params = []
        # формирование полей на изменение
        for field_name in self.changed_cells.keys():
            if self.changed_cells[field_name] != str(self.old_data[field_name]):
                query.append(f" `{field_name}` = %s")
                params.append(self.changed_cells[field_name])
        query = ",".join(query)

        # формирование части запроса для определения изменяемого кортежа
        query += " WHERE "
        key_fields_values = [self.old_data[field] for field in self.key_fields]
        key_query = [f"`{k}` = {v}" for k, v in zip(self.key_fields, key_fields_values)]
        query += " and ".join(key_query)
        if params:
            self.db.execute(f"UPDATE {self.source} SET {query} ", params=params)
            self.db.commit()
            self.p_content_up()


class TableRecordAdder(TableInfoChanger):
    def __init__(self, header, parent: TableShower):
        super().__init__(header=header, info=[""] * len(header), parent=parent)

    def push_changes(self):
        query = []
        params = []
        # формирование полей на изменение
        for field_name in self.changed_cells.keys():
            if self.changed_cells[field_name] != str(self.old_data[field_name]):
                query.append(f" `{field_name}` = %s")
                params.append(self.changed_cells[field_name])
        query = ",".join(query)

        if params:
            self.db.execute(f"insert into {self.source} SET {query} ", params=params)
            self.db.commit()
            self.p_content_up()

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
    # path = TableShower("`маршрут с названиям`", ["Номер маршрута"])
    path.show()
    drive.show()
    sys.exit((app.exec_()))
