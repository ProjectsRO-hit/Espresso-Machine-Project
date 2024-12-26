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

def turn_off():
    """Turn off the coffee machine."""
    global coffee_machine_status
    coffee_machine_status = False


def print_report():
    """Print the current status of the coffee machine's resources."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def resources_sufficient(order):
    """Check if resources are sufficient for the given order."""
    for item in MENU[order]["ingredients"]:
        if MENU[order]["ingredients"][item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def process_coins():
    """Process coins inserted by the user and return the total amount."""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def transaction_successful(payment, cost):
    """Check if the transaction is successful based on payment and cost."""
    if payment >= cost:
        change = round(payment - cost, 2)
        if change > 0:
            print(f"Here is ${change} in change.")
        global money
        money += cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def make_coffee(order):
    """Deduct the required ingredients from the resources and make the coffee."""
    for item in MENU[order]["ingredients"]:
        resources[item] -= MENU[order]["ingredients"][item]
    print(f"Here is your {order} 🍵. Enjoy!")


coffee_machine_status = True
money = 0

while coffee_machine_status:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == "off":
        turn_off()
    elif user_choice == "report":
        print_report()
    elif user_choice in MENU:
        if resources_sufficient(user_choice):
            payment = process_coins()
            if transaction_successful(payment, MENU[user_choice]["cost"]):
                make_coffee(user_choice)
    else:
        print("Error! No such items available! Please try again.")
 # type: ignore