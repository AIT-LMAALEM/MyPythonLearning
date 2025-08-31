# 1. Division by zero
try:
    x = 10 / 0
except ZeroDivisionError:
    print("⚠ You cannot divide by zero!")


# 2. Converting invalid string to integer
try:
    num = int("abc")
except ValueError:
    print("⚠ Invalid input, cannot convert to integer.")


# 3. Multiple except blocks
try:
    a = int(input("Enter number: "))
    b = int(input("Enter another number: "))
    print(a / b)
except ValueError:
    print("⚠ Please enter numbers only.")
except ZeroDivisionError:
    print("⚠ Cannot divide by zero.")


# 4. Using else with try
try:
    x = int(input("Enter number: "))
    y = int(input("Enter another number: "))
    result = x / y
except (ValueError, ZeroDivisionError) as e:
    print("⚠ Error:", e)
else:
    print("✅ Result is:", result)


# 5. Using finally
try:
    f = open("file.txt", "r")
    content = f.read()
except FileNotFoundError:
    print("⚠ File not found.")
else:
    print("✅ File content:", content)
finally:
    print("🔹 This will always run.")


# 6. Raising your own exception
try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative!")
except ValueError as e:
    print("⚠ Error:", e)
else:
    print("✅ Your age is:", age)


# 7. Index out of range
try:
    numbers = [1, 2, 3]
    print(numbers[5])
except IndexError:
    print("⚠ List index out of range.")


# 8. Key not found in dictionary
try:
    person = {"name": "Ahmed"}
    print(person["age"])
except KeyError:
    print("⚠ Key does not exist in dictionary.")


# 9. File handling with custom exception
try:
    filename = input("Enter filename: ")
    with open(filename, "r") as f:
        print(f.read())
except FileNotFoundError:
    print("⚠ The file you entered was not found.")


# 10. TypeError example
try:
    result = "10" + 5
except TypeError:
    print("⚠ Cannot add string and integer together.")