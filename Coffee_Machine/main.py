#Coffee Machine
#20-08-2021

from Ingredients import MENU
from Ingredients import resources
from logo_data import logo
import os

clear = lambda: os.system('cls')

PENNY = 1
NICKEL = 5
DIME = 10
QUARETER = 25

def print_report():
    '''Prints the ingredients left in the machine'''
    print("\nIngredients left:")
    print(f"Water : {resources['water']} ml")
    print(f"Milk : {resources['milk']} ml")
    print(f"Coffee : {resources['coffee']} g")


def check_resources(choice):
    '''Checks if enough ingredients is present in the machine'''
    for items in MENU[choice]['ingredients']:
        if resources[items] - MENU[choice]['ingredients'][items] >= 0:
            return True
        else:
            return False


def check_coins(choice):
    '''Checks the coin given by the user'''
    print("\nEnter the coins for transaction to proceed:")
    print(f"Your order costs $ {MENU[choice]['cost']}.\n")
    quarter = int(input("Enter quarter: "))
    dime = int(input("Enter dime: "))
    nickel = int(input("Enter nickel: "))
    penny = int(input("Enter penny: "))

    price = quarter*QUARETER + dime*DIME + nickel*NICKEL + penny*PENNY
    if price > MENU[choice]['cost']*100:
        print(f"\nExtra money: {price - MENU[choice]['cost']*100} cents refunded.")
        return True
    elif price == MENU[choice]['cost']*100:
        return True
    else:
        return False


def resource_deduction(choice):
    '''Detects the resources from the total ingredients in the machine'''
    for items in MENU[choice]['ingredients']:
        resources[items] -= MENU[choice]['ingredients'][items]


decision = "yes"
while decision == "yes":
    print(logo)
    print("Welcome to the 'Coffee Machine'!\n")
    choice = input("What would you like to have?(espresso/latte/cappuccino)\n")

    if choice == "espresso" or choice == "latte" or choice == "cappuccino":
        resources_ingredients = check_resources(choice)
        if resources_ingredients == True:
            resources_coins = check_coins(choice)
            if resources_coins == True:
                print("\nTransaction successful.")
                print(f"\nHere is your {choice}. ENJOY")
                resource_deduction(choice)
                print_report()
                decision = input("\nIf you would like to order something else type 'yes' otherwise 'no'.\n")
                clear()
            else:
                print(f"\n{choice} cannot be made as coins entered are not enough. Money refunded.")
                decision = input("\nIf you would like to order something else type 'yes' otherwise 'no'.\n")
                clear()
        else:
            print(f"\n{choice} cannot be made as enough ingredients are not available.")
            print_report()
            decision = 'no'
            

print("\nCome back soon.\n")
resources['water'] = 300
resources['milk'] = 200
resources['coffee'] = 100