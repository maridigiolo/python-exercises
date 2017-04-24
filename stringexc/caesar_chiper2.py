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

#!/usr/bin/env python3

import string
import sys

def caesar_decipher (rotation, text):
  answer = ''
  for t in text:
    t = t.lower()
    if t in string.ascii_lowercase:
      index = string.ascii_lowercase.index(t)
      index = index - rotation
      t = string.ascii_lowercase[index]

    answer += t

  return answer

if __name__ == '__main__':
  rotation = int(sys.argv[1])
  text = sys.argv[2]
  answer = caesar_decipher(rotation, text)
  print('Answer: {}'.format(answer))
  
