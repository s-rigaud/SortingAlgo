from algo import *
from tkinter import *
from tkinter import ttk
import random
import time

class App:
	def __init__(self):
		self.root = Tk()
		self.canvas = Canvas(self.root, width=500, height=500, background='white')

		self.number_list = initialize_list()
		self.list_step_by_step = []

		self.animation_speed = 5
		
		self.bar_list = []
		#Not yet implemented
		self.dot_list = []

		self.reset_sort = False

		#Principal barMenu
		self.menubar = None
		self.sorted = False

		#Timer
		self.time_to_sort= 0.0
		self.start_time = 0
		self.actual_time = 0

	def start(self):
		"""Method call at the beginning of the app to initialize the UI"""
		self.canvas.pack()
		self.display()
		self.menubar = Menu(self.root)
		sort_menu = Menu(self.menubar , tearoff=0)
		sort_menu.add_command(label = 'Bubble Sort' , command= lambda: self.sort('bubble'))
		sort_menu.add_command(label = "'Better' Bubble Sort" , command= lambda: self.sort('o bubble'))
		sort_menu.add_command(label = 'Selection Sort' , command= lambda: self.sort('selection'))
		sort_menu.add_command(label = 'Insertion Sort' , command= lambda: self.sort('insertion'))
		sort_menu.add_command(label = 'Cocktail Sort', command= lambda: self.sort('cocktail'))
		sort_menu.add_command(label = 'Bogo Sort (Takes too long)', command= lambda: self.sort('bogo'))
		sort_menu.add_command(label = 'Counting Sort', command= lambda: self.sort('count'))
		sort_menu.add_command(label = 'Bucket Sort', command= lambda: self.sort('bucket'))


		self.menubar.add_cascade(label = "Choose Sort",  menu = sort_menu)
		self.menubar.add_cascade(label = "Random", command=self.random)
		self.menubar.add_cascade(label = "Time to sort " + str(self.time_to_sort)+" s")
		self.menubar.add_cascade(label = "Exit", command=self.root.quit)
		
		self.root.overrideredirect(0)

		self.root.title('Sorting Algorithm Tool')
		img = PhotoImage(file='ico.png')
		self.root.tk.call('wm', 'iconphoto', self.root._w ,  img)

		self.root.resizable(width=False, height=False)
		self.root.config(menu = self.menubar)
		self.root.mainloop()

	def sort(self ,  sort:str):
		"""Method use to sort the array with the corresponding sort if it is not sorted yet ,  and call the animation method after"""
		self.reset_sort = False
		if not self.sorted:
			self.start_time = time.time()
			if(sort=='bubble'):
				self.list_step_by_step = bubble_sort(self.number_list)
				self.animation_speed = 1
			elif(sort=='o bubble'):
				self.list_step_by_step = optimised_bubble_sort(self.number_list)
				self.animation_speed = 1
			elif(sort=='selection'):
				self.list_step_by_step = selection_sort(self.number_list)
				self.animation_speed = 5
			elif(sort=='insertion'):
				self.list_step_by_step = insertion_sort(self.number_list)
				self.animation_speed = 5
			elif(sort=='cocktail'):
				self.list_step_by_step = cocktail_sort(self.number_list)
				self.animation_speed = 1
			elif(sort=='bogo'):
				self.list_step_by_step = bogo_sort(self.number_list)
				self.animation_speed = 1
			elif(sort=='count'):
				self.list_step_by_step = counting_sort(self.number_list)
				self.animation_speed = 5
			elif(sort=='bucket'):
				self.list_step_by_step = bucket_sort(self.number_list)
				self.animation_speed = 5
		
			self.dynamic_display()

			self.menubar.entryconfig(2 , state='disable')
			self.sorted = True 
		else:
			print('Already sorted')

	def random(self):
		"""Method use to sort the list with one of the sorting algorithm"""
		self.reset_sort = True
		self.sorted = False
		self.time_to_sort = 0
		self.menubar.entryconfig(3 ,  label="Time to sort "+str(self.time_to_sort)+" s")
		self.menubar.entryconfig(2 , state='normal')
		self.number_list = initialize_list()
		self.display()


	def display(self):
		"""Method call to display the unsorted array"""
		self.canvas.delete("all")
		self.canvas.create_line(100, 100, 100, 400, fill='red', width=3) 
		self.canvas.create_line(100, 400, 400, 400, fill='red', width=3) 
		maxNumber = max(self.number_list)
		self.bar_list = []
		for _ in range(len(self.number_list)):
			self.bar_list.append(self.canvas.create_line(105+_*5 , 399, 105+_*5, (400-300*(self.number_list[_]/maxNumber)), fill='green', width=2))
			# self.dot_list.append(self.canvas.create_line(105+_*5 , (400-300*(self.number_list[_]/maxNumber))-2 , 105+_*5 , (400-300*(self.number_list[_]/maxNumber)) , fill='red' , width=2))

	def dynamic_display(self):
		"""Method use to display the animation"""
		#Index of First and Second Number which will be swaped
		indexFN = int(self.list_step_by_step[0].split("→")[0])
		indexSN = int(self.list_step_by_step[0].split("→")[1])

		self.swap_bars(indexFN, indexSN)
		
		self.list_step_by_step.pop(0)

		self.blue_bar(indexFN, indexSN)

		self.actual_time = time.time()
		self.time_to_sort = round(self.actual_time - self.start_time, 2)
		self.menubar.entryconfig(3 ,  label="Time to sort "+str(self.time_to_sort)+" s")
		time.sleep(0.01)
		if(len(self.list_step_by_step)>0 and not(self.reset_sort)):
			self.root.after(self.animation_speed, self.dynamic_display)
		else:
			self.reset_sort = False
			self.menubar.entryconfig(2, state='normal')
	
	def swap_bars(self, indexFN:int, indexSN:int):
		"""Method which swap two of the different bar on the canvas"""
		firstBar = self.bar_list[indexFN]
		secondBar = self.bar_list[indexSN]
		

		arrayXY_current = self.canvas.coords(firstBar)
		x0_current = arrayXY_current[0]
		y0_current = arrayXY_current[1]
		y1_current = arrayXY_current[3]


		arrayXY_destination = self.canvas.coords(secondBar)
		x0_destination = arrayXY_destination[0]
		y0_destination = arrayXY_destination[1]
		y1_destination = arrayXY_destination[3]

		self.canvas.coords(firstBar, x0_destination, y0_destination, x0_destination, y1_current)
		self.canvas.coords(secondBar, x0_current, y0_current, x0_current, y1_destination)

		self.bar_list[indexFN],self.bar_list[indexSN] = self.bar_list[indexSN],self.bar_list[indexFN]

	def blue_bar(self, indexFN:int, indexSN:int):
		"""If the number doesn't appear in the permutation array that means it is _currently well placed  it becomes blue"""
		firstWellSorted = True
		for i in range (0, len(self.list_step_by_step)):
			if self.list_step_by_step[i].startswith(str(indexFN)+'→') or self.list_step_by_step[i].endswith('→'+str(indexFN)) :
				firstWellSorted = False

		if firstWellSorted:
			self.canvas.itemconfig(self.bar_list[indexFN] , fill="blue")

		secondWellSorted = True
		for s in range (0, len(self.list_step_by_step)):
			if self.list_step_by_step[s].startswith(str(indexSN)+'→') or self.list_step_by_step[s].endswith('→'+str(indexSN)) :
				secondWellSorted = False

		if secondWellSorted:
			self.canvas.itemconfig(self.bar_list[indexSN], fill="blue")

if __name__ == "__main__":
	myApp = App()
	myApp.start()
