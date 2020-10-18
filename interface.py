from pathlib import Path
from tkinter import *


# static method to check for the standard addons folder for World Of Warcraft
def check_for_addons():
    addons_dir = Path('/Program Files (x86)/World of Warcraft/_retail_/Interface/AddOns')
    if addons_dir.is_dir():
        for sub_dir in addons_dir.iterdir():
            # Use names to check for addon repos?
            print(sub_dir.name)
    else:
        print('No addons currently installed, or the default path is not being used for your WoW Installation')


class Window(Frame):

    def _init_(self, master=None):
        Frame.__init__(self, master)
        self.master = master


# initialize tkinter
root = Tk()

app = Window(root)

root.wm_title('Ah! Real Addons')

# static method, check for wow interface directory and any existing addons
# use the iteration of addon names to check for repos
check_for_addons()

# initialize window
root.mainloop()

