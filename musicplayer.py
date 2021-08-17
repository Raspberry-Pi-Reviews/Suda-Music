from tkinter import *
from tkinter import filedialog
from pygame import mixer

class MusicPlayer:
    def __init__(self, window ):
        window.geometry('650x170'); window.title('Suda Music'); window.resizable(0,0)
        buttonframe = LabelFrame(root,text="Control Panel",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=7,relief=GROOVE)  
        Load = Button(window, text = 'Load',  width = 10, height = 2, font = ('Times', 10, "bold"), bg="grey", fg="white", bd=4, relief=GROOVE, command = self.load)
        Play = Button(window, text = 'Play',  width = 10, height = 2, font = ('Times', 10 , "bold"), bg="grey", fg="white", bd=4, relief=GROOVE, command = self.play)
        Pause = Button(window,text = 'Pause',  width = 10, height = 2, font = ('Times', 10, "bold"), bg="grey", fg="white", bd=4, relief=GROOVE, command = self.pause)
        Stop = Button(window ,text = 'Stop',  width = 10, height = 2, font = ('Times', 10, "bold"), bg="grey", fg="white", bd=4, relief=GROOVE, command = self.stop)
        label = Label(root, text = "Suda Music (v1.02)", bd=5, bg = "black", fg = "white", font =("times new roman",15,"bold"),relief=GROOVE)
        label.pack()
        Load.place(x=45,y=80);Play.place(x=200,y=80);Pause.place(x=355,y=80);Stop.place(x=505,y=80);buttonframe.place(x=25,y=50,width=600,height=100);label.place(x=235,y=8)
        
        
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
    
root = Tk()
app= MusicPlayer(root)
root.mainloop()