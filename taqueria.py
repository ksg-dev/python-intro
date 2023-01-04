menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}




def main():
    orders = []
    total = 0
    while True:
        try:
            x = input("Item: ").title()
            price = int(menu[x] * 100)
            orders.append(price)
            total = sum(orders)
            print("Total: $", (total / 100),"0", sep="")
        except KeyError:
            pass
        except EOFError:
            break
    print()

main()

