from turtex3 import *

arg1 = int(input("Type the size of an equilateral triangle: "))
color1 = input("Choose a color: ")
arg2 = int(input("Type the size of a square: "))
color2 = input("Choose a color: ")
# arg3 = int(input("Type the size of a pentagon: "))
# arg4 = int(input("Type the size of a hexagon: "))
# arg5 = int(input("Type the size of an octagon: "))
# arg6 = int(input("Type the size of a star: "))
# arg7 = input("Type a color for a circle line: ")
# arg8 = int(input("Type the width of a circle: "))
# arg9 = int(input("Type the radiu of the circle: "))

fillcolor(color1)
eqtrig(arg1)


up()
forward(100)
down()
fillcolor(color2)
sqr(arg2)
# 
# right(90)
# up()
# forward(200)
# down()
# pent(arg3)
# 
# right(90)
# up()
# forward(200)
# down()
# hex(arg4)
# 
# up()
# forward(200)
# down()
# oct(arg5)
# 
# right(90)
# up()
# forward(400)
# down()
# str(arg6)
# 
# right(90)
# up()
# forward(200)
# down()
# crcl(arg7, arg8, arg9)


mainloop()
 