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


def get_report(resources, money):
    return f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money}"


def check_resources(selection, resources, MENU):
    enough = True
    for ingredient in MENU[selection]['ingredients']:
        #print(resources[ingredient])
        #print(MENU[selection]['ingredients'][ingredient])
        if (resources[ingredient] - MENU[selection]['ingredients'][ingredient] >= 0):
            enough = True
        else:
            print(f" Sorry there is not enough {ingredient}")
            return False
    return enough


def make_coffee(selection, resources, MENU):
    res = {}
    print(f"Here is your {selection} ☕ Enjoy!")
    for ingredient in MENU[selection]['ingredients']:
        res[ingredient] = resources[ingredient] - MENU[selection]['ingredients'][ingredient]
        #print(res[ingredient])
    if selection == 'espresso':
        res['milk'] = resources['milk']
    return res


def process_coins():
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    total = round((quarters * .25) + (dimes * .1) + (nickles * .05) + (pennies * .01), 2)
    return total


def coffee_machine():
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }
    machine_should_continue = True
    money = 0
    while machine_should_continue:
        selection = input(" What would you like? (espresso/latte/cappuccino): ").lower()
        if selection == 'off':
            machine_should_continue = False
        elif selection == 'report':
            print(get_report(resources, money))
        elif selection == 'espresso' or selection == 'latte' or selection == 'cappuccino':
            if check_resources(selection, resources, MENU):
                #print('Enough resources')
                provided_money = process_coins()
                #print(provided_money)
                if provided_money >= MENU[selection]['cost']:
                    change = provided_money - MENU[selection]['cost']
                    money += MENU[selection]['cost']
                    print(f"Here is ${change} in change.")
                    #print(money)
                    resources = make_coffee(selection, resources, MENU)
                    #print(resources)
                else:
                    print("Sorry that's not enough money. Money refunded")
        else:
            print('Invalid selection')


coffee_machine()