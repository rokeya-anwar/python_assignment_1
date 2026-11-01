
password = "python123"
attempts = 0

while attempts < 3:
    user_password = input("Enter password: ")

    if user_password == password:
        print("Login successful")
        break
    else:
        attempts += 1
        print("Incorrect password")

if attempts == 3:
    print("Account locked")