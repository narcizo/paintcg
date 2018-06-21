from tkinter import *

root = Tk()
root.title("Paint CG")
root.resizable(0,0)
canvas_width = 1000
canvas_height = 500
points = []


def resetLabels():
	operacaoEntry.pack_forget()
	operacoesLabel["text"] = ""
	infoLabel["text"] = ""


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

		select = Button(primeiroContainer)
		select["text"] = "Seleção Livre"
		select["font"] = ("Calibri", "8")
		select.config(height = 0, width = 15)
		select["command"] = self.freeSelect
		select["pady"] = 0
		select["padx"] = 0
		select.pack(side=TOP)

		rotate	= Button(primeiroContainer)
		rotate["text"] = "Rotacionar Objeto"
		rotate["font"] = ("Calibri", "8")
		rotate.config(height = 0, width = 15)
		rotate["command"] = self.rotatingSelect
		rotate["pady"] = 0
		rotate["padx"] = 0
		rotate.pack(side=TOP)

		translate = Button(primeiroContainer)
		translate["text"] = "Transladar Objeto"
		translate["font"] = ("Calibri", "8")
		translate.config(height = 0, width = 15)
		translate["command"] = self.translateSelect
		translate["pady"] = 0
		translate["padx"] = 0
		translate.pack(side=TOP)

		scale = Button(primeiroContainer)
		scale["text"] = "Mudar Escala"
		scale["font"] = ("Calibri", "8")
		scale.config(height = 0, width = 15)
		scale["command"] = self.scaleChange
		scale["pady"] = 0
		scale["padx"] = 0
		scale.pack(side=TOP)



	def freeSelect(self):
		operacaoEntry.pack_forget()
		operacoesLabel["text"] = ""
		def selectObj(event):
			mx = mainCanvas.canvasx(event.x)
			my = mainCanvas.canvasy(event.y)
			self.canvasObject = mainCanvas.find_closest(mx, my, halo=5)
			self.canvasObject.config(outline='red')


		def fClear(event):
			None

		mainCanvas.bind("<ButtonPress-1>", selectObj)
		mainCanvas.bind("<ButtonRelease-1>", fClear)


	def scaleChange(self):
		resetLabels()
		def scaleObj(event):
			mx = mainCanvas.canvasx(event.x)
			my = mainCanvas.canvasy(event.y)
			canvasObject = mainCanvas.find_closest(mx, my, halo=5)
			newEscala = operacaoEntry.get()
			resetLabels()
			#implementar operaçao de mudança de escala
		
		def sClear(event):
			None
		
		mainCanvas.bind("<ButtonPress-1>", scaleObj)
		mainCanvas.bind("<ButtonRelease-1>", sClear)	


	def rotatingSelect(self):
		resetLabels()
		
		def rotateObj(event):
			mx = mainCanvas.canvasx(event.x)
			my = mainCanvas.canvasy(event.y)
			canvasObject = mainCanvas.find_closest(mx, my, halo=5)
			angulo = operacaoEntry.get()
			resetLabels()
			#implementar operacao de rotaçao

		def ffClear(event):
			None

		mainCanvas.bind("<ButtonPress-1>", rotateObj)
		mainCanvas.bind("<ButtonRelease-1>", ffClear)


	def translateSelect(self):
		resetLabels()
	
		def getObj(event):
			mx = mainCanvas.canvasx(event.x)
			my = mainCanvas.canvasy(event.y)
			canvasObject = mainCanvas.find_closest(mx, my, halo=5)
			#implementar operacao de translaçao
		
		def transObj(event):
			None		


		mainCanvas.bind("<ButtonPress-1>", getObj)
		mainCanvas.bind("<ButtonRelease-1>", transObj)



	def clearCanvas(self):
		operacaoEntry.pack_forget()
		operacoesLabel["text"] = ""
		mainCanvas.delete("all")
		def clearEvent(event):
			None

		mainCanvas.bind("<ButtonPress-1>", clearEvent)
		mainCanvas.bind("<ButtonRelease-1>", clearEvent)


	def drawTriangle(self):
		operacaoEntry.pack_forget()
		operacoesLabel["text"] = ""

		infoLabel["text"] = "Escolha três pontos para desenhar o triângulo"
		def tPoint(event):
			if len(points) < 6:
				x1, y1 = (event.x -1), (event.y -1)
				x2, y2 = (event.x +1), (event.y +1)
				mainCanvas.create_oval(x1, y1, x1, y1, fill="black")
				points.append(event.x)
				points.append(event.y)
			else:
				mainCanvas.create_polygon(points, outline='black', fill='')
				i = len(points)
				while i > 0:
					points.pop()
					i = i-1

		def	tGraph(event):
			None

		mainCanvas.bind ("<ButtonPress-1>", tPoint)
		mainCanvas.bind ("<ButtonRelease-1>", tGraph)


	def drawLine(self):
		operacaoEntry.pack_forget()
		operacoesLabel["text"] = ""

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
		operacaoEntry.pack_forget()
		operacoesLabel["text"] = ""

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
		operacaoEntry.pack_forget()
		operacoesLabel["text"] = ""

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



#definição canvas e labels
mainCanvas = Canvas(root, width = canvas_width, height = canvas_height, bg="white")
mainCanvas.pack(expand = True, fill = "both")


coordLabel = Label(root, text="Coordenadas")
coordLabel["font"] = ("Calibri", "8")
coordLabel.pack(side=BOTTOM)

infoLabel = Label(root)
infoLabel["font"] = ("Calibri", "8")
infoLabel.pack(side = TOP)

#definições containers entrada de valor mudança escala e rotaçao
containerOperacoes = Frame(root)
containerOperacoes.pack(side = RIGHT)
operacoesLabel = Label(containerOperacoes)
operacoesLabel["font"] = ("Calibri", "8")
operacoesLabel.pack(side=LEFT)
operacaoEntry = Entry(containerOperacoes)

# posicao cursor
def motion(event):
	posx, posy = event.x, event.y
	coordLabel["text"] = ("PosX = " + str(posx) + " PosY = " + str(posy))

mainCanvas.bind('<Motion>', motion)



Application(root)
root.mainloop()
