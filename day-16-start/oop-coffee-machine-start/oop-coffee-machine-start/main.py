from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

class CoffeMachine:
    
    def Machine():
        objMenu = Menu()
        objCoffeMaker = CoffeeMaker()
        objMoneyMachine = MoneyMachine()
        while True:
            
            choice = input(f"What would you like? ({objMenu.get_items()}) :")

            if choice == "off":
                break
            elif choice == "report":
                objCoffeMaker.report()
                objMoneyMachine.report()
            else:
                drink = objMenu.find_drink(choice)
                if drink == None:
                    continue
                if objCoffeMaker.is_resource_sufficient(drink) and objMoneyMachine.make_payment(drink.cost):
                    objCoffeMaker.make_coffee(drink)
                
                




    if __name__ == "__main__":
        Machine()