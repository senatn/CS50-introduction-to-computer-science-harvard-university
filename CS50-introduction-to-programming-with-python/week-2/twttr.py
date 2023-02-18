vowels = "AEIOUaeiou"
text = input("Input: ")
result = ''.join(c for c in text if c not in vowels)
print("Output:",result)