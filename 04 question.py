# which number is greater...  

# with function
def greater(a,b,c):
    if(a > b):
        if(a > c):
            return 1
        else:
            return 3
    else:
        if(b > c):
            return 2
        else:
            return 3

a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
c = int(input("Enter the third number : "))

num = greater(a,b,c)

if(num == 1):
    print("First number is greater")
elif(num == 2):
    print("Second number is greater")
else:
    print("Third number is greater")
    
   

    
'''

### Without Function

a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
c = int(input("Enter the third number : "))

if(a > b):
    if(a > c):
        print("First number is greater")
    else:
        print("Third number is greater")
else:
    if(b > c):
        print("Second number is greater")
    else:
        print("Third number is greater")
'''
