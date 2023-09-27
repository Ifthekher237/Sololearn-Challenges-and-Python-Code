string = input()
splitted_string = string.split(" ")
index = 0
for word in splitted_string:
    converted_word = word[1:] + word[0] + "ay"
    splitted_string[index] = converted_word
    index += 1
pig_latin = " ".join(splitted_string)
print(pig_latin)