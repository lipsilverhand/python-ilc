import menu
import coffee_maker
import money_machine

money_machine = money_machine.MoneyMachine()
coffee_maker = coffee_maker.CoffeeMaker()
menu = menu.Menu()

ready = True

while ready:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        ready = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
          coffee_maker.make_coffee(drink)
