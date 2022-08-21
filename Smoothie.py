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