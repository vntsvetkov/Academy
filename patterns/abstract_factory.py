from abc import ABC, abstractmethod


class FurnitureItem(ABC):
    pass


class Chair(FurnitureItem):
    pass


class Table(FurnitureItem):
    pass


class Sofa(FurnitureItem):
    pass


class ModernChair(Chair):
    pass


class ModernTable(Table):
    pass


class ModernSofa(Sofa):
    pass


class ClassicChair(Chair):
    pass


class ClassicTable(Table):
    pass


class ClassicSofa(Sofa):
    pass


class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self):
        raise NotImplementedError

    @abstractmethod
    def create_table(self):
        raise NotImplementedError

    @abstractmethod
    def create_sofa(self):
        raise NotImplementedError


class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return ModernChair()

    def create_table(self):
        return ModernTable()

    def create_sofa(self):
        return ModernSofa()


class ClassicFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return ClassicChair()

    def create_table(self):
        return ClassicTable()

    def create_sofa(self):
        return ClassicSofa()


class Furniture:
    __furniture = []

    def add(self, item: FurnitureItem):
        self.__furniture.append(item)


class Shop:
    @staticmethod
    def create_furniture_set(factory: FurnitureFactory):
        furniture = Furniture()
        furniture.add(factory.create_sofa())
        furniture.add(factory.create_table())
        furniture.add(factory.create_chair())
        return furniture


if __name__ == "__main__":
    shop = Shop()
    fur = shop.create_furniture_set(ModernFurnitureFactory())
    print(fur)
