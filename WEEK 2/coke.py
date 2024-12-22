def main():
    # sets price and amount due to a value
    price = 50
    amount = 50
    paid = 0
    # denominations of coins accepted by machine
    coins = [25, 10, 5]
    # to ask the user for money until amount due is not zero
    while amount > 0:
        print(f"Amount Due: {amount}")
        pay = int(input("Insert Coin: "))
        # if the denomination of coin entered is accepted then that amount is deducted from the amount due
        if pay in coins:
            amount = amount - pay
            paid = paid + pay
        else:
            print("Invalid coin")
            continue
   # if amount paid is greater than amount due then return the change
    if paid >= price:
       print(f"Change Owed: {paid - 50}")


main()
