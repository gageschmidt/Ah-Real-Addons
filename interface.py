from upkeep.installed import Installed
from tkinter.scrolledtext import ScrolledText
from tkinter import Frame, Tk, WORD


class Window(Frame):

    def _init_(self, master=None):
        Frame.__init__(self, master)
        self.master = master


# initialize tkinter top level widget
root = Tk()

app = Window(root)

root.wm_title('Ah! Real Addons')

# instantiate empty, scrollable container for list of addons
addon_check_status = ScrolledText(root, wrap=WORD, width=40, height=10,
                                  font=("Times New Roman", 15))
addon_check_status.grid(row=1, column=0, columnspan=2)

# use the iteration of addon names to check for repos
# passing text container to insert the list of addons
Installed.check_for_addons(addon_check_status)

# initialize window
root.mainloop()
