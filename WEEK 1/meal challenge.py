def main():
    # take input from user and convert entered time to required format
    time = convert(input("What time is it? ").strip())
    # checks for cases and returns which meal time it is accordingly
    if time >= 7.00 and time <= 8.00:
        print("breakfast time")
    elif time >= 12.00 and time <= 13.00:
        print("lunch time")
    elif time >= 18.00 and time <= 19.00:
        print("dinner time")
    else:
        print("Not a meal time.")


# to convert string to float value of time input
def convert(time):
    # for tim in 12hr format
    if time.endswith("a.m."):
        y = time.removesuffix("a.m.")
        H, M = y.split(":")
        h = int(H)
        m = int(M)
        T = float(h + m/60)
        return T
    elif time.endswith("p.m."):
        x = time.removesuffix("p.m.")
        Hs, Ms = x.split(":")
        hs = int(Hs)
        ms = int(Ms)
        Ts = float(12.00 + hs + ms/60)
        return Ts
    # for time in 24 hr format
    else:
        Hours, Minutes = time.split(":")
        hours = int(Hours)
        minutes = int(Minutes)
        TIME = float(hours + minutes/60)
        return TIME


if __name__ == "__main__":
    main()
