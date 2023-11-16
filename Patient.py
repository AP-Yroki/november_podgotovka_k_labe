
class Patient:
    def __init__(self, name, patronymic, surname, address, city, area, postal_code, phone_number,emergency_contact_name, emergency_contact_phone):
        self.name = name
        self.patronymic = patronymic
        self.surname = surname
        self.address = address
        self.city = city
        self.area = area
        self.postal_code = postal_code
        self.phone_number = phone_number
        self.emergency_contact_name = emergency_contact_name
        self.emergency_contact_phone = emergency_contact_phone

    def get_name(self):
        print(self.name)

    def get_patronymic(self):
        print(self.patronymic)

    def get_surname(self):
        print(self.surname)

    def get_address(self):
        print(self.address)

    def get_city(self):
        print(self.city)

    def get_area(self):
        print(self.area)

    def get_postal_code(self):
        print(self.postal_code)

    def get_phone_number(self):
        print(self.phone_number)

    def get_emergency_contact_name(self):
        print(self.emergency_contact_name)

    def get_emergency_contact_phone(self):
        print(self.emergency_contact_phone)

    def set_name(self, string):
        self.name = string

    def set_patronymic(self, string):
        self.patronymic = string

    def set_surname(self, string):
        self.surname = string

    def set_address(self, string):
        self.address = string

    def set_city(self, string):
        self.city = string

    def set_area(self, string):
        self.area = string

    def set_postal_code(self, string):
        self.postal_code = string

    def set_phone_number(self, string):
        self.phone_number = string

    def set_emergency_contact_name(self, string):
        self.emergency_contact_name = string

    def set_emergency_contact_phone(self, phone):
        self.emergency_contact_phone = phone

    def display_info(self):
        print(f'Имя: {self.name}, Отчество: {self.patronymic}, Фамилия: {self.surname}, '
              f'Адрес: {self.address}, Город: {self.city}, Область: {self.area}, '
              f'Почтовый код: {self.postal_code}, имя и телефон контактного лица для экстренной связи:  {self.emergency_contact_name}, {self.emergency_contact_phone}')


class Procedure:

    def __init__(self, procedure_name, date, doc_name, price):
        self.procedure_name = procedure_name
        self.date = date
        self.doc_name = doc_name
        self.price = price

    def get_procedure_name(self):
        print(self.procedure_name)

    def get_date(self):
        print(self.date)

    def get_doc_name(self):
        print(self.doc_name)

    def get_price(self):
        print(self.price)

    def set_procedure_name(self, string):
        self.procedure_name = string

    def set_date(self, string):
        self.date = string

    def set_doc_name(self, string):
        self.doc_name = string

    def set_price(self, string):
        self.price = string

    def display_info(self):
        print(f'Название процедуры: {self.procedure_name}, Дата: {self.date}, Врач: {self.doc_name}, Стоимость: {self.price}')

print()
pat = Patient('Ivan', 'Ivanovich', 'Ivanov', 'Groov st. 15', 'Vashington', 'America', 1241242, '+1345344356143', 'Anatoliy', '+789313445566')
pat.display_info()
print()
procedure1 = Procedure('Врачебный осмотр', 'сегодняшняя', 'Ирвин', 250)
procedure2 = Procedure('Рентгеноскопия', 'сегодняшняя', 'Джёмисон', 500)
procedure3 = Procedure('Анализ крови', 'сегодняшняя', 'Смит', 200)

procedure1.display_info()
procedure2.display_info()
procedure3.display_info()
print()
result = procedure1.price + procedure2.price + procedure3.price
print(f'Общая сумма всех трёх процедур: {result}')