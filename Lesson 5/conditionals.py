#create program that checks temperature to decide clothes
temperature = int(input("What is the temperature? "))

if temperature>60:
  print("You should wear shorts and a t-shirt.")
else:
  print("You should wear pants and a jacket.")