
celsius = float(input("Enter your number: "))

if celsius > 0:
    farenheit =(celsius*9/5)+32
    print ("Temperature in farenheit: ",farenheit)

elif celsius < 0:
    kelvin = celsius+273.15
    print("Temparature in kelvin: ",kelvin)

else:
    print("Temparature  is 0")

