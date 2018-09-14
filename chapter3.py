import fundamentals as fd
import chapter1 as ch1
import chapter2 as ch2


a = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,1,0,1,0,1,0,1,0]

a_prev = 0
clk = 0
i = 0
while i<len(a):
    x = fd.dff(a_prev,a[i],clk)
    a_prev = a[i]
    clk = fd.master_clock(clk)
    print("a=%d,x=%d,clk=%d"%(a[i],x,clk))
    x = fd.dff(a_prev,a[i],clk)
    clk = fd.master_clock(clk)
    print("a=%d,x=%d,clk=%d"%(a[i],x,clk))
    i+=1
