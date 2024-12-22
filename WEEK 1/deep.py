def main():
    # takes answer from the user
    answer = input(
        "What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()
    # matches the answer with specific cases
    match answer:
        case "42" | "forty-two" | "forty two": print("Yes")
        case _: print("No")


main()
