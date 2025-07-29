try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Which operation do you want to perform?")
    print("For Addition     enter: +")
    print("For Subtraction  enter: -")
    print("For Multiplication enter: *")
    print("For Division     enter: /")

    operation = input("Enter operation: ")

    if operation == "+":
        print("Result:", a + b)
    elif operation == "-":
        print("Result:", a - b)
    elif operation == "*":
        print("Result:", a * b)
    elif operation == "/":
        if b != 0:
            print("Result:", a / b)
        else:
            print("Error: Division by zero!")
    else:
        print("Invalid operation")

except Exception as e:
    print("Error:", e)
