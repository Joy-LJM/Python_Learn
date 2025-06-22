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


# espresso 50, 18g
# latte: 200ml, 24g, 150ml milk
# cappuccino: 250ml, 24g, 100ml milk

# TODO-2: Check resource enough or not
def check_resources(drink_type):
    ingredients = MENU[drink_type]["ingredients"]

    for item in ingredients:
        if resources[item] <= ingredients[item]:
            print(f"Sorry, there is not enough {item}.")
            return False

    return True


# TODO-3: Reduce Resources
def make_coffee(drink_type):
    ingredients = MENU[drink_type]["ingredients"]
    for item in ingredients:
        resources[item] -= ingredients[item]


# TODO-1：print report
should_off = False
earn_money = 0

while not should_off:
    choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if choice == "report":
        for key in resources:
            print(f"{key.capitalize()}: {resources[key]}ml")
        print(f"Money: ${earn_money}")
    elif choice == 'off':
        should_off = True
    else:
        is_resource_enough = check_resources(choice)
        if is_resource_enough:
            print("Please insert coins.")
            quarters_amount = int(input("How many quarters?: "))
            dimes_amount = int(input("How many dimes?: "))
            nickles_amount = int(input("How many nickles?: "))
            pennies_amount = int(input("How many pennies?: "))
            quarter = 0.25
            dime = 0.10
            nickle = 0.05
            penny = 0.01
            cost = MENU[choice]["cost"]
            amount = quarters_amount * quarter + dime * dimes_amount + nickle * nickles_amount + pennies_amount * penny

            if amount >= cost:
                change = "{:.2f}".format(amount - cost)
                print(f"Here is ${change} in change")
                earn_money += cost
                make_coffee(choice)
                print(f"Here is your {choice}☕, please enjoy!")
            elif amount < cost:
                print("Sorry that's not enough money. Money refunded.")
