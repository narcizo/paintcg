from tkinter import *

root = Tk()
root.title("Paint CG")
root.resizable(0,0)
canvas_width = 1000
canvas_height = 500
points = []




class Application:

	def __init__(self, master=None):
		primeiroContainer = Frame(master, width=100, height=100)
		primeiroContainer["pady"] = 10
		primeiroContainer["padx"] = 10
		primeiroContainer.pack(side=LEFT)		


		clear = Button(primeiroContainer)
		clear["text"] = "Clear"
		clear["font"] = ("Calibri", "8")
		clear["command"] = self.clearCanvas
		clear.config (height = 0, width = 15)
		clear["pady"] = 0
		clear["padx"] = 0
		clear.pack(side=BOTTOM)

		linha = Button(primeiroContainer)
		linha["text"] = "Linha"
		linha["font"] = ("Calibri", "8")
		linha.config (height = 0, width = 15)
		linha["command"] = self.drawLine
		linha["pady"] = 0
		linha["padx"] = 0 
		linha.pack(side=TOP)

		retangulo = Button(primeiroContainer)
		retangulo["text"] = "Retangulo"
		retangulo["font"] = ("Calibri", "8")
		retangulo.config (height = 0, width = 15)
		retangulo["command"] = self.drawRectangle
		retangulo["pady"] = 0
		retangulo["padx"] = 0
		retangulo.pack(side=TOP)	


		triangulo = Button(primeiroContainer)
		triangulo["text"] = "Triangulo"
		triangulo["font"] = ("Calibri", "8")
		triangulo.config (height = 0, width = 15)
		triangulo["command"] = self.drawTriangle
		triangulo["pady"] = 0
		triangulo["padx"] = 0
		triangulo.pack(side=TOP)	




	def clearCanvas(self):
		mainCanvas.delete("all")

	def drawLine(self):
		def point(event):
			x1, y1 = (event.x -1), (event.y -1)
			x2, y2 = (event.x +1), (event.y +1)
			points.append(event.x)
			points.append(event.y)
		
		def	graph(event):
			x1, y1 = (event.x-1), (event.y-1)
			x2, y2 = (event.x+1), (event.y+1)
			points.append(event.x)
			points.append(event.y)
			mainCanvas.create_line(points)
			i = len(points)
			while i > 0:
				points.pop()
				i = i-1
		mainCanvas.bind ("<ButtonPress-1>", point)
		mainCanvas.bind ("<ButtonRelease-1>", graph)
	
	def drawRectangle(self):
		def rPoint(event):
			x1, y1 = (event.x-1), (event.y-1)
			x2, y2 = (event.x+1), (event.y+1)
			points.append(event.x)
			points.append(event.y)
		
		def rGraph(event):
			x1, y1 = (event.x-1), (event.y-1)
			x2, y2 = (event.x+1), (event.y+1)
			points.append(event.x)
			points.append(event.y)	
			mainCanvas.create_rectangle(points)
			i = len(points)
			while i > 0:
				points.pop()
				i = i-1
		mainCanvas.bind ("<ButtonPress-1>", rPoint)
		mainCanvas.bind ("<ButtonRelease-1>", rGraph)

	def drawTriangle(self):
		def tPoint(event):
			x1, y1 = (event.x-1), (event.y-1)
			x2, y2 = (event.x+1), (event.y+1)
			points.append(event.x)
			points.append(event.y)
		
		def tGraph(event):
			x1, y1 = (event.x-1), (event.y-1)
			x2, y2 = (event.x+1), (event.y+1)
			points.append(event.x)
			points.append(event.y)	
			mainCanvas.create_triangle(points)
			i = len(points)
			while i > 0:
				points.pop()
				i = i-1
		mainCanvas.bind ("<ButtonPress-1>", tPoint)
		mainCanvas.bind ("<ButtonRelease-1>", tGraph)




mainCanvas = Canvas(root, width = canvas_width, height = canvas_height, bg="white")
mainCanvas.pack(expand = True, fill = "both")
Application(root)
root.mainloop()
