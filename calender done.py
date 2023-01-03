yeari=int(input("Enter the Year of which calender is reqiured: "))
monthi=int(input("Enter the month  of which calender is reqiured: "))
nodays=0
if monthi==1:
    monthi=11
    yeari-=1
    nodays=31
elif monthi==2:
    if yeari%4==0:
        monthi=12
        yeari-=1
        nodays=29
    else:
        monthi=12
        yeari-=1
        nodays=28
elif monthi==3:
    monthi=1
    nodays=31
elif monthi==4:
    monthi=2
    nodays=30
elif monthi==5:
    monthi=3
    nodays=31 
elif monthi==6:
    monthi=4
    nodays=30
elif monthi==7:
    monthi=5
    nodays=31
elif monthi==8:
    monthi=6
    nodays=31
elif monthi==9:
    monthi=7
    nodays=30
elif monthi==10:
    monthi=8
    nodays=31
elif monthi==11:
    monthi=9
    nodays=30
elif monthi==12:
    monthi=10
    nodays=31
m=((13*monthi)-1)//5
d=yeari%100
c=yeari//100
third=d//4
foruth=c//4
fifth=(2*c)
monday=[]
tuesday=[]
wednesday=[]
thursday=[]
friday=[]
saturday=[]
sunday=[] 
for i in range(1,nodays+1):
    equation=(i+m+d+third+foruth-fifth)%7
    if equation==0:
        sunday.append(i)
    elif equation==1:
        monday.append(i)
    elif equation==2:
        tuesday.append(i)
    elif equation==3:
        wednesday.append(i)
    elif equation==4:
        thursday.append(i)
    elif equation==5:
        friday.append(i)
    elif equation==6:
        saturday.append(i)
print("Sun Mon Tue Wed Thu Fri Sat")
for i in range(1,10):
    if 1 in sunday: 
        print("",i,end="  ")
        if i==7:
            print("\n",end="")
    elif 1 in monday:
        if i==1:
             print(" "*4,i,end="  ")
        elif i<10 and i>1:
            print(" ",i,end=" ")
        if i==6:
            print("\n",end="") 
    elif 1 in tuesday:
        if i==1:
             print(" "*8,i,end="  ")
        elif i<10 and i>1:
            print(" ",i,end=" ")
        if i==5:
            print("\n",end="")  
    elif 1 in wednesday:
        if i==1:
             print(" "*12,i,end="  ")
        elif i<10 and i>1:
            print(" ",i,end=" ")
        if i==4:
            print("\n",end="")
    elif 1 in thursday:
        if i==1:
             print(" "*16,i,end="  ")
        elif i<10 and i>1:
            print(" ",i,end=" ")
        if i==3:
            print("\n",end="")
    elif 1 in friday:
        if i==1:
             print(" "*20,i,end="  ")
        elif i<10 and i>1:
            print(" ",i,end=" ")
        if i==2 or i==9:
            print("\n",end="")  
    elif 1 in saturday:
        if i==1:
             print(" "*24,i,end="  ")
        elif i<10 and i>1:
            print(" ",i,end=" ")
        if i==1 or i==8:
            print("\n",end="")

for i in range(10,nodays+1):
    if 1 in sunday:
        print("",i,end=' ')
        if i==14 or i==21 or i==7 or i==28:
            print("\n",end="")
    elif 1 in monday:
        print("",i,end=' ')
        if i==13 or i==20  or i==27:
            print("\n",end="")
    elif 1 in tuesday:
        print("",i,end=' ')
        if i==12 or i==19  or i==26:
            print("\n",end="")
    elif 1 in wednesday:
        print("",i,end=' ')
        if i==11 or i==18  or i==25:
            print("\n",end="")
    elif 1 in thursday:
        print("",i,end=' ')
        if i==10 or i==17  or i==24:
            print("\n",end="")
    elif 1 in friday:
        print("",i,end=' ')
        if i==16  or i==23 or i==30:
            print("\n",end="")
    elif 1 in saturday:
        print("",i,end=' ')
        if i==15  or i==22 or i==29:
            print("\n",end="")