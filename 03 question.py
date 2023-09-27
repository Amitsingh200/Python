# factorial number

def function(n):
    if(n < 0):
        print("Not valid Number , Enter positive number")
    elif(n == 0 or n == 1):
        return 1
    else:
        return n * function(n - 1)

num = int(input("Enter the Number : "))
factorial = function(num)
print(f"factorial of {num} is : {factorial}")
