''' code for main program '''
import tkinter as tk
from tkinter import *
from menu import menu

# create overall window with title
root = tk.Tk()
root.geometry("800x700")
root['bg']='black'
root.title("GestureLibrary")
root.iconphoto = ("")
topFrame = Frame(root)
topFrame.place(relx=0,relheight=1,relwidth=1)
mainMenu = menu(topFrame)
mainMenu.place(relx=0,relheight=1,relwidth=1)


# display the window
root.mainloop()