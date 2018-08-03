from drink import Drink


class DrinkHolder:

    def __init__(self):
        self.drink_stocks = {}
        self.drink_stocks.update({Drink.COKE.name: 5})
        self.drink_stocks.update({Drink.DIET_COKE.name: 5})
        self.drink_stocks.update({Drink.TEA.name: 5})

    def remove_drink(self, drink_type: Drink):
        self.drink_stocks[drink_type.name] -= 1
        return Drink(drink_type)

    def drink_sold_out(self, drink_type):
        if self.drink_stocks[drink_type.name] == 0:
            return True
        return False
