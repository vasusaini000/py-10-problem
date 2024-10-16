w,h=map(eval,input().split())
BMI=w/(h*h)
if BMI>0:
    print(BMI)
else :
    print("invalid input")

c=float(input())
b=float(input())
f=float(input())
SI = (c*b*f)/100
if SI < 0:
    print("invalid input")
else:
    print(SI)

import math 
radius=float(input())
area=math.pi*radius**2
if radius<0:
    print("input cant be a negative number")
else:
    print(area)


dist,time=map(eval,input().split())
acceleration=(2*dist)/(time**2)
if distance <0 or time <0 :
    print ("invalid input")
else:
    print(acceleration)


Rows = int(input())
for i in range(0,Rows):
    if Rows<0:
        print('invalid input')
    else:
        print(' ' * (Rows - i - 1) + '* ' * (i + 1))

KM = float(input())
Miles = 0.62*KM
if KM<0:
    print("wrong input")
else:
    print(Miles)


Force,dist=map(eval,input().split())
joule=Force*dist
if Force <0 or dist <0 :
    print("wrong input")
else:
    print(joule , "joules")


import math 
math.sqrt 
n1 = int(input())
n2 = int(input())
v1 = int(input())
v2 = int(input())
point_a = ((n2-n1)**2)
point_b = ((v2-v1)**2)
x=(math.sqrt(point_a+point_b))
print(x)


cents = float(input())
dollars = cents // 100
cents %= 100
quarters = cents // 25
cents %= 25
pennies = cents % 5
print(f"Dollars: {dollars}, Quarters: {quarters},  Pennies: {pennies}")