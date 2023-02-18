def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    counter = 0
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_ ~'''
    punctuations_counter = 0
    numbers = []

    # vanity plates may contain a maximum of 6 characters (letters or numbers)
    # and a minimum of 2 characters.
    # All vanity plates must start with at least two letters.
    if len(s) >= 2 and len(s) <= 6 and s[0].isalpha() and s[1].isalpha():
        counter += 1


    # The first number used cannot be a ‘0’
    # Numbers cannot be used in the middle of a plate.
    for char in s:
        if char.isdigit():
            numbers.append(char)
    if len(numbers) == 0:
        counter += 1
    if len(numbers) > 0 and list(s[-len(numbers):]) == numbers and numbers[0] != "0":
        counter += 1


    # No periods, spaces, or punctuation marks are allowed.
    for char in s:
        if char not in punctuations:
            punctuations_counter += 1
    if len(s) == punctuations_counter:
        counter += 1


    if counter == 3:
        return True
    else:
        return False


main()