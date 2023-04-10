def main_menu():
    print('1. Посмотреть контакты')
    print('2. Создать контакт')
    print('3. Найти контакт')
    print('4. Изменить контакт')
    print('5. Удалить контакт')
    print('6. Выход')

def show_directory():
    file = open('phonebook.txt', 'r', encoding='UTF-8')
    data = file.readlines()
    file.close()
    for i in data:
        print(i)

def add_contact():
    file = open('phonebook.txt', 'a', encoding='UTF-8')
    data = input('Введите фамилию, телефон, комментарий, через ; ')
    file.write(f'\n{data}')
    file.close()

def find_contact():
    find_element = input('Кого ищем? ')
    file = open('phonebook.txt', 'r', encoding='UTF-8')
    data = file.readlines()
    for item in data:
        if find_element in item:
            print(item)
            break
    file.close()


def edit_contact():
    file = open('phonebook.txt', 'r', encoding='UTF-8')
    find_element = input('Какой контакт изменить? ')
    data = file.readlines()
    for item in data:
        if find_element in item:
            print(item)
    file.close()
    file = open('phonebook.txt', 'w', encoding='UTF-8')
    new_item = input('Для изменения контакта введите фамилию, телефон, комментарий, через ; ')
    item = item.replace(item, new_item)
    file.write(f'\n{item}')
    file.close()

def delete_contact():
    file = open('phonebook.txt', 'r', encoding='UTF-8')
    find_element = input('Какой контакт удалить? ')
    data = file.readlines()
    file = open('phonebook.txt', 'w', encoding='UTF-8')
    for item in data:
        if find_element in item:
            print(item)
    file.close()

main_menu()
while True:
    choose = int(input('Введите пункт меню: '))
    if choose == 1:
        show_directory()
    if choose == 2:
        add_contact()
    if choose == 3:
        find_contact()
    if choose == 4:
        edit_contact()
    if choose == 5:
        delete_contact()
    if choose == 6:
        main_menu()
