import math
pi = 3.14
r = float(input("Enter the radius of a cone in centimeters: "))
h=float(input("Enter height of a cone in centimeters: "))
l = math.sqrt(math.pow(r,2)+math.pow(h,2))

surface_area =  pi*math.pow(r,2) + pi*r*l

print(surface_area)
  