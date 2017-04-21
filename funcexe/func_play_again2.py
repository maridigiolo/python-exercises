#!/usr/bin/env python3
	
def f():
	ans = input('Do you want to play again? Ans - Y or N ')
	return ans

while True:
	ans = f()
	if ans == 'Y':
		continue
		
	elif ans == 'N':
		break
	else:
		print('Invalid Input')
		