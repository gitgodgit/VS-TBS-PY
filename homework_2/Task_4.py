#this program inputs car speed and prints its fastness
speed = int(input("Please enter the car speed integer in km/h: "))

if speed < 30:
    print("SLOW")
elif speed >= 30 and speed < 60:
    print("MODERATE")
elif speed >= 60 and speed < 120:
    print("FAST")
elif speed >= 120:
    print("VERY FAST")
    
