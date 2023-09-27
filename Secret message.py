alphabet = "abcdefghijklmnopqrstuvwxyz"
string = input().lower()
encoded = ""
for chars in string:
    if chars == " ":
        encoded += chars
    else:
        index = alphabet.find(chars)
        encoded += alphabet[-index - 1]
print(encoded)

