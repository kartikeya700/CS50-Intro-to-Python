def main():
    # to take input from user
    text = input("Input: ")
    # defines vowels
    vowel = ["a", "e", "i", "o", "u"]
    print("Output: ", end="")
    # to print the input text without vowels
    for c in text:
        # if c is a vowel it is omitted
        if c.lower() in vowel:
            print("", end="")
        # if c is not a vowel then it is printed as it is
        else:
            print(c, end="")
    # for new line character
    print()


main()
