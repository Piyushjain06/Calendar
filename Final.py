"""This Program allows user to enter a year and a month and display its repectivite calender.
The Program is based on a conecpt called Zeller's Congurence """


def print1(a, b):  # Defining Function for 1st print statement
    if i == 1:
        print(" "*a, i, end="  ")
    elif i < 10 and i > 1:
        print(" ", i, end=" ")
    if i == b:
        print("\n", end="")


def print2(a, b, c):  # Defining Function for 2nd print statement
    if i == 1:
        print(" "*a, i, end="  ")
    elif i < 10 and i > 1:
        print(" ", i, end=" ")
    if i == b or i == c:
        print("\n", end="")


def print3(a, b, c):  # Defining Function for 3rd print statement
    print("", i, end=' ')
    if i == a or i == b or i == c:
        print("\n", end="")


# taking A year from the user
year = int(input("Enter the year of which calender is reqiured: "))
# taking A month from the user
month = int(input("Enter the month of which calender is reqiured: "))
if month > 12:  # providing with error if the entered value of the month is greater than 12
    print("Enter valid value!!!!")
    exit()
days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}  # A dict for no days present in a mont h
if year % 4 == 0:
    days[2] = 29
days1 = days[month]  # declaring the number days present in a month
if month == 1:  # In the concept  of Zeller Congurence Jan is counted as the 11th month of the last year
    year -= 1
    month = 11
elif month == 2:  # In the concept  of Zeller Congurence Feb is counted as the 11th month of the last year
    year -= 1
    month = 12
elif month > 2:  # In the concept  of Zeller Congurence the year begins with the month of march
    month -= 2
# Calculations below are based on zeller congurence
m = ((13*month)-1)//5
d = year % 100
c = year//100
third = d//4
foruth = c//4
fifth = (2*c)

monday, tuesday, wednesday, thursday, friday, saturday, sunday = [], [], [], [], [], [], []

equation = (1+m+d+third+foruth-fifth) % 7
if equation == 0:
    sunday.append(1)
elif equation == 1:
    monday.append(1)
elif equation == 2:
    tuesday.append(1)
elif equation == 3:
    wednesday.append(1)
elif equation == 4:
    thursday.append(1)
elif equation == 5:
    friday.append(1)
elif equation == 6:
    saturday.append(1)
print("Sun Mon Tue Wed Thu Fri Sat")  # printing Header of the calender
# Printing The Calender!!!!!!!!!!
for i in range(1, 10):
    
    if 1 in sunday:
        print("", i, end="  ")
        if i == 7:
            print("\n", end="")

    elif 1 in monday:
        print1(4, 6)

    elif 1 in tuesday:
        print1(8, 5)

    elif 1 in wednesday:
        print1(12, 4)

    elif 1 in thursday:
        print1(16, 3)

    elif 1 in friday:
        print2(20, 2, 9)

    elif 1 in saturday:
        print2(24, 1, 8)

for i in range(10, days1+1):

    if 1 in sunday:
        print("", i, end=' ')
        if i == 14 or i == 21 or i == 7 or i == 28:
            print("\n", end="")

    elif 1 in monday:
        print3(13, 20, 27)

    elif 1 in tuesday:
        print3(12, 19, 26)

    elif 1 in wednesday:
        print3(11, 18, 25)

    elif 1 in thursday:
        print3(10, 17, 24)

    elif 1 in friday:
        print3(16, 23, 30)

    elif 1 in saturday:
        print3(15, 12, 29)