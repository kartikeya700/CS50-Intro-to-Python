def main():
    # take time as input from user and convert it to time in hours
    time = convert(input("What time is it? "))
    # checks cases and returns which meal time it is accordingly
    if time >= 7.00 and time <= 8.00:
        print("breakfast time")
    elif time >= 12.00 and time <= 13.00:
        print("lunch time")
    elif time >= 18.00 and time <= 19.00:
        print("dinner time")


# to convert time entered as string in 24hr format to a float value
def convert(time):
    hours, minutes = time.split(":")
    time_in_hours = float(int(hours) + int(minutes)/60)
    return time_in_hours


if __name__ == "__main__":
    main()
