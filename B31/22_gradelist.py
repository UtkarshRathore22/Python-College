list=[]
for i in range(1,11):
    avg=float(input("Enter the average:"))
    if(avg>=90):
        gr='A'
        list.append(gr)
        print("Grade:A")
    elif(avg<90 and avg>=80):
        gr='B'
        list.append(gr)
        print("Grade:B")
    elif(avg<80 and avg>=70):
        gr='C'
        list.append(gr)
        print("Grade:C")
    elif(avg<70 and avg>=60):
        gr='D'
        list.append(gr)
        print("Grade:D")
    elif(avg<60 and avg>=50):
        gr='E'
        list.append(gr)
        print("Grade:E")
    elif(avg<50):
        gr='F'
        list.append(gr)
        print("Grade:F")
list.sort()
print(list)
print("The students with grade A are:",list.count('A'))
print("The students with grade B are:",list.count('B'))
print("The students with grade C are:",list.count('C'))
print("The students with grade D are:",list.count('D'))
print("The students with grade E are:",list.count('E'))
print("The students with grade F are:",list.count('F'))