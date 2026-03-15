# Creating an array (list) of integers
numbers = [10, 20, 30, 40, 50]

# Accessing elements
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# Modifying an element
numbers[2] = 35
print("Modified array:", numbers)

# Adding elements
numbers.append(60)
print("After appending 60:", numbers)

# Removing elements
numbers.remove(20)
print("After removing 20:", numbers)

# Iterating through the array
print("All elements:")
for num in numbers:
    print(num)