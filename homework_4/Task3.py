entered_number = int(input("please enter your number between 1-1000: "))

if entered_number < 1 or entered_number > 1000 :
    print("number you entered was out of range of 1-1000, please run the program again")
else:
    for i in range (1, entered_number + 1):
        if entered_number % i == 0:
            print(i)
        