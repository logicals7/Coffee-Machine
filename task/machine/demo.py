def ingredients_avail():
    print('''The coffee machine has:
400 of water
540 of milk
120 of coffee beans
9 of disposable cups
550 of money
    ''')


def buy():
    buy_option = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")

    if buy_option == "1":
        espresso_water_need = 250
        espresso_coffee_beans_need = 16
        espresso_cost = 4

        x = print("\nThe coffee machine has:\n", avail_water - espresso_water_need, "of water\n",
                  avail_milk, "of milk\n",
                  avail_coffee_beans - espresso_coffee_beans_need, "of coffee beans\n", avail_disposable_cups - 1,
                  "of disposable cups\n",
                  avail_money + espresso_cost, "of money")
        return x

    elif buy_option == "2":
        latte_water_need = 350
        latte_milk_need = 75
        latte_coffee_beans_need = 20
        latte_cost = 7
        x = print("\nThe coffee machine has:\n", avail_water - latte_water_need, "of water\n",
                  avail_milk - latte_milk_need, "of milk\n",
                  avail_coffee_beans - latte_coffee_beans_need, "of coffee beans\n", avail_disposable_cups - 1,
                  "of disposable cups\n",
                  avail_money + latte_cost, "of money")
        return x

    elif buy_option == "3":
        cappuccino_water_need = 200
        cappuccino_milk_need = 100
        cappuccino_coffee_beans_need = 12
        cappuccino_cost = 6
        x = print("\nThe coffee machine has:\n", avail_water - cappuccino_water_need, "of water\n",
                  avail_milk - cappuccino_milk_need, "of milk\n",
                  avail_coffee_beans - cappuccino_coffee_beans_need, "of coffee beans\n", avail_disposable_cups - 1,
                  "of disposable cups\n",
                  avail_money + cappuccino_cost, "of money")
        return x


def fill():
    water_fill_amt = int(input("Write how many ml of water do you want to add:"))
    milk_fill_amt = int(input("Write how many ml of milk do you want to add:"))
    coffee_beans_fill_amt = int(input("Write how many grams of coffee beans do you want to add:"))
    disposable_cups_fill_amt = int(input("Write how many disposable cups of coffee do you want to add:"))

    x = print("\nThe coffee machine has:\n", avail_water + water_fill_amt, "of water\n", avail_milk + milk_fill_amt,
              "of milk\n",
              avail_coffee_beans + coffee_beans_fill_amt, "of coffee beans\n",
              avail_disposable_cups + disposable_cups_fill_amt, "of disposable cups\n",
              avail_money, "of money")
    return x


def take():
    print("I gave you $" + str(avail_money))
    x = print("\nThe coffee machine has:\n", avail_water, "of water\n", avail_milk, "of milk\n",
              avail_coffee_beans, "of coffee beans\n", avail_disposable_cups, "of disposable cups\n",
              avail_money - avail_money, "of money")
    return x


def remaining():


def exit():
    pass


# ingredients available initially
avail_water = 400
avail_milk = 540
avail_coffee_beans = 120
avail_disposable_cups = 9
avail_money = 550

# variable declared for remaining amt of ingredients


# main code
ingredients_avail()

while True:
    choose_option = input("Write action (buy, fill, take, remaining, exit):")
    if choose_option == "buy":
        buy()
    elif choose_option == "fill":
        fill()
    elif choose_option == "take":
        take()
    elif choose_option == "remaining":
        remaining()
    elif choose_option == "exit":
        break