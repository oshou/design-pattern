from coin import Coin
import copy


class CoinHolder:

    def __init__(self, yen_500=0, yen_100=0, yen_10=0):
        self.coin_stocks = {}
        self.coin_stocks.update({Coin.YEN_500.name: yen_500})
        self.coin_stocks.update({Coin.YEN_100.name: yen_100})
        self.coin_stocks.update({Coin.YEN_10.name: yen_10})

    def __add__(self, other):
        new_holder = CoinHolder()

        for coin in Coin:
            new_holder.coin_stocks[coin.name] = \
                self.coin_stocks[coin.name] + other.coin_stocks[coin.name]

        return new_holder

    def __sub__(self, other):
        new_holder = CoinHolder()

        for coin in Coin:
            new_holder.coin_stocks[coin.name] = \
                self.coin_stocks[coin.name] - other.coin_stocks[coin.name]

        return new_holder

    def sum(self):
        sum_of_coins = 0

        for coin in Coin:
            sum_of_coins += self.coin_stocks[coin.name] * coin.value

        return sum_of_coins

    def reset(self):
        for coin in Coin:
            self.coin_stocks[coin.name] = 0
        return self

    def calc_coin(self, change: int):
        my_coin_holder = CoinHolder()
        val = change
        coin_stocks = copy.deepcopy(self.coin_stocks)

        for coin in Coin:
            while val - coin.value >= 0 and coin_stocks[coin.name] > 0:
                val -= coin.value
                coin_stocks[coin.name] -= 1
                my_coin_holder.coin_stocks[coin.name] += 1

        return my_coin_holder

    def has_enough_coin(self, change: int):
        val = change
        coin_stocks = copy.deepcopy(self.coin_stocks)
        for coin in Coin:
            while val - coin.value >= 0 and coin_stocks[coin.name] > 0:
                val -= coin.value
                coin_stocks[coin.name] -= 1

        if val == 0:
            return True

        return False
