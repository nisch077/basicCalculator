def add(num1, num2):
    """Adds two numbers."""
    return num1 + num2

def subtract(num1, num2):
    """Subtracts two numbers."""
    return num1 - num2

def multiply(num1, num2):
    """Multiply two numbers."""
    return num1 * num2

def divide(num1, num2):
  """Divides two numbers."""
  if num2 == 0:
      return "Error! Division by zero."
  return num1 / num2

def modulo(num1, num2):
    """Calculates the modulo (remainder) of two numbers."""
    if num2 == 0:
        return "Error! Cannot perform modulo with a divisor of zero."
    return num1 % num2

while True:
    print("\nSelect Operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulo")
    print("6. Exit")

    choice = input("Enter choice(1/2/3/4/5/6): ")

    if choice in ('1', '2', '3', '4', '5'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid Input. Please enter numbers only.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        elif choice == '5':
            print(num1, "%", num2, "=", modulo(num1, num2))
    
    elif choice == '6':
        print("Exiting calculator.")
        break

    else:
        print("Invalid input. Please enter a number between 1 and 5.")