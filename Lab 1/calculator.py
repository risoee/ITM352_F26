def add(x, y):
    """Add two numbers"""
    return x + y

def subtract(x, y):
    """Subtract two numbers"""
    return x - y

def multiply(x, y):
    """Multiply two numbers"""
    return x * y

def divide(x, y):
    """Divide two numbers"""
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def main():
    """Main function to run the calculator"""
    print("=" * 40)
    print("Simple Calculator")
    print("=" * 40)
    
    while True:
        try:
            # Get user inputs
            num1 = float(input("\nEnter first number: "))
            num2 = float(input("Enter second number: "))
            
            # Display operation choices
            print("\nChoose an operation:")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            
            choice = input("\nEnter operation (1/2/3/4): ")
            
            # Perform the selected operation
            if choice == '1':
                result = add(num1, num2)
                operation = "+"
            elif choice == '2':
                result = subtract(num1, num2)
                operation = "-"
            elif choice == '3':
                result = multiply(num1, num2)
                operation = "*"
            elif choice == '4':
                result = divide(num1, num2)
                operation = "/"
            else:
                print("Invalid choice. Please select 1, 2, 3, or 4.")
                continue
            
            # Display the result
            print("\n" + "=" * 40)
            print(f"Result: {num1} {operation} {num2} = {result}")
            print("=" * 40)
            
            # Ask if user wants to continue
            again = input("\nDo you want to perform another calculation? (yes/no): ")
            if again.lower() != 'yes' and again.lower() != 'y':
                print("Thank you for using the calculator!")
                break
                
        except ValueError as e:
            print(f"\nError: {e}")
        except ZeroDivisionError:
            print("\nError: Cannot divide by zero")

if __name__ == "__main__":
    main()
