from drink import Drink
from coin_holder import CoinHolder
from drink_holder import DrinkHolder
from vending_coin_holder import VendingCoinHolder


class VendingMachine:

    def __init__(self):
        self.drink_holder = DrinkHolder()
        self.vending_coin_holder = VendingCoinHolder()

    def buy(self, inserted_coins: CoinHolder, drink_type: Drink):
        self.vending_coin_holder.insert_coin(inserted_coins)
        if self._can_buy(drink_type) is False:
            return None
        self.vending_coin_holder.save_drink_coin(drink_type)
        return self.drink_holder.remove_drink(Drink.COKE)

    def refund(self)->CoinHolder:
        return self.vending_coin_holder.refund_coin()

    def _can_buy(self, drink_type: Drink):
        if self.drink_holder.drink_sold_out(drink_type) or \
                self.vending_coin_holder.coin_shortage(drink_type):
            return False
        return True
