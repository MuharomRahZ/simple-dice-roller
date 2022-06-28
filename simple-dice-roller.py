import random as rd

mataDadu1 = {
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6
}

mataDadu2 = {
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6
}

def mainMenu():
    try:
        print(f"==================================")
        print(f"WELCOME TO THE SIMPLE DICE ROLLER!")
        print(f"This program will help you roll a dice or two")
        print(f"---CHOOSE MENU---\n1. ROLL ONE DICE\n2. ROLE TWO DICES\n3. EXIT")
        menu = int(input("Enter your menu choice: "))
        opsiMenu(menu)
    except Exception as exception:
        print("Error: %s!\n\n" % exception)

def opsiMenu(menu):
    if menu == 1:
        rollOneDice()
    elif menu == 2:
        rollTwoDices()
    elif menu == 3:
        print("Thank you for using the Simple Dice Roller!")
        exit()
    else:
        print("Invalid menu choice!")
        mainMenu()

def rollOneDice():
    print(f"==============================")
    print(f"You have chosen to roll a dice")
    print(f"------------------------------")
    print(f"|Hasil Mata Dadu:            |")
    roll = mataDadu1[rd.randint(1,6)]
    print(f"|              {roll}             |")
    print(f"------------------------------")
    print(f"==============================")
    print()
    mainMenu()

def rollTwoDices():
    print(f"=================================")
    print(f"You have chosen to roll two dices")
    print(f"---------------------------------")
    print(f"|Hasil Mata Dadu:               |")
    print(f"---------------------------------")
    roll1 = mataDadu1[rd.randint(1,6)]
    roll2 = mataDadu2[rd.randint(1,6)]
    print(f"|  Dadu Pertama  |  Dadu Kedua  |")
    print(f"|       {roll1}        |      {roll2}       |")
    # print(f"The dices have been rolled and they're {roll1} and {roll2}")
    print(f"---------------------------------")
    print(f"=================================")
    print()
    mainMenu()

mainMenu()