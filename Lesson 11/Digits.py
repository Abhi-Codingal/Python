num=int(input("Enter a number:"))
digitsNumber = 0
while num>0:
    num //= 10
    digitsNumber += 1
print(digitsNumber)