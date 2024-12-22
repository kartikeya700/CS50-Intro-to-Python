def main():
    # list of items in menu along with their pricse in dollars
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    bill = 0
    while True:
        # executes only if item name is in menu
        try:
            item = input("Item (Ctrl + D to end order): ").title()
            # adds cost of item entered and prints total current bill amount
            bill += menu[item]
            print(f"Total: ${bill:0.2f}")
        # terminates if item is not in list
        except KeyError:
            print("Please enter an item which is in the menu")
        # to terminate program if user inputs Ctrl + D
        except EOFError:
            print()
            break


main()
