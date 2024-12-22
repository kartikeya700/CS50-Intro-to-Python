def main():
    # Takes input from user
    greet = input("Greeting: ").lower().strip()
    # Checks if the greeting is hello or if it starts with an h and returns reward amount accordingly
    if is_hello(greet):
        print("$0")
    elif starts_with_h(greet):
        print("$20")
    else:
        print("$100")


# to check if greeting is hello
def is_hello(str_1):
    return str_1.startswith("hello")


# to check if greeting starts with h
def starts_with_h(str_0):
    return str_0.startswith("h")


main()
