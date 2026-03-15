# 1. ZeroDivisionError
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("ZeroDivisionError:", e)

# 2. ValueError
try:
    num = int("abc")
except ValueError as e:
    print("ValueError:", e)

# 3. IndexError
try:
    lst = [1, 2, 3]
    print(lst[5])
except IndexError as e:
    print("IndexError:", e)

# 4. KeyError
try:
    d = {'a': 1}
    print(d['b'])
except KeyError as e:
    print("KeyError:", e)

# 5. FileNotFoundError
try:
    with open("nonexistentfile.txt", "r") as f:
        content = f.read()
except FileNotFoundError as e:
    print("FileNotFoundError:", e)

# Custom Exception
class MyCustomException(Exception):
    pass

try:
    raise MyCustomException("This is a custom exception!")
except MyCustomException as e:
    print("MyCustomException:", e)