from algo import *
from tkinter import *
from tkinter import ttk
import random
import time

class App:
	def __init__(self):
		self.frame = Tk()
		self.canvas = Canvas(self.frame, width=500, height=500, background='white')

		self.numList = initializeList()
		self.arrayStepByStep = []

		self.animationSpeed = 5
		
		self.barArray = []

		#Not yet implemented
		self.dotArray = []
		self.resetSort = False

		#Principal bar of menu
		self.menubar = None
		self.sorted = False

		#Timer
		self.timeToSort= 0.0
		self.startTime = 0
		self.actualTime = 0

	#Initialisation of the UI 
	def start(self):
		self.canvas.pack()

		self.display()

		self.menubar = Menu(self.frame)
		sortMenu = Menu(self.menubar,tearoff=0)
		sortMenu.add_command(label = 'Bubble Sort',command= lambda: self.sort('bubble'))
		sortMenu.add_command(label = "'Better' Bubble Sort",command= lambda: self.sort('o bubble'))
		sortMenu.add_command(label = 'Selection Sort',command= lambda: self.sort('selection'))
		sortMenu.add_command(label = 'Insertion Sort',command= lambda: self.sort('insertion'))
		sortMenu.add_command(label = 'Cocktail Sort',command= lambda: self.sort('cocktail'))
		sortMenu.add_command(label = 'Bogo Sort (Takes too long)',command= lambda: self.sort('bogo'))
		sortMenu.add_command(label = 'Counting Sort',command= lambda: self.sort('count'))
		sortMenu.add_command(label = 'Bucket Sort',command= lambda: self.sort('bucket'))


		self.menubar.add_cascade(label = "Choose Sort", menu = sortMenu)
		self.menubar.add_cascade(label = "Random", command=self.random)
		self.menubar.add_cascade(label = "Time to sort "+str(self.timeToSort)+" s")
		self.menubar.add_cascade(label = "Exit", command=self.frame.quit)
		
		self.frame.overrideredirect(0)

		self.frame.title('Sorting Algorithm Tool')
		img = PhotoImage(file='ico.png')
		self.frame.tk.call('wm', 'iconphoto',  self.frame._w, img)

		self.frame.resizable(width=False, height=False)
		self.frame.config(menu = self.menubar)
		self.frame.mainloop()

	#Call the funtion to sort the array if it not sorted yet
	def sort(self,sort):
		self.resetSort = False
		if not self.sorted:
			self.startTime = time.time()
			if(sort=='bubble'):
				self.arrayStepByStep = bubbleSort(self.numList)
				self.animationSpeed = 1
			elif(sort=='o bubble'):
				self.arrayStepByStep = optimisedBubbleSort(self.numList)
				self.animationSpeed = 1
			elif(sort=='selection'):
				self.arrayStepByStep = selectionSort(self.numList)
			elif(sort=='insertion'):
				self.arrayStepByStep = insertionSort(self.numList)
			elif(sort=='cocktail'):
				self.arrayStepByStep = cocktailSort(self.numList)
				self.animationSpeed = 1
			elif(sort=='bogo'):
				self.arrayStepByStep = bogoSort(self.numList)
				self.animationSpeed = 1
			elif(sort=='count'):
				self.arrayStepByStep = countingSort(self.numList)
			elif(sort=='bucket'):
				self.arrayStepByStep = bucketSort(self.numList)
		
			self.dynamicDisplay()

			self.menubar.entryconfig(2,state='disable')
			self.sorted = True 
		else:
			print('Already sorted')

	#Define an other array to work on
	def random(self):
		self.resetSort = True
		self.sorted = False
		self.timeToSort = 0
		self.menubar.entryconfig(3, label="Time to sort "+str(self.timeToSort)+" s")
		self.menubar.entryconfig(2,state='normal')
		self.numList = initializeList()
		self.display()



	#Initial print of the array
	def display(self):
		self.canvas.delete("all")
		self.canvas.create_line(100,100,100,400,fill='red',width=3) 
		self.canvas.create_line(100,400,400,400,fill='red',width=3) 
		maxNumber = max(self.numList)
		self.barArray = []
		for _ in range(len(self.numList)):
			self.barArray.append(self.canvas.create_line(105+_*5,399,105+_*5,(400-300*(self.numList[_]/maxNumber)),fill='green',width=2))
			# self.dotArray.append(self.canvas.create_line(105+_*5,(400-300*(self.numList[_]/maxNumber))-2,105+_*5,(400-300*(self.numList[_]/maxNumber)),fill='red',width=2))

	def dynamicDisplay(self):

		#Index of First and Second Number which will be swaped
		indexFN = int(self.arrayStepByStep[0].split("→")[0])
		indexSN = int(self.arrayStepByStep[0].split("→")[1])

		self.swapBar(indexFN,indexSN)
		
		self.arrayStepByStep.pop(0)

		self.blueBar(indexFN,indexSN)

		self.actualTime = time.time()
		self.timeToSort = round(self.actualTime - self.startTime,2)
		self.menubar.entryconfig(3, label="Time to sort "+str(self.timeToSort)+" s")
		time.sleep(0.01)
		if(len(self.arrayStepByStep)>0 and not(self.resetSort)):
			self.frame.after(self.animationSpeed,self.dynamicDisplay)
		else:
			self.resetSort = False
			self.menubar.entryconfig(2,state='normal')
	
	#Function that swap two bar on the canvas
	def swapBar(self,indexFN,indexSN):
		firstBar = self.barArray[indexFN]
		secondBar = self.barArray[indexSN]
		

		arrayXYCurrent = self.canvas.coords(firstBar)
		x0Current = arrayXYCurrent[0]
		y0Current = arrayXYCurrent[1]
		y1Current = arrayXYCurrent[3]


		arrayXYDestination = self.canvas.coords(secondBar)
		x0Destination = arrayXYDestination[0]
		y0Destination = arrayXYDestination[1]
		y1Destination = arrayXYDestination[3]

		self.canvas.coords(firstBar,x0Destination,y0Destination,x0Destination,y1Current)
		self.canvas.coords(secondBar,x0Current,y0Current,x0Current,y1Destination)

		self.barArray[indexFN],self.barArray[indexSN] = self.barArray[indexSN],self.barArray[indexFN]

	def blueBar(self,indexFN,indexSN):
		#If the number doesn't appear in the permutation array that means it is currently well placed  it becomes blue
		firstWellSorted = True
		for i in range (0,len(self.arrayStepByStep)):
			if self.arrayStepByStep[i].startswith(str(indexFN)+'→') or self.arrayStepByStep[i].endswith('→'+str(indexFN)) :
				firstWellSorted = False

		if firstWellSorted:
			self.canvas.itemconfig(self.barArray[indexFN],fill="blue")

		secondWellSorted = True
		for s in range (0,len(self.arrayStepByStep)):
			if self.arrayStepByStep[s].startswith(str(indexSN)+'→') or self.arrayStepByStep[s].endswith('→'+str(indexSN)) :
				secondWellSorted = False

		if secondWellSorted:
			self.canvas.itemconfig(self.barArray[indexSN],fill="blue")

if __name__ == '__main__':
	myApp = App()
	myApp.start()
