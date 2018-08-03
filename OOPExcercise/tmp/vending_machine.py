from drink import Drink


class VendingMachine:

    def __init__(self):
        self.quantity_of_coke = 5
        self.quantity_of_diet_coke = 5
        self.quantity_of_tea = 5
        self.number_of_100_yen = 10
        self.change = 0

    # 投入金額. 100円と500円のみ受け付ける.
    # return. ジュース or None
    def buy(self, i, kind_of_drink):

        if (i != 100) and (i != 500):
            self.change += i
            return None

        if (kind_of_drink == Drink.COKE) and (self.quantity_of_coke == 0):
            self.change += i
            return None

        if (kind_of_drink == Drink.DIET_COKE) and (self.quantity_of_diet_coke == 0):
            self.change += i
            return None

        if (kind_of_drink == Drink.TEA) and (self.quantity_of_tea == 0):
            self.change += i
            return None

        if i == 500 and self.number_of_100_yen < 4:
            self.change += i
            return None

        if i == 100:
            self.number_of_100_yen += 1

        if i == 500:
            self.change += (i - 100)
            self.number_of_100_yen -= (i - 100) / 100

        if kind_of_drink == Drink.COKE:
            self.quantity_of_coke -= 1
        elif kind_of_drink == Drink.DIET_COKE:
            self.quantity_of_diet_coke -= 1
        else:
            self.quantity_of_tea -= 1

        return Drink(kind_of_drink)

    def refund(self):
        result = self.change
        self.change = 0
        return result
