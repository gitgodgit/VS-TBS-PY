#determines if one number is multiple of another
print("this program determines if first number is multiple of the second number")
number_a = int(input("please enter first natural number: "))
number_b = int(input("please enter second natural number: "))

if number_a > 0 and number_b > 0:

    if number_a % number_b == 0 :
        print("the first number IS MULTIPLE of the second number")
    else:
        print("first number is NOT multiple of the second number")
else:
    print("some entered numbers were not natural")