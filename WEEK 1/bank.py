def main():
    Greet = input("Greeting: ").lower().strip()
    if Valid(Greet):
        print("$0")
    elif Invalid(Greet):
        print("$20")
    else:
        print("$100")
def Valid(str_1):
    return str_1.startswith("hello")
def Invalid(str_0):
    return str_0.startswith("h")
main()
