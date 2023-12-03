MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0.0


def user_choice():
    """Returns what user would like to drink or do"""
    input_str = "What would you like? (espresso/latte/cappuccino): "
    possible_choices = ['espresso', 'latte', 'cappuccino', 'report', 'off']
    ans = input(input_str)

    while ans not in possible_choices:
        ans = input("Wrong answer! Choose only from the possibilities! " + input_str)

    return ans


def off():
    """Exit code - Prints out a leaving message"""
    print("Shutting down...")


def report():
    """Prints out the resources and profit of the coffee machine"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def make_coffee(choice):
    global money

    if is_resources_sufficient(MENU[choice]['ingredients']):
        inserted_money = process_coins()

        if check_transaction(choice, inserted_money):
            money += MENU[choice]['cost']

            return_money = inserted_money - MENU[choice]['cost']
            print(f"Here is ${round(return_money,2)} dollars in change.")

            resources['water'] -= MENU[choice]['ingredients']['water']
            resources['coffee'] -= MENU[choice]['ingredients']['coffee']
            if choice != 'espresso':
                resources['milk'] -= MENU[choice]['ingredients']['milk']
        else:
            print("Sorry that's not enough money. Money refunded.")


def is_resources_sufficient(order_ingredients):
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            is_enough = False

    return is_enough


def check_transaction(drink, inserted_money):
    """Returns true or false depends on whether inserted money is enough for the chosen drink or not"""
    if inserted_money >= MENU[drink]['cost']:
        return True
    else:
        return False


def process_coins():
    quarters = int(input("How many quarters do you give? "))
    dimes = int(input("How many dimes do you give? "))
    nickles = int(input("How many nickles do you give? "))
    pennies = int(input("How many pennies do you give? "))

    return 0.25*quarters + 0.10*dimes + 0.05*nickles + 0.01*pennies


def coffee_machine():
    """Coffee machine in work"""
    choice = ""

    while choice != "off":
        choice = user_choice()

        if choice == "off":
            off()
        elif choice == "report":
            report()
        else:
            make_coffee(choice=choice)


coffee_machine()
