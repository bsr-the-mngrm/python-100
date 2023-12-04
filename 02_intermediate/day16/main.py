from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

if __name__ == '__main__':
    my_coffee_maker = CoffeeMaker()
    my_menu = Menu()
    my_money_machine = MoneyMachine()

    user_input = ""

    while user_input != "off":
        user_input = input()
