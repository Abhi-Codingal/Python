weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))
bmi = weight / height**2

print("Your BMI is",bmi)

if bmi<18.5:
    print("You are underweight.")
elif bmi<25:
    print("You are on target/healthy.")
elif bmi<30:
    print("You are overweight.")
elif bmi<35:
    print("You are severely overweight.")
elif bmi < 40:
    print("You are obese.")
else:
    print("You are severely obese.")        