
x = float(input("x coordinates: "))
y= float(input("y coordinate: "))

if x > 0 and y > 0:
    print("1st quadrant")

elif x < 0 and y > 0:
    print("2nd quadrant")

elif x < 0 and y < 0:
    print("3rd quadrant")

elif x > 0 and y < 0:
    print("4th Quadrant")

else:
    print("Axis") 
