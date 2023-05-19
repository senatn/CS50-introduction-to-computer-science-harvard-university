def get_farewell_message(names):
    if len(names) == 0:
        return ""
    elif len(names) == 1:
        return "Adieu, adieu, to "+names[0]
    elif len(names) == 2:
        return "Adieu, adieu, to "+names[0]+" and "+names[1]
    else:
        farewell_message = "Adieu, adieu, to "
        for i in range(len(names)-1):
            farewell_message += names[i] + ", "
        farewell_message += "and "+names[-1]
        return farewell_message

names = []
try:
    while True:
        name = input("Name: ").capitalize()
        names.append(name)
except EOFError:
    print()
    print(get_farewell_message(names))
