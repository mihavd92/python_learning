# Создать класс Beverage, который при конструировании принимает список ингредиентов
# - поддерживает атрибут ingredients, возвращающий список ингредиентов, переданный при конструировании класса
# - поддерживает функцию get_cost, вычисляющую итоговую стоимость всех ингредиентов напитка
# (получается себестоимость напитка)
# - поддерживает функцию get_price, вычисляющую цену напитка посредством умножения себестоимости на 2.5
# - поддерживает функцию get_name, которая возвращает строку, перечисляющую ингредиенты, сортируя их
# в алфавитном порядке. Если ингредиентов больше одного, то в конце добавляет слово “Fusion”, иначе добавляет слово
# ‘Smoothie’. Эта функция также должна заменять ‘berries’ на ‘berry’

# Ингредианты и их себестоимость:

# Strawberries $1.50
# Banana $0.50
# Mango $2.50
# Blueberries $1.00
# Raspberries $1.00
# Apple $1.75
# Pineapple $3.50

# Примеры вызовов:
# s1 = Beverage([‘Banana’])
# s1.ingredients -> [‘Banana’]
# s1.get_cost() -> ‘$0.50’
# s1.get_price() -> ‘$1.25’
# s1.get_name() -> ‘Banana Smoothie’
# s2 = Beverage([‘Raspberries’, ‘Strawberries’, ‘Blueberries’])
# s2.ingredients -> [‘Raspberries’, ‘Strawberries’, ‘Blueberries’]
# s2.get_cost() -> ‘$3.50’
# s2.get_price() -> ‘$8.75’
# s2.get_name() -> ‘Blueberry Raspberry Strawberry Fusion’


ingridients = {
    'Strawberries': 1.50,
    'Banana': 0.50,
    'Mango': 2.50,
    'Blueberries': 1.00,
    'Raspberries': 1.00,
    'Apple': 1.75,
    'Pineapple': 3.50
}

class Beverage:
    def __init__(self, ingridients):
        self.ingridients = ingridients
    
    def get_cost(self):
        cost = 0
        for ingridient in self.ingridients:
            cost = cost + ingridients[ingridient]
        return cost
    
    def get_price(self):
        return self.get_cost() * 2.5

    def get_name(self):
        name = ''
        ingridients = sorted(self.ingridients)
        for ingridient in ingridients:
            name = name + ' ' + ingridient
        if len(ingridients) > 1:
            beverage_type = 'Fusion'
        else:
            beverage_type = 'Smoozi'
        return name[1:] + ' ' + beverage_type

b1 = Beverage(['Apple', 'Banana'])
cost = b1.get_cost()
name = b1.get_name()
print(cost)
print(name)
