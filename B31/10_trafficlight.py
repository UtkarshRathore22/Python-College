signal=int(input("Enter signal number\n1.RED\n2.YELLOW\n3.GREEN\n"))
if(signal<=3 and signal>=1):
    if(signal==1):
        print("STOP")
    if(signal==2):
        print("WAIT")
    if(signal==3):
        print("GO")
else:
    print("Enter valid input")