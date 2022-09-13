from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

maker = CoffeeMaker()
machine = MoneyMachine()
menu =Menu()

is_on = True
while is_on:
    options = menu.get_items()
    ask_user = input((f"Which coffe do you want {options}"))
    if ask_user == 'off':
        is_on = False
    elif ask_user == 'report':
        maker.report()
        machine.report()
    else:
        drink = menu.find_drink(ask_user)
        if maker.is_resource_sufficient(drink) == True:
            if machine.make_payment(drink.cost):
                maker.make_coffee(drink)
            else:
                is_on = False
        else:
            is_on = False







