from tkinter import *
import math

root = Tk()
root.title("Paint CG")
root.resizable(0,0)
canvas_width = 1000
canvas_height = 400
canvas_mid_x = canvas_width/2
canvas_mid_y = canvas_height/2
side = canvas_width/4
points = []
vertices = [
				[canvas_mid_x - side/2, canvas_mid_y - side/2],
				[canvas_mid_x + side/2, canvas_mid_y - side/2],
				[canvas_mid_x + side/2, canvas_mid_y + side/2],
				[canvas_mid_x - side/2, canvas_mid_y + side/2]]
center = (canvas_mid_x, canvas_mid_y)



def resetLabels():
	operacaoEntry.pack_forget()
	operacaoEntry2.pack_forget()
	operacoesLabel["text"] = ""
	infoLabel["text"] = ""
	mainCanvas.itemconfig('all', outline='black')
	def fClear(event):
		None
	mainCanvas.bind("<B1-Motion>", fClear)
	mainCanvas.bind("<ButtonPress-1>", fClear)
	mainCanvas.bind("<ButtonRelease-1>", fClear)
	mainCanvas.bind('<Button-5>', fClear)  # only with Linux, wheel scroll down
	mainCanvas.bind('<Button-4>', fClear)  # only with Linux, wheel scroll up	



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

		moveCnv = Button(primeiroContainer)
		moveCnv	["text"] = "Mover pos canvas"
		moveCnv	["font"] = ("Calibri", "8")
		moveCnv.config(height = 0, width = 15)
		moveCnv["command"] = self.moveCanvas
		moveCnv["pady"] = 0
		moveCnv["padx"] = 0
		moveCnv.pack(side=TOP)
		x0 = mainCanvas.canvasx(0)
		y0 = mainCanvas.canvasy(0)

		zoomExtend = Button(primeiroContainer)
		zoomExtend["text"] = "Zoom Extend"
		zoomExtend["font"] = ("Calibri", "8")
		zoomExtend.config(height = 0, width = 15)
		zoomExtend["command"] = self.zoomExtend
		zoomExtend["pady"] = 0
		zoomExtend["padx"] = 0
		zoomExtend.pack(side=TOP)
		
		zoomMove = Button(primeiroContainer)
		zoomMove["text"] = "Zoom seleciona janela"
		zoomMove["font"] = ("Calibri", "8")
		zoomMove.config(height = 0, width = 15)
		zoomMove["command"] = self.zoomMove
		zoomMove["pady"] = 0
		zoomMove["padx"] = 0
		zoomMove.pack(side=TOP)
		

	def zoomMove(self):
		resetLabels()
		infoLabel["text"] = "Escolha dois pontos, um mais a cima e a esquerda e outro mais a baixo e a direita de onde quer fazer o zoom (zoom 2x)"
		def rPoint(event):
			if len(points) < 4:
				points.append(event.x+mainCanvas.canvasx(0))
				points.append(event.y+mainCanvas.canvasy(0))
			else:
				quadrado = mainCanvas.find_overlapping(points[0], points[1], points[2], points[3])
				print(points)
				i = len(points)
				while i > 0:
					points.pop()
					i = i-1
				counter = 0
				for i in quadrado:
					coords = mainCanvas.coords(quadrado[counter])
					mainCanvas.scale(quadrado[counter], coords[0], coords[1], 2., 2.)
					counter += 1
		def rGraph(event):
			None

		mainCanvas.bind ("<ButtonPress-1>", rPoint)
		mainCanvas.bind ("<ButtonRelease-1>", rGraph)




	def zoomExtend(self):
		resetLabels()
		def focus(event):
			mx = mainCanvas.canvasx(event.x)
			my = mainCanvas.canvasy(event.y)
			canvas_mid_x = (canvas_width/2)+mainCanvas.canvasx(0)
			canvas_mid_y = (canvas_height/2)+mainCanvas.canvasy(0)
			self.canvasObject = mainCanvas.find_closest(mx, my, halo=5)
			coords = mainCanvas.coords(self.canvasObject)
			higherx = coords[2]+mainCanvas.canvasx(0)
			highery = coords[7]+mainCanvas.canvasy(0)
			lowerx = coords[0]+mainCanvas.canvasx(0)
			lowery = coords[1]+mainCanvas.canvasy(0)
			xpos = ((higherx + lowerx) / 2)+mainCanvas.canvasx(0) 
			ypos = ((highery + lowery) / 2)+mainCanvas.canvasy(0)
			mainCanvas.scan_dragto(int(canvas_mid_x-xpos+mainCanvas.canvasx(0)), int(canvas_mid_y-ypos+mainCanvas.canvasy(0)), gain=1)
		def fClear(event):
			None
			
		mainCanvas.bind("<ButtonPress-1>", focus)
		mainCanvas.bind("<ButtonRelease-1>", fClear)

	def moveCanvas(self):
		resetLabels()

		def wheelup(event):
			x = mainCanvas.canvasx(event.x)
			y = mainCanvas.canvasy(event.y)
			scale = 2.
			mainCanvas.scale('all', x, y, scale, scale)
			mainCanvas.configure(scrollregion=mainCanvas.bbox("all"))				

		def wheeldown(event):
			x = mainCanvas.canvasx(event.x)
			y = mainCanvas.canvasy(event.y)
			scale = 0.5
			mainCanvas.scale('all', x, y, scale, scale)
			mainCanvas.configure(scrollregion=mainCanvas.bbox("all"))

		def scroll_start(event):
			x = mainCanvas.canvasx(event.x)
			y = mainCanvas.canvasy(event.y)		
			mainCanvas.scan_mark(event.x, event.y)
