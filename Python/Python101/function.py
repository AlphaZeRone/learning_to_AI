def Hello(name):
    print("Hello", name)

def add(a, b):
    return a+b

name = input("Enter your name: ")
Hello(name)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = add(num1, num2)
print("The sum of", num1, "and", num2, "is", result)
