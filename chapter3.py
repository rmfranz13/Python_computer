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


class RAM64:
    def __init__(self, d16=[0 for i in range(16)], 
                 address6=[0 for i in range(6)],
                 load = 0, clk = 0, Q16=[0 for i in range(16)]):
        self.d16 = d16
        self.address6 = address6
        self.load = load
        self.clk = clk
        self.Q16 = Q16
        self.ram8s = [RAM8() for i in range(8)]
        return(None)

    def update(self):
        dmux8 = ch1.DMux8Way(self.load,self.address6[:3])
        dmux8.update()
        ram8_0 = self.ram8s[0]
        ram8_0.d16 = self.d16
        ram8_0.load = dmux8.x0
        ram8_0.clk = self.clk
        ram8_0.address3 = self.address6[3:]
        if self.address6[:3]==[0,0,0]:
            ram8_0.update()
        self.ram8s[0] = ram8_0
        ram8_1 = self.ram8s[1]
        ram8_1.d16 = self.d16
        ram8_1.load = dmux8.x1
        ram8_1.clk = self.clk
        ram8_1.address3 = self.address6[3:]
        if self.address6[:3]==[0,0,1]:
            ram8_1.update()
        self.ram8s[1] = ram8_1
        ram8_2 = self.ram8s[2]
        ram8_2.d16 = self.d16
        ram8_2.load = dmux8.x2
        ram8_2.clk = self.clk
        ram8_2.address3 = self.address6[3:]
        if self.address6[:3]==[0,1,0]:
            ram8_2.update()
        self.ram8s[2] = ram8_2
        ram8_3 = self.ram8s[3]
        ram8_3.d16 = self.d16
        ram8_3.load = dmux8.x3
        ram8_3.clk = self.clk
        ram8_3.address3 = self.address6[3:]
        if self.address6[:3]==[0,1,1]:
            ram8_3.update()
        self.ram8s[3] = ram8_3
        ram8_4 = self.ram8s[4]
        ram8_4.d16 = self.d16
        ram8_4.load = dmux8.x4
        ram8_4.clk = self.clk
        ram8_4.address3 = self.address6[3:]
        if self.address6[:3]==[1,0,0]:
            ram8_4.update()
        self.ram8s[4] = ram8_4
        ram8_5 = self.ram8s[5]
        ram8_5.d16 = self.d16
        ram8_5.load = dmux8.x5
        ram8_5.clk = self.clk
        ram8_5.address3 = self.address6[3:]
        if self.address6[:3]==[1,0,1]:
            ram8_5.update()
        self.ram8s[5] = ram8_5
        ram8_6 = self.ram8s[6]
        ram8_6.d16 = self.d16
        ram8_6.load = dmux8.x6
        ram8_6.clk = self.clk
        ram8_6.address3 = self.address6[3:]
        if self.address6[:3]==[1,1,0]:
            ram8_6.update()
        self.ram8s[6] = ram8_6 
        ram8_7 = self.ram8s[7] 
        ram8_7.d16 = self.d16 
        ram8_7.load = dmux8.x7 
        ram8_7.clk = self.clk 
        ram8_7.address3 = self.address6[3:] 
        if self.address6[:3]==[1,1,1]:
            ram8_7.update()
        self.ram8s[7] = ram8_6
        mux816 = ch1.Mux8Way16(ram8_0.Q16,ram8_1.Q16,ram8_2.Q16,ram8_3.Q16,
                               ram8_4.Q16,ram8_5.Q16,ram8_6.Q16,ram8_7.Q16,
                               self.address6[:3])
        mux816.update() 
        self.Q16 = mux816.x16
        return(self.Q16)


