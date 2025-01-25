num=int(input("Enter a number:"))
n=num
num2=0
while(n!=0):
    q=n//10
    r=n%10
    num2=num2+r*r*r
    n=q
if(num2==num):
    print("The number is armstrong")
else:
    print("Not an armstrong")