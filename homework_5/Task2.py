#this should print multiplication table 1-9
#which will be in columns and should not contain
#previus multiplications

n = int(input("please enter number 1-9: "))

left = 1
right = 1
if  1 <= n <= 9:
    while right <= n:
        while left <= n:
            if left <= right:
                print(left, "*", right, "=", left * right, end="     ")
            left += 1

        print("")
        left = 1
        right += 1
else:
    print("please enter number 1-9")

