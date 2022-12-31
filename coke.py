values = []

def main():
    while True:
        values.append(get_coins())
        money = sum(values)
        diff = 50 - money
        if 0 < money < 50:
            print("Amount owed: ", diff)
        else:
            break
    print("Change owed: ", abs(diff))

def get_coins():
    coin = input("Enter coin: ")
    only_coin = int(coin)
    if only_coin == 5:
        return 5
    elif only_coin == 10:
        return 10
    elif only_coin ==25:
        return 25
    else:
        return 0

main()
