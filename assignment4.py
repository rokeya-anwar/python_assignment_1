
Height = float(input("Enter your number: "))
weight = float(input("Enter your number: "))

bmi = weight / (Height**2)
print("print Your bmi: ")

if bmi <= 18.5:
    print("Underweight")
    
elif bmi >= 18.5 and bmi <= 24.9:
    print("Normal")

elif bmi >= 25 and bmi <= 29:
    print("overweight")

else:
    print("obesed")


