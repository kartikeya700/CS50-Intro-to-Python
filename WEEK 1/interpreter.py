def main():
    Expression = input("Expression: ").strip()
    x, y, z = Expression.split(" ")
    n1 = float(x)
    n2 = float(z)
    if y=="+":
        ans=round(n1 + n2, 2)
        print(ans)
    elif y=="-":
        ans=round(n1 - n2, 2)
        print(ans)
    elif y=="*":
        ans=round(n1 * n2, 2)
        print(ans)
    elif y=="/":
        ans=round(n1 / n2, 2)
        print(ans)
    else:
        print("Expression not defined")
main()
