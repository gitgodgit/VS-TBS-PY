import math

side1 = float(input("Enter side 1: "))
side2 = float(input("Enter side 2: "))
side3 = float(input("Enter side 3: "))

perimeter = side1 + side2 + side3

p = perimeter / 2

area = math.sqrt(p * (p - side1) * (p - side2) * (p - side3))

if side1 +side2 <= side3 or side1 + side3 <= side2 or side1 >= side2 + side3:
    print("triangle with this sides does not exist")
else:
    print("area is:", area, "perimeter is:", perimeter )
