def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if 2 <= len(s) <= 6 and s.isalnum():
        if s.isalpha():
            return True
        else:
            if s[:2].isalpha() and s[-1:].isdigit():
                for i in range(len(s)):
                    if s[i].isdigit():
                        if s[i:].isdigit():
                            if s[i:].startswith("0"):
                                return False
                            else:
                                return True
                        else:
                            return False
            else:
                return False
    else:
        return False
main()
