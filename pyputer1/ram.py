import fundamentals
import logic_gates
import alu


class NandLatch:
    def __init__(self, a=0, b=0, x=0, y=0):
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        self.nand_1 = fundamentals.Nand(self.a, self.y)
        self.nand_2 = fundamentals.Nand(self.x, self.b)
        return(None)

    def update(self):
        self.nand_1.update()
        self.x = nand_1.x
        self.nand_2.update()
        self.y = nand_2.x
        self.nand_1.b = self.y
        self.nand_1.update()
        self.nand_2.a = self.x
        self.nand_2.update()
        self.x = nand_1.x
        self.y = nand_2.x
        return(self.x, self.y)


class DFF:
    def __init__(self, d=0, clk=0, Q=0, Qbar=0):
        self.d = d
        self.clk = clk
        self.Q = Q
        self.Qbar = Qbar
        self.nand_latch = NandLatch()
        self.not_1 = logic_gates.Not(self.d)
        self.nand_1 = fundamentals.Nand(self.d, self.clk)
        self.nand_2 = fundamentals.Nand(self.clk, self.not_1.x)
        return(None)

    def update(self):
        not_1 = logic_gates.Not(self.d)
        not_1.update()
        nand_1 = fundamentals.Nand(self.d, self.clk)
        nand_1.update()
        nand_2 = fundamentals.Nand(self.clk, not_1.x)
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
        mux_1 = logic_gates.Mux(self.dff.Q, self.d, self.store)
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
    def __init__(self, d16=[0 for i in range(16)], address3=[0, 0, 0], load=0, clk=0, Q16=[0 for i in range(16)]):
        self.d16 = d16
        self.address3 = address3
        self.load = load
        self.clk = clk
        self.Q16 = Q16
        self.registers = [Register16() for i in range(8)]
        return(None)

    def update(self):
        dmux8 = logic_gates.DMux8Way(self.load, self.address3)
        dmux8.update()
        # reg_0 = self.registers[0]
        self.registers[0].d16 = self.d16
        self.registers[0].load = dmux8.x0
        self.registers[0].clk = self.clk
        self.registers[0].update()
        self.registers[1].d16 = self.d16
        self.registers[1].load = dmux8.x1
        self.registers[1].clk = self.clk
        self.registers[1].update()
        self.registers[2].d16 = self.d16
        self.registers[2].load = dmux8.x2
        self.registers[2].clk = self.clk
        self.registers[2].update()
        self.registers[3].d16 = self.d16
        self.registers[3].load = dmux8.x3
        self.registers[3].clk = self.clk
        self.registers[3].update()
        self.registers[4].d16 = self.d16
        self.registers[4].load = dmux8.x4
        self.registers[4].clk = self.clk
        self.registers[4].update()
        self.registers[5].d16 = self.d16
        self.registers[5].load = dmux8.x5
        self.registers[5].clk = self.clk
        self.registers[5].update()
        self.registers[6].d16 = self.d16
        self.registers[6].load = dmux8.x6
        self.registers[6].clk = self.clk
        self.registers[6].update()
        self.registers[7].d16 = self.d16
        self.registers[7].load = dmux8.x7
        self.registers[7].clk = self.clk
        self.registers[7].update()
        mux816 = logic_gates.Mux8Way16(self.registers[0].Q16, self.registers[1].Q16, self.registers[2].Q16, self.registers[3].Q16, self.registers[4].Q16, self.registers[5].Q16, self.registers[6].Q16, self.registers[7].Q16, self.address3)
        mux816.update()
        self.Q16 = mux816.x16
        return(self.Q16)


