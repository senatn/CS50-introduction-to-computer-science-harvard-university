def fuel_gauge():
    while True:
        try:
            x, y = map(int,input("Fraction: ").split("/"))
            fuel = x / y
            if fuel > 1:
                continue
            break
        except (ValueError, ZeroDivisionError):
            pass


    percentage  = round(fuel * 100)
    if percentage  >= 99:
        print("F")
    elif percentage  <= 1:
        print("E")
    else:
        print(f"{percentage }%")


fuel_gauge()