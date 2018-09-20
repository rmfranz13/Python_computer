from fundamentals import Nand
import chapter1 as ch1
import chapter2 as ch2

class NandLatch:
    def __init__(self, a=0, b=0, x=0, y=0):
        self.a = a 
        self.b = b 
        self.x = x 
        self.y = y 
        return(None)
    
    def update(self):
        nand_1 = Nand(self.a, self.y)
        nand_1.update()
        self.x = nand_1.x
        nand_2 = Nand(self.x, self.b)
        nand_2.update()
        self.y = nand_2.x 
        nand_1.b = self.y 
        nand_1.update()
        nand_2.a = self.x 
        nand_2.update()
        self.x = nand_1.x 
        self.y = nand_2.x 
        return(self.x,self.y)

		
class DFF:
    def __init__(self, d=0, clk=0, Q=0, Qbar=0):
        self.d = d 
        self.clk = clk 
        self.Q = Q 
        self.Qbar = Qbar
        self.nand_latch = NandLatch()
        return(None) 
    
    def update(self): 
        not_1 = ch1.Not(self.d)
        not_1.update()
        nand_1 = Nand(self.d, self.clk) 
        nand_1.update() 
        nand_2 = Nand(self.clk,not_1.x)
        nand_2.update() 
        self.nand_latch.a = nand_1.x
        self.nand_latch.b = nand_2.x
        self.nand_latch.update() 
        self.Q = self.nand_latch.x 
        self.Qbar = self.nand_latch.y 
        return(self.Q, self.Qbar) 

class Bit:
    def __init__(self, d=0, clk=0, store=0, Q=0):
        self.d = d
        self.clk = clk
        self.store = store
        self.Q = Q
        self.dff = DFF()
        return(None) 

    def update(self): 
        mux_1 = ch1.Mux(self.dff.Q,self.d,self.store)
        mux_1.update()
        self.dff.d = mux_1.x
        self.dff.clk = self.clk
        self.dff.update()
        self.Q = self.dff.Q
        return(self.Q) 

class Register16:
    def __init__(self, d16=[0 for i in range(16)], load=0, clk=0, Q16=[0 for i in range(16)]):
        self.d16 = d16,
        self.load = load
        self.clk = clk
        self.Q16 = Q16
        self.Bits = [Bit() for i in range(16)]
        return(None)

    def update(self):
        bit_0 = self.Bits[0]
        bit_0.d = self.d16[0]
        bit_0.store = self.load
        bit_0.clk = self.clk
        bit_0.update()
        self.Q16[0] = bit_0.Q
        bit_1 = self.Bits[1]
        bit_1.d = self.d16[1] 
        bit_1.store = self.load
        bit_1.clk = self.clk
        bit_1.update()
        self.Q16[1] = bit_1.Q
        bit_2 = self.Bits[2]
        bit_2.d = self.d16[2] 
        bit_2.store = self.load
        bit_2.clk = self.clk
        bit_2.update()
        self.Q16[2] = bit_2.Q
        bit_3 = self.Bits[3]
        bit_3.d = self.d16[3]
        bit_3.store = self.load
        bit_3.clk = self.clk
        bit_3.update()
        self.Q16[3] = bit_3.Q
        bit_4 = self.Bits[4]
        bit_4.d = self.d16[4]
        bit_4.store = self.load
        bit_4.clk = self.clk
        bit_4.update()
        self.Q16[4] = bit_4.Q
        bit_5 = self.Bits[5]
        bit_5.d = self.d16[5]
        bit_5.store = self.load
        bit_5.clk = self.clk
        bit_5.update()
        self.Q16[5] = bit_5.Q
        bit_6 = self.Bits[6]
        bit_6.d = self.d16[6]
        bit_6.store = self.load
        bit_6.clk = self.clk
        bit_6.update()
        self.Q16[6] = bit_6.Q
        bit_7 = self.Bits[7]
        bit_7.d = self.d16[7]
        bit_7.store = self.load
        bit_7.clk = self.clk
        bit_7.update()
        self.Q16[7] = bit_7.Q
        bit_8 = self.Bits[8]
        bit_8.d = self.d16[8]
        bit_8.store = self.load
        bit_8.clk = self.clk
        bit_8.update()
        self.Q16[8] = bit_8.Q
        bit_9 = self.Bits[9]
        bit_9.d = self.d16[9]
        bit_9.store = self.load
        bit_9.clk = self.clk
        bit_9.update()
        self.Q16[9] = bit_9.Q
        bit_10 = self.Bits[10]
        bit_10.d = self.d16[10]
        bit_10.store = self.load
        bit_10.clk = self.clk
        bit_10.update()
        self.Q16[10] = bit_10.Q
        bit_11 = self.Bits[11]
        bit_11.d = self.d16[11]
        bit_11.store = self.load
        bit_11.clk = self.clk 
        bit_11.update()
        self.Q16[11] = bit_11.Q
        bit_12 = self.Bits[12]
        bit_12.d = self.d16[12]
        bit_12.store = self.load
        bit_12.clk = self.clk
        bit_12.update()
        self.Q16[12] = bit_12.Q
        bit_13 = self.Bits[13]
        bit_13.d = self.d16[13]
        bit_13.store = self.load
        bit_13.clk = self.clk
        bit_13.update()
        self.Q16[13] = bit_13.Q
        bit_14 = self.Bits[14]
        bit_14.d = self.d16[14]
        bit_14.store = self.load
        bit_14.clk = self.clk
        bit_14.update()
        self.Q16[14] = bit_14.Q
        bit_15 = self.Bits[15]
        bit_15.d = self.d16[15]
        bit_15.store = self.load
        bit_15.clk = self.clk
        bit_15.update()
        self.Q16[15] = bit_15.Q
        return(self.Q16)

