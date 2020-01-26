import mysql.connector

# conn = mysql.connector.connect(host="localhost",
#                                user="root",
#                                passwd="111222333",
#                                database="пассажироперевозочная",
#                                use_pure=True)  # для ошибки ssl


class DbWrapper:
    """Убогая реализация шаблона одиночки для доступа к базе данных"""
    __conn = None

    @staticmethod
    def connect(**kwargs):
        DbWrapper.__conn = mysql.connector.connect(**kwargs)

    @staticmethod
    def execute(operation: str, params=(), multi=False):  # Смотри что оборачиваешь
        """Функция реализующее коннект по требованию и создание уникального курсора для каждого запроса"""
        # try:
        cur = DbWrapper.__conn.cursor()
        cur.execute(operation, params, multi)
        return cur

    @staticmethod
    def commit():
        DbWrapper.__conn.commit()
        # except StopIteration:
        #     print(Exception)
        #     return None


db_wrapper = DbWrapper


