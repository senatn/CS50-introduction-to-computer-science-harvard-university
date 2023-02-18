def main():
    exp = input('What time is it? ').strip()
    t = convert(exp)
    if 7 <= t <= 8:
        print('breakfast time')
    elif 12 <= t <= 13:
        print('lunch time')
    elif 18 <= t <= 19:
        print('dinner time')
    else:
        pass


def convert(time):
    if time.find(" ") != -1:
        time, time_format = time.split()
        hour, minute = time.split(":")
        hour = float(hour)
        minute = float(minute)
        if time_format == "p.m" or time_format == "pm":
            return hour + 12 + (minute / 60)
        else:
            return hour + (minute / 60)
    else:
        hour, minute = time.split(":")
        hour = float(hour)
        minute = float(minute)
        return hour + (minute / 60)


if __name__ == "__main__":
    main()