from turtle import *

speed(0)
bgcolor('darkblue')

# def stars(size):
# 	b = (size/2.6)
# 	c = (size/4.24)
# 	begin_fill()
# 	color('white', 'white')
# 	for i in range(5):
# 		fd(size)
# 		right(144)
# 	up()
# 	fd(b)
# 	down()
# 	for j in range (5):
# 		fd(c)
# 		right(72)
# 	end_fill()
# 
# 
# stars(45)
#mainloop()



import turtle
import random

def draw_star(size, color):
	angle = 120
	turtle.fillcolor(color)
	
	for qtd in range(random.randint(1, 20)):
		turtle.begin_fill()
		for side in range(5):
			turtle.forward(size)
			turtle.right(angle)
			turtle.forward(size)
			turtle.right(72 - angle)
		turtle.end_fill()
		
		turtle.penup()
		x = random.randint(-500, 500)
		y = random.randint(-360, 360)
		turtle.setx(x)
		turtle.sety(y)
		turtle.pendown()
		
	return

for sz in range (4, 13):
	draw_star(sz, "yellow")

turtle.mainloop()

