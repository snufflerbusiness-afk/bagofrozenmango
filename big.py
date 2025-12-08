import turtle as t
import time



t.setup(600,600,0,0)
t.bgcolor(0.5, 0.5, 0.5)
t.tracer(0)



for row in range(15):
	for col in range(15):
		color = (1, 1, 1) if (row+col)%2 == 0 else (0, 0, 0)
		t.color(color)
		t.up()
		t.goto(row*30-200, col*30-200)
		t.down()
		t.begin_fill()
		for i in range(4):
			t.fd(30)
			t.lt(90)
		t.end_fill()

dotcolor=1	


def dot(x, y):
	t.color("green")
	t.goto(round(int(x/30))*30+8 ,round(int(y/30))*30+8)
	t.dot(10)
	color = (1, 1, 1) if (dotcolor)%2 == 0 else (0, 0, 0)
	dotcolor=dotcolor-1
