import tkinter as tk 
import time as clock

root = tk.Tk() 
root.title("Stopwatch")

canvas = tk.Canvas(root, width=200, height=200)
canvas.grid(columnspan=2, rowspan=2)

running = False

def counting(label):
    global running 
    t = 0 

    while running:
        clock.sleep(1) 
        t += 1
        
        hours = t // 3600
        minutes = (t % 3600) // 60
        seconds = (t % 3600) % 60
        
        if len(str(hours)) == 1: hours = "0" + str(hours)
        if len(str(minutes)) == 1: minutes = "0" + str(minutes)
        if len(str(seconds)) == 1: seconds = "0" + str(seconds)
        label['text'] = str(hours) + ":" + str(minutes) + ":" + str(seconds)
        root.update()



def startTimer(label): 
    global running 
    running = True
    start_btn['state'] = 'disabled'
    stop_btn['state'] = 'normal'

    counting(label)


def stopTimer(): 
    global running 
    running = False
    start_btn['state'] = 'normal'
    stop_btn['state'] = 'disabled'


# Current second count 
time = tk.Label(root)
time['text'] = "00:00:00"
time.grid(column=0, columnspan=3, row=0)

# Start / Stop Button
start_text = tk.StringVar()
start_text.set("Start")
start_btn = tk.Button(root, textvariable=start_text, command=lambda:startTimer(time))
start_btn.grid(column=0, row=1)

stop_text = tk.StringVar()
stop_text.set("Stop & Reset")
stop_btn = tk.Button(root, textvariable=stop_text, command=stopTimer)
stop_btn.grid(column=1, row=1)

root.mainloop()