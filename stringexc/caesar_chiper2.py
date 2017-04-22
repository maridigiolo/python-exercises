import string

let = string.ascii_lowercase
# print (let)

text = input("Type the text to be cipher: ")

text = text.lower()

for i in text:
    if i == " ":
        print(i, end="")
        continue

    letindex  = let.index(i)
    letchip = letindex + 13

    if letchip <= 25:
        letter = letchip
        enc = let[letter]

    elif letchip > 25:
        letter = letchip - 26
        enc = let[letter]

    print (enc, end="")

print (" ")
