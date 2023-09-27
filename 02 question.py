# swap data a = 10, b = 15

def swap(a,b):
    print("Before swap\n")
    print(f"a = {a} , b = {b}\n\n")
    a , b = b , a
    print("After swap\n")
    print(f"a = {a} , b = {b}")
    
a = int(input("Enter the number : "))
b = int(input("Enter the number : "))
swap(a,b)