class RAM64:
    def __init__(self, d16=[0 for i in range(16)], address6=[0 for i in range(6)], load=0, clk=0, Q16=[0 for i in range(16)]):
        self.d16 = d16
        self.address6 = address6
        self.load = load
        self.clk = clk
        self.Q16 = Q16
        self.ram8s = [RAM8() for i in range(8)]
        return(None)

    def update(self):
        dmux8 = logic_gates.DMux8Way(self.load, self.address6[:3])
        dmux8.update()
        self.ram8s[0].d16 = self.d16
        self.ram8s[0].load = dmux8.x0
        self.ram8s[0].clk = self.clk
        self.ram8s[0].address3 = self.address6[3:]
        self.ram8s[0].update()
        self.ram8s[1].d16 = self.d16
        self.ram8s[1].load = dmux8.x1
        self.ram8s[1].clk = self.clk
        self.ram8s[1].address3 = self.address6[3:]
        self.ram8s[1].update()
        self.ram8s[2].d16 = self.d16
        self.ram8s[2].load = dmux8.x2
        self.ram8s[2].clk = self.clk
        self.ram8s[2].address3 = self.address6[3:]
        self.ram8s[2].update()
        self.ram8s[3].d16 = self.d16
        self.ram8s[3].load = dmux8.x3
        self.ram8s[3].clk = self.clk
        self.ram8s[3].address3 = self.address6[3:]
        self.ram8s[3].update()
        self.ram8s[4].d16 = self.d16
        self.ram8s[4].load = dmux8.x4
        self.ram8s[4].clk = self.clk
        self.ram8s[4].address3 = self.address6[3:]
        self.ram8s[4].update()
        self.ram8s[5].d16 = self.d16
        self.ram8s[5].load = dmux8.x5
        self.ram8s[5].clk = self.clk
        self.ram8s[5].address3 = self.address6[3:]
        self.ram8s[5].update()
        self.ram8s[6].d16 = self.d16
        self.ram8s[6].load = dmux8.x6
        self.ram8s[6].clk = self.clk
        self.ram8s[6].address3 = self.address6[3:]
        self.ram8s[6].update()
        self.ram8s[7].d16 = self.d16
        self.ram8s[7].load = dmux8.x7
        self.ram8s[7].clk = self.clk
        self.ram8s[7].address3 = self.address6[3:]
        self.ram8s[7].update()
        mux816 = logic_gates.Mux8Way16(self.ram8s[0].Q16, self.ram8s[1].Q16, self.ram8s[2].Q16, self.ram8s[3].Q16, self.ram8s[4].Q16, self.ram8s[5].Q16, self.ram8s[6].Q16, self.ram8s[7].Q16, self.address6[:3])
        mux816.update()
        self.Q16 = mux816.x16
        return(self.Q16)


class RAM512:
    def __init__(self, d16=[0 for i in range(16)], address9=[0 for i in range(9)], load=0, clk=0, Q16=[0 for i in range(16)]):
        self.d16 = d16
        self.address9 = address9
        self.load = load
        self.clk = clk
        self.Q16 = Q16
        self.ram64s = [RAM64() for i in range(8)]
        return(None)

    def update(self):
        dmux8 = logic_gates.DMux8Way(self.load, self.address9[:3])
        dmux8.update()
        self.ram64s[0].d16 = self.d16
        self.ram64s[0].load = dmux8.x0
        self.ram64s[0].load = self.load
        self.ram64s[0].clk = self.clk
        self.ram64s[0].address6 = self.address9[3:]
        self.ram64s[0].update()
        self.ram64s[1].d16 = self.d16
        self.ram64s[1].load = dmux8.x1
        self.ram64s[1].load = self.load
        self.ram64s[1].clk = self.clk
        self.ram64s[1].address6 = self.address9[3:]
        self.ram64s[1].update()
        self.ram64s[2].d16 = self.d16
        self.ram64s[2].load = dmux8.x2
        self.ram64s[2].load = self.load
        self.ram64s[2].clk = self.clk
        self.ram64s[2].address6 = self.address9[3:]
        self.ram64s[2].update()
        self.ram64s[3].d16 = self.d16
        self.ram64s[3].load = dmux8.x3
        self.ram64s[3].load = self.load
        self.ram64s[3].clk = self.clk
        self.ram64s[3].address6 = self.address9[3:]
        self.ram64s[3].update()
        self.ram64s[4].d16 = self.d16
        self.ram64s[4].load = dmux8.x4
        self.ram64s[4].load = self.load
        self.ram64s[4].clk = self.clk
        self.ram64s[4].address6 = self.address9[3:]
        self.ram64s[4].update()
        self.ram64s[5].d16 = self.d16
        self.ram64s[5].load = dmux8.x5
        self.ram64s[5].load = self.load
        self.ram64s[5].clk = self.clk
        self.ram64s[5].address6 = self.address9[3:]
        self.ram64s[5].update()
        self.ram64s[6].d16 = self.d16
        self.ram64s[6].load = dmux8.x6
        self.ram64s[6].load = self.load
        self.ram64s[6].clk = self.clk
        self.ram64s[6].address6 = self.address9[3:]
        self.ram64s[6].update()
        self.ram64s[7].d16 = self.d16
        self.ram64s[7].load = dmux8.x7
        self.ram64s[7].load = self.load
        self.ram64s[7].clk = self.clk
        self.ram64s[7].address6 = self.address9[3:]
        self.ram64s[7].update()
        mux816 = logic_gates.Mux8Way16(self.ram64s[0].Q16, self.ram64s[1].Q16, self.ram64s[2].Q16, self.ram64s[3].Q16, self.ram64s[4].Q16, self.ram64s[5].Q16, self.ram64s[6].Q16, self.ram64s[7].Q16, self.address9[:3])
        mux816.update()
        self.Q16 = mux816.x16
        return(self.Q16)


