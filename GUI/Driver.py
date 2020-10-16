import os
import subprocess
import sys
from tkinter import *

sys.path.append("TrainYourOwnYolo")
krs = '2_Training/src/keras_yolo3'
if not os.path.isdir(krs):
    #subprocess.call("python Download_and_Convert_YOLO_weights.py")
    print("not here")
else:
    print("Keras_yolo already present")

class Visual(Frame):
    def __init__(self, master):
        self.master = master
        master.title("Drone Classification")
        
        self.label = Label(master,text="A Label")
        self.label.pack()

        #self.train-button = Button(master, text="Start Training", command=self.train)
        #self.train-button.pack()

        #self.test-button = Button(master, text="Start Testing", command=self.test)
        #self.test-button.pack()

root = Tk()
gui = Visual(root)
root.mainloop()


