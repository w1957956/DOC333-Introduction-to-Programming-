import math
print("Shapes Calculator")
print("")
print("1. Calculate the surface area of a cone")
print("2. Calculate the volume of a cone")
print("3. Calculate the base area of a cone")
print("4. Calculate the volume of a rectangular pyramid")
print("5. Calculate the surface area of a rectangular pyramid")
print("6. Exit")
print("")
Option = int(input("Enter Your Preferred option : "))
pi = 3.14
A = "y"
while A == "y":
    if Option == 1:
        r = float(input("Enter the radius of the cone in centimeters:"))
        h=float(input("Enter height of the cone in centimeters: "))
        l = math.sqrt(math.pow(r,2)+math.pow(h,2))
        surface_area = round(pi*math.pow(r,2) + pi*r*l,2)
        print("The Surface Area the acone: ",surface_area)
        print("")
        A = str(input("Do you want tocontinue(y/n): "))
        Option = int(input("Enter Your Preferred option : "))
        print("")

    elif Option == 2:
        r = float(input("Enter the radius of the cone in centimeters: "))
        h=float(input("Enter height of the cone in centimeters: "))
        volume = round(1/3*pi*math.pow(r,2)*h,2)
        print("The Volume of the cone: ",volume)
        print("")
        A = str(input("Do you want to continue(y/n): "))
        Option = int(input("Enter Your Preferred option : "))
        print("")

    elif Option == 3:
        r = float(input("Enter the radius of the base in centimeters: "))
        base_area = round(pi*math.pow(r,2),2)
        print("The Base Area of the cone: ",base_area)
        print("")
        A = str(input("Do you want to continue(y/n): "))
        Option = int(input("Enter Your Preferred option : "))
        print("")

    elif Option == 4:
        l = float(input("Enter length of the rectangular pyramid in centimeters: "))
        w = float(input("Enter width of the rectangular pyramid in centimeters: "))
        h = float(input("Enter height of the rectangular pyramid in centimeters: "))
        volume = round(1/3*l*w*h,2)
        print("The Volume of the rectangular pyramid:",volume)
        print("")
        A = str(input("Do you want to continue(y/n): "))
        Option = int(input("Enter Your Preferred option : "))
        print("")

    elif Option == 5:
        l=float(input("Enter length of the rectangular pyramid in centimeters: "))
        w=float(input("Enter width of the rectangular pyramid in centimeters: "))
        h=float(input("Enter height of the rectangular pyramid in centimeters: "))
        surface_area= round((l*w)+l*(math.sqrt(math.pow((w/2),2)+math.pow(h,2)))+ w* (math.sqrt(math.pow((l/2),2)+math.pow(h,2))),2)
        print("The Surface Area of the rectangular pyramid:",surface_area)
        print("")
        A = str(input("Do you want to continue(y/n): "))
        Option = int(input("Enter Your Preferred option : "))
        print("")

    elif Option == 6:
        print("Exit")
        break
    
 
                
    
    
    

        
