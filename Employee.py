
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

us1.dispaly_info()
us2.dispaly_info()
us3.dispaly_info()