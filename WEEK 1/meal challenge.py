def main():
    Time = input("What time is it? ").strip()
    time = convert(Time)
    if time >= 7.00 and time <= 8.00:
        print("breakfast time")
    elif time >= 12.00 and time <= 13.00:
        print("lunch time")
    elif time >= 18.00 and time <= 19.00:
        print("dinner time")
def convert(time):
    if time.endswith("a.m."):
        Time = time.removesuffix("a.m.")
        H, M = Time.split(":")
        h = int(H)
        m = int(M)
        T = float(h + m/60)
        return T
    elif time.endswith("p.m."):
        Time = time.removesuffix("p.m.")
        Hs, Ms = Time.split(":")
        hs = int(Hs)
        ms = int(Ms)
        Ts = float(12.00 + hs + ms/60)
        return Ts
    else:
        Hours, Minutes = time.split(":")
        hours = int(Hours)
        minutes = int(Minutes)
        TIME = float(hours + minutes/60)
        return TIME
if __name__ == "__main__":
    main()
