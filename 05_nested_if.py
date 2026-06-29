age = int(input("Enter your age: "))
if age >= 18:
    citizen = input("are you a indian citizen? (yes/no): " )
    if citizen == "yes":
        print("You are eligible to vote")
    else:
        print("not eligible to vote")
else:
    print("Age is less than 18")            