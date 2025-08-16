num=int(input("Enter a number:"))
sum=0
number=num
while number>0:
    digits=number%10
    sum+=digits**3
    number//=10
if num==sum:
    print(num,"is an armstrong number.")
else:
    print(num,"is not an armstrong number.")
