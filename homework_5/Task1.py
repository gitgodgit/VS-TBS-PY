#takes in n where 0<n<50
#program should find divisors of evdry number up until n 
#also it should pront maximum 3 divisors

n = int(input("please enter n where 0 < n < 50: "))

if not 0 < n < 50 : 
    print("please enter valid number between 1-49: ")
else:
    counter = 1
    while counter <= n:
        
        MAX_PRINT = 3
        print(counter, "-", end="")
        for i in range(1, counter +1):
            if MAX_PRINT > 0 :
                if counter % i == 0:
                    print(i, end=" ")
                    MAX_PRINT -= 1
                
            else: 
                continue
        print("")
        counter += 1
