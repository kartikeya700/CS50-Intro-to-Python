def main():
   price = 50
   amount = 50
   paid = 0
   coins = [25, 10, 5]
   while amount > 0:
      print(f"Amount Due: {amount}")
      pay = int(input("Insert Coin: "))
      if pay in coins:
         amount = amount - pay
         paid = paid + pay
      if paid >= price:
         print(f"Change Owed: {paid - 50}")
main()
