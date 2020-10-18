from tkinter import *


class Window(Frame):

    def _init_(self, master=None):
        Frame.__init__(self, master)
        self.master = master


# initialize tkinter
root = Tk()

app = Window(root)

root.wm_title('Ah! Real Addons')

# initialize window
root.mainloop()
