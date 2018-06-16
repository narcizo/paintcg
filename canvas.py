from tkinter import *


def paint(event):
	python_green ="#476042"
	x1, y1 = (event.x-1), (event.y-1)
	x2,y2 = (event.x+1), (event.y+1)
	backGround.create_oval(x1, y1, x2, y2, fill = python_green)

class Application:
	def __init__(self, master=None):
		width = 400
		height = 400
		backGround = Canvas(master, width=width, height=height, bg="white")
		backGround.pack()
		backGround.bind ("<B1-Motion>", paint)
#		backGround.create_line(400, 0, 0, 400)			
	



root = Tk()
root.title("Trabalho CG")
Application(root)
root.mainloop()
