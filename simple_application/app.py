"""
The goal of the project is to allow everyone to understand many sorting algorithm by providing them a visualization of what each of them looks like
"""

from tkinter import Tk, Canvas, Menu, PhotoImage
from random import randint
import time

from algo import bubble_sort, optimised_bubble_bort, cocktail_sort, selection_sort, insertion_sort, bucket_sort, counting_sort, bogo_sort

class App:
    """ Class using Tkinter to display an animation for each different implemented sort algorithm """
    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=500, height=500, background='white')

        self.intial_numbers = App.get_random_list(60)
        self.gen_steps: list

        self.animation_speed = 5

        self.bar_list: list
        self.dot_list: list

        #Principal barMenu
        self.menubar: Menu
        self.sorted = False

        #Timer
        self.time_to_sort = 0.0
        self.start_time = 0
        self.actual_time = 0

    def start(self):
        """Initialize the UI"""
        self.canvas.pack()
        self.display()
        self.menubar = Menu(self.root)
        sort_menu = Menu(self.menubar, tearoff=0)
        sort_menu.add_command(label='Bubble Sort', command=lambda: self.sort('bubble'))
        sort_menu.add_command(label='"Better" Bubble Sort', command=lambda: self.sort('o bubble'))
        sort_menu.add_command(label='Selection Sort', command=lambda: self.sort('selection'))
        sort_menu.add_command(label='Insertion Sort', command=lambda: self.sort('insertion'))
        sort_menu.add_command(label='Cocktail Sort', command=lambda: self.sort('cocktail'))
        sort_menu.add_command(label='Bogo Sort', command=lambda: self.sort('bogo'))
        sort_menu.add_command(label='Counting Sort', command=lambda: self.sort('count'))
        sort_menu.add_command(label='Bucket Sort', command=lambda: self.sort('bucket'))

        self.menubar.add_cascade(label='Choose Sort', menu=sort_menu)
        self.menubar.add_cascade(label='Randomize', command=self.random)
        self.menubar.add_cascade(label='Time to sort ' + str(self.time_to_sort)+" s")
        self.menubar.add_cascade(label='Exit', command=self.root.quit)

        self.root.overrideredirect(0)

        self.root.title('Sorting Algorithm Tool')
        img = PhotoImage(file='ico.png')
        self.root.tk.call('wm', 'iconphoto', self.root._w, img)

        self.root.resizable(width=False, height=False)
        self.root.config(menu=self.menubar)
        self.root.mainloop()

    @classmethod
    def get_random_list(cls, size: str):
        """
        Return an array of int fill with random number between 4 and 10000
        List type is useful : max value is used to map size of bars to values
        """
        return [randint(4, 10000) for _ in range(int(size))]

    def sort(self, sort: str):
        """Method use to sort the array with the corresponding sort if it is not sorted yet ,  and call the animation method after"""
        if not self.sorted:
            self.start_time = time.time()
            if sort == 'bubble':
                self.gen_steps = bubble_sort(self.intial_numbers)
                self.animation_speed = 1
            elif sort == 'o bubble':
                self.gen_steps = optimised_bubble_bort(self.intial_numbers)
                self.animation_speed = 1
            elif sort == 'selection':
                self.gen_steps = selection_sort(self.intial_numbers)
                self.animation_speed = 5
            elif sort == 'insertion':
                self.gen_steps = insertion_sort(self.intial_numbers)
                self.animation_speed = 5
            elif sort == 'cocktail':
                self.gen_steps = cocktail_sort(self.intial_numbers)
                self.animation_speed = 1
            elif sort == 'bogo':
                self.gen_steps = bogo_sort(self.intial_numbers)
                self.animation_speed = 1
            elif sort == 'count':
                self.gen_steps = counting_sort(self.intial_numbers)
                self.animation_speed = 5
            elif sort == 'bucket':
                self.gen_steps = bucket_sort(self.intial_numbers)
                self.animation_speed = 5

            self.dynamic_display()

            self.menubar.entryconfig(2, state='disable')
            self.sorted = True
        else:
            print('Already sorted')

    def random(self):
        """Method use to sort the list with one of the sorting algorithm"""
        self.sorted = False
        self.time_to_sort = 0
        self.menubar.entryconfig(2, state='normal')
        self.menubar.entryconfig(3, label='Time to sort ' + str(self.time_to_sort) + ' s')
        self.intial_numbers = App.get_random_list(60)
        self.display()


    def display(self):
        """Method call to display the unsorted array"""
        self.canvas.delete('all')
        self.canvas.create_line(100, 100, 100, 400, fill='red', width=3)
        self.canvas.create_line(100, 400, 402, 400, fill='red', width=3)
        # Used to map the maximum size of the bar to the maximum value
        max_num = max(self.intial_numbers)
        self.bar_list = []
        self.dot_list = []
        for i in range(len(self.intial_numbers)):
            #Maping sizes and values
            self.bar_list.append(self.canvas.create_line(105+ i*5, 399, 105+ i*5, (400- 300*(self.intial_numbers[i]/max_num)), fill='green', width=2))
            self.dot_list.append(self.canvas.create_line(105+i*5, (400- 300*(self.intial_numbers[i]/max_num))-2, 105+i*5, (400-300*(self.intial_numbers[i]/max_num)), fill='red', width=2))

    def dynamic_display(self):
        """Method use to display the animation"""
        #Index of First and Second Number which will be swaped
        try:
            initial_state = next(self.gen_steps)
        except StopIteration:
            self.blue_bar()
            self.menubar.entryconfig(2, state='normal')
            return

        index_fn, index_sn = initial_state.split('-')

        self.swap_bars(int(index_fn), int(index_sn))
        self.swap_dots(int(index_fn), int(index_sn))

        #self.blue_bar(index_fn, index_sn)

        self.actual_time = time.time()
        self.time_to_sort = round(self.actual_time - self.start_time, 2)
        self.menubar.entryconfig(3, label='Time to sort ' + str(self.time_to_sort) + ' s')
        time.sleep(0.01)

        self.root.after(self.animation_speed, self.dynamic_display)

    def swap_bars(self, index_fn: int, index_sn: int):
        """Swap two bars on the canvas"""
        first_bar = self.bar_list[index_fn]
        second_bar = self.bar_list[index_sn]

        x0_first_bar, y0_first_bar, _, y1_first_bar = self.canvas.coords(first_bar)
        x0_second_bar, y0_second_bar, _, y1_second_bar = self.canvas.coords(second_bar)

        self.canvas.coords(first_bar, x0_second_bar, y0_second_bar, x0_second_bar, y1_first_bar)
        self.canvas.coords(second_bar, x0_first_bar, y0_first_bar, x0_first_bar, y1_second_bar)

        self.bar_list[index_fn], self.bar_list[index_sn] = self.bar_list[index_sn], self.bar_list[index_fn]


    def swap_dots(self, index_fn: int, index_sn: int):
        """Swap two dots on the canvas"""
        first_dot = self.dot_list[index_fn]
        second_dot = self.dot_list[index_sn]

        x0_first_dot, y0_first_dot, _, y1_first_dot = self.canvas.coords(first_dot)
        x0_second_dot, y0_second_dot, _, y1_second_dot = self.canvas.coords(second_dot)

        self.canvas.coords(first_dot, x0_second_dot, y0_first_dot, x0_second_dot, y1_first_dot)
        self.canvas.coords(second_dot, x0_first_dot, y0_second_dot, x0_first_dot, y1_second_dot)

        self.dot_list[index_fn], self.dot_list[index_sn] = self.dot_list[index_sn], self.dot_list[index_fn]


    def blue_bar(self):
        """If the sort animation end, all the bars become blue"""
        for green_bar in self.bar_list:
            self.canvas.itemconfig(green_bar, fill='blue')

if __name__ == "__main__":
    my_app = App()
    my_app.start()
