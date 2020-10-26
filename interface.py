from upkeep.installed import CheckAddons
from tkinter import scrolledtext
import tkinter as tk


class Window(tk.Frame):

    def _init_(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master


# initialize tkinter
root = tk.Tk()

app = Window(root)

root.wm_title('Ah! Real Addons')

# instantiate empty, scrollable container for list of addons
addon_check_status = tk.scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10,
                                                  font=("Times New Roman", 15))
addon_check_status.grid(row=1, column=0, columnspan=2)

# use the iteration of addon names to check for repos
# passing text container to insert the list of addons
CheckAddons.check_for_addons(addon_check_status)

# initialize window
root.mainloop()
