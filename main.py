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

def getMoney():
    print("Please insert coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    return ((quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01))

def resourceCheck(drink):
    if drink == "espresso":
        if resources.get("water") < MENU.get(drink).get("ingredients").get("water"):
            return 0
        elif resources.get("coffee") < MENU.get(drink).get("ingredients").get("coffee"):
            return 1
        else:
            return 4
    else:
        if resources.get("water") < MENU.get(drink).get("ingredients").get("water"):
            return 0
        elif resources.get("coffee") < MENU.get(drink).get("ingredients").get("coffee"):
            return 1
        elif resources.get("milk") < MENU.get(drink).get("ingredients").get("milk"):
            return 2
        else:
            return 4

output = ["water", "coffee", "milk"]


while input != "off":
    userInput = input("What would you like? (espresso/latte/cappuccino): ")
    if userInput == "report":
        print("Water: ", resources["water"], "ml")
        print("Milk: ", resources["milk"], "ml")
        print("Coffee: ", resources["coffee"], "g")
    elif userInput == "off":
        break
    elif userInput == "espresso":
        resource = resourceCheck("espresso")
        if resource == 4:
            cash = getMoney()
            if cash > MENU.get("espresso").get("cost"):
                cash = cash - float(MENU["espresso"]["cost"])
                resources["water"] = resources.get("water") - MENU.get("espresso").get("ingredients").get("water")
                resources["coffee"] = resources.get("coffee") - MENU.get("espresso").get("ingredients").get("coffee")
                if cash != 0:
                    print("Here is $%1.2f in change." %(cash))
                print("Here is your espresso, enjoy!")
            else:
                print("Sorry that's not enough money. Cash refunded.")
        else:
            print("Sorry there is not enough", output[resource])
    elif userInput == "latte":
        resource = resourceCheck("latte")
        if resource == 4:
            cash = getMoney()
            if cash > MENU.get("latte").get("cost"):
                cash = cash - float(MENU["latte"]["cost"])
                resources["water"] = resources.get("water") - MENU.get("latte").get("ingredients").get("water")
                resources["coffee"] = resources.get("coffee") - MENU.get("latte").get("ingredients").get("coffee")
                resources["milk"] = resources.get("milk") - MENU.get("latte").get("ingredients").get("milk")
                if cash != 0:
                    print("Here is $%1.2f in change." %(cash))
                print("Here is your latte, enjoy!")
            else:
                print("Sorry that's not enough money. Cash refunded.")
        else:
            print("Sorry there is not enough", output[resource])
    elif userInput == "cappuccino":
        resource = resourceCheck("cappuccino")
        if resource == 4:
            cash = getMoney()
            if cash > MENU.get("cappuccino").get("cost"):
                cash = cash - float(MENU["cappuccino"]["cost"])
                resources["water"] = resources.get("water") - MENU.get("cappuccino").get("ingredients").get("water")
                resources["coffee"] = resources.get("coffee") - MENU.get("cappuccino").get("ingredients").get("coffee")
                resources["milk"] = resources.get("milk") - MENU.get("cappuccino").get("ingredients").get("milk")
                if cash != 0:
                    print("Here is $%1.2f in change." %(cash))
                print("Here is your cappuccino, enjoy!")
            else:
                print("Sorry that's not enough money. Cash refunded.")
        else:
            print("Sorry there is not enough", output[resource])
