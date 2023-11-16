
class Pet:

    def __init__(self, name, animal_type, age):
        self.name = name
        self.animal_type = animal_type
        self.age = age

    def set_name(self, new_name):
        self.name = new_name

    def set_animal_type(self, animal_type):
        self.animal_type = animal_type

    def set_age(self, age):
        self.age = age

    def get_name(self):
        return self.name

    def get_animal_type(self):
        return self.animal_type

    def get_age(self):
        return self.age

p = Pet(input('Введите имя животного: '), input('Введите тип животного: '), int(input('Введите возраст животного: ')))
print(p.get_name(), p.get_animal_type(), p.get_age())