def calculator():
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        op = input("Enter operation (+ - * /): ")

        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '*':
            result = a * b
        elif op == '/':
            result = a / b   # may raise ZeroDivisionError
        else:
            raise ValueError("Invalid operation!")

    except ValueError as e:
        print("⚠ Input error:", e)
    except ZeroDivisionError:
        print("⚠ Cannot divide by zero")
    else:
        print("✅ Result:", result)
    finally:
        print("🔹 End of calculation.")

calculator()