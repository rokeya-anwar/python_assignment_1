
a = int(input("Enter your number: "))
b= int(input("Enter your number: "))
c=int(input("Enter your number: "))

if a >= b and a >= c:
    max= a

elif b >= a and b >= c:
    max = b

else:
    max=c

print(max)
