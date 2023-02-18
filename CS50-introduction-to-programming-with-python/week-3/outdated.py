months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def iso_8601_date():
    while True:
        try:
            date = input("Date: ").strip().split(" ")
            if date[0] in months and int(date[1][:-1]) < 32:
                print(f"{date[2]:04}-{(months.index(date[0]) + 1):02}-{int(date[1][:-1]):02}")
                break
            else:
                date = date[0].split("/")
                if int(date[0]) < 13 and int(date[1]) < 32:
                    print(f"{date[2]:04}-{int(date[0]):02}-{int(date[1]):02}")
                    break
        except (ValueError, IndexError, KeyboardInterrupt):
            pass

iso_8601_date()