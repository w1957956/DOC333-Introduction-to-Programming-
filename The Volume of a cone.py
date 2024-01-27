import math
pi =3.14
r = float(input("Enter the radius of the cone in centimeters: "))
h=float(input("Enter height of the cone in centimeters: "))
volume = round(1/3*pi*math.pow(r,2)*h,2)
print("The Volume of a cone: ",volume)
