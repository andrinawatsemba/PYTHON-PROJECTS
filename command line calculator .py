def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

print("Command-Line Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1-4): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == "1":
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == "2":
    print(num1, "-", num2, "=", subtract(num1, num2))
    #the end
elif choice == "3":
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == "4":
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid choice!")

#note that I've added indentation (four spaces) to the code blocks inside the `if`/`elif`/`else` statements and the function definitions. This should fix any indentation-related issues.
