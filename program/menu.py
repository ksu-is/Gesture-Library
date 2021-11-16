''' code for main menu '''
# from tkinter import *

# class menu(Frame):

#     def __init__(self,parent):
#         super().__init__(parent)
#         self.topFrame = parent
#         # hold text within the previous root instance and with horizontal & vertical padding
#         label = Label(text="Gesture Library", fg='Gold', font=("Helvetica",40), padx=100, pady=50)
#         label.pack()        
#         self.btClose = Button(self,text="Exit",height=3,width=15,command=self.quit)
#         self.btClose.place(anchor="center",relx=0.5,rely=0.5,y=270)
from tkinter import *
import library as imgMan

class MainMenu(Frame):

    def __init__(self,parent):
        super().__init__(parent)
        self.topFrame = parent        
        self.time = 0
        self.images = 0
        self.foldersSelected = []
        self.createFolderList(self)
        self.createTimeSelection(self)
        self.createImageSelection(self)
        self.avaliable = StringVar(value="Total Images Avaliable: 0")
        self.labelTotalImages = Label(self,textvariable=self.avaliable)
        self.labelTotalImages.place(anchor="n",relx=0.5,rely=0.5)
        self.btStart = Button(self,text="Draw",height=3,width=15,command=self.prepareSession)
        self.btStart.place(anchor="center",relx=0.5,rely=0.5,y=200)



    def createFolderList(self,parent):
        self.foldersContainer = LabelFrame(parent,text="Select the folders: ")
        self.foldersContainer.place(anchor="s",relx=0.5,rely=0.5,relheight=0.5,relwidth=1)
        self.canvasScrollBar = Scrollbar(self.foldersContainer,orient="vertical")
        self.canvasScrollBar.pack(side="right",fill="y")
        self.canvasScrollBar.bind("<Configure>",self.updateScrollBar)
        self.folderCanvas = Canvas(self.foldersContainer,yscrollcommand=self.canvasScrollBar.set)
        self.canvasScrollBar.configure(command=self.folderCanvas.yview)
        self.foldersList = Frame(self.folderCanvas)
        self.folderCanvas.create_window(0,0,window=self.foldersList,anchor="nw")
        self.folderCanvas.pack(side="left",fill="both")
    
    def createTimeSelection(self,parent):
        self.menuTime = IntVar(value=30)
        self.menuTimeTxt = StringVar(value="30")
        btPlacementy=10
        self.labelTime = Label(parent,text="Select a fixed time for your session:",height=3)
        self.labelTime.place(anchor="n",relx=0.5,rely=0.5,y=btPlacementy)
        self.bt00 = Radiobutton(parent,text="Inf", variable=self.menuTime, value=0,command=self.selectTime)
        btPlacementy+=60
        self.bt00.place(anchor="center",relx=0.5,rely=0.5,y=btPlacementy,x=-240)
        self.bt30 = Radiobutton(parent,text="30s", variable=self.menuTime, value=30,command=self.selectTime)
        self.bt30.place(anchor="center",relx=0.5,rely=0.5,y=btPlacementy,x=-180)
        self.bt45 = Radiobutton(parent,text="45s", variable=self.menuTime, value=45,command=self.selectTime)
        self.bt45.place(anchor="center",relx=0.5,rely=0.5,y=btPlacementy,x=-120)
        self.bt60 = Radiobutton(parent,text="1m", variable=self.menuTime, value=60,command=self.selectTime)
        self.bt60.place(anchor="center",relx=0.5,rely=0.5,y=btPlacementy,x=-60)
        self.bt120 = Radiobutton(parent,text="2m", variable=self.menuTime, value=120,command=self.selectTime)
        self.bt120.place(anchor="center",relx=0.5,rely=0.5,y=btPlacementy,x=0)
        self.bt300 = Radiobutton(parent,text="5m", variable=self.menuTime, value=300,command=self.selectTime)
        self.bt300.place(anchor="center",relx=0.5,rely=0.5,y=btPlacementy,x=60)
        self.bt600 = Radiobutton(parent,text="10m", variable=self.menuTime, value=600,command=self.selectTime)
        self.bt600.place(anchor="center",relx=0.5,rely=0.5,y=btPlacementy,x=120)
        self.btcustom = Radiobutton(parent,text="Custom", variable=self.menuTime, value=-1,command=self.selectTime)
        self.btcustom.place(anchor="center",relx=0.5,rely=0.5,y=btPlacementy,x=180)
        self.entryTime = Entry(parent,width=6,textvariable=self.menuTimeTxt)
        self.entryTime.config(state=DISABLED)
        self.entryTime.place(anchor="center",relx=0.5,rely=0.5,y=btPlacementy,x=240)

    def createImageSelection(self,parent):
        self.menuImages = IntVar(value=20)

    def setFolders(self):
        for dir in imgMan.dirList:
            var = BooleanVar()
            self.foldersSelected.append(var)
            self.btca = Checkbutton(self.foldersList,text=dir,variable=var,command=self.getFolders)
            self.btca.pack(side="top",anchor="nw")


    def getFolders(self):
        list = []
        for b in self.foldersSelected:
            list.append(b.get())
        #print(self.passFolders(list))
        #self.avaliable.set("Total Images Avaliable: "+self.passFolders(list))
        self.avaliable.set("Total Images Avaliable: "+imgMan.updateImageCount(list))
        
        

    def selectTime(self):
        self.time = self.menuTime.get()
        if(self.time>-1):
           self.menuTimeTxt.set(self.time)
           self.entryTime.config(state=DISABLED)
        else:
            self.entryTime.config(state=NORMAL)

    
    def updateScrollBar(self,event):
       self.folderCanvas.configure(scrollregion=self.folderCanvas.bbox("all"))

    def prepareSession(self):
        self.topFrame
        
        self.images = self.menuImages.get()
        self.time = self.menuTime.get()
        sessionOptions = (self.time,self.images)
        self.setSession(sessionOptions)

    def bindStartSession(self,func):
        self.setSession = func