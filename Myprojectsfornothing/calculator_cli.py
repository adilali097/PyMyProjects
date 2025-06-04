def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")
    a = float(input("Enter first number: "))
    op = input("Enter operator: ")
    b = float(input("Enter second number: "))

    if op == "+":
        print("Result:", a + b)
    elif op == "-":
        print("Result:", a - b)
    elif op == "*":
        print("Result:", a * b)
    elif op == "/":
        print("Result:", a / b)
    else:
        print("Invalid operator")

if __name__ == '__main__':
    calculator()
