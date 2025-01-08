print("                                             CALCULATOR                                        ")
loop=0
while(loop==0):
    num1=int(input("Enter a number:"))
    num2=int(input("Enter another number:"))
    operator=input("The function you want to perform:")
    if(operator=="+"):
        print(num1,"+",num2,"=",num1+num2)
    elif(operator=="-"):
        print(num1,"-",num2,"=",num1-num2)
    elif(operator=="*"):
        print(num1,"*",num2,"=",num1*num2)
    elif(operator=="/"):
        print(num1,"/",num2,"=",num1/num2)
    elif(operator=="%"):
        print(num1,"%",num2,"=",num1%num2)
    elif(operator=="//"):
        print(num1,"//",num2,"=",num1//num2)
    elif(operator==">"):
        if(num1>num2):
            print("TRUE")
        else:
            print("FALSE")
    elif(operator=="<"):
        if(num1<num2):
            print("TRUE")
        else:
            print("FALSE")
    elif(operator==">="):
        if(num1>=num2):
            print("TRUE")
        else:
            print("FALSE")
    elif(operator=="<="):
        if(num1<=num2):
            print("TRUE")
        else:
            print("FALSE")
    elif(operator=="ac"):
        print("exiting")
        loop=1
