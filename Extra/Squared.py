print("This program will square the numbers within a given range and sort them into evens and odds")
startNum = int(input("Enter a starting number: "))
endNum = int(input("Enter an ending number: "))
squaredList = []
evenList = []
oddList = []

def squared(start, end):
    while start <= end:
        squaredList.append(start**2)
        start += 1
squared(startNum,endNum)
print(squaredList)

for i in squaredList:
    if i % 2 == 0:
        evenList.append(i)
    else:
        oddList.append(i)
print("The even numbers are:",evenList)
print("The odd numbers are:",oddList)