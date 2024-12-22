def main():
    item_list = []
    while True:
        # appends the list of grocery items until user ends input with Ctrl+D
        try:
            item_list.append(input().lower().strip())
        except EOFError:
            break
    item_quantity = {}
    # stores quantity of each item in dictionary
    for item in item_list:
        if (item in item_quantity):
            item_quantity[item] += 1
        else:
            item_quantity[item] = 1
    # sorts the list of grocery items alphabetically
    grocery_items = list(item_quantity.keys())
    grocery_items.sort()
    # creates a sorted dictionary with the quantity of each item stored in their keys
    grocery_list = {i: item_quantity[i] for i in grocery_items}
    # prints the list
    for item in grocery_list:
        print(f"{grocery_list[item]} {item  .upper()}")


main()
