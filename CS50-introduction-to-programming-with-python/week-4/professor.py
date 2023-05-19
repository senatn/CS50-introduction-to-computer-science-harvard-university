import random


def main():
    level = get_level()
    score = 0
    errors = 0

    for _ in range(10):
        x = generete_integer(level)
        y = generete_integer(level)
        answer = x + y
        while True:
            if errors < 3:
                try:
                    users_answer = input(f"{x} + {y} = ")
                    if int(users_answer) == answer:
                        score +=1
                        break
                    else:
                        print("EEE")
                        errors +=1
                        pass
                except ValueError:
                    print("EEE")
                    errors +=1
                    pass
            elif errors == 3:
                    print(f"{x} + {y} = {answer}")
                    errors = 0
                    break
    print(f"Score : {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level <= 0 or level > 3:
                raise ValueError
            return level
        except ValueError:
            pass


def generete_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    else:
        return random.randint(100,999)


if __name__ == "__main__":
    main()