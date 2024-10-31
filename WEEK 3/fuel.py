def main():
    fuel = fuel_gauge()
    if fuel <= 1:
        print("E")
    elif fuel > 100:
        main()
    elif fuel >= 99:
        print("F")
    else:
        print(f"{fuel}%")

def fuel_gauge():
    while True:
        try:
            x,y = input("How much fuel is in the tank (in fractions)? ").split("/")
            X = int(x)
            Y = int(y)
            return int(round((X/Y)*100,0))
        except ValueError:
            print("Please enter a valid fuel amount")
        except ZeroDivisionError:
            print("Fuel amount can't have zero in denominator")
main()
