import mysql.connector
from PyQt5.QtWidgets import QErrorMessage


class DbWrapper:
    """Убогая реализация шаблона одиночки для доступа к базе данных"""
    __conn = None
    last_error_widget = None  # надо, чтобы хоть где-то была ссылка на виджет, иначе его сборщик сожрёт

    @staticmethod
    def connect(**kwargs):
        DbWrapper.__conn = mysql.connector.connect(**kwargs)

    @staticmethod
    def execute(operation: str, params=(), multi=False):  # Смотри что оборачиваешь, и его параметры
        """Функция не реализующая коннект по требованию и создание уникального курсора для каждого запроса"""
        try:
            cur = DbWrapper.__conn.cursor()
            cur.execute(operation, params, multi)
            return cur
        except Exception as err:
            DbWrapper.last_error_widget = QErrorMessage()
            DbWrapper.last_error_widget.showMessage(str(err))
            return None

    @staticmethod
    def callproc(procname: str, arg: tuple):
        cur = DbWrapper.__conn.cursor()
        cur.callproc(procname, arg)
        return cur

    def executemany(operation, seq_of_param):
        cur = DbWrapper.__conn.cursor()
        cur.executemany(operation, seq_of_param)
        return cur

    @staticmethod
    def commit():
        DbWrapper.__conn.commit()


db_wrapper = DbWrapper  # для соответствия стиля наименования python, потому что используется как объект, а не класс


