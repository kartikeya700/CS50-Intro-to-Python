def main():
    fuel = fuel_gauge()
    # checks amount of fuel in tank and returns condition of fuel tank accordingly
    if fuel <= 1:
        print("E")
    elif fuel > 100:
        main()
    elif fuel >= 99:
        print("F")
    else:
        print(f"{fuel}%")


# to take input and convert fractional fuel amount to percentage
def fuel_gauge():
    while True:
        # executes code if input is valid
        try:
            x, y = input("How much fuel is in the tank (in fractions)? ").split("/")
            X = int(x)
            Y = int(y)
            return int(round((X/Y) * 100, 0))
        # terminates the code if the values entered in fraction are not valid
        except ValueError:
            print("Please enter a valid fuel amount")
        # terminates code if denominator of fractional fuel amount is zero
        except ZeroDivisionError:
            print("Fuel amount can't have zero in denominator")


main()
