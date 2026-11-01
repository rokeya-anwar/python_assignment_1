
n = int(input("Enter a number: "))

digits = str(n)
power = len(digits)
total = 0

for digit in digits:
    total = total + int(digit) ** power

if total == n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")