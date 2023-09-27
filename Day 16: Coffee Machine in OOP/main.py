from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

machine_on = True

while machine_on:
    menu_items = menu.get_items()
    order_name = input(f"What would you like? {menu_items}?\n").lower()

    if order_name == "report":
        print(money_machine.report())
        print(coffee_maker.report())
    elif order_name == "off":
        machine_on = False
    else:
        drink = menu.find_drink(order_name)

        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
