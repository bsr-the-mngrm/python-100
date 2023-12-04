from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

if __name__ == '__main__':
    my_coffee_maker = CoffeeMaker()
    my_menu = Menu()
    my_money_machine = MoneyMachine()

    user_input = ""

    while user_input != "off":
        user_input = input(f"What would you like? ({my_menu.get_items()}): ")
        user_choice = my_menu.find_drink(user_input)

        if user_input == "report":
            my_coffee_maker.report()
            my_money_machine.report()
        elif user_choice is not None:
            if my_coffee_maker.is_resource_sufficient(user_choice):
                if my_money_machine.make_payment(user_choice.cost):
                    my_coffee_maker.make_coffee(user_choice)

