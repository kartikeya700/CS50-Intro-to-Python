def main():
    # take input of operation to be performed
    expression = input("Expression (with spaces in between operator and numbers): ").strip()
    # seperate the binary operation and assign the values to three different variables
    x, y, z = expression.split(" ")
    n1 = float(x)
    n2 = float(z)
    # to check the operation type and performing it and returning the answer simultaneously
    if y == "+":
        ans = round(n1 + n2, 2)
        print(ans)
    elif y == "-":
        ans = round(n1 - n2, 2)
        print(ans)
    elif y == "*":
        ans = round(n1 * n2, 2)
        print(ans)
    elif y == "/":
        # to handle division by zero
        if n2 == 0:
            print("Division by zero not possible.")
        else:
            ans = round(n1 / n2, 2)
            print(ans)
    # for exceptional cases
    else:
        print("Expression not defined")


main()
