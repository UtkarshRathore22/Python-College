#%%

def sum(a,b): #parameter 


#data type - data and operation 
#collection - list, tuple, set
#string
#conditional statement 
#looping statement 


#%%
 def mul(a, b):
    print(a * b)

n = int(input("Enter number one: "))
m = int(input("Enter number two: "))
mul(n, m)


# %%
def fact(a):
    factorial = 1
    if a < 0:
     print("Factorial not defined .")
    elif a == 0 or a == 1:
     print("The factorial of",a,"is 1")
    else:
      for i in range(1, a + 1):
        factorial *= i
    print("The factorial of",a,"is",factorial)

num = int(input("Enter a number: "))
fact(num)

# %%
def fact(a):
   fact = 1
   i = a
   while i > 1:
     fact *= i
     i -= 1
   print("The factorial of",a,"is",fact)

num = int(input("Enter a number: "))
fact(num)


# %%
def fact():
   num = int(input("Enter a number: "))
   fact = 1
   i = num
   while i > 1:
     fact *= i
     i -= 1
   print("The factorial of",num,"is",fact)


fact()

# %%
