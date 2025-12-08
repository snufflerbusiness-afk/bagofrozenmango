theme: jekyll-theme-minimal
title: Bagofrozenmango
description: Bookmark this to keep an eye on my project updates!

@import "{{Midnight}}";

import turtle as t
import random

rain= 0.1

thickness = 1



def draw_branch(x, y, size, heading):
	t.up()
	t.goto(x, y)
	t.down()
	t.seth(heading)
	t.fd(size)

def fractal_tree(x, y, size, heading, level, gap):


	# change for each level
	if level == 0:
		return


	# center branch
	draw_branch(x, y, size, heading)
	fractal_tree(t.xcor(), t.ycor(), size/2, t.heading(), level-1, gap)

	# left branch
	draw_branch(x, y, size, heading+random.randint(20, 40))
	fractal_tree(t.xcor(), t.ycor(), size/2, t.heading(), level-1, gap)

	# right branch
	draw_branch(x, y, size, heading-random.randint(20, 40))
	fractal_tree(t.xcor(), t.ycor(), size/2, t.heading(), level-1, gap)

	t.pensize(thickness*level)

	if level < 5:
		t.color(0,random.randint(40, 50)/100,0)
		t.dot(20)
		t.color('saddle brown')
	else:
		
		t.color('saddle brown')

	

	

t.bgcolor(0, 0, 0)
t.color('saddle brown')
t.pensize(thickness*6)
t.tracer(0)
t.ht()

fractal_tree(0,-100, 200, 90, 7, 30)

t.penup()
t.goto(0,-100)
t.pendown()
t.goto(0,-200)


t.update()
t.done()
