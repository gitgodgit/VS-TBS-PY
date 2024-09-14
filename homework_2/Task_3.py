#this program tells you the prime factors of the number
number_a = int(input("please input number between 1-10: "))


if number_a > 10 or number_a <= 0:
    print("only whole numbers are allowed: ")
else:
    print("this number is divisble by: ")
    for i in range(1,number_a):
        # 1 is not prime and 4 is not prime . in this specific 
        if number_a % i == 0 and i != 1 and i != 4:
            print(i)

