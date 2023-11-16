
class Retailitem:

    def __init__(self, product_descruption, count, price):
        self.product_descruption = product_descruption
        self.count = count
        self.price = price

    def display_info(self):
        print(f'Описание: {self.product_descruption}, Количество на складе: {self.count}, Цена: {self.price}')

    def display_info2(self):
        return f'Описание: {self.product_descruption}, Количество на складе: {self.count}, Цена: {self.price}'

class CashReqister:

    def __init__(self):
        self.items = []

    def purchase_item(self, retail_item):
        self.items.append(retail_item)

    def get_total(self):
        total = sum(item.price for item in self.items)
        return total

    def show_items(self):
        result = []
        for item in self.items:
            result.append(item.display_info2())
        return result

    def clear(self):
        self.items = []



prod1 = Retailitem('Пиджак', 12, 59.95)
prod2 = Retailitem('Дизайнерские джинсы', 40, 34.95)
prod3 = Retailitem('Рубашка', 20, 20.95)

prod1.display_info()
prod2.display_info()
prod3.display_info()


register = CashReqister()

print('Выберите товары для покупки:')
print('1. Пиджак')
print('2. Дизайнерские джинсы')
print('3. Рубашка')

while True:
    answer = input('Введите номер товара, или "q" для завершения: ')

    if answer.lower() == 'q':
        break

    if answer.isdigit():
        answer = int(answer)
        if 1 <= answer <= 3:
            if answer == 1:
                register.purchase_item(prod1)
            elif answer == 2:
                register.purchase_item(prod2)
            elif answer == 3:
                register.purchase_item(prod3)
            print('Товар добавлен в корзину. ')
        else:
            print('Некорректный выбор. Выберите от 1 до 3. ')
    else:
        print('Некорректный ввод, введите ')


print('\nВыбранные товары: ')
for item_info in register.show_items():
    print(item_info)

print('\nОбщая стоимость покупки: ', register.get_total())
print('Товары в кассовом аппарате: ', register.show_items())

register.clear()

register.show_items()


