def main():
    # list of months along with their month number
    month = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }
    flag = 1
    while flag:
        # date input from user
        date = input("Date (month day year format): ")
        # splits the input string about / to get month date and year respectively
        try:
            m, d, y = date.split("/")
            Month = int(m)
            Year = int(y)
            Day = int(d)
        # executes diff code if date entered is in different format
        except ValueError:
            # splits the input string about ,
            try:
                if "," in date:
                    Date = date.replace(",", "")
                    m, d, y = Date.split(" ")
                    # gets month number from dictionary according to month
                    Month = month.get(m.title(), None)
                    Day = int(d)
                    Year = int(y)
                    # if month is invalid ValueError is raised
                    if Month is None:
                        raise ValueError("Invalid Month name")
                # for date format other than above two
                else:
                    raise ValueError("Invalid Date format.")
            except ValueError:
                print("Invalid date format. Try again.")
                continue
        # checks if dat eis entered in mm-dd-yyyy format or not
        if (Month < 1 or Month > 12 or Day < 1 or Day > 31):
            print("Invalid Date. Try again.")
        # prints date in yyyy-mm-dd format
        else:
            print(f"{Year}-{Month:02}-{Day:02}")
            flag = 0


main()
