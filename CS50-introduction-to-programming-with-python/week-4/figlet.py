import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

def main():
    fig_let()

def fig_let():
    if len(sys.argv) == 1:
        input_text = input("Input: ")
        random_font = random.choice(figlet.getFonts())
        figlet.setFont(font=random_font)
        print(figlet.renderText(input_text))

    elif len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            chosen_font = sys.argv[2]
            if chosen_font in figlet.getFonts():
                input_text = input("Input: ")
                figlet.setFont(font=sys.argv[2])
                print(figlet.renderText(input_text))
            else:
                sys.exit("Invalid usage")

        else:
            sys.exit("Invalid usage")

    else:
        sys.exit("Invalid usage")
        

if __name__ == "__main__":
    main()