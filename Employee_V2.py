
class Employee:

    def __init__(self, name, id, departament, post):
        self.name = name
        self.id = id
        self.departament = departament
        self.post = post

    def dispaly_info(self):
        print(f'Имя: {self.name}, Идентификационный номер: {self.id}, Отдел: {self.departament}, Должность: {self.post}')



us1 = Employee('Сьюзан Мейерс', 47899, 'Бухгалтерия', 'Вице-президент')
us2 = Employee('Марк Джоунс', 39119, 'ИТ', 'Программист')
us3 = Employee('Джой Роджерс', 81744, 'Производственный', 'Инженер')


emp_dict = {us1.id: us1, us2.id: us2, us3.id: us3}

while True:
    print('\nМеню:')
    print('1. Найти сотрудника')
    print('2. Добавить нового сотрудника')
    print('3. Изменить информацию о сотруднике')
    print('4. Удалить сотрудника')
    print('5. Выйти из программы')

    answer = int(input('Выберите действие: '))

    if answer == 1:
        emp_id = int(input('Введите id сотрудника: '))
        if emp_id in emp_dict:
            emp_dict[emp_id].dispaly_info()
        else:
            print('Сотрудник не найден!')
    elif answer == 2:
        name = input('Введите имя нового сотрудника: ')
        emp_id = int(input('Введите id нового сотрудника: '))
        departament = input('Введите отдел нового сотрудника: ')
        post = input('Введите должность нового сотрудника: ')
        new_emp = Employee(name, emp_id, departament, post)
        emp_dict[emp_id] = new_emp
        print('Сотрудник добавлен!')
    elif answer == 3:
        emp_id = int(input('Введите id сотрудника для изменения информации: '))
        if emp_id in emp_dict:
            name = input('Введите новое имя: ')
            departament = input('Введите новый отдел: ')
            post = input('Введите новую должность: ')
            emp_dict[emp_id].name = name
            emp_dict[emp_id].departament = departament
            emp_dict[emp_id].post = post
            print('Информация о сотруднике обмновлена.')
        else:
            print('Сотрудник не найден!')
    elif answer == 4:
        emp_id = int(input('Введите id сотрудника для удаления: '))
        if emp_id in emp_dict:
            del emp_dict[emp_id]
            print('Сотрудник удален.')
        else:
            print('Сотрудник не найден!')
    elif answer == 5:
        print('Программа завершена.')
        break
    else:
        print('Выберите существующий номер')


