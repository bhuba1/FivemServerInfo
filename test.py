from pynput._util.win32_vks import SLEEP
from pynput.keyboard import Key, Listener
from os import system, name 
from datetime import datetime

import time
import threading
import sys


def on_release(key):
    if (key == Key.esc):
        sys.exit("ESC pressed") 

def getData(data):
    while(True):
        _ = system("cls")
        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")
        print(current_time)
        time.sleep(1)

if __name__ == "__main__":
    x = threading.Thread(target=getData,args=("asd",))
    x.setDaemon(True)
    x.start()
    with Listener( on_release=on_release) as listener:
        listener.join()

        