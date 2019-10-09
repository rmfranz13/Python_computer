import tkinter 
#from tkinter import ttk
import ram as ch3

class MonitorMM():
    def __init__():
        #RAM 512 represents the 512 screen columns.
        #Each of the 512 RAM512 registers contains 16 bits
        #Therefore, the 256 screen rows are represented by
        # 16x16 = 256 bits.
        self.registers = [ch3.RAM512() for i in range(16)]

class Monitor():
    def __init__(self):
        self.window = tkinter.Tk()

        self.canvas = tkinter.Canvas(self.window, width=1024, height=512, bg="#000000")
        self.canvas.pack()
        #self.canvas.place(x=0, y=0, height=512, width=1024)

        ii=0
        for a in range(1024):
            for b in range(512):

                if(ii%2==0):
                    self.canvas.create_line(a, b, a+1, b+1, fill='black')
                else:
                    self.canvas.create_line(a, b, a+1, b+1, fill='white')
                ii+=1

        #canvas.grid(column=0, row=0, sticky=(tkinter.N, tkinter.W, tkinter.E, tkinter.S))

    def run(self):
        self.window.mainloop()

#Instantiate and run
MonitoryTheMonitor = Monitor()
MonitoryTheMonitor.run()