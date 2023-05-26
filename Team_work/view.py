def greetings():
    print('Привет!')
    
    
def display_contacts(data):
    if len(data)==0:
        print("Нет данных! ")
        return
    format_title='{:^6}\t{:^12}\t{:^8}\t{:^10}'
    print(format_title.format('Номер телефона','Фамилия','Имя','Отчество'))
    format_data='{:^6}\t{:^12}\t{:^8}\t{:^10}'
    for item in data:
        print(format_data.format(item.get('number'),item.get('name')))
        
        
        
def menu():
    print(
        'Выберите действие:\n'
        '1 - Вывести список контактов\n'
        
        '2 - Поиск\n'
        
        '3 - Добавить контакт\n'
        
        '4 - Изменить контакт\n'
        
        '5 - Удалить контакт\n'
        
        '6 - Выход'
    )
    
    