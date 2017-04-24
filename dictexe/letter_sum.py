#!/usr/bin/env python3

import string
# letters = string.ascii_lowercase
# #print (letter)
#
# word = input('Type any word: ')
# histlist = {}

# for i in letters:
#     tally = 0
#     for chac in word:
#         if chac == i:
#             tally += 1
#
#     if tally > 0:
#         histlist[i] = tally
# print(histlist)


def histogram (word):
    letters = string.ascii_lowercase
    #print (letter)
    histlist = {}

    for i in letters:
        tally = 0
        for chac in word:
            if chac == i:
                tally += 1

            else:
                pass

            if tally > 0:
                histlist[i] = tally

    return histlist

if __name__ == '__main__':
    word = input('Type any word: ')
    histlist = histogram(word)
    print(histlist)
