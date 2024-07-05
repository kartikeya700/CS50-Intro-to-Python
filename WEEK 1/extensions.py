def main():
    Extension = input("File Name: ").lower().strip()
    if Extension.endswith(".gif"):
        print("image/gif")
    elif Extension.endswith("jpg"):
        print("image/jpeg")
    elif Extension.endswith("jpeg"):
        print("image/jpeg")
    elif Extension.endswith("png"):
        print("image/png")
    elif Extension.endswith("pdf"):
        print("application/pdf")
    elif Extension.endswith("txt"):
        print("text/plain")
    elif Extension.endswith("zip"):
        print("application/zip")
    else:
        print("application/octet-stream")
main()
 