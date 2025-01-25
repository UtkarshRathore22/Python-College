subject=input("Enter a string:")
revsubject=subject[ ::-1]
print(revsubject)
if(subject==revsubject):
    print("Palindrome")
else:
    print("Not a Palindrome")