entered_number = int(input("please enter your number between 0-19: "))


if entered_number < 0 or entered_number > 19 :
    print("number you entered was out of range of 0-19, please run th program again")
else:
    temp0 = 0
    temp1 = 1
    if entered_number == 0:
        print(temp0)
    else:
        for i in range (1, entered_number):
            answer = temp0 + temp1
            temp0 = temp1
            temp1 = answer
        print(temp1)