#			canvas.configure(scrollregion=canvas.bbox("all"))

		def scroll_move(event):
			x = mainCanvas.canvasx(event.x)
			y = mainCanvas.canvasy(event.y)	
			mainCanvas.scan_dragto(event.x, event.y, gain=1)
#			canvas.configure(scrollregion=canvas.bbox("all"))
		def fClear(event):
			None

		mainCanvas.bind("<ButtonPress-1>", scroll_start)
		mainCanvas.bind("<B1-Motion>", scroll_move)
		mainCanvas.bind("<ButtonRelease-1>", fClear)
#		mainCanvas.bind('<MouseWheel>', wheel)  # with Windows and MacOS, but not Linux
		mainCanvas.bind('<Button-5>', wheeldown)  # only with Linux, wheel scroll down
		mainCanvas.bind('<Button-4>', wheelup)  # only with Linux, wheel scroll up	

	def freeSelect(self):
		resetLabels()
		operacaoEntry.pack_forget()
		operacoesLabel["text"] = ""
		infoLabel["text"] = "Escolha um objeto para seleção ou clique em dois pontos que irão conter os objetos a serem selecionados"
		def selectObj(event):
			mainCanvas.itemconfig('all', outline='black')
			mx = mainCanvas.canvasx(event.x+mainCanvas.canvasx(0))
			my = mainCanvas.canvasy(event.y+mainCanvas.canvasy(0))
			self.canvasObject = mainCanvas.find_closest(mx, my, halo=5)
			mainCanvas.focus(self.canvasObject)
			mainCanvas.itemconfig(self.canvasObject, outline='red')
			
		def selectCon(event):
			mainCanvas.itemconfig('all', outline='black')
			if len(points) < 4:
				points.append(event.x+mainCanvas.canvasx(0))
				points.append(event.y+mainCanvas.canvasy(0))
			else:
				quadrado = mainCanvas.find_overlapping(points[0], points[1], points[2], points[3])
				print(points)
				i = len(points)
				while i > 0:
					points.pop()
					i = i-1
				counter = 0
				for i in quadrado:
					coords = mainCanvas.coords(quadrado[counter])
					mainCanvas.itemconfig(quadrado[counter], outline='red')
					counter += 1


		def fClear(event):
			None
		
		mainCanvas.bind("<ButtonPress-1>", selectCon)
		mainCanvas.bind("<ButtonRelease-1>", fClear)


	def scaleChange(self):
		resetLabels()
		operacoesLabel["text"] = "Insira a proporcao da mudanca de escala e selecione o objeto (proporcao X cima proporcao Y baixo)"
		operacaoEntry.pack(side=TOP)
		operacaoEntry2.pack(side=BOTTOM)
		def scaleObj(event):
			mx = mainCanvas.canvasx(event.x+mainCanvas.canvasx(0))
			my = mainCanvas.canvasy(event.y+mainCanvas.canvasy(0))
			self.canvasObject = mainCanvas.find_closest(mx, my, halo=5)
			newEscalax = operacaoEntry.get()
			newEscalay = operacaoEntry2.get()
			coords = mainCanvas.coords(self.canvasObject)
			mainCanvas.scale(self.canvasObject, coords[0], coords[1], newEscalax, newEscalay)
			
			#implementar operaçao de mudança de escala
		
		def sClear(event):
			None
		
		mainCanvas.bind("<ButtonPress-1>", scaleObj)
		mainCanvas.bind("<ButtonRelease-1>", sClear)	


	def rotatingSelect(self):
		resetLabels()
		operacoesLabel["text"] = "Insira o angulo de rotaçao e selecione qual objeto sera rotacionado (rotaçao no ponto de criaçao)"
		operacaoEntry.pack(side=LEFT)
		def rotateObj(event):
			mx = mainCanvas.canvasx(event.x+mainCanvas.canvasx(0))
			my = mainCanvas.canvasy(event.y+mainCanvas.canvasy(0))
			self.canvasObject = mainCanvas.find_closest(mx, my, halo=5)
			angulo = float(operacaoEntry.get())
			angulo = math.radians(angulo)
			cos_val = math.cos(angulo)
			sin_val = math.sin(angulo)
			coords = mainCanvas.coords(self.canvasObject)
			mainCanvas.delete(self.canvasObject)
			new_coords = coords.copy()
			cx = coords[0]
			cy = coords[1]
			
			#implementar operacao de rotaçao
			posx = 0
			posy = 1
			for coordenadas in coords:
				if (posx <= len(coords)-1):
					coords[posx] -= cx
					coords[posy] -= cy
					new_coords[posx] = (coords[posx] * cos_val - coords[posy] * sin_val) + cx
					new_coords[posy] = (coords[posx] * sin_val + coords[posy] * cos_val) + cy
				posx += 2
				posy += 2
			mainCanvas.create_polygon(new_coords, outline='black', fill='')	
			
				
		def ffClear(event):
			None

		mainCanvas.bind("<ButtonPress-1>", rotateObj)
		mainCanvas.bind("<ButtonRelease-1>", ffClear)


	def translateSelect(self):
		resetLabels()
		operacoesLabel["text"] = "Clique no objeto a ser transladado e arraste para a posiçao desejada (translaçao baseada no ponto de criaçao)"
		def getObj(event):
			mx = mainCanvas.canvasx(event.x)
			my = mainCanvas.canvasy(event.y)
			self.canvasObject = mainCanvas.find_closest(mx, my, halo=5)	
			#implementar operacao de translaçao
		
		def transObj(event):
			mx = mainCanvas.canvasx(event.x)
			my = mainCanvas.canvasy(event.y)
			coords = mainCanvas.coords(self.canvasObject)
			deltaX = mx - coords[0]
			deltaY = my - coords[1]
			mainCanvas.move(self.canvasObject, deltaX, deltaY)
			None		
			###### se pegar o x y novo e subtrair dos x y antigo tem a posicao nova

		mainCanvas.bind("<ButtonPress-1>", getObj)
		mainCanvas.bind("<ButtonRelease-1>", transObj)



	def clearCanvas(self):
		resetLabels()
		mainCanvas.delete("all")
		def clearEvent(event):
			None

		mainCanvas.bind("<ButtonPress-1>", clearEvent)
		mainCanvas.bind("<ButtonRelease-1>", clearEvent)


	def drawTriangle(self):
		resetLabels()

		infoLabel["text"] = "Escolha três pontos para desenhar o triângulo"
		def tPoint(event):
			if len(points) < 6:
				x1, y1 = (event.x -1), (event.y -1)
				x2, y2 = (event.x +1), (event.y +1)
				points.append(event.x+mainCanvas.canvasx(0))
				points.append(event.y+mainCanvas.canvasy(0))
			else:
				mainCanvas.create_polygon(points, outline='black', fill='')
				print(points)
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
		resetLabels()
		infoLabel["text"] = "Clique e arraste para desenhar a linha"
		def point(event):
			x1, y1 = (event.x -1), (event.y -1)
			x2, y2 = (event.x +1), (event.y +1)
			points.append(event.x+mainCanvas.canvasx(0))
			points.append(event.y+mainCanvas.canvasy(0))

		def	graph(event):
			x1, y1 = (event.x-1), (event.y-1)
			x2, y2 = (event.x+1), (event.y+1)
			points.append(event.x+mainCanvas.canvasx(0))
			points.append(event.y+mainCanvas.canvasy(0))
			mainCanvas.create_line(points)
			i = len(points)
			while i > 0:
				points.pop()
				i = i-1
		mainCanvas.bind ("<ButtonPress-1>", point)
		mainCanvas.bind ("<ButtonRelease-1>", graph)

	def drawRectangle(self):
		operacoesLabel["text"] = ""
		resetLabels()
		infoLabel["text"] = "Clique e arraste para desenhar o retângulo"
		def rPoint(event):
			x1, y1 = mainCanvas.canvasx(event.x-1), mainCanvas.canvasy(event.y-1)
			x2, y2 = mainCanvas.canvasx(event.x+1), mainCanvas.canvasy(event.y+1)
			points.append(event.x+mainCanvas.canvasx(0))
			points.append(event.y+mainCanvas.canvasy(0))


		def rGraph(event):
			x1, y1 = mainCanvas.canvasx(event.x-1), mainCanvas.canvasy(event.y-1)
			x2, y2 = mainCanvas.canvasx(event.x+1), mainCanvas.canvasy(event.y+1)
			points.append(event.x+mainCanvas.canvasx(0))
			points.append(event.y+mainCanvas.canvasy(0))
			fpoints = [points[0],points[1], points[2], points[1], points[2], points[3], points[0], points[3]]
			mainCanvas.create_polygon(fpoints, outline='black', fill='')
			i = len(fpoints)
			while i > 0:
				fpoints.pop()
				i = i-1
			i = len(points)
			while i > 0:
				points.pop()
				i = i-1
		mainCanvas.bind ("<ButtonPress-1>", rPoint)
		mainCanvas.bind ("<ButtonRelease-1>", rGraph)

	def drawCircle(self):
		operacaoEntry.pack_forget()
		operacoesLabel["text"] = ""
		resetLabels()
		infoLabel["text"] = "Clique e arraste para desenhar o circulo"
		def cPoint(event):
			x1, y1 = (event.x-1), (event.y-1)
			x2, y2 = (event.x+1), (event.y+1)
			points.append(event.x+mainCanvas.canvasx(0))
			points.append(event.y+mainCanvas.canvasy(0))

		def cGraph(event):
			x1, y1 = (event.x-1), (event.y-1)
			x2, y2 = (event.x+1), (event.y+1)
			points.append(event.x+mainCanvas.canvasx(0))
			points.append(event.y+mainCanvas.canvasy(0))
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
operacaoEntry2 = Entry(containerOperacoes)
global x0
global y0
x0 = mainCanvas.canvasx(0)
y0 = mainCanvas.canvasy(0)


# posicao cursor
def motion(event):
	posx, posy = event.x, event.y
	coordLabel["text"] = ("PosX = " + str(posx) + " PosY = " + str(posy))

mainCanvas.bind('<Motion>', motion)



Application(root)
root.mainloop()
