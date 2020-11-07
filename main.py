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
def macprinter():
    top=Toplevel(root)
    top.title=("Your MAC address is...")
    top.geometry("200x100")
    w2='200'
    h2='100'
    cv2=tk.Canvas(master=top, width=w2,height=h2,bg='#856ff9')
    cv2.pack(side='top',fill='y',expand='no')
    def getmymac():
        mactext=(gma())
        cv2.create_text(15,20,text=mactext,fill="black",anchor='nw')
    getmymac()
    top.mainloop()

#who is this mac

#obfuscate me

#restore

#info
def infostuff():
    top2=Toplevel(root)
    top2.title=("Info")
    top2.geometry("500x500")
    w3='500'
    h3='500'
    cv3=tk.Canvas(master=top2,width=w3,height=h3,bg='#f23a83')
    cv3.pack(side='top',fill='y',expand='no')
    cv3.create_text(15,20,text="What's A MAC Address?",fill="#FFFFFF",anchor='nw')

#buttons
btn1=tk.Button(cv,text="What's my MAC?",command=macprinter)
btn1.pack(side='left',padx=10,pady=5,anchor='sw')
btn2=tk.Button(cv,text="Info",command=infostuff)
btn2.pack(side='left',padx=10,pady=5,anchor='sw')
