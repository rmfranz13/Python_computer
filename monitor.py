import tkinter 
from tkinter import ttk

#lastx, lasty = 0, 0

def xy(event):
    global lastx, lasty
    lastx, lasty = event.x, event.y

def addLine(event):
    global lastx, lasty
    canvas.create_line((lastx, lasty, event.x, event.y))
    lastx, lasty = event.x, event.y

root = tkinter.Tk()
root.columnconfigure(10, weight=1)
root.rowconfigure(10, weight=1)

canvas = tkinter.Canvas(root)
canvas.place(x=0, y=0, height=256, width=512)
ii=0
for a in range(256):
    for b in range(512):
        if(ii%5==0):
            canvas.create_line(a, b, a+1, b+1, fill='black')
        else:
            canvas.create_line(a, b, a+1, b+1, fill='white')
        ii+=1
#canvas.grid(column=10, row=10)
canvas.grid(column=0, row=0, sticky=(tkinter.N, tkinter.W, tkinter.E, tkinter.S))
#canvas.bind("<Button-1>", xy)
#canvas.bind("<B1-Motion>", addLine)

root.mainloop()