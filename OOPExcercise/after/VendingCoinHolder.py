from coin_holder import CoinHolder
import copy
from drink_holder import Drink


class VendingCoinHolder:

    def __init__(self):
        self.coin_holder = CoinHolder(yen_500=10, yen_100=10, yen_10=10)
        self.refund = CoinHolder(yen_500=0, yen_100=0, yen_10=0)

    def insert_coin(self, client_coin_holder: CoinHolder)->CoinHolder:
        self.coin_holder = self.coin_holder + client_coin_holder
        self.refund = self.refund + client_coin_holder
        return self.coin_holder

    def save_drink_coin(self, drink_type: Drink)->CoinHolder:
        drink_coins = self.refund.calc_coin(drink_type.value["price"])
        self.refund = self.refund - drink_coins
        return self.coin_holder

    def refund_coin(self)->CoinHolder:
        refund = copy.deepcopy(self.refund)
        self.coin_holder = self.coin_holder - self.refund
        self.refund.reset()
        return refund

    def calc_coin(self, drink_type: Drink):
        if self.has_enough_coin(drink_type):
            change = self.refund.sum() - drink_type.value["price"]
            return self.coin_holder.calc_coin(change)
        return None

    def has_enough_coin(self, drink_type: Drink)->bool:
        change = self.refund.sum() - drink_type.value["price"]
        return self.coin_holder.has_enough_coin(change)

    def coin_shortage(self, drink_type: Drink)->bool:
        change = self.refund.sum() - drink_type.value["price"]
        return not self.coin_holder.has_enough_coin(change)