class RAM8:
    def __init__(self, d16=[0 for i in range(16)], address3=[0,0,0], load=0, 
                 clk=0, Q16=[0 for i in range(16)]):
        self.d16 = d16
        self.address3 = address3
        self.load = load
        self.clk = clk 
        self.Q16 = Q16
        self.registers = [Register16() for i in range(8)]
        return(None)

    def update(self):
        dmux8 = ch1.DMux8Way(self.load,self.address3)
        dmux8.update()
        print("%d %d %d %d %d %d %d %d"%(dmux8.x0,dmux8.x1,dmux8.x2,dmux8.x3,dmux8.x4,dmux8.x5,dmux8.x6,dmux8.x7))
        reg_0 = self.registers[0]
        reg_0.d16 = self.d16
        reg_0.load = dmux8.x0
        reg_0.clk = self.clk
        if self.address3 == [0,0,0]:
            reg_0.update()
        self.registers[0] = reg_0
        reg_1 = self.registers[1] 
        reg_1.d16 = self.d16
        reg_1.load = dmux8.x1
        reg_1.clk = self.clk
        if self.address3 == [0,0,1]:
            reg_1.update()
        self.registers[1] = reg_1
        reg_2 = self.registers[2]
        reg_2.d16 = self.d16
        reg_2.load = dmux8.x2
        reg_2.clk = self.clk
        if self.address3 == [0,1,0]:
            reg_2.update()
        self.registers[2] = reg_2
        reg_3 = self.registers[3]
        reg_3.d16 = self.d16
        reg_3.load = dmux8.x3
        reg_3.clk = self.clk
        if self.address3 == [0,1,1]:
            reg_3.update()
        self.registers[3] = reg_3
        reg_4 = self.registers[4]
        reg_4.d16 = self.d16
        reg_4.load = dmux8.x4
        reg_4.clk = self.clk
        if self.address3 == [1,0,0]:
            reg_4.update()
        self.registers[4] = reg_4
        reg_5 = self.registers[5]
        reg_5.d16 = self.d16
        reg_5.load = dmux8.x5
        reg_5.clk = self.clk
        if self.address3 == [1,0,1]:
            reg_5.update()
        self.registers[5] = reg_5
        reg_6 = self.registers[6]
        reg_6.d16 = self.d16
        reg_6.load = dmux8.x6
        reg_6.clk = self.clk
        if self.address3 == [1,1,0]:
            reg_6.update()
        self.registers[6] = reg_6
        reg_7 = self.registers[7]
        reg_7.d16 = self.d16
        reg_7.load = dmux8.x7
        reg_7.clk = self.clk
        if self.address3 == [1,1,1]:
            reg_7.update()
        self.registers[7] = reg_7
        mux816 = ch1.Mux8Way16(reg_0.Q16,reg_1.Q16,reg_2.Q16,reg_3.Q16,
                               reg_4.Q16,reg_5.Q16,reg_6.Q16,reg_7.Q16,self.address3)
        mux816.update()
        self.Q16 = mux816.x16
        return(self.Q16)


import random

ram8 = RAM8()
clk = 0
for i in range(100):
    ram8.d16 = [random.randint(0,1) for i in range(16)]
    ram8.address3 = [random.randint(0,1) for i in range(3)]
    ram8.load = random.randint(0,1)
    ram8.clk = clk
    ram8.update()
    print("load=%d, clk=%d"%(ram8.load,ram8.clk))
    print("address=%s, d16=%s, Q16=%s"%(ram8.address3,ram8.d16,ram8.Q16))

    if clk == 0:
        clk = 1
    else:
        clk = 0







