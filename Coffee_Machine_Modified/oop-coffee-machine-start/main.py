#Modifying a Coffee Machine Program
#Date: 26-08-2021

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import os
clear = lambda: os.system('cls')

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

decision = "yes"
clear()
while decision == "yes":
    print("\n \033[1m Welcome to the coffee machine. \033[0m\n")
    choice = menu.get_items()
    question = input(f"What would you like to order? {choice}\n")

    if question == "report":
        coffee_maker.report()
        money_machine.report()
    elif question == "off":
        decision = "no"
    else:
        drink = menu.find_drink(question)
        is_ingredient_sufficient = coffee_maker.is_resource_sufficient(drink)

        print(f"Your {question} cost $ {drink.cost}.\n")
        is_money_sufficient = money_machine.make_payment(drink.cost)
        if is_ingredient_sufficient == True and is_money_sufficient == True:
            coffee_maker.make_coffee(drink)
            print("\n")
        elif is_ingredient_sufficient == False:
            coffee_maker.report()







