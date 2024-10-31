def main():
    month = {
        "January" : 1,
        "February" : 2,
        "March" : 3,
        "April" : 4,
        "May": 5,
        "June" : 6,
        "July" : 7,
        "August" : 8,
        "September" : 9,
        "October" : 10,
        "November" : 11,
        "December" : 12
    }
    while True:
        date = input("Date: ")
        try:
            m, d, y = date.split("/")
            Month = int(m)
            Year = int(y)
            Day = int(d)
        except ValueError:
            try:
                if "," in date:
                    Date = date.replace(",", "")
                    M, d, y = Date.split(" ")
                    Month = month.get(M.title(), None)
                    Day = int(d)
                    Year = int(y)
                    if Month is None:
                        raise ValueError("Invalid Month name")
                else:
                    raise ValueError("Invalid Date format.")
            except ValueError:
                print("Invalid date format. Try again.")
                continue
        if (Month < 1 or Month > 12 or Day < 1 or Day > 31):
            print("Invalid Date. Try again.")
            continue
        else:
            print(f"{Year}-{Month:02}-{Day:02}")
            break
main()