class RAM4K:
    def __init__(self, d16=[0 for i in range(16)], address12=[0 for i in range(12)], load=0, clk=0, Q16=[0 for i in range(16)]):
        self.d16 = d16
        self.address12 = address12
        self.load = load
        self.clk = clk
        self.Q16 = Q16
        self.ram512s = [RAM512() for i in range(8)]
        return(None)

    def update(self):
        dmux8 = logic_gates.DMux8Way(self.load, self.address12[:3])
        dmux8.update()
        self.ram512s[0].d16 = self.d16
        self.ram512s[0].load = dmux8.x0
        self.ram512s[0].clk = self.clk
        self.ram512s[0].address9 = self.address12[3:]
        self.ram512s[0].update()
        self.ram512s[1].d16 = self.d16
        self.ram512s[1].load = dmux8.x1
        self.ram512s[1].clk = self.clk
        self.ram512s[1].address9 = self.address12[3:]
        self.ram512s[1].update()
        self.ram512s[2].d16 = self.d16
        self.ram512s[2].load = dmux8.x2
        self.ram512s[2].clk = self.clk
        self.ram512s[2].address9 = self.address12[3:]
        self.ram512s[2].update()
        self.ram512s[3].d16 = self.d16
        self.ram512s[3].load = dmux8.x3
        self.ram512s[3].clk = self.clk
        self.ram512s[3].address9 = self.address12[3:]
        self.ram512s[3].update()
        self.ram512s[4].d16 = self.d16
        self.ram512s[4].load = dmux8.x4
        self.ram512s[4].clk = self.clk
        self.ram512s[4].address9 = self.address12[3:]
        self.ram512s[4].update()
        self.ram512s[5].d16 = self.d16
        self.ram512s[5].load = dmux8.x5
        self.ram512s[5].clk = self.clk
        self.ram512s[5].address9 = self.address12[3:]
        self.ram512s[5].update()
        self.ram512s[6].d16 = self.d16
        self.ram512s[6].load = dmux8.x6
        self.ram512s[6].clk = self.clk
        self.ram512s[6].address9 = self.address12[3:]
        self.ram512s[6].update()
        self.ram512s[7].d16 = self.d16
        self.ram512s[7].load = dmux8.x7
        self.ram512s[7].clk = self.clk
        self.ram512s[7].address9 = self.address12[3:]
        self.ram512s[7].update()

        mux816 = logic_gates.Mux8Way16(self.ram512s[0].Q16, self.ram512s[1].Q16, self.ram512s[2].Q16, self.ram512s[3].Q16, self.ram512s[4].Q16, self.ram512s[5].Q16, self.ram512s[6].Q16, self.ram512s[7].Q16, self.address12[:3])
        mux816.update()
        self.Q16 = mux816.x16
        return(self.Q16)


