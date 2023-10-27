def calculator():
    num1 = input("Please input the first Number: ")
    op = input("Please input the operator (+-*/): ")
    num2 = input("Please input the first Number: ")

    num1 = int(num1)
    num2 = int(num2)
    res = None

    match op:
        case "+":
            res = num1 + num2
        case "-":
            res = num1 - num2
        case "*":
            res = num1 * num2
        case "/":
            res = num1 / num2
        case _:
            print("Unknown operator")

    print("The answer is: ", res)

calculator()
