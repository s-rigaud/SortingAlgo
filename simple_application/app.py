from tkinter import *
from algo import *
import random, time

class App:
	def __init__(self):
		self.root = Tk()
		self.canvas = Canvas(self.root, width=500, height=500, background='white')

		self.intial_numbers = self.getRandomList(60)
		self.gen_steps : list

		self.animation_speed = 5

		self.bar_list : list
		self.dot_list : list

		#Principal barMenu
		self.menubar : Menu
		self.sorted = False

		#Timer
		self.time_to_sort= 0.0
		self.start_time = 0
		self.actual_time = 0

	def start(self):
		"""Initialize the UI"""
		self.canvas.pack()
		self.display()
		self.menubar = Menu(self.root)
		sort_menu = Menu(self.menubar , tearoff=0)
		sort_menu.add_command(label = 'Bubble Sort' , command= lambda: self.sort('bubble'))
		sort_menu.add_command(label = "'Better' Bubble Sort" , command= lambda: self.sort('o bubble'))
		sort_menu.add_command(label = 'Selection Sort' , command= lambda: self.sort('selection'))
		sort_menu.add_command(label = 'Insertion Sort' , command= lambda: self.sort('insertion'))
		sort_menu.add_command(label = 'Cocktail Sort', command= lambda: self.sort('cocktail'))
		sort_menu.add_command(label = 'Bogo Sort', command= lambda: self.sort('bogo'))
		sort_menu.add_command(label = 'Counting Sort', command= lambda: self.sort('count'))
		sort_menu.add_command(label = 'Bucket Sort', command= lambda: self.sort('bucket'))

		self.menubar.add_cascade(label = 'Choose Sort',  menu = sort_menu)
		self.menubar.add_cascade(label = 'Randomize', command=self.random)
		self.menubar.add_cascade(label = 'Time to sort ' + str(self.time_to_sort)+" s")
		self.menubar.add_cascade(label = 'Exit', command=self.root.quit)

		self.root.overrideredirect(0)

		self.root.title('Sorting Algorithm Tool')
		img = PhotoImage(file='ico.png')
		self.root.tk.call('wm', 'iconphoto', self.root._w ,  img)

		self.root.resizable(width = False, height = False)
		self.root.config(menu = self.menubar)
		self.root.mainloop()

	def getRandomList(self, size):
		"""
		Return an array of int fill with random number between 4 and 10000
		List type is useful : max value is used to map size of bars to values
		"""
		return [random.randint(4,10000) for _ in range(int(size))]

	def sort(self, sort:str):
		"""Method use to sort the array with the corresponding sort if it is not sorted yet ,  and call the animation method after"""
		self.reset_sort = False
		if not self.sorted:
			self.start_time = time.time()
			if(sort == 'bubble'):
				self.gen_steps = bubble_sort(self.intial_numbers)
				self.animation_speed = 1
			elif(sort == 'o bubble'):
				self.gen_steps = optimised_bubble_bort(self.intial_numbers)
				self.animation_speed = 1
			elif(sort == 'selection'):
				self.gen_steps = selection_sort(self.intial_numbers)
				self.animation_speed = 5
			elif(sort == 'insertion'):
				self.gen_steps = insertion_sort(self.intial_numbers)
				self.animation_speed = 5
			elif(sort == 'cocktail'):
				self.gen_steps = cocktail_sort(self.intial_numbers)
				self.animation_speed = 1
			elif(sort == 'bogo'):
				self.gen_steps = bogo_sort(self.intial_numbers)
				self.animation_speed = 1
			elif(sort == 'count'):
				self.gen_steps = counting_sort(self.intial_numbers)
				self.animation_speed = 5
			elif(sort == 'bucket'):
				self.gen_steps = bucket_sort(self.intial_numbers)
				self.animation_speed = 5

			self.dynamic_display()

			self.menubar.entryconfig(2, state = 'disable')
			self.sorted = True
		else:
			print('Already sorted')

	def random(self):
		"""Method use to sort the list with one of the sorting algorithm"""
		self.reset_sort = True
		self.sorted = False
		self.time_to_sort = 0
		self.menubar.entryconfig(2, state = 'normal')
		self.menubar.entryconfig(3, label = 'Time to sort ' + str(self.time_to_sort) + ' s')
		self.intial_numbers = self.getRandomList(60)
		self.display()


	def display(self):
		"""Method call to display the unsorted array"""
		self.canvas.delete('all')
		self.canvas.create_line(100, 100, 100, 400, fill = 'red', width = 3)
		self.canvas.create_line(100, 400, 402, 400, fill = 'red', width = 3)
		# Used to map the maximum size of the bar to the maximum value
		maxNumber = max(self.intial_numbers)
		self.bar_list = []
		self.dot_list = []
		for i in range(len(self.intial_numbers)):
			#Maping sizes and values
			self.bar_list.append(self.canvas.create_line(105+ i*5, 399, 105+ i*5, (400- 300*(self.intial_numbers[i]/maxNumber)), fill = 'green', width = 2))
			self.dot_list.append(self.canvas.create_line(105+ i*5, (400- 300*(self.intial_numbers[i]/maxNumber))-2, 105+i*5, (400-300*(self.intial_numbers[i]/maxNumber)) , fill='red' , width=2))

	def dynamic_display(self):
		"""Method use to display the animation"""
		#Index of First and Second Number which will be swaped
		try:
			initial_state = next(self.gen_steps)
		except StopIteration:
			self.blue_bar()
			self.menubar.entryconfig(2, state='normal')
			return

		indexFN, indexSN = initial_state.split('-')

		self.swap_bars(int(indexFN), int(indexSN))
		self.swap_dots(int(indexFN), int(indexSN))

		#self.blue_bar(indexFN, indexSN)

		self.actual_time = time.time()
		self.time_to_sort = round(self.actual_time - self.start_time, 2)
		self.menubar.entryconfig(3 ,  label='Time to sort '+str(self.time_to_sort)+' s')
		time.sleep(0.01)

		self.root.after(self.animation_speed, self.dynamic_display)

	def swap_bars(self, indexFN:int, indexSN:int):
		"""Swap two bars on the canvas"""
		firstBar = self.bar_list[indexFN]
		secondBar = self.bar_list[indexSN]

		x0_first_bar, y0_first_bar, _, y1_first_bar = self.canvas.coords(firstBar)
		x0_second_bar, y0_second_bar, _, y1_second_bar  = self.canvas.coords(secondBar)

		self.canvas.coords(firstBar, x0_second_bar, y0_second_bar, x0_second_bar, y1_first_bar)
		self.canvas.coords(secondBar, x0_first_bar, y0_first_bar, x0_first_bar, y1_second_bar)

		self.bar_list[indexFN], self.bar_list[indexSN] = self.bar_list[indexSN], self.bar_list[indexFN]


	def swap_dots(self, indexFN:int, indexSN:int):
		"""Swap two dots on the canvas"""
		firstDot = self.dot_list[indexFN]
		secondDot = self.dot_list[indexSN]

		x0_first_dot, y0_first_dot, _, y1_first_dot = self.canvas.coords(firstDot)
		x0_second_dot, y0_second_dot, _, y1_second_dot = self.canvas.coords(secondDot)

		self.canvas.coords(firstDot, x0_second_dot, y0_first_dot, x0_second_dot, y1_first_dot)
		self.canvas.coords(secondDot, x0_first_dot, y0_second_dot, x0_first_dot, y1_second_dot)

		self.dot_list[indexFN], self.dot_list[indexSN] = self.dot_list[indexSN], self.dot_list[indexFN]


	def blue_bar(self):
		"""If the sort animation end, all the bars become blue"""
		for bar in self.bar_list:
			self.canvas.itemconfig(bar, fill='blue')

if __name__ == "__main__":
	my_app = App()
	my_app.start()
