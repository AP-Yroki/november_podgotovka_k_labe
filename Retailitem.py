
class Retailitem:

    def __init__(self, product_descruption, count, price):
        self.product_descruption = product_descruption
        self.count = count
        self.price = price

    def display_info(self):
        print(f'Описание: {self.product_descruption}, Количество на складе: {self.count}, Цена: {self.price}')

prod1 = Retailitem('Пиджак', 12, 59.95)
prod2 = Retailitem('Дизайнерские джинсы', 40, 34.95)
prod3 = Retailitem('Рубашка', 20, 20.95)

prod1.display_info()
prod2.display_info()
prod3.display_info()