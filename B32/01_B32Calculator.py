Num1= int(input("Enter Number1:"))
Num2= int(input("Enter Number2:"))
act = int(input("\n Choose Operation \n 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division \n"))

a= Num1+Num2  #Addition
b= Num1-Num2  #Subtraction
c= Num1*Num2  #Multiplication
d= Num1/Num2  #Division

print("\nResult:", end="")
if act==1:
    print(a)
elif act==2:
    print(b)
elif act==3:
    print(c)
elif act==4:
    print(d)
else:
    print("Choose another operation")
    print("Vanshika")
