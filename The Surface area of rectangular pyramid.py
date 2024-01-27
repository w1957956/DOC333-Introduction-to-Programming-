#surface are of rectangular based pyramid

import math

l=float(input("Enter length of the pyramid in centimeters: "))
w=float(input("Enter width of the pyramid in centimeters: "))
h=float(input("Enter height of the pyramid in centimeters: "))
surface_area=(l*w)+l*(math.sqrt(math.pow((w/2),2)+math.pow(h,2)))+ w* (math.sqrt(math.pow((l/2),2)+math.pow(h,2)))
print(surface_area)
 