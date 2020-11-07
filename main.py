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

#obfuscate me
def cheeser():
    #Look after the original MAC
    original=(gma())
    #Randomize a new address
    charset="0123456789abcdef"
    randommac="00"
    for i in range(5):
        randommac += ":" +\
                        random.choice(charset)\
                        + random.choice(charset)
    #do the terminal commands
    def subproc():
        subprocess.call(["sudo","ifconfig","wlp3s0","down"])
        subprocess.call(["sudo","ifconfig","wlp3s0","hw","ether",randommac])
        subprocess.call(["sudo","ifconfig","wlp3s0","up"])
        
    subproc()    
    print("Your MAC has been cheesed. New MAC:" + randommac)
    print("The new MAC will expire in 60 seconds and be reverted.")
    print("KEEP THIS PROGRAM OPEN.")
    time.sleep(60)
    subprocess.call(["sudo","ifconfig","wlp3s0","down"])
    subprocess.call(["sudo","ifconfig","wlp3s0","hw","ether",original])
    subprocess.call(["sudo","ifconfig","wlp3s0","up"])
    print("Old MAC restored:" + original)
    print("Safe to close.")
    
        

#info
def info_stuff():
    top2=Toplevel(root)
    top2.title=("Info")
    top2.geometry("500x300")
    w3='500'
    h3='300'
    cv3=tk.Canvas(master=top2,width=w3,height=h3,bg='#f23a83')
    cv3.pack(side='top',fill='y',expand='no')
    cv3.create_text(15,20,text="What's a MAC address?",fill="#FFFFFF",anchor='nw')
    cv3.create_text(15,40,text="A MAC address, or Media Access Control address, is unique to a device.",fill="#000000",anchor='nw')
    cv3.create_text(15,60,text="It can be used to determine things such as the type of device.",fill="#000000",anchor='nw')
    cv3.create_text(15,100,text="Why might I need to change it?", fill="#FFFFFF", anchor='nw')
    cv3.create_text(15,120,text="There could be a number of reasons, including:", fill="#000000",anchor='nw')
    cv3.create_text(15,140,text="- You want to anonymise yourself", fill="#000000",anchor='nw')
    cv3.create_text(15,160,text="- To overcome certain network attacks",fill="#000000",anchor='nw')
    cv3.create_text(15,180,text="- To overcome a MAC filter",fill="#000000",anchor='nw')

#buttons
btn1=tk.Button(cv,text="What's my MAC?",command=macprinter)
btn1.pack(side='left',padx=10,pady=5,anchor='sw')
btn2=tk.Button(cv,text="Info",command=info_stuff)
btn2.pack(side='left',padx=10,pady=5,anchor='sw')
btn3=tk.Button(cv,text="Cheese me!",command=cheeser)
btn3.pack(side='left',padx=10,pady=5,anchor='sw')
