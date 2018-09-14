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

def dff(a_prev,a,t):
    if t==1:
        x=a
    else:
        x=a_prev
    return(x)

def master_clock(clk):
    if clk == 0:
        time.sleep(clock_speed)
        clk = 1
    else:
        time.sleep(clock_speed)
        clk = 0
    return(clk)
            
        







            
