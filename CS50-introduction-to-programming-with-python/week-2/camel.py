def main():
    camel_case = str(input("camelCase: "))
    snake_case = convert_case(camel_case)
    print("snake_case:", snake_case)


def convert_case(case):
    for char in case:
        if char == char.upper():
            case = case.replace(char, "_" + char.lower())
    return case


if __name__ == "__main__":
    main()