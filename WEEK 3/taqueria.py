def main():
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
    sum = 0
    while True:
        try:
            item = input("Item: ").title()
            sum += menu[item]
            print(f"Total: ${sum:0.2f}")
        except KeyError:
            print("Please enter an item which is in the menu")
        except EOFError:
            print()
            break
main()
