Depository = {
    "water": {"value": 400, "text": "of water"},
    "milk": {"value": 540, "text": "of milk"},
    "beans": {"value": 120, "text": "of coffee beans"},
    "cups": {"value": 9, "text": "disposable cups"},
    "money": {"sign": "$", "value": 550, "text": "of money"}}


def remaining():
    global Depository
    print("The coffee machine has:")
    print(Depository["water"]["value"], Depository["water"]["text"])
    print(Depository["milk"]["value"], Depository["milk"]["text"])
    print(Depository["beans"]["value"], Depository["beans"]["text"])
    print(Depository["cups"]["value"], Depository["cups"]["text"])
    print(Depository["money"]["sign"] + str(Depository["money"]["value"]), Depository["money"]["text"])
    return action()


def buy():
    global Depository
    a = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n> ")
    if a == '1':
        if Depository["water"]["value"] >= 250 and Depository["beans"]["value"] >= 16 and Depository["cups"]["value"] >= 1:
            print("I have enough resources, making you a coffee!")
            Depository["water"]["value"] -= 250
            Depository["beans"]["value"] -= 16
            Depository["money"]["value"] += 4
            Depository["cups"]["value"] -= 1
        elif Depository["water"]["value"] < 250:
            print("Sorry, not enough water!")
        elif Depository["beans"]["value"] < 16:
            print("Sorry, not enough coffee beans!")
        elif Depository["cups"]["value"] < 1:
            print("Sorry, not enough disposable cups!")
    elif a == '2':
        if Depository["water"]["value"] >= 350 and Depository["beans"]["value"] >= 20 and Depository["milk"]["value"] >= 75 and Depository["cups"]["value"] >= 1:
            print("I have enough resources, making you a coffee!")
            Depository["water"]["value"] -= 350
            Depository["milk"]["value"] -= 75
            Depository["beans"]["value"] -= 20
            Depository["money"]["value"] += 7
            Depository["cups"]["value"] -= 1
        elif Depository["water"]["value"] < 350:
            print("Sorry, not enough water!")
        elif Depository["milk"]["value"] < 75:
            print("Sorry, not enough milk!")
        elif Depository["beans"]["value"] < 20:
            print("Sorry, not enough coffee beans!")
        elif Depository["cups"]["value"] < 1:
            print("Sorry, not enough disposable cups!")
    elif a == '3':
        if Depository["water"]["value"] >= 200 and Depository["beans"]["value"] >= 12 and Depository["milk"]["value"] >= 100 and Depository["cups"]["value"] >= 1:
            print("I have enough resources, making you a coffee!")
            Depository["water"]["value"] -= 200
            Depository["milk"]["value"] -= 100
            Depository["beans"]["value"] -= 12
            Depository["money"]["value"] += 6
            Depository["cups"]["value"] -= 1
        elif Depository["water"]["value"] < 200:
            print("Sorry, not enough water!")
        elif Depository["milk"]["value"] < 100:
            print("Sorry, not enough milk!")
        elif Depository["beans"]["value"] < 12:
            print("Sorry, not enough coffee beans!")
        elif Depository["cups"]["value"] < 1:
            print("Sorry, not enough disposable cups!")
    return action()


def fill():
    global Depository
    Depository["water"]["value"] += int(input("Write how many ml of water do you want to add:\n> "))
    Depository["milk"]["value"] += int(input("Write how many ml of milk do you want to add:\n> "))
    Depository["beans"]["value"] += int(input("Write how many grams of coffee beans do you want to add:\n> "))
    Depository["cups"]["value"] += int(input("Write how many disposable cups of coffee do you want to add:\n> "))
    return action()


def take():
    print("I gave you", Depository["money"]["sign"] + str(Depository["money"]["value"]))
    Depository["money"]["value"] = 0
    return action()


def action():
    while True:
        a = input("Write action (buy, fill, take, remaining, exit):\n> ").lower()
        if a == "buy":
            return buy()
        elif a == "fill":
            return fill()
        elif a == "take":
            return take()
        elif a == "remaining":
            return remaining()
        elif a == "exit":
            break
        else:
            print("error")


action()
