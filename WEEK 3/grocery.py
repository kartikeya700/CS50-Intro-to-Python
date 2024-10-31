def main():
    item = []
    while True:
        try:
            item.append(input().lower().strip())
        except EOFError:
            break
    my_list = {}
    for items in item:
        if (items in my_list):
            my_list[items] += 1
        else:
            my_list[items] = 1
    grocery_items = list(my_list.keys())
    grocery_items.sort()
    grocery_list = {i : my_list[i] for i in grocery_items}
    for items in grocery_list:
        print(f"{grocery_list[items]} {items.upper()}")
main()
