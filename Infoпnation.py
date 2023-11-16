class Information:

    def __init__(self, name, address, age, phone):
        self.name = name
        self.address = address
        self.age = age
        self.phone = phone

    def get_name(self):
        print(self.name)

    def get_address(self):
        print(self.address)

    def get_age(self):
        print(self.age)

    def get_phone(self):
        print(self.phone)

    def set_name(self, name):
        self.name = name

    def set_address(self, address):
        self.address = address

    def set_age(self, age):
        self.age = age

    def set_phone(self, phone):
        self.phone = phone


me = Information('Bob', 'st. Foods 16', 23, '+79843557568')
other1 = Information('Jhosh', 'st. Markson 2', 13, '+193356677332')
other2 = Information('Allien', 'st. Moskovskaya 32', 17, '+78935666734')

