#!/usr/bin/env python3

def hello (name):
	print ('Hello {}'.format(name))
	
if __name__ == "__main__":
	name = input("name? ")
	hello(name)
	