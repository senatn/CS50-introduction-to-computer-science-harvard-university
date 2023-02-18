def main():
    answer = str(input("What is the Answer to the Great Question of Life, the Universe and Everything? ")).lower().strip()
    print(deep_thought(answer))


def deep_thought(answer):
    if answer == "42" or answer == "forty-two" or answer == "forty two":
        return "Yes"
    else:
        return "No"


main()