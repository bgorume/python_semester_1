# coke.py

amount_due = 50

while amount_due > 0:
    print(f"Amount Due: {amount_due}")
    coin = input("Insert Coin: ")


    try:
        coin = int(coin)
    except ValueError:
        continue  # ignore invalid inputs


    if coin in [25, 10, 5]:
        amount_due -= coin
    else:
        continue  # ignore invalid coins

if amount_due < 0:
    print(f"Change Owed: {abs(amount_due)}")
else:
    print("Change Owed: 0")

