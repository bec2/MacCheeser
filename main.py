import tkinter as tk
from tkinter import *
from getmac import get_mac_address as gma

import sys
import subprocess
import argparse
import random
import time
import re

#tkinter setup stuff yadda yadda
root = tk.Tk()
root.title('MacCheeser')
fname="bg.gif"
bg_image=tk.PhotoImage(file=fname)
w=bg_image.width()
h=bg_image.height()
root.geometry("%dx%d+50+30"%(w,h))
cv=tk.Canvas(width=w,height=h)
cv.pack(side='top',fill='both',expand='yes')
cv.create_image(0,0,image=bg_image,anchor='nw')
mainframe=tk.Frame(root)

#whats my mac
def getmymac():
    print(gma())

def macprinter():
    top=Toplevel(root)
    top.title=("Your MAC address is...")
    top.geometry("500x100")
    w2='500'
    h2='100'
    cv2=tk.Canvas(master=top, width=w2,height=h2)
    cv2.pack(side='top',fill='y',expand='no')
    getmymac()
    top.mainloop()

#who is this mac

#obfuscate me

#restore 

#buttons
btn1=tk.Button(cv,text="What's my MAC?",command=macprinter)
btn1.pack(side='left',padx=10,pady=5,anchor='sw')
