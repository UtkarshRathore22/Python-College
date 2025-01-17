age=int(input("Enter your age:"))
if(age>0):
    if(age>18):
        print("Eligible for vote")
    else:
        print("Not eligible for vote")
else:
    print("Enter valid age")