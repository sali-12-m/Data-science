#Create a CLI-based calculator using functions
def add(x,y):
    #Return the sum of two numbers
    return x+y
def subtract(x,y):
    #Return the difference of two numbers
    return x-y
def multiply(x,y):
    #Return the product of two numbers
    return x*y
def divide(x,y):
    #Return the division of two numbers
    if y==0:
        return "Error: Cannot divide by zero!"
    return x/y


def calculator():
    #The calculator functions
    while True:
        print("\nCalculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Chose From(1-5): ")

        if choice == '5':
            print("Exiting calculator")
            break
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice! Try again.")
            continue
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Please enter numeric values.")
            continue

        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)

        print("Result:", result)

# Run the calculator
print(calculator())
