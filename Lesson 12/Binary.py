num=int(input("Enter a number:"))
binaryNum=''
while num>0:
    remainder = str(num % 2)
    binaryNum = remainder + binaryNum
    num //= 2

print("binary number is: ", binaryNum)
    


