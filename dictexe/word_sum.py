#!/usr/bin/env python3

word = input('Paste a paragraph: ')
histlist = {}

tally = 0
for wrds in word:
    if wrds not in histlist:
        tally += 1

    if tally > 0:
        histlist[wrds] = tally

print(histlist)
