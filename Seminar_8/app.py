# Задача 38:
# Создать телефонный справочник с возможностью импорта и экспорта данных
# в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться
# в файле.

# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной
# записи
# (Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

#  Дополнить телефонный справочник возможностью изменения и удаления данных.
#  Пользователь также может ввести имя или фамилию, и Вы должны реализовать
#  функционал для изменения и удаления данных

def correct_input() -> int:
    is_correct = True
    while is_correct:
        a = input()
        try:
            a = int(a)
            if a >= 0 and a < 7:
                is_correct = False
                return a
            else:
                print(
                    'Input Error. Please, type digits in the range [0 ; 6] !')
        except ValueError:
            print('Input error')


def help_menu():
    print("\nWelcome to the Phone Book program!\n"
          "\nPlease, choose the mode from the list and press ENTER:\n")
    print("0 -> Exit program")
    print("1 -> view all Phone Book data")
    print("2 -> add new record")
    print("3 -> find a certain user data")
    print("4 -> edit data")
    print("5 -> delete data")
    print("6 -> help menu")


def view_data():
    print("\n PHONE BOOK LIST: \n")
    with open("PHONE_BOOK.txt", "r", encoding="utf-8") as file:
        return file.read().replace(";", " ")


def add_data() -> str:
    print("\n___ADD NEW RECORD mode___\n")
    print("Enter new data: ")
    with open("PHONE_BOOK.txt", "a", encoding="utf-8") as data:
        data.write(";".join(tuple(input().split())) + "\n")
    return ("New record added")


def find_data(search_data: str) -> str:
    with open("PHONE_BOOK.txt", "r", encoding="utf-8") as file:
        res = []
        for data in file:
            # *поиск только по инициалам:
            # first_letter = str([i[0] for i in data.split(";")])
            # if search_data.upper() in first_letter.upper():
            # *поиск только по номерам телефонов:
            # phones = list(data.split(";"))[3]
            # if search_data in phones:
            if search_data.lower() in data.lower():
                res.append(data.replace(";", " "))
        if len(res) == 0:
            return "No data found"
    return ("".join(res))


def edit_data(record_to_be_changed: str) -> str:
    temp = ""
    with open("PHONE_BOOK.txt", "r", encoding="utf-8") as file:
        for line in file:
            if record_to_be_changed.lower() in line.lower():
                print(f"Data found -> {line}")
                y = "y"
                print("Is record correct: Y/N")
                if input().lower() == y:
                    print("Enter new data: ")
                    new_data = tuple(input().split(" "))
                    temp += ";".join(new_data) + "\n"
                else:
                    temp += line
            else:
                temp += line
        with open("PHONE_BOOK.txt", "w", encoding="utf-8") as file:
            file.write(temp)
        return "The record has been changed"


def delete_data(to_delete: str) -> str:
    temp = ""
    with open("PHONE_BOOK.txt", "r", encoding="utf-8") as file:
        for data in file:
            if to_delete.lower() in data.lower():
                print(f"Data found -> {data}")
                n = "n"
                print("Is record correct: Y/N")
                if input().lower() == n:
                    temp += data
            else:
                temp += data
        with open("PHONE_BOOK.txt", "w", encoding="utf-8") as file:
            file.write(temp)
        return "The record has been deleted"


help_menu()

while True:
    mode = correct_input()
    if mode == 0:
        break
    elif mode == 1:
        print(view_data())
    elif mode == 2:
        print(add_data())
    elif mode == 3:
        print("\n___SEARCH DATA mode___\n")
        print("Enter data for search: ")
        print(find_data(str(input())))
    elif mode == 4:
        print("\n___EDIT DATA mode___\n")
        print("Enter the record to be changed:\n")
        print(edit_data(str(input())))
    elif mode == 5:
        print("\n___DELETE DATA mode___\n")
        print("Enter the required data to be deleted: ")
        print(delete_data(str(input())))
    elif mode == 6:
        help_menu()
