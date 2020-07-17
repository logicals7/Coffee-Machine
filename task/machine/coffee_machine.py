# class for defining variables for ingredients_needed
class IngredientsNeeded:
    def __init__(self,water_needed, milk_needed, coffee_beans_needed, cost_needed):
        self.water_needed = water_needed
        self.milk_needed = milk_needed
        self.coffee_beans_needed = coffee_beans_needed
        self.cost_needed = cost_needed

# Instances & class for individual coffee type requirement
class IndividualCoffeeRequirement:
    espresso_ingredients_req = IngredientsNeeded(250, 0, 16, 4)
    latte_ingredients_req = IngredientsNeeded(350, 75, 20, 7)
    cappuccino_ingredients_req = IngredientsNeeded(200, 100, 12, 6)

# class for choosing user actions
class Actions:
    def __init__(self):
        self.avail_water = 400
        self.avail_milk = 540
        self.avail_coffee_beans = 120
        self.avail_money = 550
        self.avail_disposable_cups = 9

    def check_possible(self, coffee):
        if self.avail_water < coffee.water_needed:
            print("Sorry, not enough water!")
        elif self.avail_milk < coffee.milk_needed:
            print('Sorry, not enough milk!')
        elif self.avail_coffee_beans < coffee.coffee_beans_needed:
            print('Sorry, not enough coffee beans!')
        elif self.avail_disposable_cups < 1:
            print('Sorry, not enough disposable cups!')
        else:
            print('I have enough resources, making you a coffee!')
            self.avail_water -= coffee.water_needed
            self.avail_milk -= coffee.milk_needed
            self.avail_coffee_beans -= coffee.coffee_beans_needed
            self.avail_disposable_cups -= 1
            self.avail_money += coffee.cost_needed


    def buy(self):
        buy_option = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if buy_option == "1":
            self.check_possible(IndividualCoffeeRequirement.espresso_ingredients_req)
        elif buy_option == "2":
            self.check_possible(IndividualCoffeeRequirement.latte_ingredients_req)
        elif buy_option == "3":
            self.check_possible(IndividualCoffeeRequirement.cappuccino_ingredients_req)
        elif buy_option == "back":
            while True:
                break

    def fill(self):
        self.water_fill_amt = int(input("Write how many ml of water do you want to add:"))
        self.milk_fill_amt = int(input("Write how many ml of milk do you want to add:"))
        self.coffee_beans_fill_amt = int(input("Write how many grams of coffee beans do you want to add:"))
        self.disposable_cups_fill_amt = int(input("Write how many disposable cups of coffee do you want to add:"))

        self.avail_water += self.water_fill_amt
        self.avail_milk += self.milk_fill_amt
        self.avail_coffee_beans += self.coffee_beans_fill_amt
        self.avail_disposable_cups += self.disposable_cups_fill_amt

    def take(self):
        x = print("I gave you $" + str(self.avail_money))
        #updating ingredients amount
        self.avail_money -= self.avail_money

    def remaining(self):
        print("The cofffe machine has:\n", self.avail_water, "of water\n", self.avail_milk, "of milk\n",
                  self.avail_coffee_beans, "of coffee beans\n", self.avail_disposable_cups, "of disposable cups\n",
                  "$" + str(self.avail_money), "of money")


class CoffeeMachine:
    def __init__(self):
        self.actions = Actions()
        self.individual_coffee_requirement = IndividualCoffeeRequirement()
        self.final_machine()

    def final_machine(self):
        while True:
            action = input('Write action (buy, fill, take, remaining, exit): ')
            print()
            if action == 'buy':
                self.actions.buy()
                print()
            elif action == 'fill':
                self.actions.fill()
                print()
            elif action == 'take':
                self.actions.take()
                print()
            elif action == 'remaining':
                self.actions.remaining()
                print()
            elif action == 'exit':
                break

run_machine = CoffeeMachine()