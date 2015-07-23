# run a timer that starts counting after 2 hours
import webbrowser
import time
import ctypes 

# do something with the timer control
print ("This program started on " + time.ctime())

while True:
    time.sleep(60*30)
    #time.sleep(10)
    ctypes.windll.user32.MessageBoxA(0, "Take a Break", "You should take a break", 0)