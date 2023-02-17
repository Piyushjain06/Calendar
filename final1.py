year = int(input("Enter the year of which calender is reqiured: "))
month = int(input("Enter the month of which calender is reqiured: "))
days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
if year % 4 == 0:
        days[2] = 29
days1 = days[month]
if month == 1:
    year -= 1
    month = 11
elif month == 2:
    year -= 1
    month = 12
elif month > 3:
    month -= 2
elif month > 13:
    print("Enter valid value!!!!")
    exit()
m = ((13*month)-1)//5
d = year % 100
c = year//100
third = d//4
foruth = c//4
fifth = (2*c)
monday, tuesday, wednesday, thursday, friday, saturday, sunday = [], [], [], [], [], [], []

for i in range(1, days1+1):
    equation = (i+m+d+third+foruth-fifth) % 7
    if equation == 0:
        sunday.append(i)
    elif equation == 1:
        monday.append(i)
    elif equation == 2:
        tuesday.append(i)
    elif equation == 3:
        wednesday.append(i)
    elif equation == 4:
        thursday.append(i)
    elif equation == 5:
        friday.append(i)
    elif equation == 6:
        saturday.append(i)
print("Sun Mon Tue Wed Thu Fri Sat")
for i in range(1, 10):
    if 1 in sunday:
        print("", i, end="  ")
        if i == 7:
            print("\n", end="")

    elif 1 in monday:
        if i == 1:
            print(" "*4, i, end="  ")
        elif i < 10 and i > 1:
            print(" ", i, end=" ")
        if i == 6:
            print("\n", end="")

    elif 1 in tuesday:
        if i == 1:
            print(" "*8, i, end="  ")
        elif i < 10 and i > 1:
            print(" ", i, end=" ")
        if i == 5:
            print("\n", end="")

    elif 1 in wednesday:
        if i == 1:
            print(" "*12, i, end="  ")
        elif i < 10 and i > 1:
            print(" ", i, end=" ")
        if i == 4:
            print("\n", end="")

    elif 1 in thursday:
        if i == 1:
            print(" "*16, i, end="  ")
        elif i < 10 and i > 1:
            print(" ", i, end=" ")
        if i == 3:
            print("\n", end="")

    elif 1 in friday:
        if i == 1:
            print(" "*20, i, end="  ")
        elif i < 10 and i > 1:
            print(" ", i, end=" ")
        if i == 2 or i == 9:
            print("\n", end="")

    elif 1 in saturday:
        if i == 1:
            print(" "*24, i, end="  ")
        elif i < 10 and i > 1:
            print(" ", i, end=" ")
        if i == 1 or i == 8:
            print("\n", end="")

for i in range(10, days1+1):
    if 1 in sunday:
        print("", i, end=' ')
        if i == 14 or i == 21 or i == 7 or i == 28:
            print("\n", end="")

    elif 1 in monday:
        print("", i, end=' ')
        if i == 13 or i == 20 or i == 27:
            print("\n", end="")

    elif 1 in tuesday:
        print("", i, end=' ')
        if i == 12 or i == 19 or i == 26:
            print("\n", end="")

    elif 1 in wednesday:
        print("", i, end=' ')
        if i == 11 or i == 18 or i == 25:
            print("\n", end="")

    elif 1 in thursday:
        print("", i, end=' ')
        if i == 10 or i == 17 or i == 24:
            print("\n", end="")

    elif 1 in friday:
        print("", i, end=' ')
        if i == 16 or i == 23 or i == 30:
            print("\n", end="")

    elif 1 in saturday:
        print("", i, end=' ')
        if i == 15 or i == 22 or i == 29:
            print("\n", end="")
