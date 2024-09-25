n = int(input("please enter number 0-19: "))

temp_0 = 0
temp_1 = 1


if  0 <= n < 20:
   
    counter = 1

    print(temp_0," ", end="")
    if n == 0:
        exit(1)

    print(temp_1," ", end="")
    if n == 1:
        exit(1)

    while counter < n:
       next = temp_0 + temp_1
       temp_0 = temp_1
       temp_1 = next
       print(temp_1," ",  end="")
       counter += 1

else:
    print("please enter number 0-19")