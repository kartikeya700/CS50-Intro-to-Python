def main():
    Input=input()
    message=convert(Input)
    print(message)
def convert(str):
    return str.replace(":(","🙁").replace(":)","🙂")
main()
