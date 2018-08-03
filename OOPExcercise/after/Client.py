from drink import Drink
from coin_holder import CoinHolder
from vending_machine import VendingMachine
from coin import Coin

if __name__ == '__main__':
    my_vending_machine = VendingMachine()
    coins = CoinHolder(yen_500=0, yen_100=12, yen_10=10)

    my_drink = my_vending_machine.buy(coins, Drink.COKE)
    refund = my_vending_machine.refund()

    print("my_drink:", my_drink)
    print("refund: ", refund.__dict__)
    print("vending_coins: ", my_vending_machine.vending_coin_holder.coin_holder.__dict__)
    print("vending_drinks: ", my_vending_machine.drink_holder.__dict__)

    for coins in Coin:
        print()
