from vending_machine import VendingMachine
from drink import Drink

if __name__ == '__main__':
    money = 200
    drinkType = 0
    vendingMachine = VendingMachine()
    myDrink = vendingMachine.buy(money, drinkType)
    change = vendingMachine.refund()
    print(myDrink)
    print(change)
