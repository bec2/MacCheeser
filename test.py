import subprocess
import random
import time
import sys

def elementAfter(lst,element):  
    try:
        elementIndex = lst.index(element)

        elementAfter = lst[elementIndex + 1]
        return elementAfter
    except ValueError:
        return False

def change_mac(interface, new_mac_address):
    #Does the terminal commands for changing the MAC
    subprocess.call(["sudo","ifconfig",interface,"down"])
    subprocess.call(["sudo","ifconfig",interface,"hw","ether",new_mac_address])
    subprocess.call(["sudo","ifconfig",interface,"up"])

def get_random_mac():
    #Randomizes MAC
    charset="0123456789abcdef"
    random_mac="00"
    for i in range(5):
        random_mac += ":" + \
                      random.choice(charset) \
                      + random.choice(charset)
        return random_mac

def get_original(interface):
    #Holds the current MAC for restoration purposes
    currentMac = subprocess.run(f'cat /sys/class/net/{interface}/address', shell=True, capture_output=True)
    return currentMac.stdout.decode("utf-8").rstrip()

#Now let's do the magic and change the mac every 2 minutes
if __name__ == "__main__":
    print("Initializing MAC scrambler. Generating new MAC every 2 minutes.")
    sleeper=120
    interface=elementAfter(sys.argv,"-i") or elementAfter(sys.argv,"--interface")
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
        print("Original MAC restored. Terminating scrambling.")
