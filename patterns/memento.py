

class DocMomento:

    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


class Document:
    __text = ""

    def add_str(self, text):
        self.__text += text + "\n"

    def get_text(self):
        return self.__text

    def save(self):
        return DocMomento(self.__text)

    def restore(self, doc: DocMomento):
        self.__text = doc.text


class EditorHistory:

    def __init__(self):
        self.__history = []

    @property
    def history(self):
        return self.__history

    def push(self, doc: DocMomento):
        self.__history.append(doc)

    def pop(self):
        return self.__history.pop()


if __name__ == '__main__':
    document = Document()
    history = EditorHistory()

    document.add_str("Строка 1")
    document.add_str("Строка 2")
    history.push(document.save())
    document.add_str("Строка 3")

    document.restore(history.pop())

    print(document.get_text())