class RAM512:
    def __init__(self, d16=[0 for i in range(16)],
            address9=[0 for i in range(9)],
            load=0, clk=0, Q16=[0 for i in range(16)]):
        self.d16 = d16
        self.address9 = address9 
        self.load = load
        self.clk = clk
        self.Q16 = Q16
        self.ram64s = [RAM64() for i in range(8)]
        return(None)

    def update(self):
        dmux8 = ch1.DMux8Way(self.load, self.address9[:3])
        dmux8.update()
        ram64_0 = self.ram64s[0]
        ram64_0.d16 = self.d16
        ram64_0.load = self.load
        ram64_0.clk = self.clk
        ram64_0.address6 = self.address9[3:]
        if self.address9[:3]==[0,0,0]:
            ram64_0.update()
        self.ram64s[0] = ram64_0
        ram64_1 = self.ram64s[1]
        ram64_1.d16 = self.d16 
        ram64_1.load = self.load 
        ram64_1.clk = self.clk
        ram64_1.address6 = self.address9[3:]
        if self.address9[:3]==[0,0,1]:
            ram64_1.update()
        self.ram64s[1] = ram64_1 
        ram64_2 = self.ram64s[2]
        ram64_2.d16 = self.d16 
        ram64_2.load = self.load 
        ram64_2.clk = self.clk 
        ram64_2.address6 = self.address9[3:]
        if self.address9[:3]==[0,1,0]:
            ram64_2.update()
        self.ram64s[2] = ram64_2
        ram64_3 = self.ram64s[3]
        ram64_3.d16 = self.d16
        ram64_3.load = self.load
        ram64_3.clk = self.clk
        ram64_3.address6 = self.address9[3:]
        if self.address9[:3]==[0,1,1]:
            ram64_3.update()
        self.ram64s[3] = ram64_3
        ram64_4 = self.ram64s[4]
        ram64_4.d16 = self.d16
        ram64_4.load = self.load
        ram64_4.clk = self.clk
        ram64_4.address6 = self.address9[3:]
        if self.address9[:3]==[1,0,0]:
            ram64_4.update()
        self.ram64s[4] = ram64_4
        ram64_5 = self.ram64s[5]
        ram64_5.d16 = self.d16
        ram64_5.load = self.load 
        ram64_5.clk = self.clk 
        ram64_5.address6 = self.address9[3:]
        if self.address9[:3]==[1,0,1]:
            ram64_5.update()
        self.ram64s[5] = ram64_5 
        ram64_6 = self.ram64s[6]
        ram64_6.d16 = self.d16 
        ram64_6.load = self.load 
        ram64_6.clk = self.clk 
        ram64_6.address6 = self.address9[3:] 
        if self.address9[:3]==[1,1,0]:
            ram64_6.update()
        self.ram64s[6] = ram64_6 
        ram64_7 = self.ram64s[7]
        ram64_7.d16 = self.d16 
        ram64_7.load = self.load 
        ram64_7.clk = self.clk 
        ram64_7.address6 = self.address9[3:]
        if self.address9[:3]==[1,1,1]:
            ram64_7.update()
        self.ram64s[7] = ram64_7

        mux816 = ch1.Mux8Way16(ram64_0.Q16,ram64_1.Q16,ram64_2.Q16,ram64_3.Q16,
                               ram64_4.Q16,ram64_5.Q16,ram64_6.Q16,ram64_7.Q16,
                               self.address9[:3])
        mux816.update()
        self.Q16 = mux816.x16
        return(self.Q16)


class RAM4K:
    def __init__(self, d16 = [0 for i in range(16)],
            address12 = [0 for i in range(12)],
            load = 0, clk = 0, Q16 = [0 for i in range(16)]):
        self.d16 = d16 
        self.address12 = address12
        self.load = load 
        self.clk = clk
        self.Q16 = Q16 
        self.ram512s = [RAM512() for i in range(8)]
        return(None)

    def update(self):
        ram512_0 = self.ram512s[0]
        ram512_0.d16 = self.d16 
        ram512_0.load = self.load 
        ram512_0.clk = self.clk 
        ram512_0.address9 = self.address12[3:]
        if self.address12[:3]==[0,0,0]:
            ram512_0.update() 
        self.ram512s[0] = ram512_0
        ram512_1 = self.ram512s[1]
        ram512_1.d16 = self.d16 
        ram512_1.load = self.load 
        ram512_1.clk = self.clk 
        ram512_1.address9 = self.address12[3:]
        if self.address12[:3]==[0,0,1]:
            ram512_1.update()
        self.ram512s[1] = ram512_1 
        ram512_2 = self.ram512s[2] 
        ram512_2.d16 = self.d16 
        ram512_2.load = self.load 
        ram512_2.clk = self.clk 
        ram512_2.address9 = self.address12[3:]
        if self.address12[:3]==[0,1,0]:
            ram512_2.update() 
        self.ram512s[2] = ram512_2 
        ram512_3 = self.ram512s[3] 
        ram512_3.d16 = self.d16 
        ram512_3.load = self.load 
        ram512_3.clk = self.load 
        ram512_3.address9 = self.address12[3:] 
        if self.address12[:3]==[0,1,1]:
            ram512_3.update()
        self.ram512s[3] = ram512_3 
        ram512_4 = self.ram512s[4]
        ram512_4.d16 = self.d16 
        ram512_4.load = self.load 
        ram512_4.clk = self.clk 
        ram512_4.address9 = self.address12[3:]
        if self.address12[:3]==[1,0,0]:
            ram512_4.update()
        self.ram512s[4] = ram512_4
        ram512_5 = self.ram512s[5]
        ram512_5.d16 = self.d16 
        ram512_5.load = self.load
        ram512_5.clk = self.clk 
        ram512_5.address9 = self.address12[3:]
        if self.address12[:3]==[1,0,1]:
            ram512_5.update()
        self.ram512s[5] = ram512_5 
        ram512_6 = self.ram512s[6] 
        ram512_6.d16 = self.d16 
        ram512_6.load = self.load 
        ram512_6.clk = self.clk 
        ram512_6.address9 = self.address12[3:]
        if self.address12[:3]==[1,1,0]:
            ram512_6.update() 
        self.ram512s[6] = ram512_6 
        ram512_7 = self.ram512s[7] 
        ram512_7.d16 = self.d16 
        ram512_7.load = self.load 
        ram512_7.clk = self.clk 
        ram512_7.address9 = self.address12[3:]
        if self.address12[:3]==[1,1,1]:
            ram512_7.update()
        self.ram512s[7] = ram512_7

        mux816 = ch1.Mux8Way16(ram512_0.Q16,ram512_1.Q16,ram512_2.Q16,ram512_3.Q16,
                               ram512_4.Q16,ram512_5.Q16,ram512_6.Q16,ram512_7.Q16,
                               self.address12[:3])
        mux816.update()
        self.Q16 = mux816.x16
        return(self.Q16)

