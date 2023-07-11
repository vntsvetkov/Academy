from phonebook import DBPhonebook, Entry, Phonebook


def execute_application():

    db_phonebook = DBPhonebook()
    db_phonebook.connect('phonebook.db')
    db_phonebook.create_cursor()

    new_entry = Entry("Tom", "Jones", "456-988", "New York", "5 Avenu")
    db_phonebook.add_entry(new_entry.get_tuple_entry())

    data = db_phonebook.get_data()
    current_phonebook = Phonebook.create_from_execute(data)

    db_phonebook.close_cursor()


if __name__ == "__main__":
    execute_application()