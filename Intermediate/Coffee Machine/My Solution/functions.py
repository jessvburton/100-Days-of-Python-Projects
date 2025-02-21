from configs import *


def check_resources(customer_order):
    for item in MENU[customer_order]['ingredients']:
        if resources[item] >= MENU[customer_order]['ingredients'][item]:
            return True
        else:
            print(f"Sorry, there is not enough {item}")
            return


def process_money(customer_order):
    cost = MENU[customer_order].get('cost')
    print(f"A {customer_order} costs ${cost}")
    print("Please insert coins.")

    quarters = int(input("How many quarters? ")) * COIN_VALUES.get('quarter')
    dimes = int(input("How many dimes? ")) * COIN_VALUES.get('dime')
    nickles = int(input("How many nickles? ")) * COIN_VALUES.get('nickle')
    pennies = int(input("How many pennies? ")) * COIN_VALUES.get('penny')

    total_coins = quarters + pennies + nickles + dimes
    change = round(total_coins - cost, 2)

    if total_coins < cost:
        print("Sorry that is not enough money. Money refunded.")
        return
    else:
        print(f"Here is ${change} in change.")
        return True


def make_coffee(customer_order):
    resources['money'] += MENU[customer_order]['cost']
    for item in MENU[customer_order]['ingredients']:
        resources[item] -= MENU[customer_order]['ingredients'][item]

    print(f"Enjoy your {customer_order}")


def place_order(customer_order):
    step1 = check_resources(customer_order)
    if step1:
        step2 = process_money(customer_order)
        if step2:
            make_coffee(customer_order)


def machine_working():
    machine_on = True

    while machine_on:
        customer_order = input("What would you like? (espresso/latte/cappuccino)\n").lower()

        if customer_order == "report":
            for keys, values in resources.items():
                print(keys, ':', values)
        elif customer_order == "off":
            machine_on = False
        elif customer_order == "espresso" or customer_order == "latte" or customer_order == "cappuccino":
            place_order(customer_order)
        else:
            print("Command not recognised. Try again.")
