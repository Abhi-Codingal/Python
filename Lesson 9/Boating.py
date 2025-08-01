print("To go boating you must be older than the age 10 and younger than the age 20")
age=int(input("Enter your age:"))
if age>10:
    if age<20:
        print("You are the right age.")
    else:
        print("You are too old.")
else:
    print("You are too young.")         