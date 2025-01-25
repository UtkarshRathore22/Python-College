t1=(1,2,3,4,5,6,7)
print(t1)
print(t1[1])
print(t1[1:5])
print(t1*2)
t2=()
count=0
item=int(input("Enter the number to be found:"))
for i in t1:
    if(item==i):
        print("The index of ",item, "is",count)
    else:
        count+=1
print(t1.count(5))