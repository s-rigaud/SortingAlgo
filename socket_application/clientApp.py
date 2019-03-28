from tkinter import *
import random, time
import socket, pickle

class App:
	def __init__(self):
		self.root = Tk()
		self.canvas = Canvas(self.root, width=500, height=500, background='white')

		self.number_list = self.getRandomList(60)
		self.list_array_steps = []

		self.animation_speed = 5
		
		self.bar_list = []
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


		self.menubar.add_cascade(label = 'Choose Sort from the server',  menu = sort_menu)
		self.menubar.add_cascade(label = 'Random', command=self.random)
		self.menubar.add_cascade(label = 'Time to sort ' + str(self.time_to_sort)+" s")
		self.menubar.add_cascade(label = 'Exit', command=self.root.quit)
		
		self.root.overrideredirect(0)

		self.root.title('Sorting Algorithm Tool - Client')
		img = PhotoImage(file='ico.png')
		self.root.tk.call('wm', 'iconphoto', self.root._w ,  img)

		self.root.resizable(width=False, height=False)
		self.root.config(menu = self.menubar)
		self.root.mainloop()

	def getRandomList(self, size):
		"""Return an array of int fill with random number between 4 and 10000"""
		return [random.randint(4,10000) for _ in range(int(size))]

	def sort(self, sort:str):
		"""Method use to sort the array with the corresponding sort if it is not sorted yet ,  and call the animation method after"""
		self.reset_sort = False
		if not self.sorted:
			self.start_time = time.time()
			if(sort=='bubble'):
				self.list_array_steps = self.contactServer('bubble_sort',self.number_list)
				self.animation_speed = 1
			elif(sort=='o bubble'):
				self.list_array_steps = self.contactServer('optimised_bubble_sort',self.number_list)
				self.animation_speed = 1
			elif(sort=='selection'):
				self.list_array_steps = self.contactServer('selection_sort',self.number_list)
				self.animation_speed = 5
			elif(sort=='insertion'):
				self.list_array_steps = self.contactServer('insertion_sort',self.number_list)
				self.animation_speed = 5
			elif(sort=='cocktail'):
				self.list_array_steps = self.contactServer('cocktail_sort',self.number_list)
				self.animation_speed = 1
			elif(sort=='bogo'):
				self.list_array_steps = self.contactServer('bogo_sort',self.number_list)
				self.animation_speed = 1
			elif(sort=='count'):
				self.list_array_steps = self.contactServer('count_sort',self.number_list)
				self.animation_speed = 5
			elif(sort=='bucket'):
				self.list_array_steps = self.contactServer('bucket_sort',self.number_list)
				self.animation_speed = 5
		
			if(self.list_array_steps != None):
				self.dynamic_display()

			self.menubar.entryconfig(2 , state='disable')
			self.sorted = True 
		else:
			print('Already sorted')

	def contactServer(self,sort,array):
		"""Contact the server to get the sorting array step by step"""
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
			try :
				s.connect(('localhost', 15151))
			
					#Sending all the data to the server
				sort = [sort,array]
				data = pickle.dumps(sort)
				s.sendall(data)

				#Receive all the data encoded after trying to decode them
				data=b''
				while True:
					packet = s.recv(4096)
					if not packet: break
					data += packet

				res = pickle.loads(data)
				# print('Received', repr(res))
				return res
			except ConnectionRefusedError:
				self.menubar.entryconfig(1 ,  label='Connexion to server is impossible - Have you run it ?')
		

	def random(self):
		"""Method use to sort the list with one of the sorting algorithm"""
		self.reset_sort = True
		self.sorted = False
		self.time_to_sort = 0
		self.menubar.entryconfig(3 ,  label='Time to sort '+str(self.time_to_sort)+' s')
		self.menubar.entryconfig(2 , state='normal')
		self.number_list = self.getRandomList(60)
		self.display()


	def display(self):
		"""Method call to display the unsorted array"""
		self.canvas.delete('all')
		self.canvas.create_line(100, 100, 100, 400, fill='red', width=3) 
		self.canvas.create_line(100, 400, 402, 400, fill='red', width=3)
		# Map the maximum size of the bar to the maximum value 
		maxNumber = max(self.number_list)
		self.bar_list = []
		self.dot_list = []
		for i in range(len(self.number_list)):
			self.bar_list.append(self.canvas.create_line(105+i*5 , 399, 105+i*5, (400-300*(self.number_list[i]/maxNumber)), fill='green', width=2))
			self.dot_list.append(self.canvas.create_line(105+i*5 , (400-300*(self.number_list[i]/maxNumber))-2 , 105+i*5 , (400-300*(self.number_list[i]/maxNumber)) , fill='red' , width=2))

	def dynamic_display(self):
		"""Method use to display the animation"""
		#Index of First and Second Number which will be swaped
		indexFN = int(self.list_array_steps[0].split('-')[0])
		indexSN = int(self.list_array_steps[0].split('-')[1])

		self.swap_bars(indexFN, indexSN)
		self.swap_dots(indexFN, indexSN)
		
		self.list_array_steps.pop(0)

		self.blue_bar(indexFN, indexSN)

		self.actual_time = time.time()
		self.time_to_sort = round(self.actual_time - self.start_time, 2)
		self.menubar.entryconfig(3 ,  label='Time to sort '+str(self.time_to_sort)+' s')
		time.sleep(0.01)

		if len(self.list_array_steps)>0 and not(self.reset_sort):
			self.root.after(self.animation_speed, self.dynamic_display)
		else:
			self.reset_sort = False
			self.menubar.entryconfig(2, state='normal')
	
	def swap_bars(self, indexFN:int, indexSN:int):
		"""Swap two bars on the canvas"""
		firstBar = self.bar_list[indexFN]
		secondBar = self.bar_list[indexSN]

		arrayXY_first_bar = self.canvas.coords(firstBar)
		x0_first_bar = arrayXY_first_bar[0]
		y0_first_bar = arrayXY_first_bar[1]
		y1_first_bar = arrayXY_first_bar[3]

		arrayXY_second_bar = self.canvas.coords(secondBar)
		x0_second_bar = arrayXY_second_bar[0]
		y0_second_bar = arrayXY_second_bar[1]
		y1_second_bar = arrayXY_second_bar[3]

		self.canvas.coords(firstBar, x0_second_bar, y0_second_bar, x0_second_bar, y1_first_bar)
		self.canvas.coords(secondBar, x0_first_bar, y0_first_bar, x0_first_bar, y1_second_bar)

		self.bar_list[indexFN], self.bar_list[indexSN] = self.bar_list[indexSN], self.bar_list[indexFN]


	def swap_dots(self, indexFN:int, indexSN:int):
		"""Swap two dots on the canvas"""
		firstDot = self.dot_list[indexFN]
		secondDot = self.dot_list[indexSN]

		arrayXY_first_dot = self.canvas.coords(firstDot)
		x0_first_dot = arrayXY_first_dot[0]
		y0_first_dot = arrayXY_first_dot[1]
		y1_first_dot = arrayXY_first_dot[3]

		arrayXY_second_dot = self.canvas.coords(secondDot)
		x0_second_dot = arrayXY_second_dot[0]
		y0_second_dot = arrayXY_second_dot[1]
		y1_second_dot = arrayXY_second_dot[3]

		self.canvas.coords(firstDot, x0_second_dot, y0_first_dot, x0_second_dot, y1_first_dot)
		self.canvas.coords(secondDot, x0_first_dot, y0_second_dot, x0_first_dot, y1_second_dot)

		self.dot_list[indexFN], self.dot_list[indexSN] = self.dot_list[indexSN], self.dot_list[indexFN]


	def blue_bar(self, indexFN:int, indexSN:int):
		"""If the number doesn't appear in the permutation array that means it is firstly well placed and becomes blue"""
		firstWellSorted = True
		for array_steps in self.list_array_steps :
			if array_steps.startswith(str(indexFN)+'-') or array_steps.endswith('-'+str(indexFN)) :
				firstWellSorted = False

		if firstWellSorted:
			self.canvas.itemconfig(self.bar_list[indexFN] , fill='blue')

		secondWellSorted = True
		for array_steps in self.list_array_steps :
			if array_steps.startswith(str(indexSN)+'-') or array_steps.endswith('-'+str(indexSN)) :
				secondWellSorted = False

		if secondWellSorted:
			self.canvas.itemconfig(self.bar_list[indexSN], fill='blue')

if __name__ == "__main__":
	myApp = App()
	myApp.start()
