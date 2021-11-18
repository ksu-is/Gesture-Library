''' code for main program '''

from tkinter import *

from menu import MainMenu
from screen import GestureScreen
import library as imgMan

def startSession(tu):
    if(imgMan.getImageLen()>0):
        imgMan.randomizeImages()
        mainMenu.place_forget()
        
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

topFrame.place(relx=0,relheight=1,relwidth=1)
mainMenu = MainMenu(topFrame)
mainMenu.place(relx=0,relheight=1,relwidth=1)
mainMenu.setFolders()

mainMenu.bindStartSession(startSession)
gestureScreen = GestureScreen(topFrame)
gestureScreen.bindExitSession(exitSession)

root.mainloop()