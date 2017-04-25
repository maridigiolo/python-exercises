#!/usr/bin/env python3

#phar - Objects are like people. They're living, breathing things that have knowledge inside them about how to do things and have memory inside them so they can remember things.

phar = input('Paste a paragraph: ').split()
histlist = {}

for word in phar:
    tally = 0
    if word in histlist:
        tally += 1
    else:
        histlist[word]


print(histlist)
