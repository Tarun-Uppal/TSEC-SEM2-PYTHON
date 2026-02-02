count = input("Enter factorial number: ")
factorial = 1
for i in range(1, int(count) + 1):
    factorial = factorial * i
print("Factorial of " + str(count) + " is: " + str(factorial))