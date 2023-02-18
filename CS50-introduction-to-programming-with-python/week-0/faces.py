def main ():
    text = str(input(""))
    convert(text)

def convert(text):
    print(text.replace(":)", "🙂").replace(":(", "🙁"))

main()