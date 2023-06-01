"""
Печать содержимого файла на бумаге через принтер
"""

class GetPaperError(Exception):
    def __init__(self, text):
        self.__text = text


class PaperTray:

    def __init__(self, count):
        self.__count_paper = count

    def get_count_paper(self):
        return self.__count_paper

    def remove(self, count):
        self.__count_paper -= count


class Printer:

    @staticmethod
    def __draw_text(text):
        print(f"Содержимое страницы: {text}")

    def print(self, paper: PaperTray, text: str):
        if paper.get_count_paper() > 0:
            self.__draw_text(text)
            paper.remove(1)
        else:
            raise GetPaperError("Бумага закончилась")


class PrinterFacade:

    def __init__(self, count):
        self.__paper = PaperTray(count)
        self.__printer = Printer()

    def print(self, text):
        self.__printer.print(self.__paper, text)


if __name__ == "__main__":
    facade = PrinterFacade(3)
    facade.print("Пробная страница 1")
    facade.print("Пробная страница 2")
    facade.print("Пробная страница 3")
    facade.print("Пробная страница 4")
