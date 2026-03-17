try:
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    num1 = float(num1)
    num2 = float(num2)
    result = num1 / num2
    print(f"Result of {num1} / {num2} = {result}")
        
except ZeroDivisionError:
    print("Error: Cannot divide by zero! Please enter a non-zero divisor.")
except ValueError:
    print("Error: Invalid input! Please enter valid numeric values.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print("Division completed successfully!")
finally:
    print("Program execution finished.")
