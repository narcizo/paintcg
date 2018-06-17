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


		circulo = Button(primeiroContainer)
		circulo["text"] = "Circulo"
		circulo["font"] = ("Calibri", "8")
		circulo.config (height = 0, width = 15)
		circulo["command"] = self.drawCircle
		circulo["pady"] = 0
		circulo["padx"] = 0
		circulo.pack(side=TOP)	


		triangulo = Button(primeiroContainer)
		triangulo["text"] = "Triangulo"
		triangulo["font"] = ("Calibri", "8")
		triangulo.config (height = 0, width = 15)
		triangulo["command"] = self.drawTriangle
		triangulo["pady"] = 0
		triangulo["padx"] = 0
		triangulo.pack(side=TOP)	




	def clearCanvas(self):
		infoLabel["text"] = ""
		mainCanvas.delete("all")
		def clearEvent(event):
			None		

		mainCanvas.bind("<ButtonPress-1>", clearEvent)
		mainCanvas.bind("<ButtonRelease-1>", clearEvent)


	def drawTriangle(self):
		infoLabel["text"] = "Escolha três pontos para desenhar o triângulo"
		def tPoint(event):
			if len(points) < 6:
				x1, y1 = (event.x -1), (event.y -1)
				x2, y2 = (event.x +1), (event.y +1)
				mainCanvas.create_oval(x1, y1, x1, y1, fill="black")
				points.append(event.x)
				points.append(event.y)
			else:
				mainCanvas.create_polygon(points, outline='black', fill='white')
				i = len(points)
				while i > 0:
					points.pop()
					i = i-1	
		
		def	tGraph(event):
			None

		mainCanvas.bind ("<ButtonPress-1>", tPoint)
		mainCanvas.bind ("<ButtonRelease-1>", tGraph)
	

	def drawLine(self):
		infoLabel["text"] = "Clique e arraste para desenhar a linha"
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
		infoLabel["text"] = "Clique e arraste para desenhar o retângulo"
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

	def drawCircle(self):
		infoLabel["text"] = "Clique e arraste para desenhar o circulo"
		def cPoint(event):
			x1, y1 = (event.x-1), (event.y-1)
			x2, y2 = (event.x+1), (event.y+1)
			points.append(event.x)
			points.append(event.y)
		
		def cGraph(event):
			x1, y1 = (event.x-1), (event.y-1)
			x2, y2 = (event.x+1), (event.y+1)
			points.append(event.x)
			points.append(event.y)	
			mainCanvas.create_oval(points)
			i = len(points)
			while i > 0:
				points.pop()
				i = i-1
		mainCanvas.bind ("<ButtonPress-1>", cPoint)
		mainCanvas.bind ("<ButtonRelease-1>", cGraph)




mainCanvas = Canvas(root, width = canvas_width, height = canvas_height, bg="white")
mainCanvas.pack(expand = True, fill = "both")

coordLabel = Label(root, text="Coordenadas")
coordLabel["font"] = ("Calibri", "8")
coordLabel.pack(side=BOTTOM)

infoLabel = Label(root)
infoLabel["font"] = ("Calibri", "8")
infoLabel.pack(side = TOP)

def motion(event):
	posx, posy = event.x, event.y
	coordLabel["text"] = ("PosX = " + str(posx) + " PosY = " + str(posy))	

mainCanvas.bind('<Motion>', motion)



Application(root)
root.mainloop()
