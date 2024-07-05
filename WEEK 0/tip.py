def main():
    Dollars = dollars(input("How much did the meal cost? "))
    Percent = percent(input("How much do you want to tip? "))
    tip = Dollars * Percent
    print(f"Leave ${tip:0.2f}")
def dollars(str_1):
    return float(str_1.replace("$",""))
def percent(str_2):
    return float(str_2.replace("%",""))/100
main()
