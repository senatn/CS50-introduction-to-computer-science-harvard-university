def main():
    greeting = str(input("Greeting: ")).lower().strip()
    print(how_much_money(greeting))


def how_much_money(greeting):
    if greeting[:5] == "hello":
        return "$0"
    elif greeting[:1] == "h":
        return "$20"
    else:
        return "$100"


main()