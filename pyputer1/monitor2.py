# from tkinter import Tk, Canvas, PhotoImage, mainloop
import tkinter
import math
import ram


class MonitorMM():
    def __init__(self):
        # RAM 512 represents the 512 screen columns.
        # Each of the 512 RAM512 registers contains 16 bits
        # Therefore, the 256 screen rows are represented by
        # 16x16 = 256 bits.
        self.ram512s = [ram.RAM512() for ii in range(16)]
        return(None)


class Monitor():
    def __init__(self):
        self.MemoryMap = MonitorMM()
        self.WIDTH = 512
        self.HEIGHT = 256
        self.window = tkinter.Tk()
        self.canvas = tkinter.Canvas(window, width=self.WIDTH, height=self.HEIGHT, bg="#000000")
        self.canvas.pack()
        self.img = tkinter.PhotoImage(width=self.WIDTH, height=self.HEIGHT)
        self.canvas.create_image((WIDTH / 2, HEIGHT / 2), image=img, state="normal")

# WIDTH, HEIGHT = 640, 480
    def update(self):
        for ram512 in self.MemoryMap.ram512s:
            




# window = tkinter.Tk()
# canvas = tkinter.Canvas(window, width=WIDTH, height=HEIGHT, bg="#000000")
# canvas.pack()
# img = tkinter.PhotoImage(width=WIDTH, height=HEIGHT)
# canvas.create_image((WIDTH/2, HEIGHT/2), image=img, state="normal")


for x in range(4 * WIDTH):
    y = int(HEIGHT / 2 + HEIGHT / 4 * math.sin(x / 80.0))
    img.put("#ffffff", (x // 4, y))

tkinter.mainloop()