class RAM16K:
    def __init__(self, d16=[0 for i in range(16)], address14=[0 for i in range(14)], load=0, clk=0, Q16=[0 for i in range(16)]):
        self.d16 = d16
        self.address14 = address14
        self.load = load
        self.clk = clk
        self.Q16 = Q16
        self.ram4ks = [RAM4K() for i in range(4)]
        return(None)

    def update(self):
        self.ram4ks[0].d16 = self.d16
        self.ram4ks[0].load = self.load
        self.ram4ks[0].clk = self.clk
        self.ram4ks[0].address12 = self.address14[2:]
        self.ram4ks[0].update()
        self.ram4ks[1].d16 = self.d16
        self.ram4ks[1].load = self.load
        self.ram4ks[1].clk = self.clk
        self.ram4ks[1].address12 = self.address14[2:]
        self.ram4ks[1].update()
        self.ram4ks[2].d16 = self.d16
        self.ram4ks[2].load = self.load
        self.ram4ks[2].clk = self.clk
        self.ram4ks[2].address12 = self.address14[2:]
        self.ram4ks[2].update()
        self.ram4ks[3].d16 = self.d16
        self.ram4ks[3].load = self.load
        self.ram4ks[3].clk = self.clk
        self.ram4ks[3].address12 = self.address14[2:]
        self.ram4ks[3].update()

        mux416 = logic_gates.Mux4Way16(self.ram4ks[0].Q16, self.ram4ks[1].Q16, self.ram4ks[2].Q16, self.ram4ks[3].Q16, self.address14[:2])
        mux416.update()
        self.Q16 = mux416.x16
        return(self.Q16)


class PC:
    def __init__(self, d16=[0 for i in range(16)], load=0, reset=0, inc=0, clk=0, Q16=[0 for i in range(16)]):
        self.d16 = d16
        self.load = load
        self.reset = reset
        self.inc = inc
        self.clk = clk
        self.Q16 = Q16
        self.register = Register16()
        self.zeros = [0 for i in range(16)]
        return(None)

    def update(self):
        inc1 = alu.Inc16(self.Q16)
        inc1.update()
        mux1 = logic_gates.Mux16(self.d16, inc1.sum16, [self.inc for i in range(16)])
        mux1.update()
        mux2 = logic_gates.Mux16(mux1.x16, self.zeros, [self.reset for i in range(16)])
        mux2.update()
        or1 = logic_gates.Or(self.inc, self.load)
        or1.update()
        or2 = logic_gates.Or(or1.x, self.reset)
        or2.update()
        self.register.d16 = mux2.x16
        self.register.load = or2.x
        self.register.clk = self.clk
        self.register.update()
        self.Q16 = self.register.Q16
        return(self.Q16)


if __name__ == '__main__':
    my_Bit = Bit()
    my_DFF = DFF()
    my_Nand = fundamentals.Nand()
    my_NandLatch = NandLatch()
    my_PC = PC()
    my_RAM4K = RAM4K()
    my_RAM8 = RAM8()
    my_RAM16K = RAM16K()
    my_RAM64 = RAM64()
    my_RAM512 = RAM512()

    for ii in range(8):
        for jj in range(8):
            for kk in range(8):
                print(my_RAM512.ram64s[ii].ram8s[jj].registers[kk].Q16)
    print("=======================================================================")

    my_RAM512.address9 = [0, 0, 0, 0, 0, 0, 0, 1, 0]
    my_RAM512.d16 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    my_RAM512.clk = 0
    my_RAM512.update()
    my_RAM512.clk = 1
    my_RAM512.update()

    for ii in range(8):
        for jj in range(8):
            for kk in range(8):
                print(my_RAM512.ram64s[ii].ram8s[jj].registers[kk].Q16)
