def main():
    # takes string input in camel case from user
    camel = input("camelCase: ")
    print("snake_case: ", end="")
    # prints the string in snake case
    for c in camel:
        # if the letter is lower case it is printed as such
        if c.islower():
            print(c, end="")
        # if letter is uppercase it is printed with _ as a prefix
        if c.isupper():
            print("_", c.lower(), end="", sep="")
    # adds empty line character after completion
    print()


main()
