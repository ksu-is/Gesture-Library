''' code for main program '''
# import tkinter as tk
# from tkinter import *
# from menu import menu

# # create overall window with title
# root = tk.Tk()
# root.geometry("800x700")
# root['bg']='black'
# root.title("GestureLibrary")
# root.iconphoto = ("")
# topFrame = Frame(root)
# topFrame.place(relx=0,relheight=1,relwidth=1)
# mainMenu = menu(topFrame)
# mainMenu.place(relx=0,relheight=1,relwidth=1)


# # display the window
# root.mainloop()

from tkinter import *

from menu import MainMenu
from screen import GestureScreen
import library as imgMan

def startSession(tu):
    if(imgMan.getImageLen()>0):
        imgMan.randomizeImages()
        mainMenu.place_forget()
        #mainMenu.place(relx=0,relheight=1,relwidth=1)
        gestureScreen.setSession(tu)
        gestureScreen.place(relx=0,relheight=1,relwidth=1)
def exitSession():
    if(imgMan.getImageLen()>0):
        gestureScreen.place_forget()
        mainMenu.place(relx=0,relheight=1,relwidth=1)

root = Tk()
root.geometry("800x600")
root.title("GestureLibrary")
root.iconphoto = ("")
topFrame = Frame(root)
imgMan.loadFolders()
#imgManager = ImageManager()
#imgManager.loadFolders()
#help(os)
#topFrame.pack(side="top",fill="both",expand=True)
topFrame.place(relx=0,relheight=1,relwidth=1)
mainMenu = MainMenu(topFrame)
mainMenu.place(relx=0,relheight=1,relwidth=1)
mainMenu.setFolders()
#mainMenu.bindUpdateImageCount(imgManager.updateImageCount)
mainMenu.bindStartSession(startSession)
gestureScreen = GestureScreen(topFrame)
gestureScreen.bindExitSession(exitSession)
#gestureScreen.place(relx=0,relheight=1,relwidth=1)
#root.bind("<ButtonPress>",teste)
root.mainloop()