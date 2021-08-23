import random


def diceSim():

    x = random.randint(1, 6)

    if (x == 1):
        print(
            "[-----------]\n[           ]\n[     0     ]\n[           ]\n[-----------]")
    elif(x == 2):
        print(
            "[-----------]\n[           ]\n[   0   0   ]\n[           ]\n[-----------]")
    elif(x == 3):
        print(
            "[-----------]\n[     0     ]\n[     0     ]\n[     0     ]\n[-----------]")
    elif(x == 4):
        print(
            "[-----------]\n[   0   0   ]\n[           ]\n[   0   0   ]\n[-----------]")
    elif(x == 5):
        print(
            "[-----------]\n[   0   0   ]\n[     0     ]\n[   0   0   ]\n[-----------]")
    elif(x == 6):
        print(
            "[-----------]\n[   0   0   ]\n[   0   0   ]\n[   0   0   ]\n[-----------]")


while(True):
    option = input("Please enter 'y' to roll the dice uwu: ")
    if(option == "y"):
        diceSim()
    else:
        break
