"""
Fundamental functions (nand and d-flip-flop) for building a computer
"""
import time

clock_speed = 1.0

def nand(a,b):
    if ((a and b)==1):
        x = 0
    else:
        x = 1
    return(x)

class Nand:
    def __init__(self, a, b, x=None):
        self.a = a
        self.b = b
        self.x = x

    def update(self):
        if (self.a and self.b) == 1:
            self.x = 0
        else:
            self.x = 1
        return(self.x)

def master_clock(clk):
    if clk == 0:
        time.sleep(clock_speed)
        clk = 1
    else:
        time.sleep(clock_speed)
        clk = 0
    return(clk)
            
        







            
