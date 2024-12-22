def main():
    # Input from user
    message = convert(input())
    print(message)

# Function to convert message to required emoticons.
def convert(str):
    return str.replace(":(", "🙁").replace(":)", "🙂")


main()
