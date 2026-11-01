
age = int(input("age: "))

if age >= 0 and age <= 1:
    print("infant")

elif age >= 2 and age <= 3:
    print("toodler")

elif age >= 4 and age <= 12:
    print("Child")

elif age >= 13 and age <= 19:
    print("teenager")


else:
    print("Adult")
