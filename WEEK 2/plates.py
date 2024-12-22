def main():
    # takes input of plate number which is to be verified
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


# to check validity of number plate
def is_valid(s):
    # to check for length of string in vanity plate and if it consists of only alphanumeric characters or not
    if 2 <= len(s) <= 6 and s.isalnum():
        # if plate has only alphabets it is valid
        if s.isalpha():
            return True
        else:
            # numbers can only be used in the end after all alphabets and first two characters should be alphabets
            if s[:2].isalpha() and s[-1:].isdigit():
                for i in range(len(s)):
                    if s[i].isdigit():
                        # no number should be followed by an alphabet
                        if s[i:].isdigit():
                            # first number shouldn't be 0
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
