from random import randint
player_count = int(input("please enter players number: "))

for i in range (player_count):
    for i in range (0 , 2):
        print(randint(1, 6), end = "")
    print("\n")