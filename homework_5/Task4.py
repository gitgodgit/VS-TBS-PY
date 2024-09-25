n = int(input("please enter number 1-49: "))


if  0 < n < 50:
    row_counter = 0
    column_counter = 0
    n = n - 1
    while row_counter <= n + 1:
        if row_counter == 0:
            for i in range(1, n+1):
                print(" ", end="")
            print("*", end = "")
        
        elif row_counter == n + 1:
            for i in range(1, n+1):
                print(" ", end="")
            print("|")
        else:

            while column_counter < n - row_counter:
                    print(" ", end="")
                    column_counter += 1
            while column_counter >= n - row_counter and column_counter < n:
                    print("/", end="")
                    column_counter += 1
            if column_counter == n:
                    print("|", end="")
                    column_counter += 1
            while column_counter > n and column_counter <= n + row_counter:
                    print("\\", end="")
                    column_counter += 1
            
        print("")   

        column_counter = 0
        row_counter += 1
    

        



        

else:
    print("please enter number 1-49")