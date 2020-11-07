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
def cheeser():
    def get_args():
        #Get interface stuff
        prsr = argparse.ArgumentParser()
        prsr.add_argument("-i","--interface",dest="interface",help="Name of interface.")
        options = prsr.parse_args()
        if options.interface:
            return options.interface
        else:
            prsr.error("Oopsy woopsy syntax error did a bungly wungly uwu")
    def changer(interface, new_mac_address):
        #Does the terminal commands
        subprocess.call(["sudo","ifconfig",interface,"down"])
        subprocess.call(["sudo","ifconfig",interface,"hw","ether",new_mac_address])
        subprocess.call(["sudo","ifconfig",interface,"up"])
    def get_random_mac():
        #Randomizes
        charset="0123456789abcdef"
        random_mac="00"
        for i in range(5):
            random_mac += ":" + \
                          random.choice(charset) \
                          + random.choice(charset)
            return random_mac
    def get_original(interface):
        #Holds the current MAC for restoration purposes
        output=subprocess.check_output(["ifconfig",interface])
        return re.search("\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(output)).group(0)

    #Now let's do the magic and change the mac every 2 minutes
    if __name__ == "__main__":
        print("Initializing MAC cheeser. Generating new MAC every 2 minutes.")
        sleeper=120
        interface=get_args()
        current_mac=get_original(interface)
        try:
            while True:
                random_mac=get_random_mac()
                change_mac(interface,random_mac)
                new_mac_info=subprocess.check_output(["ifconfig",interface])
                if random_mac in str(new_mac_info):
                    print("New MAC:",random_mac,end=" ")
                    sys.stdout.flush()
                    time.sleep(sleeper)
        except KeyboardInterrupt:
            change_mac(interface,current_mac)
            print("Original MAC restored. Terminating the cheeser.")
        

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
