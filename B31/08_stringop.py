name=input("Enter your name:")
# finding length
print("Length of name:",len(name))
surname=input("Enter surname:")
# Adding string
print(name+surname)
#Ends with function
print("surname ending with ore?:",surname.endswith("ore"))
#Capitalizing first alphabet
print("Name capitalized:",name.capitalize())
#Replacing letters by call by value
print("Name of with replacing:",name.replace('U','R'))
#Finding a substring
substring=input("Enter the substring you want to find:")
print("The substring starts from:",name.find(substring))