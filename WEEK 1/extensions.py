def main():
    # take file name as input
    extension = input("File Name: ").lower().strip()
    # to check file extension and returns file type accordingly
    if extension.endswith(".gif"):
        print("image/gif")
    elif extension.endswith("jpg"):
        print("image/jpeg")
    elif extension.endswith("jpeg"):
        print("image/jpeg")
    elif extension.endswith("png"):
        print("image/png")
    elif extension.endswith("pdf"):
        print("application/pdf")
    elif extension.endswith("txt"):
        print("text/plain")
    elif extension.endswith("zip"):
        print("application/zip")
    # default case
    else:
        print("application/octet-stream")


main()