class RAM16K:
    def __init__(self, d16 = [0 for i in range(16)],
            address14 = [0 for i in range(14)],
            load = 0, clk = 0, Q16 = [0 for i in range(16)]):
        self.d16 = d16 
        self.address14 = address14 
        self.load = load 
        self.clk = clk 
        self.Q16 = Q16 
        self.ram4ks = [RAM4K() for i in range(4)]
        return(None)

    def update(self):
        ram4k_0 = self.ram4ks[0]
        ram4k_0.d16 = self.d16 
        ram4k_0.load = self.load 
        ram4k_0.clk = self.clk 
        ram4k_0.address12 = self.address14[2:]
        if self.address14[:2] == [0,0]:
            ram4k_0.update()
        self.ram4ks[0] = ram4k_0
        ram4k_1 = self.ram4ks[1]
        ram4k_1.d16 = self.d16 
        ram4k_1.load = self.load 
        ram4k_1.clk = self.clk 
        ram4k_1.address12 = self.address14[2:]
        if self.address14[:2] == [0,1]:
            ram4k_1.update() 
        self.ram4ks[1] = ram4k_1
        ram4k_2 = self.ram4ks[2]
        ram4k_2.d16 = self.d16 
        ram4k_2.load = self.load
        ram4k_2.clk = self.clk 
        ram4k_2.address12 = self.address14[2:]
        if self.address14[:2]==[1,0]:
            ram4k_2.update()
        self.ram4ks[2] = ram4k_2 
        ram4k_3 = self.ram4ks[3]
        ram4k_3.d16 = self.d16 
        ram4k_3.load = self.load
        ram4k_3.clk = self.clk 
        ram4k_3.address12 = self.address14[2:]
        if self.address14[:2]==[1,1]:
            ram4k_3.update()
        self.ram4ks[3] = ram4k_3

        mux416 = ch1.Mux4Way16(ram4k_0.Q16,ram4k_1.Q16,ram4k_2.Q16,ram4k_3.Q16,self.address14[:2])
        mux416.update()
        self.Q16 = mux416.x16
        return(self.Q16)




def read_write():
    user_input = input("read or write?\n > ")
    return(user_input)

def get_address():
    user_input = input("enter the address (ex 01011010001010)\n > ")
    address = []
    for i in user_input:
        address.append(int(i))
    return(address)

def get_data():
    user_input = input("enter data (ex 0001011001011101)\n > ")
    data = []
    for i in user_input:
        data.append(int(i))
    return(data)

def next_state_logic(user_input, current_state):
    if current_state == 0:
        if user_input == "read":
            next_state = 1
        elif user_input == "write":
            next_state = 2 
        else:
            print("please enter read or write")
            next_state = 0 
    elif current_state == 1:
        next_state = 0
    elif current_state == 2:
        next_state = 0 
    else:
        print('invalid state, starting over')
        next_state = 0
    return(next_state)

ram16k = RAM16K()
ram16k.clk = 1
ram16k.load = 1
ram16k.d16 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ram16k.address14 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Inc1 = ch2.Inc16(ram16k.d16)
for i in range(16384):
    ram16k.update()
    Inc1.a16 = ram16k.d16
    Inc1.update()
    ram16k.d16 = Inc1.sum16
    ram16k.address14 = ram16k.d16[2:]
    ram16k.clk = 0
    ram16k.update()
    ram16k.clk = 1
    ram16k.update()
    print("Q16[%d] = %s"%(i,str(ram16k.Q16)))


def output_logic(current_state):
    if current_state == 0:
        user_input = read_write()
    elif current_state == 1:
        address = get_address()
        ram16k.address14 = address
        ram16k.clk = 1
        ram16k.load = 0
        ram16k.update()
        print(ram16k.Q16)
        user_input = ''
    elif current_state == 2:
        address = get_address()
        data = get_data()
        ram16k.address14 = address
        ram16k.d16 = data 
        ram16k.clk = 1 
        ram16k.load = 1
        ram16k.update()
        user_input = ''
    else:
        print("uh oh")
        user_input = ''
    return(user_input)

def loop():
    current_state = 0
    while True:
        user_input = output_logic(current_state)
        current_state = next_state_logic(user_input,current_state)
        ram16k.clk = 1 
        ram16k.update()
        ram16k.clk = 0
        ram16k.update()

loop()
        






