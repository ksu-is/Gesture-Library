''' code for main menu '''
from tkinter import *

class menu(Frame):

    def __init__(self,parent):
        super().__init__(parent)
        self.topFrame = parent
        # hold text within the previous root instance and with horizontal & vertical padding
        label = Label(text="Gesture Library", fg='Gold', font=("Helvetica",40), padx=100, pady=50)
        label.pack()        
        self.btClose = Button(self,text="Exit",height=3,width=15,command=self.quit)
        self.btClose.place(anchor="center",relx=0.5,rely=0.5,y=270)
