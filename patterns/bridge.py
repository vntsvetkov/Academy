from abc import ABC, abstractmethod


class ThemePage(ABC):

    @abstractmethod
    def get_color(self):
        raise NotImplementedError


class DarkTheme(ThemePage):
    __name = "Dark theme"

    def get_color(self):
        return self.__name


class OfficeTheme(ThemePage):
    __name = "Office theme"

    def get_color(self):
        return self.__name


class WebPage(ABC):

    @abstractmethod
    def get_content(self):
        raise NotImplementedError


class HomePage(WebPage):

    def __init__(self, theme: ThemePage):
        self.__theme = theme

    @property
    def theme(self):
        return self.__theme

    def get_content(self):
        print("Содержимое домашней страницы")


class AboutPage(WebPage):

    def __init__(self, theme: ThemePage):
        self.__theme = theme

    def get_content(self):
        print("Содержимое страницы о нас")


if __name__ == "__main__":

    page = HomePage(DarkTheme())
    print(page.theme.get_color())
