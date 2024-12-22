def main():
    # User inputs bill amount and tip percent
    dollars = meal_cost(input("How much did the meal cost? "))
    tip_percent = tip_percentage(input("How much do you want to tip? "))
    # Calculate tipping amount
    tip_amount = dollars * tip_percent
    print(f"Leave ${tip_amount:0.2f}")

# Function to convert string input in meal cost to float
def meal_cost(str_1):
    return float(str_1.replace("$", ""))

# Function to convert percentage to float value
def tip_percentage(str_2):
    return float(str_2.replace("%", ""))/100


main()
