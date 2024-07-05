def main():
    text = input("Input: ")
    vowel = ["a", "e", "i", "o", "u"]
    print("Output: ", end="")
    for c in text:
        if c.lower() in vowel:
            print("", end="")
        else:
            print(c, end="")
    print()
main()
