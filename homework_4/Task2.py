from random import randint
entered_number = int(input("please enter your number between 1-30: "))


if entered_number < 1 or entered_number > 30 :
    print("number you entered was out of range of 1-30, please run th program again")
else:
    for i in range (entered_number):
        print(randint(1,999))