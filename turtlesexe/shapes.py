from turtle import *


# an equilateral triangle
def eqtrig(arg1):
	for i in range(3):
		forward(arg1)
		right(120)
 	
 
#a square 
def sqr(arg2):
 	for i in range(4):
 		forward(arg2)
 		right(90)
  
  	 
#a pentagon
def pent(arg3):
	for i in range(5):
		forward(arg3)
		right(72)
 
#a hexagon
def hex(arg4):
	for i in range(6):
		forward(arg4)
		right(60)
 		 
 		 
#an octagon
def oct(arg5):
	for i in range(8):
		forward(arg5)
		right(45)
 
  
#a star
def str(arg6):
 	for i in range(5):
 		forward(arg6)
 		right(144)
 

#a circle
def crcl(arg7, arg8, arg9):
	pencolor(arg7)
	width(arg8)
	circle(arg9)

if __name__ == "__main__":
	eqtrig(arg1)
	sqr(arg2)
	pent(arg3)
	hex(arg4)
	oct(arg5)
	str(arg6)
	crcl(arg7, arg8, arg9)

	mainloop()