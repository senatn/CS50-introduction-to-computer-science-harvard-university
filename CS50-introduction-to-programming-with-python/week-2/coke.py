def main():
    coin_calculator()


def coin_calculator():
    total_coin = 0
    amount_due = 50
    while total_coin < 50:
        try:
            insert_coin = int(input("Insert Coin: "))
        except ValueError:
            print("upss!")
            break
        if insert_coin == 25 or insert_coin == 10 or insert_coin == 5:
            amount_due -= insert_coin
            if amount_due > 0:
                print("Amount Due:", amount_due)
            total_coin += insert_coin
        else:
            print("Amount Due:", amount_due)
    if total_coin >= 50:
        print("Change Owed:",total_coin - 50)


if __name__ == "__main__":
    main()