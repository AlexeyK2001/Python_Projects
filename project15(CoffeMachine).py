# TODO 1. Print the report of existing machine resources
# TODO 2. Check resources sufficient to make drink order

import time
import sys
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 100,
            "milk": 200,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 70,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

water = 500
milk = 500
coffee = 300
money = 0


def make_coffee(choice):
    global water, milk, coffee
    """Subtracts ingredients from available resources"""
    water -= MENU[choice]["ingredients"]["water"]
    milk -= MENU[choice]["ingredients"]["milk"]
    coffee -= MENU[choice]["ingredients"]["coffee"]
    making_a_choice()

def process_coins(choice):
    """Processes the inserted coins"""
    global money
    global enough_money
    enough_money = True
    print("Please insert coins.")
    coffee_price = MENU[choice]["cost"]
    num_of_quarters = int(input("How many quarters?: "))
    num_of_dimes = int(input("How many dimes?: "))
    num_of_nickles = int(input("How many nickles?: "))
    num_of_pennies = int(input("How many pennies?: "))
    money_inserted = num_of_quarters*0.25+num_of_dimes*0.1+num_of_nickles*0.05+num_of_pennies*0.01
    money += money_inserted
    if coffee_price < money_inserted:
        print(f"Here is ${round(money_inserted-coffee_price,2)} dollars in change.\n")
        money = money - (money_inserted-coffee_price)
        print(f"Here is your {choice} ☕ Enjoy!")
        make_coffee(choice)
    elif coffee_price == money_inserted:
        print("Thanks for purchasing without a change!")
        make_coffee(choice)
    else:
        print("Sorry, that's not enough money. Money refunded.")
        money -= money_inserted
        making_a_choice()


def user_choice(choice):
    """Processes the user choice and reacts"""
    if water >= MENU[choice]["ingredients"]["water"]:
        if milk >= MENU[choice]["ingredients"]["milk"]:
            if coffee >= MENU[choice]["ingredients"]["coffee"]:
                process_coins(choice)
            else:
                print("Sorry, there is not enough coffee.")
                making_a_choice()
                time.sleep(0.5)
        else:
            print("Sorry, there is not enough milk.")
            making_a_choice()
            time.sleep(0.5)
    else:
        print("Sorry, there is not enough water.")
        making_a_choice()
        time.sleep(0.5)


def report(water_available, milk_available, coffee_available, money_available):
    """Outputs the available resources and money in the machine"""
    print(f"Water: {water_available}ml\nMilk: {milk_available}ml\nCoffee: {coffee_available}g\nMoney: ${money_available}")
    making_a_choice()


def making_a_choice():
    """Asks user to make a choice of a drink"""
    global choice
    choice = input("What would you like to buy? (espresso / latte / cappuccino): ").lower()
    if choice == "off":
        sys.exit()
    if choice == "report":
        report(water, milk, coffee, money)
    user_choice(choice)
    

making_a_choice()

