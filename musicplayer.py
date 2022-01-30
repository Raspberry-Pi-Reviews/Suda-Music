from tkinter import *
from tkinter import filedialog
from pygame import mixer

class MusicPlayer:
    def __init__(self, window ):
        window.geometry('650x650'); window.title('Suda Music'); window.resizable(0,0); window.configure(background = "lightblue")
        self.bttn_clicks = 0
        self.bttn_clicks1 = 0
        self.background = "white"
        buttonframe = LabelFrame(root,text="Control Panel",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=7,relief=GROOVE)
        sliderframe = LabelFrame(root,text="Volume Control",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=7,relief=GROOVE)
        infoframe = LabelFrame(root,text="Updates",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=7,relief=GROOVE)
        Load = Button(window, text = 'Load',  width = 10, height = 2, font = ('Times', 10, "bold"), bg="grey", fg="white", bd=4, relief=GROOVE, command = self.load)
        Play = Button(window, text = 'Play',  width = 10, height = 2, font = ('Times', 10 , "bold"), bg="grey", fg="white", bd=4, relief=GROOVE, command = self.play)
        volumeupButton = Button(window, text = 'Volume',  width = 10, height = 2, font = ('Times', 10, "bold"), bg="grey", fg="white", bd=4, relief=GROOVE, command = self.volumeup)
        Pause = Button(window,text = 'Pause',  width = 10, height = 2, font = ('Times', 10, "bold"), bg="grey", fg="white", bd=4, relief=GROOVE, command = self.pause)
        Stop = Button(window ,text = 'Stop',  width = 10, height = 2, font = ('Times', 10, "bold"), bg="grey", fg="white", bd=4, relief=GROOVE, command = self.stop)
        label = Label(root, text = "Suda Music (v1.01)", bd=5, bg = "black", fg = "white", font =("times new roman",15,"bold"),relief=GROOVE)
        label.pack()
        label2 = Label(root, text = "- Click the volume button 10 times for max volume", bg = "grey", fg = "white", font =("times new roman",15,"bold"))
        label2.pack()
        label4 = Label(root, text = "- Changed Background Color From Light Grey To Light Blue", bg = "grey", fg = "white", font =("times new roman",15,"bold"))
        label4.pack()
        label3 = Label(root, text = "- Added New Control Panel Design", bg = "grey", fg = "white", font =("times new roman",15,"bold"))
        label3.pack()
        Load.place(x=45,y=80);Play.place(x=200,y=80);Pause.place(x=355,y=80);Stop.place(x=505,y=80);buttonframe.place(x=25,y=50,width=600,height=100);label.place(x=235,y=8)
        sliderframe.place(x=25,y=170,width=170,height=100)
        volumeupButton.place(x=55, y=200)
        infoframe.place(x=25,y=300,width=600,height=300)
        label2.place(x=45,y=330)
        label3.place(x=45,y=360)
        label4.place(x=45,y=390)
        self.music_file = False
        self.playing_state = False
    def load(self):
        self.music_file = filedialog.askopenfilename()
    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()
    def pause(self):
        if not self.playing_state:
            mixer.init()
            mixer.music.pause()
            self.playing_state=True
        else:
            mixer.music.unpause()
            self.playing_state = False
    def stop(self):
        mixer.init()
        mixer.music.stop()
        
    
        
    def volumedown(self):
        self.bttn_clicks += 1
        while True:
            if self.bttn_clicks==1:
                mixer.init()
                mixer.music.set_volume(0.9)
            elif self.bttn_clicks==2:
                mixer.init()
                mixer.music.set_volume(0.8)
            elif self.bttn_clicks==3:
                mixer.init()
                mixer.music.set_volume(0.7)
            elif self.bttn_clicks==4:
                mixer.init()
                mixer.music.set_volume(0.6)
            elif self.bttn_clicks==5:
                mixer.init()
                mixer.music.set_volume(0.5) 
            elif self.bttn_clicks==6:
                mixer.init()
                mixer.music.set_volume(0.4)
            elif self.bttn_clicks==7:
                mixer.init()
                mixer.music.set_volume(0.3)
            elif self.bttn_clicks==8:
                mixer.init()
                mixer.music.set_volume(0.2)
            elif self.bttn_clicks==9:
                mixer.init()
                mixer.music.set_volume(0.1)
            elif self.bttn_clicks==10:
                mixer.init()
                mixer.music.set_volume(0.0)
            
                self.bttn_clicks=0
            break
            #print("Total Clicks: " + str(self.bttn_clicks))
    
    def volumeup(self):
        self.bttn_clicks1 += 1
        while True:  
            if self.bttn_clicks1==1:
                mixer.init()
                mixer.music.set_volume(0.1)
            elif self.bttn_clicks1==2:
                mixer.init()
                mixer.music.set_volume(0.2)
            elif self.bttn_clicks1==3:
                mixer.init()
                mixer.music.set_volume(0.3)
            elif self.bttn_clicks1==4:
                mixer.init()
                mixer.music.set_volume(0.4)
            elif self.bttn_clicks1==5:
                mixer.init()
                mixer.music.set_volume(0.5) 
            elif self.bttn_clicks1==6:
                mixer.init()
                mixer.music.set_volume(0.6)
            elif self.bttn_clicks1==7:
                mixer.init()
                mixer.music.set_volume(0.7)
            elif self.bttn_clicks1==8:
                mixer.init()
                mixer.music.set_volume(0.8)
            elif self.bttn_clicks1==9:
                mixer.init()
                mixer.music.set_volume(0.9)
            elif self.bttn_clicks1==10:
                mixer.init()
                mixer.music.set_volume(1.0)
                
                self.bttn_clicks1=0 
            #print("Total Clicks: " + str(self.bttn_clicks))
            break
            
root = Tk()
app= MusicPlayer(root)
root.mainloop()
