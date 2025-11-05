
import sys
menu={
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

total_in_basket = 0

while True:
    try:
        basket = input('Select an Item: ').title()

        if basket in menu:
            price = menu[basket]
            total_in_basket += price
            print(f'Total: ${total_in_basket:.2f} \n')
            prompt = input('Do you want to add more? ')

            attempt = input("Do you want to add more?: ")
            if attempt in ["yes", "yea", "si", "neh", "definitly"]:
                continue
            else:
                print('Your order will be served shortly!')
                sys.exit(1)
        else:
            print ('Invalid Selection try again')

    except EOFError:
        sys.exit(1)

    except KeyboardInterrupt:
        print('Interuppted by user')
        sys.exit(1)