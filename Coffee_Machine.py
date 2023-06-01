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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

machineStatus = True
money = 0

def report():
    for i in resources:
        print(i + ":", resources[i])
def resourcesLeft(beverage):
    for i in MENU[beverage]["ingredients"]:
        if resources[i] >= MENU[beverage]["ingredients"][i]:
            return True
        else:
            print("Please refill " + i + "!")
            return False
def coins(beverage):
    total = 0
    pennies = int(input("how many pennies?: "))
    total += pennies
    nickles = int(input("how many nickles?: "))
    total += nickles * 5
    dimes = int(input("how many dimes?: "))
    total += dimes * 10
    quarters = int(input("how many quarters?: "))
    total += quarters * 25
    if (total / 100 >= MENU[beverage]["cost"]):
        print("Here, your change is $" + str(total / 100 - MENU[beverage]["cost"]))
        return True
    return False, 0
def updateResources(beverage):
    for i in MENU[beverage]["ingredients"]:
        resources[i] -= MENU[beverage]["ingredients"][i]


while (machineStatus):
    selection = input("What would you like? (espresso/latte/cappuccino): ")
    if selection == "off":
        machineStatus = False
        break
    if selection == "report":
        report()
        print("profit: " + str(money))
        continue
    if resourcesLeft(selection):
        if coins(selection):
            money += MENU[selection]["cost"]
            updateResources(selection)
            print("Here is your " + str(selection) + ". Enjoy!")
        else:
            print("Please insert more funds")
