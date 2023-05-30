class Singleton:
    __instance = None
    __database: list = []

    @classmethod
    def get_instance(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance

    def get_data(self):
        return self.__database

    def add_data(self, data):
        self.__database.append(data)

    def remove_data(self):
        self.__database.pop()


database1 = Singleton.get_instance()
database1.add_data("Добавили данные черезх db1")

database2 = Singleton.get_instance()
database2.add_data("Добавили данные черезх db2")

print(database1.get_data())
database1.remove_data()
print(database2.get_data())


