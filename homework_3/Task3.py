from datetime import date

year = int(input("please enter this persons birth year as number:"))

month = int(input("please enter this persons birth month as number:")) 

day = int(input("please enter this persons birth day as number:"))

birthdate = date(year, month, day)

birthday = birthdate.weekday()

if birthday == 0:
    print("this person was borh on monday")
if birthday == 1:
    print("this person was borh on tuesday")
if birthday == 2:
    print("this person was borh on wednesday")
if birthday == 3:
    print("this person was borh on thursday")
if birthday == 4:
    print("this person was borh on friday")
if birthday == 5:
    print("this person was borh on satureday")
if birthday == 6:
    print("this person was borh on sunday")