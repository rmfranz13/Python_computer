import logic_gates as lg


class NandLatch:
    def __init__(self):
        self.pin_a = 0
        self.pin_b = 0
        self.pin_x = 0
        self.pin_y = 0
        self.nand_1 = lg.NandGate()
        self.nand_2 = lg.NandGate()

    def update(self):
        self.nand_1.pin_a = self.pin_a
        self.nand_1.pin_b = self.pin_b
        self.nand_1.update()
        self.pin_x = self.nand_1.pin_x
        self.nand_2.pin_a = self.pin_x
        self.nand_2.pin_b = self.pin_y
        self.nand_2.update()
        self.pin_y = self.nand_2.pin_x
        self.nand_1.pin_b = self.pin_y
        self.nand_1.update()
        self.nand_2.pin_a = self.pin_x
        self.nand_2.update()
        self.pin_x = self.nand_1.pin_x
        self.pin_y = self.nand_2.pin_x


class DFF:
    def __init__(self):
        self.pin_d = 0
        self.pin_clk = 0
        self.pin_Q = 0
        self.pin_Qbar = 0
        self.nand_latch = NandLatch()
        self.not_1 = lg.NotGate()
        self.nand_1 = lg.NandGate()
        self.nand_2 = lg.NandGate()

    def update(self):
        self.not_1.pin_a = self.pin_clk
        self.not_1.update()
        self.nand_1.pin_a = self.pin_d
        self.nand_1.pin_b = self.pin_clk
        self.nand_1.update()
        self.nand_2.pin_a = self.pin_clk
        self.nand_2.pin_b = self.not_1.pin_x
        self.nand_2.update()
        self.nand_latch.pin_a = self.nand_1.pin_x
        self.nand_latch.pin_b = self.nand_2.pin_x
        self.nand_latch.update()
        self.pin_Q = self.nand_latch.pin_x
        self.pin_Qbar = self.nand_latch.pin_y


class Bit:
    def __init__(self):
        self.pin_d = 0
        self.pin_clk = 0
        self.pin_store = 0
        self.pin_Q = 0
        self.dff = DFF()
        self.mux_1 = lg.MuxGate()

    def update(self):
        self.mux_1.pin_a = self.dff.pin_Q
        self.mux_1.pin_b = self.pin_d
        self.mux_1.pin_sel = self.pin_store
        self.mux_1.update()
        self.dff.pin_d = self.mux_1.pin_x
        self.dff.pin_clk = self.pin_clk
        self.dff.update()
        self.pin_Q = self.dff.pin_Q


class Register16:
    def __init__(self):
        self.bus_d16 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.pin_load = 0
        self.pin_clk = 0
        self.bus_Q16 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.Bits = [Bit(), Bit(), Bit(), Bit(), Bit(), Bit(), Bit(), Bit(), Bit(), Bit(), Bit(), Bit(), Bit(), Bit(), Bit(), Bit()]

    def update(self):
        # Assign input pins:
        self.Bits[0].d_pin = self.bus_d16[0]
        self.Bits[1].d_pin = self.bus_d16[1]
        self.Bits[2].d_pin = self.bus_d16[2]
        self.Bits[3].d_pin = self.bus_d16[3]
        self.Bits[4].d_pin = self.bus_d16[4]
        self.Bits[5].d_pin = self.bus_d16[5]
        self.Bits[6].d_pin = self.bus_d16[6]
        self.Bits[7].d_pin = self.bus_d16[7]
        self.Bits[8].d_pin = self.bus_d16[8]
        self.Bits[9].d_pin = self.bus_d16[9]
        self.Bits[10].d_pin = self.bus_d16[10]
        self.Bits[11].d_pin = self.bus_d16[11]
        self.Bits[12].d_pin = self.bus_d16[12]
        self.Bits[13].d_pin = self.bus_d16[13]
        self.Bits[14].d_pin = self.bus_d16[14]
        self.Bits[15].d_pin = self.bus_d16[15]

        # Assign control bits:
        self.Bits[0].pin_clk = self.pin_clk
        self.Bits[1].pin_clk = self.pin_clk
        self.Bits[2].pin_clk = self.pin_clk
        self.Bits[3].pin_clk = self.pin_clk
        self.Bits[4].pin_clk = self.pin_clk
        self.Bits[5].pin_clk = self.pin_clk
        self.Bits[6].pin_clk = self.pin_clk
        self.Bits[7].pin_clk = self.pin_clk
        self.Bits[8].pin_clk = self.pin_clk
        self.Bits[9].pin_clk = self.pin_clk
        self.Bits[10].pin_clk = self.pin_clk
        self.Bits[11].pin_clk = self.pin_clk
        self.Bits[12].pin_clk = self.pin_clk
        self.Bits[13].pin_clk = self.pin_clk
        self.Bits[14].pin_clk = self.pin_clk
        self.Bits[15].pin_clk = self.pin_clk

        self.Bits[0].pin_store = self.pin_load
        self.Bits[1].pin_store = self.pin_load
        self.Bits[2].pin_store = self.pin_load
        self.Bits[3].pin_store = self.pin_load
        self.Bits[4].pin_store = self.pin_load
        self.Bits[5].pin_store = self.pin_load
        self.Bits[6].pin_store = self.pin_load
        self.Bits[7].pin_store = self.pin_load
        self.Bits[8].pin_store = self.pin_load
        self.Bits[9].pin_store = self.pin_load
        self.Bits[10].pin_store = self.pin_load
        self.Bits[11].pin_store = self.pin_load
        self.Bits[12].pin_store = self.pin_load
        self.Bits[13].pin_store = self.pin_load
        self.Bits[14].pin_store = self.pin_load
        self.Bits[15].pin_store = self.pin_load

        # Update all bits:
        self.Bits[0].update()
        self.Bits[1].update()
        self.Bits[2].update()
        self.Bits[3].update()
        self.Bits[4].update()
        self.Bits[5].update()
        self.Bits[6].update()
        self.Bits[7].update()
        self.Bits[8].update()
        self.Bits[9].update()
        self.Bits[10].update()
        self.Bits[11].update()
        self.Bits[12].update()
        self.Bits[13].update()
        self.Bits[14].update()
        self.Bits[15].update()

        # Assign output pins:
        self.bus_Q16[0] = self.Bits[0].pin_Q
        self.bus_Q16[1] = self.Bits[1].pin_Q
        self.bus_Q16[2] = self.Bits[2].pin_Q
        self.bus_Q16[3] = self.Bits[3].pin_Q
        self.bus_Q16[4] = self.Bits[4].pin_Q
        self.bus_Q16[5] = self.Bits[5].pin_Q
        self.bus_Q16[6] = self.Bits[6].pin_Q
        self.bus_Q16[7] = self.Bits[7].pin_Q
        self.bus_Q16[8] = self.Bits[8].pin_Q
        self.bus_Q16[9] = self.Bits[9].pin_Q
        self.bus_Q16[10] = self.Bits[10].pin_Q
        self.bus_Q16[11] = self.Bits[11].pin_Q
        self.bus_Q16[12] = self.Bits[12].pin_Q
        self.bus_Q16[13] = self.Bits[13].pin_Q
        self.bus_Q16[14] = self.Bits[14].pin_Q
        self.bus_Q16[15] = self.Bits[15].pin_Q
        

class RAM8:
    def __init__(self):
        self.bus_d16 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.bus_address3 = [0, 0, 0]
        self.pin_load = 0
        self.pin_clk = 0
        self.bus_Q16 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.registers = [Register16(), Register16(), Register16(), Register16(), Register16(), Register16(), Register16(), Register16()]
        self.dmux8 = lg.DMux8Way()
        self.mux8_16 = lg.Mux8Way16()

    def update(self):

        # Load the dmux with load and address pins
        self.dmux8.pin_a = self.pin_load
        self.dmux8.pin_sel0 = self.bus_address3[0]
        self.dmux8.pin_sel1 = self.bus_address3[1]
        self.dmux8.pin_sel2 = self.bus_address3[2]
        self.dmux8.update()
        # reg_0 = self.registers[0]

        # Put data on input pins of registers:
        self.registers[0].bus_d16[0] = self.bus_d16[0]
        self.registers[0].bus_d16[1] = self.bus_d16[1]
        self.registers[0].bus_d16[2] = self.bus_d16[2]
        self.registers[0].bus_d16[3] = self.bus_d16[3]
        self.registers[0].bus_d16[4] = self.bus_d16[4]
        self.registers[0].bus_d16[5] = self.bus_d16[5]
        self.registers[0].bus_d16[6] = self.bus_d16[6]
        self.registers[0].bus_d16[7] = self.bus_d16[7]
        self.registers[0].bus_d16[8] = self.bus_d16[8]
        self.registers[0].bus_d16[9] = self.bus_d16[9]
        self.registers[0].bus_d16[10] = self.bus_d16[10]
        self.registers[0].bus_d16[11] = self.bus_d16[11]
        self.registers[0].bus_d16[12] = self.bus_d16[12]
        self.registers[0].bus_d16[13] = self.bus_d16[13]
        self.registers[0].bus_d16[14] = self.bus_d16[14]
        self.registers[0].bus_d16[15] = self.bus_d16[15]

        self.registers[1].bus_d16[0] = self.bus_d16[0]
        self.registers[1].bus_d16[1] = self.bus_d16[1]
        self.registers[1].bus_d16[2] = self.bus_d16[2]
        self.registers[1].bus_d16[3] = self.bus_d16[3]
        self.registers[1].bus_d16[4] = self.bus_d16[4]
        self.registers[1].bus_d16[5] = self.bus_d16[5]
        self.registers[1].bus_d16[6] = self.bus_d16[6]
        self.registers[1].bus_d16[7] = self.bus_d16[7]
        self.registers[1].bus_d16[8] = self.bus_d16[8]
        self.registers[1].bus_d16[9] = self.bus_d16[9]
        self.registers[1].bus_d16[10] = self.bus_d16[10]
        self.registers[1].bus_d16[11] = self.bus_d16[11]
        self.registers[1].bus_d16[12] = self.bus_d16[12]
        self.registers[1].bus_d16[13] = self.bus_d16[13]
        self.registers[1].bus_d16[14] = self.bus_d16[14]
        self.registers[1].bus_d16[15] = self.bus_d16[15]

        self.registers[2].bus_d16[0] = self.bus_d16[0]
        self.registers[2].bus_d16[1] = self.bus_d16[1]
        self.registers[2].bus_d16[2] = self.bus_d16[2]
        self.registers[2].bus_d16[3] = self.bus_d16[3]
        self.registers[2].bus_d16[4] = self.bus_d16[4]
        self.registers[2].bus_d16[5] = self.bus_d16[5]
        self.registers[2].bus_d16[6] = self.bus_d16[6]
        self.registers[2].bus_d16[7] = self.bus_d16[7]
        self.registers[2].bus_d16[8] = self.bus_d16[8]
        self.registers[2].bus_d16[9] = self.bus_d16[9]
        self.registers[2].bus_d16[10] = self.bus_d16[10]
        self.registers[2].bus_d16[11] = self.bus_d16[11]
        self.registers[2].bus_d16[12] = self.bus_d16[12]
        self.registers[2].bus_d16[13] = self.bus_d16[13]
        self.registers[2].bus_d16[14] = self.bus_d16[14]
        self.registers[2].bus_d16[15] = self.bus_d16[15]

        self.registers[3].bus_d16[0] = self.bus_d16[0]
        self.registers[3].bus_d16[1] = self.bus_d16[1]
        self.registers[3].bus_d16[2] = self.bus_d16[2]
        self.registers[3].bus_d16[3] = self.bus_d16[3]
        self.registers[3].bus_d16[4] = self.bus_d16[4]
        self.registers[3].bus_d16[5] = self.bus_d16[5]
        self.registers[3].bus_d16[6] = self.bus_d16[6]
        self.registers[3].bus_d16[7] = self.bus_d16[7]
        self.registers[3].bus_d16[8] = self.bus_d16[8]
        self.registers[3].bus_d16[9] = self.bus_d16[9]
        self.registers[3].bus_d16[10] = self.bus_d16[10]
        self.registers[3].bus_d16[11] = self.bus_d16[11]
        self.registers[3].bus_d16[12] = self.bus_d16[12]
        self.registers[3].bus_d16[13] = self.bus_d16[13]
        self.registers[3].bus_d16[14] = self.bus_d16[14]
        self.registers[3].bus_d16[15] = self.bus_d16[15]

        self.registers[4].bus_d16[0] = self.bus_d16[0]
        self.registers[4].bus_d16[1] = self.bus_d16[1]
        self.registers[4].bus_d16[2] = self.bus_d16[2]
        self.registers[4].bus_d16[3] = self.bus_d16[3]
        self.registers[4].bus_d16[4] = self.bus_d16[4]
        self.registers[4].bus_d16[5] = self.bus_d16[5]
        self.registers[4].bus_d16[6] = self.bus_d16[6]
        self.registers[4].bus_d16[7] = self.bus_d16[7]
        self.registers[4].bus_d16[8] = self.bus_d16[8]
        self.registers[4].bus_d16[9] = self.bus_d16[9]
        self.registers[4].bus_d16[10] = self.bus_d16[10]
        self.registers[4].bus_d16[11] = self.bus_d16[11]
        self.registers[4].bus_d16[12] = self.bus_d16[12]
        self.registers[4].bus_d16[13] = self.bus_d16[13]
        self.registers[4].bus_d16[14] = self.bus_d16[14]
        self.registers[4].bus_d16[15] = self.bus_d16[15]

        self.registers[5].bus_d16[0] = self.bus_d16[0]
        self.registers[5].bus_d16[1] = self.bus_d16[1]
        self.registers[5].bus_d16[2] = self.bus_d16[2]
        self.registers[5].bus_d16[3] = self.bus_d16[3]
        self.registers[5].bus_d16[4] = self.bus_d16[4]
        self.registers[5].bus_d16[5] = self.bus_d16[5]
        self.registers[5].bus_d16[6] = self.bus_d16[6]
        self.registers[5].bus_d16[7] = self.bus_d16[7]
        self.registers[5].bus_d16[8] = self.bus_d16[8]
        self.registers[5].bus_d16[9] = self.bus_d16[9]
        self.registers[5].bus_d16[10] = self.bus_d16[10]
        self.registers[5].bus_d16[11] = self.bus_d16[11]
        self.registers[5].bus_d16[12] = self.bus_d16[12]
        self.registers[5].bus_d16[13] = self.bus_d16[13]
        self.registers[5].bus_d16[14] = self.bus_d16[14]
        self.registers[5].bus_d16[15] = self.bus_d16[15]

        self.registers[6].bus_d16[0] = self.bus_d16[0]
        self.registers[6].bus_d16[1] = self.bus_d16[1]
        self.registers[6].bus_d16[2] = self.bus_d16[2]
        self.registers[6].bus_d16[3] = self.bus_d16[3]
        self.registers[6].bus_d16[4] = self.bus_d16[4]
        self.registers[6].bus_d16[5] = self.bus_d16[5]
        self.registers[6].bus_d16[6] = self.bus_d16[6]
        self.registers[6].bus_d16[7] = self.bus_d16[7]
        self.registers[6].bus_d16[8] = self.bus_d16[8]
        self.registers[6].bus_d16[9] = self.bus_d16[9]
        self.registers[6].bus_d16[10] = self.bus_d16[10]
        self.registers[6].bus_d16[11] = self.bus_d16[11]
        self.registers[6].bus_d16[12] = self.bus_d16[12]
        self.registers[6].bus_d16[13] = self.bus_d16[13]
        self.registers[6].bus_d16[14] = self.bus_d16[14]
        self.registers[6].bus_d16[15] = self.bus_d16[15]

        self.registers[7].bus_d16[0] = self.bus_d16[0]
        self.registers[7].bus_d16[1] = self.bus_d16[1]
        self.registers[7].bus_d16[2] = self.bus_d16[2]
        self.registers[7].bus_d16[3] = self.bus_d16[3]
        self.registers[7].bus_d16[4] = self.bus_d16[4]
        self.registers[7].bus_d16[5] = self.bus_d16[5]
        self.registers[7].bus_d16[6] = self.bus_d16[6]
        self.registers[7].bus_d16[7] = self.bus_d16[7]
        self.registers[7].bus_d16[8] = self.bus_d16[8]
        self.registers[7].bus_d16[9] = self.bus_d16[9]
        self.registers[7].bus_d16[10] = self.bus_d16[10]
        self.registers[7].bus_d16[11] = self.bus_d16[11]
        self.registers[7].bus_d16[12] = self.bus_d16[12]
        self.registers[7].bus_d16[13] = self.bus_d16[13]
        self.registers[7].bus_d16[14] = self.bus_d16[14]
        self.registers[7].bus_d16[15] = self.bus_d16[15]


        # Load output of DMUX to load pin of each register:
        self.registers[0].pin_load = self.dmux8.pin_s
        self.registers[1].pin_load = self.dmux8.pin_t
        self.registers[2].pin_load = self.dmux8.pin_u
        self.registers[3].pin_load = self.dmux8.pin_v
        self.registers[4].pin_load = self.dmux8.pin_w
        self.registers[5].pin_load = self.dmux8.pin_x
        self.registers[6].pin_load = self.dmux8.pin_y
        self.registers[7].pin_load = self.dmux8.pin_z

        # Load clock pin to each register:
        self.registers[0].pin_clk = self.pin_clk
        self.registers[1].pin_clk = self.pin_clk
        self.registers[2].pin_clk = self.pin_clk
        self.registers[3].pin_clk = self.pin_clk
        self.registers[4].pin_clk = self.pin_clk
        self.registers[5].pin_clk = self.pin_clk
        self.registers[6].pin_clk = self.pin_clk
        self.registers[7].pin_clk = self.pin_clk

        # Update each register:
        self.registers[0].update()
        self.registers[1].update()
        self.registers[2].update()
        self.registers[3].update()
        self.registers[4].update()
        self.registers[5].update()
        self.registers[6].update()
        self.registers[7].update()
        
        # Load each register's output to a input line of the MUX 8 by 16:
        self.mux8_16.bus_s = self.registers[0].bus_Q16
        self.mux8_16.bus_t = self.registers[1].bus_Q16
        self.mux8_16.bus_u = self.registers[2].bus_Q16
        self.mux8_16.bus_v = self.registers[3].bus_Q16
        self.mux8_16.bus_w = self.registers[4].bus_Q16
        self.mux8_16.bus_x = self.registers[5].bus_Q16
        self.mux8_16.bus_y = self.registers[6].bus_Q16
        self.mux8_16.bus_z = self.registers[7].bus_Q16
        
        # Load address lines to the MUX 8 by 16:
        self.mux8_16.pin_sel0 = self.bus_address3[0]
        self.mux8_16.pin_sel1 = self.bus_address3[1]
        self.mux8_16.pin_sel2 = self.bus_address3[2]

        # Update the MUX 8 by 16:
        self.mux8_16.update()

        # Output of Mux 8 by 16 is now output of this chip.
        self.bus_Q16[0] = self.mux8_16.bus_x[0]
        self.bus_Q16[1] = self.mux8_16.bus_x[1]
        self.bus_Q16[2] = self.mux8_16.bus_x[2]
        self.bus_Q16[3] = self.mux8_16.bus_x[3]
        self.bus_Q16[4] = self.mux8_16.bus_x[4]
        self.bus_Q16[5] = self.mux8_16.bus_x[5]
        self.bus_Q16[6] = self.mux8_16.bus_x[6]
        self.bus_Q16[7] = self.mux8_16.bus_x[7]
        self.bus_Q16[8] = self.mux8_16.bus_x[8]
        self.bus_Q16[9] = self.mux8_16.bus_x[9]
        self.bus_Q16[10] = self.mux8_16.bus_x[10]
        self.bus_Q16[11] = self.mux8_16.bus_x[11]
        self.bus_Q16[12] = self.mux8_16.bus_x[12]
        self.bus_Q16[13] = self.mux8_16.bus_x[13]
        self.bus_Q16[14] = self.mux8_16.bus_x[14]
        self.bus_Q16[15] = self.mux8_16.bus_x[15]



class RAM64:
    def __init__(self):
        self.bus_d16 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.bus_address6 = [0, 0, 0, 0, 0, 0]
        self.pin_load = 0
        self.pin_clk = 0
        self.bus_Q16 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.ram8s = [RAM8(), RAM8(), RAM8(), RAM8(), RAM8(), RAM8(), RAM8(), RAM8()]
        self.dmux8 = lg.DMux8Way()
        self.mux8_16 = lg.Mux8Way16()

    def update(self):
        self.dmux8.pin_a = self.pin_load
        self.dmux8.pin_sel0 = self.bus_address6[0]
        self.dmux8.pin_sel1 = self.bus_address6[1]
        self.dmux8.pin_sel2 = self.bus_address6[2]
        self.dmux8.update()
        
        # Load each RAM8 with input data bus:
        self.ram8s[0].bus_d16[0] = self.bus_d16[0]
        self.ram8s[0].bus_d16[1] = self.bus_d16[1]
        self.ram8s[0].bus_d16[2] = self.bus_d16[2]
        self.ram8s[0].bus_d16[3] = self.bus_d16[3]
        self.ram8s[0].bus_d16[4] = self.bus_d16[4]
        self.ram8s[0].bus_d16[5] = self.bus_d16[5]
        self.ram8s[0].bus_d16[6] = self.bus_d16[6]
        self.ram8s[0].bus_d16[7] = self.bus_d16[7]
        self.ram8s[0].bus_d16[8] = self.bus_d16[8]
        self.ram8s[0].bus_d16[9] = self.bus_d16[9]
        self.ram8s[0].bus_d16[10] = self.bus_d16[10]
        self.ram8s[0].bus_d16[11] = self.bus_d16[11]
        self.ram8s[0].bus_d16[12] = self.bus_d16[12]
        self.ram8s[0].bus_d16[13] = self.bus_d16[13]
        self.ram8s[0].bus_d16[14] = self.bus_d16[14]
        self.ram8s[0].bus_d16[15] = self.bus_d16[15]

        self.ram8s[1].bus_d16[0] = self.bus_d16[0]
        self.ram8s[1].bus_d16[1] = self.bus_d16[1]
        self.ram8s[1].bus_d16[2] = self.bus_d16[2]
        self.ram8s[1].bus_d16[3] = self.bus_d16[3]
        self.ram8s[1].bus_d16[4] = self.bus_d16[4]
        self.ram8s[1].bus_d16[5] = self.bus_d16[5]
        self.ram8s[1].bus_d16[6] = self.bus_d16[6]
        self.ram8s[1].bus_d16[7] = self.bus_d16[7]
        self.ram8s[1].bus_d16[8] = self.bus_d16[8]
        self.ram8s[1].bus_d16[9] = self.bus_d16[9]
        self.ram8s[1].bus_d16[10] = self.bus_d16[10]
        self.ram8s[1].bus_d16[11] = self.bus_d16[11]
        self.ram8s[1].bus_d16[12] = self.bus_d16[12]
        self.ram8s[1].bus_d16[13] = self.bus_d16[13]
        self.ram8s[1].bus_d16[14] = self.bus_d16[14]
        self.ram8s[1].bus_d16[15] = self.bus_d16[15]

        self.ram8s[2].bus_d16[0] = self.bus_d16[0]
        self.ram8s[2].bus_d16[1] = self.bus_d16[1]
        self.ram8s[2].bus_d16[2] = self.bus_d16[2]
        self.ram8s[2].bus_d16[3] = self.bus_d16[3]
        self.ram8s[2].bus_d16[4] = self.bus_d16[4]
        self.ram8s[2].bus_d16[5] = self.bus_d16[5]
        self.ram8s[2].bus_d16[6] = self.bus_d16[6]
        self.ram8s[2].bus_d16[7] = self.bus_d16[7]
        self.ram8s[2].bus_d16[8] = self.bus_d16[8]
        self.ram8s[2].bus_d16[9] = self.bus_d16[9]
        self.ram8s[2].bus_d16[10] = self.bus_d16[10]
        self.ram8s[2].bus_d16[11] = self.bus_d16[11]
        self.ram8s[2].bus_d16[12] = self.bus_d16[12]
        self.ram8s[2].bus_d16[13] = self.bus_d16[13]
        self.ram8s[2].bus_d16[14] = self.bus_d16[14]
        self.ram8s[2].bus_d16[15] = self.bus_d16[15]

        self.ram8s[3].bus_d16[0] = self.bus_d16[0]
        self.ram8s[3].bus_d16[1] = self.bus_d16[1]
        self.ram8s[3].bus_d16[2] = self.bus_d16[2]
        self.ram8s[3].bus_d16[3] = self.bus_d16[3]
        self.ram8s[3].bus_d16[4] = self.bus_d16[4]
        self.ram8s[3].bus_d16[5] = self.bus_d16[5]
        self.ram8s[3].bus_d16[6] = self.bus_d16[6]
        self.ram8s[3].bus_d16[7] = self.bus_d16[7]
        self.ram8s[3].bus_d16[8] = self.bus_d16[8]
        self.ram8s[3].bus_d16[9] = self.bus_d16[9]
        self.ram8s[3].bus_d16[10] = self.bus_d16[10]
        self.ram8s[3].bus_d16[11] = self.bus_d16[11]
        self.ram8s[3].bus_d16[12] = self.bus_d16[12]
        self.ram8s[3].bus_d16[13] = self.bus_d16[13]
        self.ram8s[3].bus_d16[14] = self.bus_d16[14]
        self.ram8s[3].bus_d16[15] = self.bus_d16[15]

        self.ram8s[4].bus_d16[0] = self.bus_d16[0]
        self.ram8s[4].bus_d16[1] = self.bus_d16[1]
        self.ram8s[4].bus_d16[2] = self.bus_d16[2]
        self.ram8s[4].bus_d16[3] = self.bus_d16[3]
        self.ram8s[4].bus_d16[4] = self.bus_d16[4]
        self.ram8s[4].bus_d16[5] = self.bus_d16[5]
        self.ram8s[4].bus_d16[6] = self.bus_d16[6]
        self.ram8s[4].bus_d16[7] = self.bus_d16[7]
        self.ram8s[4].bus_d16[8] = self.bus_d16[8]
        self.ram8s[4].bus_d16[9] = self.bus_d16[9]
        self.ram8s[4].bus_d16[10] = self.bus_d16[10]
        self.ram8s[4].bus_d16[11] = self.bus_d16[11]
        self.ram8s[4].bus_d16[12] = self.bus_d16[12]
        self.ram8s[4].bus_d16[13] = self.bus_d16[13]
        self.ram8s[4].bus_d16[14] = self.bus_d16[14]
        self.ram8s[4].bus_d16[15] = self.bus_d16[15]

        self.ram8s[5].bus_d16[0] = self.bus_d16[0]
        self.ram8s[5].bus_d16[1] = self.bus_d16[1]
        self.ram8s[5].bus_d16[2] = self.bus_d16[2]
        self.ram8s[5].bus_d16[3] = self.bus_d16[3]
        self.ram8s[5].bus_d16[4] = self.bus_d16[4]
        self.ram8s[5].bus_d16[5] = self.bus_d16[5]
        self.ram8s[5].bus_d16[6] = self.bus_d16[6]
        self.ram8s[5].bus_d16[7] = self.bus_d16[7]
        self.ram8s[5].bus_d16[8] = self.bus_d16[8]
        self.ram8s[5].bus_d16[9] = self.bus_d16[9]
        self.ram8s[5].bus_d16[10] = self.bus_d16[10]
        self.ram8s[5].bus_d16[11] = self.bus_d16[11]
        self.ram8s[5].bus_d16[12] = self.bus_d16[12]
        self.ram8s[5].bus_d16[13] = self.bus_d16[13]
        self.ram8s[5].bus_d16[14] = self.bus_d16[14]
        self.ram8s[5].bus_d16[15] = self.bus_d16[15]

        self.ram8s[6].bus_d16[0] = self.bus_d16[0]
        self.ram8s[6].bus_d16[1] = self.bus_d16[1]
        self.ram8s[6].bus_d16[2] = self.bus_d16[2]
        self.ram8s[6].bus_d16[3] = self.bus_d16[3]
        self.ram8s[6].bus_d16[4] = self.bus_d16[4]
        self.ram8s[6].bus_d16[5] = self.bus_d16[5]
        self.ram8s[6].bus_d16[6] = self.bus_d16[6]
        self.ram8s[6].bus_d16[7] = self.bus_d16[7]
        self.ram8s[6].bus_d16[8] = self.bus_d16[8]
        self.ram8s[6].bus_d16[9] = self.bus_d16[9]
        self.ram8s[6].bus_d16[10] = self.bus_d16[10]
        self.ram8s[6].bus_d16[11] = self.bus_d16[11]
        self.ram8s[6].bus_d16[12] = self.bus_d16[12]
        self.ram8s[6].bus_d16[13] = self.bus_d16[13]
        self.ram8s[6].bus_d16[14] = self.bus_d16[14]
        self.ram8s[6].bus_d16[15] = self.bus_d16[15]

        self.ram8s[7].bus_d16[0] = self.bus_d16[0]
        self.ram8s[7].bus_d16[1] = self.bus_d16[1]
        self.ram8s[7].bus_d16[2] = self.bus_d16[2]
        self.ram8s[7].bus_d16[3] = self.bus_d16[3]
        self.ram8s[7].bus_d16[4] = self.bus_d16[4]
        self.ram8s[7].bus_d16[5] = self.bus_d16[5]
        self.ram8s[7].bus_d16[6] = self.bus_d16[6]
        self.ram8s[7].bus_d16[7] = self.bus_d16[7]
        self.ram8s[7].bus_d16[8] = self.bus_d16[8]
        self.ram8s[7].bus_d16[9] = self.bus_d16[9]
        self.ram8s[7].bus_d16[10] = self.bus_d16[10]
        self.ram8s[7].bus_d16[11] = self.bus_d16[11]
        self.ram8s[7].bus_d16[12] = self.bus_d16[12]
        self.ram8s[7].bus_d16[13] = self.bus_d16[13]
        self.ram8s[7].bus_d16[14] = self.bus_d16[14]
        self.ram8s[7].bus_d16[15] = self.bus_d16[15]

        # Load the load bits for each RAM8 with the output of the dmux8:
        self.ram8s[0].load = self.dmux8.pin_s
        self.ram8s[1].load = self.dmux8.pin_t
        self.ram8s[2].load = self.dmux8.pin_u
        self.ram8s[3].load = self.dmux8.pin_v
        self.ram8s[4].load = self.dmux8.pin_w
        self.ram8s[5].load = self.dmux8.pin_x
        self.ram8s[6].load = self.dmux8.pin_y
        self.ram8s[7].load = self.dmux8.pin_z

        # Load the clock bits for each RAM8:
        self.ram8s[0].pin_clk = self.pin_clk
        self.ram8s[1].pin_clk = self.pin_clk
        self.ram8s[2].pin_clk = self.pin_clk
        self.ram8s[3].pin_clk = self.pin_clk
        self.ram8s[4].pin_clk = self.pin_clk
        self.ram8s[5].pin_clk = self.pin_clk
        self.ram8s[6].pin_clk = self.pin_clk
        self.ram8s[7].pin_clk = self.pin_clk

        # Load the address bits for each RAM8:
        self.ram8s[0].bus_address3[0] = self.bus_address6[3]
        self.ram8s[0].bus_address3[1] = self.bus_address6[4]
        self.ram8s[0].bus_address3[2] = self.bus_address6[5]

        self.ram8s[1].bus_address3[0] = self.bus_address6[3]
        self.ram8s[1].bus_address3[1] = self.bus_address6[4]
        self.ram8s[1].bus_address3[2] = self.bus_address6[5]

        self.ram8s[2].bus_address3[0] = self.bus_address6[3]
        self.ram8s[2].bus_address3[1] = self.bus_address6[4]
        self.ram8s[2].bus_address3[2] = self.bus_address6[5]

        self.ram8s[3].bus_address3[0] = self.bus_address6[3]
        self.ram8s[3].bus_address3[1] = self.bus_address6[4]
        self.ram8s[3].bus_address3[2] = self.bus_address6[5]

        self.ram8s[4].bus_address3[0] = self.bus_address6[3]
        self.ram8s[4].bus_address3[1] = self.bus_address6[4]
        self.ram8s[4].bus_address3[2] = self.bus_address6[5]

        self.ram8s[5].bus_address3[0] = self.bus_address6[3]
        self.ram8s[5].bus_address3[1] = self.bus_address6[4]
        self.ram8s[5].bus_address3[2] = self.bus_address6[5]

        self.ram8s[6].bus_address3[0] = self.bus_address6[3]
        self.ram8s[6].bus_address3[1] = self.bus_address6[4]
        self.ram8s[6].bus_address3[2] = self.bus_address6[5]

        self.ram8s[7].bus_address3[0] = self.bus_address6[3]
        self.ram8s[7].bus_address3[1] = self.bus_address6[4]
        self.ram8s[7].bus_address3[2] = self.bus_address6[5]

        # Update each RAM8:
        self.ram8s[0].update()
        self.ram8s[1].update()
        self.ram8s[2].update()
        self.ram8s[3].update()
        self.ram8s[4].update()
        self.ram8s[5].update()
        self.ram8s[6].update()
        self.ram8s[7].update()

        # Load the output of each RAM8 into the input busses of Mux8Way16:
        self.mux8_16.bus_a[0] = self.ram8s[0].bus_Q16[0]
        self.mux8_16.bus_a[1] = self.ram8s[0].bus_Q16[1]
        self.mux8_16.bus_a[2] = self.ram8s[0].bus_Q16[2]
        self.mux8_16.bus_a[3] = self.ram8s[0].bus_Q16[3]
        self.mux8_16.bus_a[4] = self.ram8s[0].bus_Q16[4]
        self.mux8_16.bus_a[5] = self.ram8s[0].bus_Q16[5]
        self.mux8_16.bus_a[6] = self.ram8s[0].bus_Q16[6]
        self.mux8_16.bus_a[7] = self.ram8s[0].bus_Q16[7]
        self.mux8_16.bus_a[8] = self.ram8s[0].bus_Q16[8]
        self.mux8_16.bus_a[9] = self.ram8s[0].bus_Q16[9]
        self.mux8_16.bus_a[10] = self.ram8s[0].bus_Q16[10]
        self.mux8_16.bus_a[11] = self.ram8s[0].bus_Q16[11]
        self.mux8_16.bus_a[12] = self.ram8s[0].bus_Q16[12]
        self.mux8_16.bus_a[13] = self.ram8s[0].bus_Q16[13]
        self.mux8_16.bus_a[14] = self.ram8s[0].bus_Q16[14]
        self.mux8_16.bus_a[15] = self.ram8s[0].bus_Q16[15]

        self.mux8_16.bus_b[0] = self.ram8s[1].bus_Q16[0]
        self.mux8_16.bus_b[1] = self.ram8s[1].bus_Q16[1]
        self.mux8_16.bus_b[2] = self.ram8s[1].bus_Q16[2]
        self.mux8_16.bus_b[3] = self.ram8s[1].bus_Q16[3]
        self.mux8_16.bus_b[4] = self.ram8s[1].bus_Q16[4]
        self.mux8_16.bus_b[5] = self.ram8s[1].bus_Q16[5]
        self.mux8_16.bus_b[6] = self.ram8s[1].bus_Q16[6]
        self.mux8_16.bus_b[7] = self.ram8s[1].bus_Q16[7]
        self.mux8_16.bus_b[8] = self.ram8s[1].bus_Q16[8]
        self.mux8_16.bus_b[9] = self.ram8s[1].bus_Q16[9]
        self.mux8_16.bus_b[10] = self.ram8s[1].bus_Q16[10]
        self.mux8_16.bus_b[11] = self.ram8s[1].bus_Q16[11]
        self.mux8_16.bus_b[12] = self.ram8s[1].bus_Q16[12]
        self.mux8_16.bus_b[13] = self.ram8s[1].bus_Q16[13]
        self.mux8_16.bus_b[14] = self.ram8s[1].bus_Q16[14]
        self.mux8_16.bus_b[15] = self.ram8s[1].bus_Q16[15]

        self.mux8_16.bus_c[0] = self.ram8s[2].bus_Q16[0]
        self.mux8_16.bus_c[1] = self.ram8s[2].bus_Q16[1]
        self.mux8_16.bus_c[2] = self.ram8s[2].bus_Q16[2]
        self.mux8_16.bus_c[3] = self.ram8s[2].bus_Q16[3]
        self.mux8_16.bus_c[4] = self.ram8s[2].bus_Q16[4]
        self.mux8_16.bus_c[5] = self.ram8s[2].bus_Q16[5]
        self.mux8_16.bus_c[6] = self.ram8s[2].bus_Q16[6]
        self.mux8_16.bus_c[7] = self.ram8s[2].bus_Q16[7]
        self.mux8_16.bus_c[8] = self.ram8s[2].bus_Q16[8]
        self.mux8_16.bus_c[9] = self.ram8s[2].bus_Q16[9]
        self.mux8_16.bus_c[10] = self.ram8s[2].bus_Q16[10]
        self.mux8_16.bus_c[11] = self.ram8s[2].bus_Q16[11]
        self.mux8_16.bus_c[12] = self.ram8s[2].bus_Q16[12]
        self.mux8_16.bus_c[13] = self.ram8s[2].bus_Q16[13]
        self.mux8_16.bus_c[14] = self.ram8s[2].bus_Q16[14]
        self.mux8_16.bus_c[15] = self.ram8s[2].bus_Q16[15]

        self.mux8_16.bus_d[0] = self.ram8s[3].bus_Q16[0]
        self.mux8_16.bus_d[1] = self.ram8s[3].bus_Q16[1]
        self.mux8_16.bus_d[2] = self.ram8s[3].bus_Q16[2]
        self.mux8_16.bus_d[3] = self.ram8s[3].bus_Q16[3]
        self.mux8_16.bus_d[4] = self.ram8s[3].bus_Q16[4]
        self.mux8_16.bus_d[5] = self.ram8s[3].bus_Q16[5]
        self.mux8_16.bus_d[6] = self.ram8s[3].bus_Q16[6]
        self.mux8_16.bus_d[7] = self.ram8s[3].bus_Q16[7]
        self.mux8_16.bus_d[8] = self.ram8s[3].bus_Q16[8]
        self.mux8_16.bus_d[9] = self.ram8s[3].bus_Q16[9]
        self.mux8_16.bus_d[10] = self.ram8s[3].bus_Q16[10]
        self.mux8_16.bus_d[11] = self.ram8s[3].bus_Q16[11]
        self.mux8_16.bus_d[12] = self.ram8s[3].bus_Q16[12]
        self.mux8_16.bus_d[13] = self.ram8s[3].bus_Q16[13]
        self.mux8_16.bus_d[14] = self.ram8s[3].bus_Q16[14]
        self.mux8_16.bus_d[15] = self.ram8s[3].bus_Q16[15]

        self.mux8_16.bus_e[0] = self.ram8s[4].bus_Q16[0]
        self.mux8_16.bus_e[1] = self.ram8s[4].bus_Q16[1]
        self.mux8_16.bus_e[2] = self.ram8s[4].bus_Q16[2]
        self.mux8_16.bus_e[3] = self.ram8s[4].bus_Q16[3]
        self.mux8_16.bus_e[4] = self.ram8s[4].bus_Q16[4]
        self.mux8_16.bus_e[5] = self.ram8s[4].bus_Q16[5]
        self.mux8_16.bus_e[6] = self.ram8s[4].bus_Q16[6]
        self.mux8_16.bus_e[7] = self.ram8s[4].bus_Q16[7]
        self.mux8_16.bus_e[8] = self.ram8s[4].bus_Q16[8]
        self.mux8_16.bus_e[9] = self.ram8s[4].bus_Q16[9]
        self.mux8_16.bus_e[10] = self.ram8s[4].bus_Q16[10]
        self.mux8_16.bus_e[11] = self.ram8s[4].bus_Q16[11]
        self.mux8_16.bus_e[12] = self.ram8s[4].bus_Q16[12]
        self.mux8_16.bus_e[13] = self.ram8s[4].bus_Q16[13]
        self.mux8_16.bus_e[14] = self.ram8s[4].bus_Q16[14]
        self.mux8_16.bus_e[15] = self.ram8s[4].bus_Q16[15]

        self.mux8_16.bus_f[0] = self.ram8s[5].bus_Q16[0]
        self.mux8_16.bus_f[1] = self.ram8s[5].bus_Q16[1]
        self.mux8_16.bus_f[2] = self.ram8s[5].bus_Q16[2]
        self.mux8_16.bus_f[3] = self.ram8s[5].bus_Q16[3]
        self.mux8_16.bus_f[4] = self.ram8s[5].bus_Q16[4]
        self.mux8_16.bus_f[5] = self.ram8s[5].bus_Q16[5]
        self.mux8_16.bus_f[6] = self.ram8s[5].bus_Q16[6]
        self.mux8_16.bus_f[7] = self.ram8s[5].bus_Q16[7]
        self.mux8_16.bus_f[8] = self.ram8s[5].bus_Q16[8]
        self.mux8_16.bus_f[9] = self.ram8s[5].bus_Q16[9]
        self.mux8_16.bus_f[10] = self.ram8s[5].bus_Q16[10]
        self.mux8_16.bus_f[11] = self.ram8s[5].bus_Q16[11]
        self.mux8_16.bus_f[12] = self.ram8s[5].bus_Q16[12]
        self.mux8_16.bus_f[13] = self.ram8s[5].bus_Q16[13]
        self.mux8_16.bus_f[14] = self.ram8s[5].bus_Q16[14]
        self.mux8_16.bus_f[15] = self.ram8s[5].bus_Q16[15]

        self.mux8_16.bus_g[0] = self.ram8s[6].bus_Q16[0]
        self.mux8_16.bus_g[1] = self.ram8s[6].bus_Q16[1]
        self.mux8_16.bus_g[2] = self.ram8s[6].bus_Q16[2]
        self.mux8_16.bus_g[3] = self.ram8s[6].bus_Q16[3]
        self.mux8_16.bus_g[4] = self.ram8s[6].bus_Q16[4]
        self.mux8_16.bus_g[5] = self.ram8s[6].bus_Q16[5]
        self.mux8_16.bus_g[6] = self.ram8s[6].bus_Q16[6]
        self.mux8_16.bus_g[7] = self.ram8s[6].bus_Q16[7]
        self.mux8_16.bus_g[8] = self.ram8s[6].bus_Q16[8]
        self.mux8_16.bus_g[9] = self.ram8s[6].bus_Q16[9]
        self.mux8_16.bus_g[10] = self.ram8s[6].bus_Q16[10]
        self.mux8_16.bus_g[11] = self.ram8s[6].bus_Q16[11]
        self.mux8_16.bus_g[12] = self.ram8s[6].bus_Q16[12]
        self.mux8_16.bus_g[13] = self.ram8s[6].bus_Q16[13]
        self.mux8_16.bus_g[14] = self.ram8s[6].bus_Q16[14]
        self.mux8_16.bus_g[15] = self.ram8s[6].bus_Q16[15]

        self.mux8_16.bus_h[0] = self.ram8s[7].bus_Q16[0]
        self.mux8_16.bus_h[1] = self.ram8s[7].bus_Q16[1]
        self.mux8_16.bus_h[2] = self.ram8s[7].bus_Q16[2]
        self.mux8_16.bus_h[3] = self.ram8s[7].bus_Q16[3]
        self.mux8_16.bus_h[4] = self.ram8s[7].bus_Q16[4]
        self.mux8_16.bus_h[5] = self.ram8s[7].bus_Q16[5]
        self.mux8_16.bus_h[6] = self.ram8s[7].bus_Q16[6]
        self.mux8_16.bus_h[7] = self.ram8s[7].bus_Q16[7]
        self.mux8_16.bus_h[8] = self.ram8s[7].bus_Q16[8]
        self.mux8_16.bus_h[9] = self.ram8s[7].bus_Q16[9]
        self.mux8_16.bus_h[10] = self.ram8s[7].bus_Q16[10]
        self.mux8_16.bus_h[11] = self.ram8s[7].bus_Q16[11]
        self.mux8_16.bus_h[12] = self.ram8s[7].bus_Q16[12]
        self.mux8_16.bus_h[13] = self.ram8s[7].bus_Q16[13]
        self.mux8_16.bus_h[14] = self.ram8s[7].bus_Q16[14]
        self.mux8_16.bus_h[15] = self.ram8s[7].bus_Q16[15]

        # Put first 3 address lines on the mux8_16
        self.mux8_16.pin_sel0 = self.bus_address6[0]
        self.mux8_16.pin_sel1 = self.bus_address6[1]
        self.mux8_16.pin_sel2 = self.bus_address6[2]

        # Update the mux8_16
        self.mux8_16.update()

        # Copy output from mux8_16 to the output bus
        self.bus_Q16[0] = self.mux8_16.bus_x[0]
        self.bus_Q16[1] = self.mux8_16.bus_x[1]
        self.bus_Q16[2] = self.mux8_16.bus_x[2]
        self.bus_Q16[3] = self.mux8_16.bus_x[3]
        self.bus_Q16[4] = self.mux8_16.bus_x[4]
        self.bus_Q16[5] = self.mux8_16.bus_x[5]
        self.bus_Q16[6] = self.mux8_16.bus_x[6]
        self.bus_Q16[7] = self.mux8_16.bus_x[7]
        self.bus_Q16[8] = self.mux8_16.bus_x[8]
        self.bus_Q16[9] = self.mux8_16.bus_x[9]
        self.bus_Q16[10] = self.mux8_16.bus_x[10]
        self.bus_Q16[11] = self.mux8_16.bus_x[11]
        self.bus_Q16[12] = self.mux8_16.bus_x[12]
        self.bus_Q16[13] = self.mux8_16.bus_x[13]
        self.bus_Q16[14] = self.mux8_16.bus_x[14]
        self.bus_Q16[15] = self.mux8_16.bus_x[15]


class RAM512:
    def __init__(self):
        self.bus_d16 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.bus_address9 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.pin_load = 0
        self.pin_clk = 0
        self.bus_Q16 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.ram64s = [RAM64(), RAM64(), RAM64(), RAM64(), RAM64(), RAM64(), RAM64(), RAM64()]
        self.dmux8 = lg.DMux8Way()
        self.mux8_16 = lg.Mux8Way16()

    def update(self):
        # Set load pin through dmux8, so first 3 address bits will select 
        # 1 of 8 RAM64s to load (if any)
        self.dmux8.pin_a = self.pin_load
        self.dmux8.pin_sel0 = self.bus_address9[0]
        self.dmux8.pin_sel1 = self.bus_address9[1]
        self.dmux8.pin_sel2 = self.bus_address9[2]
        self.dmux8.update()

        # Load input bus of each RAM64 with the input bus
        self.ram64s[0].bus_d16[0] = self.bus_d16[0]
        self.ram64s[0].bus_d16[1] = self.bus_d16[1]
        self.ram64s[0].bus_d16[2] = self.bus_d16[2]
        self.ram64s[0].bus_d16[3] = self.bus_d16[3]
        self.ram64s[0].bus_d16[4] = self.bus_d16[4]
        self.ram64s[0].bus_d16[5] = self.bus_d16[5]
        self.ram64s[0].bus_d16[6] = self.bus_d16[6]
        self.ram64s[0].bus_d16[7] = self.bus_d16[7]
        self.ram64s[0].bus_d16[8] = self.bus_d16[8]
        self.ram64s[0].bus_d16[9] = self.bus_d16[9]
        self.ram64s[0].bus_d16[10] = self.bus_d16[10]
        self.ram64s[0].bus_d16[11] = self.bus_d16[11]
        self.ram64s[0].bus_d16[12] = self.bus_d16[12]
        self.ram64s[0].bus_d16[13] = self.bus_d16[13]
        self.ram64s[0].bus_d16[14] = self.bus_d16[14]
        self.ram64s[0].bus_d16[15] = self.bus_d16[15]

        self.ram64s[1].bus_d16[0] = self.bus_d16[0]
        self.ram64s[1].bus_d16[1] = self.bus_d16[1]
        self.ram64s[1].bus_d16[2] = self.bus_d16[2]
        self.ram64s[1].bus_d16[3] = self.bus_d16[3]
        self.ram64s[1].bus_d16[4] = self.bus_d16[4]
        self.ram64s[1].bus_d16[5] = self.bus_d16[5]
        self.ram64s[1].bus_d16[6] = self.bus_d16[6]
        self.ram64s[1].bus_d16[7] = self.bus_d16[7]
        self.ram64s[1].bus_d16[8] = self.bus_d16[8]
        self.ram64s[1].bus_d16[9] = self.bus_d16[9]
        self.ram64s[1].bus_d16[10] = self.bus_d16[10]
        self.ram64s[1].bus_d16[11] = self.bus_d16[11]
        self.ram64s[1].bus_d16[12] = self.bus_d16[12]
        self.ram64s[1].bus_d16[13] = self.bus_d16[13]
        self.ram64s[1].bus_d16[14] = self.bus_d16[14]
        self.ram64s[1].bus_d16[15] = self.bus_d16[15]

        self.ram64s[2].bus_d16[0] = self.bus_d16[0]
        self.ram64s[2].bus_d16[1] = self.bus_d16[1]
        self.ram64s[2].bus_d16[2] = self.bus_d16[2]
        self.ram64s[2].bus_d16[3] = self.bus_d16[3]
        self.ram64s[2].bus_d16[4] = self.bus_d16[4]
        self.ram64s[2].bus_d16[5] = self.bus_d16[5]
        self.ram64s[2].bus_d16[6] = self.bus_d16[6]
        self.ram64s[2].bus_d16[7] = self.bus_d16[7]
        self.ram64s[2].bus_d16[8] = self.bus_d16[8]
        self.ram64s[2].bus_d16[9] = self.bus_d16[9]
        self.ram64s[2].bus_d16[10] = self.bus_d16[10]
        self.ram64s[2].bus_d16[11] = self.bus_d16[11]
        self.ram64s[2].bus_d16[12] = self.bus_d16[12]
        self.ram64s[2].bus_d16[13] = self.bus_d16[13]
        self.ram64s[2].bus_d16[14] = self.bus_d16[14]
        self.ram64s[2].bus_d16[15] = self.bus_d16[15]

        self.ram64s[3].bus_d16[0] = self.bus_d16[0]
        self.ram64s[3].bus_d16[1] = self.bus_d16[1]
        self.ram64s[3].bus_d16[2] = self.bus_d16[2]
        self.ram64s[3].bus_d16[3] = self.bus_d16[3]
        self.ram64s[3].bus_d16[4] = self.bus_d16[4]
        self.ram64s[3].bus_d16[5] = self.bus_d16[5]
        self.ram64s[3].bus_d16[6] = self.bus_d16[6]
        self.ram64s[3].bus_d16[7] = self.bus_d16[7]
        self.ram64s[3].bus_d16[8] = self.bus_d16[8]
        self.ram64s[3].bus_d16[9] = self.bus_d16[9]
        self.ram64s[3].bus_d16[10] = self.bus_d16[10]
        self.ram64s[3].bus_d16[11] = self.bus_d16[11]
        self.ram64s[3].bus_d16[12] = self.bus_d16[12]
        self.ram64s[3].bus_d16[13] = self.bus_d16[13]
        self.ram64s[3].bus_d16[14] = self.bus_d16[14]
        self.ram64s[3].bus_d16[15] = self.bus_d16[15]

        self.ram64s[4].bus_d16[0] = self.bus_d16[0]
        self.ram64s[4].bus_d16[1] = self.bus_d16[1]
        self.ram64s[4].bus_d16[2] = self.bus_d16[2]
        self.ram64s[4].bus_d16[3] = self.bus_d16[3]
        self.ram64s[4].bus_d16[4] = self.bus_d16[4]
        self.ram64s[4].bus_d16[5] = self.bus_d16[5]
        self.ram64s[4].bus_d16[6] = self.bus_d16[6]
        self.ram64s[4].bus_d16[7] = self.bus_d16[7]
        self.ram64s[4].bus_d16[8] = self.bus_d16[8]
        self.ram64s[4].bus_d16[9] = self.bus_d16[9]
        self.ram64s[4].bus_d16[10] = self.bus_d16[10]
        self.ram64s[4].bus_d16[11] = self.bus_d16[11]
        self.ram64s[4].bus_d16[12] = self.bus_d16[12]
        self.ram64s[4].bus_d16[13] = self.bus_d16[13]
        self.ram64s[4].bus_d16[14] = self.bus_d16[14]
        self.ram64s[4].bus_d16[15] = self.bus_d16[15]

        self.ram64s[5].bus_d16[0] = self.bus_d16[0]
        self.ram64s[5].bus_d16[1] = self.bus_d16[1]
        self.ram64s[5].bus_d16[2] = self.bus_d16[2]
        self.ram64s[5].bus_d16[3] = self.bus_d16[3]
        self.ram64s[5].bus_d16[4] = self.bus_d16[4]
        self.ram64s[5].bus_d16[5] = self.bus_d16[5]
        self.ram64s[5].bus_d16[6] = self.bus_d16[6]
        self.ram64s[5].bus_d16[7] = self.bus_d16[7]
        self.ram64s[5].bus_d16[8] = self.bus_d16[8]
        self.ram64s[5].bus_d16[9] = self.bus_d16[9]
        self.ram64s[5].bus_d16[10] = self.bus_d16[10]
        self.ram64s[5].bus_d16[11] = self.bus_d16[11]
        self.ram64s[5].bus_d16[12] = self.bus_d16[12]
        self.ram64s[5].bus_d16[13] = self.bus_d16[13]
        self.ram64s[5].bus_d16[14] = self.bus_d16[14]
        self.ram64s[5].bus_d16[15] = self.bus_d16[15]

        self.ram64s[6].bus_d16[0] = self.bus_d16[0]
        self.ram64s[6].bus_d16[1] = self.bus_d16[1]
        self.ram64s[6].bus_d16[2] = self.bus_d16[2]
        self.ram64s[6].bus_d16[3] = self.bus_d16[3]
        self.ram64s[6].bus_d16[4] = self.bus_d16[4]
        self.ram64s[6].bus_d16[5] = self.bus_d16[5]
        self.ram64s[6].bus_d16[6] = self.bus_d16[6]
        self.ram64s[6].bus_d16[7] = self.bus_d16[7]
        self.ram64s[6].bus_d16[8] = self.bus_d16[8]
        self.ram64s[6].bus_d16[9] = self.bus_d16[9]
        self.ram64s[6].bus_d16[10] = self.bus_d16[10]
        self.ram64s[6].bus_d16[11] = self.bus_d16[11]
        self.ram64s[6].bus_d16[12] = self.bus_d16[12]
        self.ram64s[6].bus_d16[13] = self.bus_d16[13]
        self.ram64s[6].bus_d16[14] = self.bus_d16[14]
        self.ram64s[6].bus_d16[15] = self.bus_d16[15]

        self.ram64s[7].bus_d16[0] = self.bus_d16[0]
        self.ram64s[7].bus_d16[1] = self.bus_d16[1]
        self.ram64s[7].bus_d16[2] = self.bus_d16[2]
        self.ram64s[7].bus_d16[3] = self.bus_d16[3]
        self.ram64s[7].bus_d16[4] = self.bus_d16[4]
        self.ram64s[7].bus_d16[5] = self.bus_d16[5]
        self.ram64s[7].bus_d16[6] = self.bus_d16[6]
        self.ram64s[7].bus_d16[7] = self.bus_d16[7]
        self.ram64s[7].bus_d16[8] = self.bus_d16[8]
        self.ram64s[7].bus_d16[9] = self.bus_d16[9]
        self.ram64s[7].bus_d16[10] = self.bus_d16[10]
        self.ram64s[7].bus_d16[11] = self.bus_d16[11]
        self.ram64s[7].bus_d16[12] = self.bus_d16[12]
        self.ram64s[7].bus_d16[13] = self.bus_d16[13]
        self.ram64s[7].bus_d16[14] = self.bus_d16[14]
        self.ram64s[7].bus_d16[15] = self.bus_d16[15]

        # Set load bit of each RAM64 to the corresponding output of dmux:
        self.ram64s[0].pin_load = self.dmux8.pin_s 
        self.ram64s[1].pin_load = self.dmux8.pin_t 
        self.ram64s[2].pin_load = self.dmux8.pin_u
        self.ram64s[3].pin_load = self.dmux8.pin_v
        self.ram64s[4].pin_load = self.dmux8.pin_w
        self.ram64s[5].pin_load = self.dmux8.pin_x
        self.ram64s[6].pin_load = self.dmux8.pin_y
        self.ram64s[7].pin_load = self.dmux8.pin_z

        # Load the clock bit to each RAM64 module:
        self.ram64s[0].pin_clk = self.pin_clk
        self.ram64s[1].pin_clk = self.pin_clk
        self.ram64s[2].pin_clk = self.pin_clk
        self.ram64s[3].pin_clk = self.pin_clk
        self.ram64s[4].pin_clk = self.pin_clk
        self.ram64s[5].pin_clk = self.pin_clk
        self.ram64s[6].pin_clk = self.pin_clk
        self.ram64s[7].pin_clk = self.pin_clk
        
        # Load the address bits to each RAM64 module:
        self.ram64s[0].bus_address6[0] = self.bus_address9[3]
        self.ram64s[0].bus_address6[1] = self.bus_address9[4]
        self.ram64s[0].bus_address6[2] = self.bus_address9[5]
        self.ram64s[0].bus_address6[3] = self.bus_address9[6]
        self.ram64s[0].bus_address6[4] = self.bus_address9[7]
        self.ram64s[0].bus_address6[5] = self.bus_address9[8]

        self.ram64s[1].bus_address6[0] = self.bus_address9[3]
        self.ram64s[1].bus_address6[1] = self.bus_address9[4]
        self.ram64s[1].bus_address6[2] = self.bus_address9[5]
        self.ram64s[1].bus_address6[3] = self.bus_address9[6]
        self.ram64s[1].bus_address6[4] = self.bus_address9[7]
        self.ram64s[1].bus_address6[5] = self.bus_address9[8]

        self.ram64s[2].bus_address6[0] = self.bus_address9[3]
        self.ram64s[2].bus_address6[1] = self.bus_address9[4]
        self.ram64s[2].bus_address6[2] = self.bus_address9[5]
        self.ram64s[2].bus_address6[3] = self.bus_address9[6]
        self.ram64s[2].bus_address6[4] = self.bus_address9[7]
        self.ram64s[2].bus_address6[5] = self.bus_address9[8]

        self.ram64s[3].bus_address6[0] = self.bus_address9[3]
        self.ram64s[3].bus_address6[1] = self.bus_address9[4]
        self.ram64s[3].bus_address6[2] = self.bus_address9[5]
        self.ram64s[3].bus_address6[3] = self.bus_address9[6]
        self.ram64s[3].bus_address6[4] = self.bus_address9[7]
        self.ram64s[3].bus_address6[5] = self.bus_address9[8]
        
        self.ram64s[4].bus_address6[0] = self.bus_address9[3]
        self.ram64s[4].bus_address6[1] = self.bus_address9[4]
        self.ram64s[4].bus_address6[2] = self.bus_address9[5]
        self.ram64s[4].bus_address6[3] = self.bus_address9[6]
        self.ram64s[4].bus_address6[4] = self.bus_address9[7]
        self.ram64s[4].bus_address6[5] = self.bus_address9[8]

        self.ram64s[5].bus_address6[0] = self.bus_address9[3]
        self.ram64s[5].bus_address6[1] = self.bus_address9[4]
        self.ram64s[5].bus_address6[2] = self.bus_address9[5]
        self.ram64s[5].bus_address6[3] = self.bus_address9[6]
        self.ram64s[5].bus_address6[4] = self.bus_address9[7]
        self.ram64s[5].bus_address6[5] = self.bus_address9[8]

        self.ram64s[6].bus_address6[0] = self.bus_address9[3]
        self.ram64s[6].bus_address6[1] = self.bus_address9[4]
        self.ram64s[6].bus_address6[2] = self.bus_address9[5]
        self.ram64s[6].bus_address6[3] = self.bus_address9[6]
        self.ram64s[6].bus_address6[4] = self.bus_address9[7]
        self.ram64s[6].bus_address6[5] = self.bus_address9[8]
        
        self.ram64s[7].bus_address6[0] = self.bus_address9[3]
        self.ram64s[7].bus_address6[1] = self.bus_address9[4]
        self.ram64s[7].bus_address6[2] = self.bus_address9[5]
        self.ram64s[7].bus_address6[3] = self.bus_address9[6]
        self.ram64s[7].bus_address6[4] = self.bus_address9[7]
        self.ram64s[7].bus_address6[5] = self.bus_address9[8]

        # Update the RAM64s
        self.ram64s[0].update()
        self.ram64s[1].update()
        self.ram64s[2].update()
        self.ram64s[3].update()
        self.ram64s[4].update()
        self.ram64s[5].update()
        self.ram64s[6].update()
        self.ram64s[7].update()

        # Set input busses of mux 8 way 16 with the outputs of each RAM64
        self.mux8_16.bus_a[0] = self.ram64s[0].bus_Q16[0]
        self.mux8_16.bus_a[1] = self.ram64s[0].bus_Q16[1]
        self.mux8_16.bus_a[2] = self.ram64s[0].bus_Q16[2]
        self.mux8_16.bus_a[3] = self.ram64s[0].bus_Q16[3]
        self.mux8_16.bus_a[4] = self.ram64s[0].bus_Q16[4]
        self.mux8_16.bus_a[5] = self.ram64s[0].bus_Q16[5]
        self.mux8_16.bus_a[6] = self.ram64s[0].bus_Q16[6]
        self.mux8_16.bus_a[7] = self.ram64s[0].bus_Q16[7]
        self.mux8_16.bus_a[8] = self.ram64s[0].bus_Q16[8]
        self.mux8_16.bus_a[9] = self.ram64s[0].bus_Q16[9]
        self.mux8_16.bus_a[10] = self.ram64s[0].bus_Q16[10]
        self.mux8_16.bus_a[11] = self.ram64s[0].bus_Q16[11]
        self.mux8_16.bus_a[12] = self.ram64s[0].bus_Q16[12]
        self.mux8_16.bus_a[13] = self.ram64s[0].bus_Q16[13]
        self.mux8_16.bus_a[14] = self.ram64s[0].bus_Q16[14]
        self.mux8_16.bus_a[15] = self.ram64s[0].bus_Q16[15]

        self.mux8_16.bus_b[0] = self.ram64s[1].bus_Q16[0]
        self.mux8_16.bus_b[1] = self.ram64s[1].bus_Q16[1]
        self.mux8_16.bus_b[2] = self.ram64s[1].bus_Q16[2]
        self.mux8_16.bus_b[3] = self.ram64s[1].bus_Q16[3]
        self.mux8_16.bus_b[4] = self.ram64s[1].bus_Q16[4]
        self.mux8_16.bus_b[5] = self.ram64s[1].bus_Q16[5]
        self.mux8_16.bus_b[6] = self.ram64s[1].bus_Q16[6]
        self.mux8_16.bus_b[7] = self.ram64s[1].bus_Q16[7]
        self.mux8_16.bus_b[8] = self.ram64s[1].bus_Q16[8]
        self.mux8_16.bus_b[9] = self.ram64s[1].bus_Q16[9]
        self.mux8_16.bus_b[10] = self.ram64s[1].bus_Q16[10]
        self.mux8_16.bus_b[11] = self.ram64s[1].bus_Q16[11]
        self.mux8_16.bus_b[12] = self.ram64s[1].bus_Q16[12]
        self.mux8_16.bus_b[13] = self.ram64s[1].bus_Q16[13]
        self.mux8_16.bus_b[14] = self.ram64s[1].bus_Q16[14]
        self.mux8_16.bus_b[15] = self.ram64s[1].bus_Q16[15]

        self.mux8_16.bus_c[0] = self.ram64s[2].bus_Q16[0]
        self.mux8_16.bus_c[1] = self.ram64s[2].bus_Q16[1]
        self.mux8_16.bus_c[2] = self.ram64s[2].bus_Q16[2]
        self.mux8_16.bus_c[3] = self.ram64s[2].bus_Q16[3]
        self.mux8_16.bus_c[4] = self.ram64s[2].bus_Q16[4]
        self.mux8_16.bus_c[5] = self.ram64s[2].bus_Q16[5]
        self.mux8_16.bus_c[6] = self.ram64s[2].bus_Q16[6]
        self.mux8_16.bus_c[7] = self.ram64s[2].bus_Q16[7]
        self.mux8_16.bus_c[8] = self.ram64s[2].bus_Q16[8]
        self.mux8_16.bus_c[9] = self.ram64s[2].bus_Q16[9]
        self.mux8_16.bus_c[10] = self.ram64s[2].bus_Q16[10]
        self.mux8_16.bus_c[11] = self.ram64s[2].bus_Q16[11]
        self.mux8_16.bus_c[12] = self.ram64s[2].bus_Q16[12]
        self.mux8_16.bus_c[13] = self.ram64s[2].bus_Q16[13]
        self.mux8_16.bus_c[14] = self.ram64s[2].bus_Q16[14]
        self.mux8_16.bus_c[15] = self.ram64s[2].bus_Q16[15]

        self.mux8_16.bus_d[0] = self.ram64s[3].bus_Q16[0]
        self.mux8_16.bus_d[1] = self.ram64s[3].bus_Q16[1]
        self.mux8_16.bus_d[2] = self.ram64s[3].bus_Q16[2]
        self.mux8_16.bus_d[3] = self.ram64s[3].bus_Q16[3]
        self.mux8_16.bus_d[4] = self.ram64s[3].bus_Q16[4]
        self.mux8_16.bus_d[5] = self.ram64s[3].bus_Q16[5]
        self.mux8_16.bus_d[6] = self.ram64s[3].bus_Q16[6]
        self.mux8_16.bus_d[7] = self.ram64s[3].bus_Q16[7]
        self.mux8_16.bus_d[8] = self.ram64s[3].bus_Q16[8]
        self.mux8_16.bus_d[9] = self.ram64s[3].bus_Q16[9]
        self.mux8_16.bus_d[10] = self.ram64s[3].bus_Q16[10]
        self.mux8_16.bus_d[11] = self.ram64s[3].bus_Q16[11]
        self.mux8_16.bus_d[12] = self.ram64s[3].bus_Q16[12]
        self.mux8_16.bus_d[13] = self.ram64s[3].bus_Q16[13]
        self.mux8_16.bus_d[14] = self.ram64s[3].bus_Q16[14]
        self.mux8_16.bus_d[15] = self.ram64s[3].bus_Q16[15]

        self.mux8_16.bus_e[0] = self.ram64s[4].bus_Q16[0]
        self.mux8_16.bus_e[1] = self.ram64s[4].bus_Q16[1]
        self.mux8_16.bus_e[2] = self.ram64s[4].bus_Q16[2]
        self.mux8_16.bus_e[3] = self.ram64s[4].bus_Q16[3]
        self.mux8_16.bus_e[4] = self.ram64s[4].bus_Q16[4]
        self.mux8_16.bus_e[5] = self.ram64s[4].bus_Q16[5]
        self.mux8_16.bus_e[6] = self.ram64s[4].bus_Q16[6]
        self.mux8_16.bus_e[7] = self.ram64s[4].bus_Q16[7]
        self.mux8_16.bus_e[8] = self.ram64s[4].bus_Q16[8]
        self.mux8_16.bus_e[9] = self.ram64s[4].bus_Q16[9]
        self.mux8_16.bus_e[10] = self.ram64s[4].bus_Q16[10]
        self.mux8_16.bus_e[11] = self.ram64s[4].bus_Q16[11]
        self.mux8_16.bus_e[12] = self.ram64s[4].bus_Q16[12]
        self.mux8_16.bus_e[13] = self.ram64s[4].bus_Q16[13]
        self.mux8_16.bus_e[14] = self.ram64s[4].bus_Q16[14]
        self.mux8_16.bus_e[15] = self.ram64s[4].bus_Q16[15]

        self.mux8_16.bus_f[0] = self.ram64s[5].bus_Q16[0]
        self.mux8_16.bus_f[1] = self.ram64s[5].bus_Q16[1]
        self.mux8_16.bus_f[2] = self.ram64s[5].bus_Q16[2]
        self.mux8_16.bus_f[3] = self.ram64s[5].bus_Q16[3]
        self.mux8_16.bus_f[4] = self.ram64s[5].bus_Q16[4]
        self.mux8_16.bus_f[5] = self.ram64s[5].bus_Q16[5]
        self.mux8_16.bus_f[6] = self.ram64s[5].bus_Q16[6]
        self.mux8_16.bus_f[7] = self.ram64s[5].bus_Q16[7]
        self.mux8_16.bus_f[8] = self.ram64s[5].bus_Q16[8]
        self.mux8_16.bus_f[9] = self.ram64s[5].bus_Q16[9]
        self.mux8_16.bus_f[10] = self.ram64s[5].bus_Q16[10]
        self.mux8_16.bus_f[11] = self.ram64s[5].bus_Q16[11]
        self.mux8_16.bus_f[12] = self.ram64s[5].bus_Q16[12]
        self.mux8_16.bus_f[13] = self.ram64s[5].bus_Q16[13]
        self.mux8_16.bus_f[14] = self.ram64s[5].bus_Q16[14]
        self.mux8_16.bus_f[15] = self.ram64s[5].bus_Q16[15]

        self.mux8_16.bus_g[0] = self.ram64s[6].bus_Q16[0]
        self.mux8_16.bus_g[1] = self.ram64s[6].bus_Q16[1]
        self.mux8_16.bus_g[2] = self.ram64s[6].bus_Q16[2]
        self.mux8_16.bus_g[3] = self.ram64s[6].bus_Q16[3]
        self.mux8_16.bus_g[4] = self.ram64s[6].bus_Q16[4]
        self.mux8_16.bus_g[5] = self.ram64s[6].bus_Q16[5]
        self.mux8_16.bus_g[6] = self.ram64s[6].bus_Q16[6]
        self.mux8_16.bus_g[7] = self.ram64s[6].bus_Q16[7]
        self.mux8_16.bus_g[8] = self.ram64s[6].bus_Q16[8]
        self.mux8_16.bus_g[9] = self.ram64s[6].bus_Q16[9]
        self.mux8_16.bus_g[10] = self.ram64s[6].bus_Q16[10]
        self.mux8_16.bus_g[11] = self.ram64s[6].bus_Q16[11]
        self.mux8_16.bus_g[12] = self.ram64s[6].bus_Q16[12]
        self.mux8_16.bus_g[13] = self.ram64s[6].bus_Q16[13]
        self.mux8_16.bus_g[14] = self.ram64s[6].bus_Q16[14]
        self.mux8_16.bus_g[15] = self.ram64s[6].bus_Q16[15]

        self.mux8_16.bus_h[0] = self.ram64s[7].bus_Q16[0]
        self.mux8_16.bus_h[1] = self.ram64s[7].bus_Q16[1]
        self.mux8_16.bus_h[2] = self.ram64s[7].bus_Q16[2]
        self.mux8_16.bus_h[3] = self.ram64s[7].bus_Q16[3]
        self.mux8_16.bus_h[4] = self.ram64s[7].bus_Q16[4]
        self.mux8_16.bus_h[5] = self.ram64s[7].bus_Q16[5]
        self.mux8_16.bus_h[6] = self.ram64s[7].bus_Q16[6]
        self.mux8_16.bus_h[7] = self.ram64s[7].bus_Q16[7]
        self.mux8_16.bus_h[8] = self.ram64s[7].bus_Q16[8]
        self.mux8_16.bus_h[9] = self.ram64s[7].bus_Q16[9]
        self.mux8_16.bus_h[10] = self.ram64s[7].bus_Q16[10]
        self.mux8_16.bus_h[11] = self.ram64s[7].bus_Q16[11]
        self.mux8_16.bus_h[12] = self.ram64s[7].bus_Q16[12]
        self.mux8_16.bus_h[13] = self.ram64s[7].bus_Q16[13]
        self.mux8_16.bus_h[14] = self.ram64s[7].bus_Q16[14]
        self.mux8_16.bus_h[15] = self.ram64s[7].bus_Q16[15]

        # Update the mux8_16
        self.mux8_16.update()

        # Assign output of mux8_16 to bus_Q16
        self.bus_Q16[0] = self.mux8_16.bus_x[0]
        self.bus_Q16[1] = self.mux8_16.bus_x[1]
        self.bus_Q16[2] = self.mux8_16.bus_x[2]
        self.bus_Q16[3] = self.mux8_16.bus_x[3]
        self.bus_Q16[4] = self.mux8_16.bus_x[4]
        self.bus_Q16[5] = self.mux8_16.bus_x[5]
        self.bus_Q16[6] = self.mux8_16.bus_x[6]
        self.bus_Q16[7] = self.mux8_16.bus_x[7]
        self.bus_Q16[8] = self.mux8_16.bus_x[8]
        self.bus_Q16[9] = self.mux8_16.bus_x[9]
        self.bus_Q16[10] = self.mux8_16.bus_x[10]
        self.bus_Q16[11] = self.mux8_16.bus_x[11]
        self.bus_Q16[12] = self.mux8_16.bus_x[12]
        self.bus_Q16[13] = self.mux8_16.bus_x[13]
        self.bus_Q16[14] = self.mux8_16.bus_x[14]
        self.bus_Q16[15] = self.mux8_16.bus_x[15]


class RAM4K:
    def __init__(self):
        self.bus_d16 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.bus_address12 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.pin_load = 0
        self.pin_clk = 0
        self.bus_Q16 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.ram512s = [RAM512(), RAM512(), RAM512(), RAM512(), RAM512(), RAM512(), RAM512(), RAM512()]
        self.dmux8 = lg.DMux8Way()
        self.mux8_16 = lg.Mux8Way16()

    def update(self):
        # Set load input to the single bit input of dmux8:
        self.dmux8.pin_a = self.pin_load

        # Load first 3 address lines to guide load pin to proper RAM512 module:
        self.dmux8.pin_sel0 = self.bus_address12[0]
        self.dmux8.pin_sel1 = self.bus_address12[1]
        self.dmux8.pin_sel2 = self.bus_address12[2]

        # Update the dmux8:
        self.dmux8.update()

        # Load data input to each of the 8 RAM512 modules:
        self.ram512s[0].bus_d16[0] = self.bus_d16[0]
        self.ram512s[0].bus_d16[1] = self.bus_d16[1]
        self.ram512s[0].bus_d16[2] = self.bus_d16[2]
        self.ram512s[0].bus_d16[3] = self.bus_d16[3]
        self.ram512s[0].bus_d16[4] = self.bus_d16[4]
        self.ram512s[0].bus_d16[5] = self.bus_d16[5]
        self.ram512s[0].bus_d16[6] = self.bus_d16[6]
        self.ram512s[0].bus_d16[7] = self.bus_d16[7]
        self.ram512s[0].bus_d16[8] = self.bus_d16[8]
        self.ram512s[0].bus_d16[9] = self.bus_d16[9]
        self.ram512s[0].bus_d16[10] = self.bus_d16[10]
        self.ram512s[0].bus_d16[11] = self.bus_d16[11]
        self.ram512s[0].bus_d16[12] = self.bus_d16[12]
        self.ram512s[0].bus_d16[13] = self.bus_d16[13]
        self.ram512s[0].bus_d16[14] = self.bus_d16[14]
        self.ram512s[0].bus_d16[15] = self.bus_d16[15]

        self.ram512s[1].bus_d16[0] = self.bus_d16[0]
        self.ram512s[1].bus_d16[1] = self.bus_d16[1]
        self.ram512s[1].bus_d16[2] = self.bus_d16[2]
        self.ram512s[1].bus_d16[3] = self.bus_d16[3]
        self.ram512s[1].bus_d16[4] = self.bus_d16[4]
        self.ram512s[1].bus_d16[5] = self.bus_d16[5]
        self.ram512s[1].bus_d16[6] = self.bus_d16[6]
        self.ram512s[1].bus_d16[7] = self.bus_d16[7]
        self.ram512s[1].bus_d16[8] = self.bus_d16[8]
        self.ram512s[1].bus_d16[9] = self.bus_d16[9]
        self.ram512s[1].bus_d16[10] = self.bus_d16[10]
        self.ram512s[1].bus_d16[11] = self.bus_d16[11]
        self.ram512s[1].bus_d16[12] = self.bus_d16[12]
        self.ram512s[1].bus_d16[13] = self.bus_d16[13]
        self.ram512s[1].bus_d16[14] = self.bus_d16[14]
        self.ram512s[1].bus_d16[15] = self.bus_d16[15]

        self.ram512s[2].bus_d16[0] = self.bus_d16[0]
        self.ram512s[2].bus_d16[1] = self.bus_d16[1]
        self.ram512s[2].bus_d16[2] = self.bus_d16[2]
        self.ram512s[2].bus_d16[3] = self.bus_d16[3]
        self.ram512s[2].bus_d16[4] = self.bus_d16[4]
        self.ram512s[2].bus_d16[5] = self.bus_d16[5]
        self.ram512s[2].bus_d16[6] = self.bus_d16[6]
        self.ram512s[2].bus_d16[7] = self.bus_d16[7]
        self.ram512s[2].bus_d16[8] = self.bus_d16[8]
        self.ram512s[2].bus_d16[9] = self.bus_d16[9]
        self.ram512s[2].bus_d16[10] = self.bus_d16[10]
        self.ram512s[2].bus_d16[11] = self.bus_d16[11]
        self.ram512s[2].bus_d16[12] = self.bus_d16[12]
        self.ram512s[2].bus_d16[13] = self.bus_d16[13]
        self.ram512s[2].bus_d16[14] = self.bus_d16[14]
        self.ram512s[2].bus_d16[15] = self.bus_d16[15]

        self.ram512s[3].bus_d16[0] = self.bus_d16[0]
        self.ram512s[3].bus_d16[1] = self.bus_d16[1]
        self.ram512s[3].bus_d16[2] = self.bus_d16[2]
        self.ram512s[3].bus_d16[3] = self.bus_d16[3]
        self.ram512s[3].bus_d16[4] = self.bus_d16[4]
        self.ram512s[3].bus_d16[5] = self.bus_d16[5]
        self.ram512s[3].bus_d16[6] = self.bus_d16[6]
        self.ram512s[3].bus_d16[7] = self.bus_d16[7]
        self.ram512s[3].bus_d16[8] = self.bus_d16[8]
        self.ram512s[3].bus_d16[9] = self.bus_d16[9]
        self.ram512s[3].bus_d16[10] = self.bus_d16[10]
        self.ram512s[3].bus_d16[11] = self.bus_d16[11]
        self.ram512s[3].bus_d16[12] = self.bus_d16[12]
        self.ram512s[3].bus_d16[13] = self.bus_d16[13]
        self.ram512s[3].bus_d16[14] = self.bus_d16[14]
        self.ram512s[3].bus_d16[15] = self.bus_d16[15]

        self.ram512s[4].bus_d16[0] = self.bus_d16[0]
        self.ram512s[4].bus_d16[1] = self.bus_d16[1]
        self.ram512s[4].bus_d16[2] = self.bus_d16[2]
        self.ram512s[4].bus_d16[3] = self.bus_d16[3]
        self.ram512s[4].bus_d16[4] = self.bus_d16[4]
        self.ram512s[4].bus_d16[5] = self.bus_d16[5]
        self.ram512s[4].bus_d16[6] = self.bus_d16[6]
        self.ram512s[4].bus_d16[7] = self.bus_d16[7]
        self.ram512s[4].bus_d16[8] = self.bus_d16[8]
        self.ram512s[4].bus_d16[9] = self.bus_d16[9]
        self.ram512s[4].bus_d16[10] = self.bus_d16[10]
        self.ram512s[4].bus_d16[11] = self.bus_d16[11]
        self.ram512s[4].bus_d16[12] = self.bus_d16[12]
        self.ram512s[4].bus_d16[13] = self.bus_d16[13]
        self.ram512s[4].bus_d16[14] = self.bus_d16[14]
        self.ram512s[4].bus_d16[15] = self.bus_d16[15]

        self.ram512s[5].bus_d16[0] = self.bus_d16[0]
        self.ram512s[5].bus_d16[1] = self.bus_d16[1]
        self.ram512s[5].bus_d16[2] = self.bus_d16[2]
        self.ram512s[5].bus_d16[3] = self.bus_d16[3]
        self.ram512s[5].bus_d16[4] = self.bus_d16[4]
        self.ram512s[5].bus_d16[5] = self.bus_d16[5]
        self.ram512s[5].bus_d16[6] = self.bus_d16[6]
        self.ram512s[5].bus_d16[7] = self.bus_d16[7]
        self.ram512s[5].bus_d16[8] = self.bus_d16[8]
        self.ram512s[5].bus_d16[9] = self.bus_d16[9]
        self.ram512s[5].bus_d16[10] = self.bus_d16[10]
        self.ram512s[5].bus_d16[11] = self.bus_d16[11]
        self.ram512s[5].bus_d16[12] = self.bus_d16[12]
        self.ram512s[5].bus_d16[13] = self.bus_d16[13]
        self.ram512s[5].bus_d16[14] = self.bus_d16[14]
        self.ram512s[5].bus_d16[15] = self.bus_d16[15]

        self.ram512s[6].bus_d16[0] = self.bus_d16[0]
        self.ram512s[6].bus_d16[1] = self.bus_d16[1]
        self.ram512s[6].bus_d16[2] = self.bus_d16[2]
        self.ram512s[6].bus_d16[3] = self.bus_d16[3]
        self.ram512s[6].bus_d16[4] = self.bus_d16[4]
        self.ram512s[6].bus_d16[5] = self.bus_d16[5]
        self.ram512s[6].bus_d16[6] = self.bus_d16[6]
        self.ram512s[6].bus_d16[7] = self.bus_d16[7]
        self.ram512s[6].bus_d16[8] = self.bus_d16[8]
        self.ram512s[6].bus_d16[9] = self.bus_d16[9]
        self.ram512s[6].bus_d16[10] = self.bus_d16[10]
        self.ram512s[6].bus_d16[11] = self.bus_d16[11]
        self.ram512s[6].bus_d16[12] = self.bus_d16[12]
        self.ram512s[6].bus_d16[13] = self.bus_d16[13]
        self.ram512s[6].bus_d16[14] = self.bus_d16[14]
        self.ram512s[6].bus_d16[15] = self.bus_d16[15]

        self.ram512s[7].bus_d16[0] = self.bus_d16[0]
        self.ram512s[7].bus_d16[1] = self.bus_d16[1]
        self.ram512s[7].bus_d16[2] = self.bus_d16[2]
        self.ram512s[7].bus_d16[3] = self.bus_d16[3]
        self.ram512s[7].bus_d16[4] = self.bus_d16[4]
        self.ram512s[7].bus_d16[5] = self.bus_d16[5]
        self.ram512s[7].bus_d16[6] = self.bus_d16[6]
        self.ram512s[7].bus_d16[7] = self.bus_d16[7]
        self.ram512s[7].bus_d16[8] = self.bus_d16[8]
        self.ram512s[7].bus_d16[9] = self.bus_d16[9]
        self.ram512s[7].bus_d16[10] = self.bus_d16[10]
        self.ram512s[7].bus_d16[11] = self.bus_d16[11]
        self.ram512s[7].bus_d16[12] = self.bus_d16[12]
        self.ram512s[7].bus_d16[13] = self.bus_d16[13]
        self.ram512s[7].bus_d16[14] = self.bus_d16[14]
        self.ram512s[7].bus_d16[15] = self.bus_d16[15]

        # Set the load pins of each RAM512 module to corresponding output from dmux8 
        self.ram512s[0].pin_load = self.dmux8.pin_s 
        self.ram512s[1].pin_load = self.dmux8.pin_t 
        self.ram512s[2].pin_load = self.dmux8.pin_u
        self.ram512s[3].pin_load = self.dmux8.pin_v
        self.ram512s[4].pin_load = self.dmux8.pin_w
        self.ram512s[5].pin_load = self.dmux8.pin_x
        self.ram512s[6].pin_load = self.dmux8.pin_y
        self.ram512s[7].pin_load = self.dmux8.pin_z

        # Set the clock pins of each RAM512 module to the clock pin of this module
        self.ram512s[0].pin_clk = self.pin_clk
        self.ram512s[1].pin_clk = self.pin_clk
        self.ram512s[2].pin_clk = self.pin_clk
        self.ram512s[3].pin_clk = self.pin_clk
        self.ram512s[4].pin_clk = self.pin_clk
        self.ram512s[5].pin_clk = self.pin_clk
        self.ram512s[6].pin_clk = self.pin_clk
        self.ram512s[7].pin_clk = self.pin_clk

        # Set the address pins of each RAM512 module to the remaining address pins of this RAM module
        # First 3 already used to select RAM512 module
        self.ram512s[0].pin_address9[0] = self.pin_address12[3]
        self.ram512s[0].pin_address9[1] = self.pin_address12[4]
        self.ram512s[0].pin_address9[2] = self.pin_address12[5]
        self.ram512s[0].pin_address9[3] = self.pin_address12[6]
        self.ram512s[0].pin_address9[4] = self.pin_address12[7]
        self.ram512s[0].pin_address9[5] = self.pin_address12[8]
        self.ram512s[0].pin_address9[6] = self.pin_address12[9]
        self.ram512s[0].pin_address9[7] = self.pin_address12[10]
        self.ram512s[0].pin_address9[8] = self.pin_address12[11]

        self.ram512s[1].pin_address9[0] = self.pin_address12[3]
        self.ram512s[1].pin_address9[1] = self.pin_address12[4]
        self.ram512s[1].pin_address9[2] = self.pin_address12[5]
        self.ram512s[1].pin_address9[3] = self.pin_address12[6]
        self.ram512s[1].pin_address9[4] = self.pin_address12[7]
        self.ram512s[1].pin_address9[5] = self.pin_address12[8]
        self.ram512s[1].pin_address9[6] = self.pin_address12[9]
        self.ram512s[1].pin_address9[7] = self.pin_address12[10]
        self.ram512s[1].pin_address9[8] = self.pin_address12[11]

        self.ram512s[2].pin_address9[0] = self.pin_address12[3]
        self.ram512s[2].pin_address9[1] = self.pin_address12[4]
        self.ram512s[2].pin_address9[2] = self.pin_address12[5]
        self.ram512s[2].pin_address9[3] = self.pin_address12[6]
        self.ram512s[2].pin_address9[4] = self.pin_address12[7]
        self.ram512s[2].pin_address9[5] = self.pin_address12[8]
        self.ram512s[2].pin_address9[6] = self.pin_address12[9]
        self.ram512s[2].pin_address9[7] = self.pin_address12[10]
        self.ram512s[2].pin_address9[8] = self.pin_address12[11]

        self.ram512s[3].pin_address9[0] = self.pin_address12[3]
        self.ram512s[3].pin_address9[1] = self.pin_address12[4]
        self.ram512s[3].pin_address9[2] = self.pin_address12[5]
        self.ram512s[3].pin_address9[3] = self.pin_address12[6]
        self.ram512s[3].pin_address9[4] = self.pin_address12[7]
        self.ram512s[3].pin_address9[5] = self.pin_address12[8]
        self.ram512s[3].pin_address9[6] = self.pin_address12[9]
        self.ram512s[3].pin_address9[7] = self.pin_address12[10]
        self.ram512s[3].pin_address9[8] = self.pin_address12[11]

        self.ram512s[4].pin_address9[0] = self.pin_address12[3]
        self.ram512s[4].pin_address9[1] = self.pin_address12[4]
        self.ram512s[4].pin_address9[2] = self.pin_address12[5]
        self.ram512s[4].pin_address9[3] = self.pin_address12[6]
        self.ram512s[4].pin_address9[4] = self.pin_address12[7]
        self.ram512s[4].pin_address9[5] = self.pin_address12[8]
        self.ram512s[4].pin_address9[6] = self.pin_address12[9]
        self.ram512s[4].pin_address9[7] = self.pin_address12[10]
        self.ram512s[4].pin_address9[8] = self.pin_address12[11]

        self.ram512s[5].pin_address9[0] = self.pin_address12[3]
        self.ram512s[5].pin_address9[1] = self.pin_address12[4]
        self.ram512s[5].pin_address9[2] = self.pin_address12[5]
        self.ram512s[5].pin_address9[3] = self.pin_address12[6]
        self.ram512s[5].pin_address9[4] = self.pin_address12[7]
        self.ram512s[5].pin_address9[5] = self.pin_address12[8]
        self.ram512s[5].pin_address9[6] = self.pin_address12[9]
        self.ram512s[5].pin_address9[7] = self.pin_address12[10]
        self.ram512s[5].pin_address9[8] = self.pin_address12[11]

        self.ram512s[6].pin_address9[0] = self.pin_address12[3]
        self.ram512s[6].pin_address9[1] = self.pin_address12[4]
        self.ram512s[6].pin_address9[2] = self.pin_address12[5]
        self.ram512s[6].pin_address9[3] = self.pin_address12[6]
        self.ram512s[6].pin_address9[4] = self.pin_address12[7]
        self.ram512s[6].pin_address9[5] = self.pin_address12[8]
        self.ram512s[6].pin_address9[6] = self.pin_address12[9]
        self.ram512s[6].pin_address9[7] = self.pin_address12[10]
        self.ram512s[6].pin_address9[8] = self.pin_address12[11]

        self.ram512s[7].pin_address9[0] = self.pin_address12[3]
        self.ram512s[7].pin_address9[1] = self.pin_address12[4]
        self.ram512s[7].pin_address9[2] = self.pin_address12[5]
        self.ram512s[7].pin_address9[3] = self.pin_address12[6]
        self.ram512s[7].pin_address9[4] = self.pin_address12[7]
        self.ram512s[7].pin_address9[5] = self.pin_address12[8]
        self.ram512s[7].pin_address9[6] = self.pin_address12[9]
        self.ram512s[7].pin_address9[7] = self.pin_address12[10]
        self.ram512s[7].pin_address9[8] = self.pin_address12[11]

        # Update each RAM512
        self.ram512s[0].update()
        self.ram512s[1].update()
        self.ram512s[2].update()
        self.ram512s[3].update()
        self.ram512s[4].update()
        self.ram512s[5].update()
        self.ram512s[6].update()
        self.ram512s[7].update()

        # Set output of each RAM512 to specific input bus of the Mux8Way16
        self.mux8_16.bus_a[0] = self.ram512s[0].bus_Q16[0]
        self.mux8_16.bus_a[1] = self.ram512s[0].bus_Q16[1]
        self.mux8_16.bus_a[2] = self.ram512s[0].bus_Q16[2]
        self.mux8_16.bus_a[3] = self.ram512s[0].bus_Q16[3]
        self.mux8_16.bus_a[4] = self.ram512s[0].bus_Q16[4]
        self.mux8_16.bus_a[5] = self.ram512s[0].bus_Q16[5]
        self.mux8_16.bus_a[6] = self.ram512s[0].bus_Q16[6]
        self.mux8_16.bus_a[7] = self.ram512s[0].bus_Q16[7]
        self.mux8_16.bus_a[8] = self.ram512s[0].bus_Q16[8]
        self.mux8_16.bus_a[9] = self.ram512s[0].bus_Q16[9]
        self.mux8_16.bus_a[10] = self.ram512s[0].bus_Q16[10]
        self.mux8_16.bus_a[11] = self.ram512s[0].bus_Q16[11]
        self.mux8_16.bus_a[12] = self.ram512s[0].bus_Q16[12]
        self.mux8_16.bus_a[13] = self.ram512s[0].bus_Q16[13]
        self.mux8_16.bus_a[14] = self.ram512s[0].bus_Q16[14]
        self.mux8_16.bus_a[15] = self.ram512s[0].bus_Q16[15]

        self.mux8_16.bus_b[0] = self.ram512s[1].bus_Q16[0]
        self.mux8_16.bus_b[1] = self.ram512s[1].bus_Q16[1]
        self.mux8_16.bus_b[2] = self.ram512s[1].bus_Q16[2]
        self.mux8_16.bus_b[3] = self.ram512s[1].bus_Q16[3]
        self.mux8_16.bus_b[4] = self.ram512s[1].bus_Q16[4]
        self.mux8_16.bus_b[5] = self.ram512s[1].bus_Q16[5]
        self.mux8_16.bus_b[6] = self.ram512s[1].bus_Q16[6]
        self.mux8_16.bus_b[7] = self.ram512s[1].bus_Q16[7]
        self.mux8_16.bus_b[8] = self.ram512s[1].bus_Q16[8]
        self.mux8_16.bus_b[9] = self.ram512s[1].bus_Q16[9]
        self.mux8_16.bus_b[10] = self.ram512s[1].bus_Q16[10]
        self.mux8_16.bus_b[11] = self.ram512s[1].bus_Q16[11]
        self.mux8_16.bus_b[12] = self.ram512s[1].bus_Q16[12]
        self.mux8_16.bus_b[13] = self.ram512s[1].bus_Q16[13]
        self.mux8_16.bus_b[14] = self.ram512s[1].bus_Q16[14]
        self.mux8_16.bus_b[15] = self.ram512s[1].bus_Q16[15]

        self.mux8_16.bus_c[0] = self.ram512s[2].bus_Q16[0]
        self.mux8_16.bus_c[1] = self.ram512s[2].bus_Q16[1]
        self.mux8_16.bus_c[2] = self.ram512s[2].bus_Q16[2]
        self.mux8_16.bus_c[3] = self.ram512s[2].bus_Q16[3]
        self.mux8_16.bus_c[4] = self.ram512s[2].bus_Q16[4]
        self.mux8_16.bus_c[5] = self.ram512s[2].bus_Q16[5]
        self.mux8_16.bus_c[6] = self.ram512s[2].bus_Q16[6]
        self.mux8_16.bus_c[7] = self.ram512s[2].bus_Q16[7]
        self.mux8_16.bus_c[8] = self.ram512s[2].bus_Q16[8]
        self.mux8_16.bus_c[9] = self.ram512s[2].bus_Q16[9]
        self.mux8_16.bus_c[10] = self.ram512s[2].bus_Q16[10]
        self.mux8_16.bus_c[11] = self.ram512s[2].bus_Q16[11]
        self.mux8_16.bus_c[12] = self.ram512s[2].bus_Q16[12]
        self.mux8_16.bus_c[13] = self.ram512s[2].bus_Q16[13]
        self.mux8_16.bus_c[14] = self.ram512s[2].bus_Q16[14]
        self.mux8_16.bus_c[15] = self.ram512s[2].bus_Q16[15]

        self.mux8_16.bus_d[0] = self.ram512s[3].bus_Q16[0]
        self.mux8_16.bus_d[1] = self.ram512s[3].bus_Q16[1]
        self.mux8_16.bus_d[2] = self.ram512s[3].bus_Q16[2]
        self.mux8_16.bus_d[3] = self.ram512s[3].bus_Q16[3]
        self.mux8_16.bus_d[4] = self.ram512s[3].bus_Q16[4]
        self.mux8_16.bus_d[5] = self.ram512s[3].bus_Q16[5]
        self.mux8_16.bus_d[6] = self.ram512s[3].bus_Q16[6]
        self.mux8_16.bus_d[7] = self.ram512s[3].bus_Q16[7]
        self.mux8_16.bus_d[8] = self.ram512s[3].bus_Q16[8]
        self.mux8_16.bus_d[9] = self.ram512s[3].bus_Q16[9]
        self.mux8_16.bus_d[10] = self.ram512s[3].bus_Q16[10]
        self.mux8_16.bus_d[11] = self.ram512s[3].bus_Q16[11]
        self.mux8_16.bus_d[12] = self.ram512s[3].bus_Q16[12]
        self.mux8_16.bus_d[13] = self.ram512s[3].bus_Q16[13]
        self.mux8_16.bus_d[14] = self.ram512s[3].bus_Q16[14]
        self.mux8_16.bus_d[15] = self.ram512s[3].bus_Q16[15]

        self.mux8_16.bus_e[0] = self.ram512s[4].bus_Q16[0]
        self.mux8_16.bus_e[1] = self.ram512s[4].bus_Q16[1]
        self.mux8_16.bus_e[2] = self.ram512s[4].bus_Q16[2]
        self.mux8_16.bus_e[3] = self.ram512s[4].bus_Q16[3]
        self.mux8_16.bus_e[4] = self.ram512s[4].bus_Q16[4]
        self.mux8_16.bus_e[5] = self.ram512s[4].bus_Q16[5]
        self.mux8_16.bus_e[6] = self.ram512s[4].bus_Q16[6]
        self.mux8_16.bus_e[7] = self.ram512s[4].bus_Q16[7]
        self.mux8_16.bus_e[8] = self.ram512s[4].bus_Q16[8]
        self.mux8_16.bus_e[9] = self.ram512s[4].bus_Q16[9]
        self.mux8_16.bus_e[10] = self.ram512s[4].bus_Q16[10]
        self.mux8_16.bus_e[11] = self.ram512s[4].bus_Q16[11]
        self.mux8_16.bus_e[12] = self.ram512s[4].bus_Q16[12]
        self.mux8_16.bus_e[13] = self.ram512s[4].bus_Q16[13]
        self.mux8_16.bus_e[14] = self.ram512s[4].bus_Q16[14]
        self.mux8_16.bus_e[15] = self.ram512s[4].bus_Q16[15]

        self.mux8_16.bus_f[0] = self.ram512s[5].bus_Q16[0]
        self.mux8_16.bus_f[1] = self.ram512s[5].bus_Q16[1]
        self.mux8_16.bus_f[2] = self.ram512s[5].bus_Q16[2]
        self.mux8_16.bus_f[3] = self.ram512s[5].bus_Q16[3]
        self.mux8_16.bus_f[4] = self.ram512s[5].bus_Q16[4]
        self.mux8_16.bus_f[5] = self.ram512s[5].bus_Q16[5]
        self.mux8_16.bus_f[6] = self.ram512s[5].bus_Q16[6]
        self.mux8_16.bus_f[7] = self.ram512s[5].bus_Q16[7]
        self.mux8_16.bus_f[8] = self.ram512s[5].bus_Q16[8]
        self.mux8_16.bus_f[9] = self.ram512s[5].bus_Q16[9]
        self.mux8_16.bus_f[10] = self.ram512s[5].bus_Q16[10]
        self.mux8_16.bus_f[11] = self.ram512s[5].bus_Q16[11]
        self.mux8_16.bus_f[12] = self.ram512s[5].bus_Q16[12]
        self.mux8_16.bus_f[13] = self.ram512s[5].bus_Q16[13]
        self.mux8_16.bus_f[14] = self.ram512s[5].bus_Q16[14]
        self.mux8_16.bus_f[15] = self.ram512s[5].bus_Q16[15]

        self.mux8_16.bus_g[0] = self.ram512s[6].bus_Q16[0]
        self.mux8_16.bus_g[1] = self.ram512s[6].bus_Q16[1]
        self.mux8_16.bus_g[2] = self.ram512s[6].bus_Q16[2]
        self.mux8_16.bus_g[3] = self.ram512s[6].bus_Q16[3]
        self.mux8_16.bus_g[4] = self.ram512s[6].bus_Q16[4]
        self.mux8_16.bus_g[5] = self.ram512s[6].bus_Q16[5]
        self.mux8_16.bus_g[6] = self.ram512s[6].bus_Q16[6]
        self.mux8_16.bus_g[7] = self.ram512s[6].bus_Q16[7]
        self.mux8_16.bus_g[8] = self.ram512s[6].bus_Q16[8]
        self.mux8_16.bus_g[9] = self.ram512s[6].bus_Q16[9]
        self.mux8_16.bus_g[10] = self.ram512s[6].bus_Q16[10]
        self.mux8_16.bus_g[11] = self.ram512s[6].bus_Q16[11]
        self.mux8_16.bus_g[12] = self.ram512s[6].bus_Q16[12]
        self.mux8_16.bus_g[13] = self.ram512s[6].bus_Q16[13]
        self.mux8_16.bus_g[14] = self.ram512s[6].bus_Q16[14]
        self.mux8_16.bus_g[15] = self.ram512s[6].bus_Q16[15]

        # Set address bits for mux8_16
        self.mux8_16.pin_sel0 = self.bus_address12[0]
        self.mux8_16.pin_sel1 = self.bus_address12[1]
        self.mux8_16.pin_sel2 = self.bus_address12[2]

        # Update mux8_16
        self.mux8_16.update()

        # Set output of mux8_16 to bus_Q16
        self.bus_Q16[0] = self.mux8_16.bus_x[0]
        self.bus_Q16[1] = self.mux8_16.bus_x[1]
        self.bus_Q16[2] = self.mux8_16.bus_x[2]
        self.bus_Q16[3] = self.mux8_16.bus_x[3]
        self.bus_Q16[4] = self.mux8_16.bus_x[4]
        self.bus_Q16[5] = self.mux8_16.bus_x[5]
        self.bus_Q16[6] = self.mux8_16.bus_x[6]
        self.bus_Q16[7] = self.mux8_16.bus_x[7]
        self.bus_Q16[8] = self.mux8_16.bus_x[8]
        self.bus_Q16[9] = self.mux8_16.bus_x[9]
        self.bus_Q16[10] = self.mux8_16.bus_x[10]
        self.bus_Q16[11] = self.mux8_16.bus_x[11]
        self.bus_Q16[12] = self.mux8_16.bus_x[12]
        self.bus_Q16[13] = self.mux8_16.bus_x[13]
        self.bus_Q16[14] = self.mux8_16.bus_x[14]
        self.bus_Q16[15] = self.mux8_16.bus_x[15]


class RAM16K:
    def __init__(self):
        self.bus_d16 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.bus_address14 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.pin_load = 0
        self.pin_clk = 0
        self.bus_Q16 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.ram4ks = [RAM4K(), RAM4K(), RAM4K(), RAM4K()]
        self.dmux4 = lg.DMux4Way()
        self.mux4_16 = lg.Mux4Way16()


    def update(self):
        # Send load pin through DMUX4, use first 2 address bits to send load bit to correct RAM4K
        self.dmux4.pin_a = self.pin_load
        self.dmux4.pin_sel0 = self.bus_address14[0]
        self.dmux4.pin_sel1 = self.bus_address14[1]
        self.dmux4.update()

        # Send input data bus to inputs of each RAM4K
        self.ram4ks[0].bus_d16[0] = self.bus_d16[0]
        self.ram4ks[0].bus_d16[1] = self.bus_d16[1]
        self.ram4ks[0].bus_d16[2] = self.bus_d16[2]
        self.ram4ks[0].bus_d16[3] = self.bus_d16[3]
        self.ram4ks[0].bus_d16[4] = self.bus_d16[4]
        self.ram4ks[0].bus_d16[5] = self.bus_d16[5]
        self.ram4ks[0].bus_d16[6] = self.bus_d16[6]
        self.ram4ks[0].bus_d16[7] = self.bus_d16[7]
        self.ram4ks[0].bus_d16[8] = self.bus_d16[8]
        self.ram4ks[0].bus_d16[9] = self.bus_d16[9]
        self.ram4ks[0].bus_d16[10] = self.bus_d16[10]
        self.ram4ks[0].bus_d16[11] = self.bus_d16[11]
        self.ram4ks[0].bus_d16[12] = self.bus_d16[12]
        self.ram4ks[0].bus_d16[13] = self.bus_d16[13]
        self.ram4ks[0].bus_d16[14] = self.bus_d16[14]
        self.ram4ks[0].bus_d16[15] = self.bus_d16[15]

        self.ram4ks[1].bus_d16[0] = self.bus_d16[0]
        self.ram4ks[1].bus_d16[1] = self.bus_d16[1]
        self.ram4ks[1].bus_d16[2] = self.bus_d16[2]
        self.ram4ks[1].bus_d16[3] = self.bus_d16[3]
        self.ram4ks[1].bus_d16[4] = self.bus_d16[4]
        self.ram4ks[1].bus_d16[5] = self.bus_d16[5]
        self.ram4ks[1].bus_d16[6] = self.bus_d16[6]
        self.ram4ks[1].bus_d16[7] = self.bus_d16[7]
        self.ram4ks[1].bus_d16[8] = self.bus_d16[8]
        self.ram4ks[1].bus_d16[9] = self.bus_d16[9]
        self.ram4ks[1].bus_d16[10] = self.bus_d16[10]
        self.ram4ks[1].bus_d16[11] = self.bus_d16[11]
        self.ram4ks[1].bus_d16[12] = self.bus_d16[12]
        self.ram4ks[1].bus_d16[13] = self.bus_d16[13]
        self.ram4ks[1].bus_d16[14] = self.bus_d16[14]

        self.ram4ks[2].bus_d16[0] = self.bus_d16[0]
        self.ram4ks[2].bus_d16[1] = self.bus_d16[1]
        self.ram4ks[2].bus_d16[2] = self.bus_d16[2]
        self.ram4ks[2].bus_d16[3] = self.bus_d16[3]
        self.ram4ks[2].bus_d16[4] = self.bus_d16[4]
        self.ram4ks[2].bus_d16[5] = self.bus_d16[5]
        self.ram4ks[2].bus_d16[6] = self.bus_d16[6]
        self.ram4ks[2].bus_d16[7] = self.bus_d16[7]
        self.ram4ks[2].bus_d16[8] = self.bus_d16[8]
        self.ram4ks[2].bus_d16[9] = self.bus_d16[9]
        self.ram4ks[2].bus_d16[10] = self.bus_d16[10]
        self.ram4ks[2].bus_d16[11] = self.bus_d16[11]
        self.ram4ks[2].bus_d16[12] = self.bus_d16[12]
        self.ram4ks[2].bus_d16[13] = self.bus_d16[13]
        self.ram4ks[2].bus_d16[14] = self.bus_d16[14]
        self.ram4ks[2].bus_d16[15] = self.bus_d16[15]

        self.ram4ks[3].bus_d16[0] = self.bus_d16[0]
        self.ram4ks[3].bus_d16[1] = self.bus_d16[1]
        self.ram4ks[3].bus_d16[2] = self.bus_d16[2]
        self.ram4ks[3].bus_d16[3] = self.bus_d16[3]
        self.ram4ks[3].bus_d16[4] = self.bus_d16[4]
        self.ram4ks[3].bus_d16[5] = self.bus_d16[5]
        self.ram4ks[3].bus_d16[6] = self.bus_d16[6]
        self.ram4ks[3].bus_d16[7] = self.bus_d16[7]
        self.ram4ks[3].bus_d16[8] = self.bus_d16[8]
        self.ram4ks[3].bus_d16[9] = self.bus_d16[9]
        self.ram4ks[3].bus_d16[10] = self.bus_d16[10]
        self.ram4ks[3].bus_d16[11] = self.bus_d16[11]
        self.ram4ks[3].bus_d16[12] = self.bus_d16[12]
        self.ram4ks[3].bus_d16[13] = self.bus_d16[13]
        self.ram4ks[3].bus_d16[14] = self.bus_d16[14]
        self.ram4ks[3].bus_d16[15] = self.bus_d16[15]

        # Use output of dmux4 to select which ram4k to write to:
        self.ram4ks[0].pin_load = self.dmux4.pin_w 
        self.ram4ks[1].pin_load = self.dmux4.pin_x
        self.ram4ks[2].pin_load = self.dmux4.pin_y
        self.ram4ks[3].pin_load = self.dmux4.pin_z

        # Set clock line to all ram4ks:
        self.ram4ks[0].pin_clk = self.pin_clk
        self.ram4ks[1].pin_clk = self.pin_clk
        self.ram4ks[2].pin_clk = self.pin_clk
        self.ram4ks[3].pin_clk = self.pin_clk

        # Set address lines to all ram4ks, using remaining 12 bits of address14:
        self.ram4ks[0].bus_address12[0] = self.bus_address14[2]
        self.ram4ks[0].bus_address12[1] = self.bus_address14[3]
        self.ram4ks[0].bus_address12[2] = self.bus_address14[4]
        self.ram4ks[0].bus_address12[3] = self.bus_address14[5]
        self.ram4ks[0].bus_address12[4] = self.bus_address14[6]
        self.ram4ks[0].bus_address12[5] = self.bus_address14[7]
        self.ram4ks[0].bus_address12[6] = self.bus_address14[8]
        self.ram4ks[0].bus_address12[7] = self.bus_address14[9]
        self.ram4ks[0].bus_address12[8] = self.bus_address14[10]
        self.ram4ks[0].bus_address12[9] = self.bus_address14[11]
        self.ram4ks[0].bus_address12[10] = self.bus_address14[12]
        self.ram4ks[0].bus_address12[11] = self.bus_address14[13]

        self.ram4ks[1].bus_address12[0] = self.bus_address14[2]
        self.ram4ks[1].bus_address12[1] = self.bus_address14[3]
        self.ram4ks[1].bus_address12[2] = self.bus_address14[4]
        self.ram4ks[1].bus_address12[3] = self.bus_address14[5]
        self.ram4ks[1].bus_address12[4] = self.bus_address14[6]
        self.ram4ks[1].bus_address12[5] = self.bus_address14[7]
        self.ram4ks[1].bus_address12[6] = self.bus_address14[8]
        self.ram4ks[1].bus_address12[7] = self.bus_address14[9]
        self.ram4ks[1].bus_address12[8] = self.bus_address14[10]
        self.ram4ks[1].bus_address12[9] = self.bus_address14[11]
        self.ram4ks[1].bus_address12[10] = self.bus_address14[12]
        self.ram4ks[1].bus_address12[11] = self.bus_address14[13]

        self.ram4ks[2].bus_address12[0] = self.bus_address14[2]
        self.ram4ks[2].bus_address12[1] = self.bus_address14[3]
        self.ram4ks[2].bus_address12[2] = self.bus_address14[4]
        self.ram4ks[2].bus_address12[3] = self.bus_address14[5]
        self.ram4ks[2].bus_address12[4] = self.bus_address14[6]
        self.ram4ks[2].bus_address12[5] = self.bus_address14[7]
        self.ram4ks[2].bus_address12[6] = self.bus_address14[8]
        self.ram4ks[2].bus_address12[7] = self.bus_address14[9]
        self.ram4ks[2].bus_address12[8] = self.bus_address14[10]
        self.ram4ks[2].bus_address12[9] = self.bus_address14[11]
        self.ram4ks[2].bus_address12[10] = self.bus_address14[12]
        self.ram4ks[2].bus_address12[11] = self.bus_address14[13]

        self.ram4ks[3].bus_address12[0] = self.bus_address14[2]
        self.ram4ks[3].bus_address12[1] = self.bus_address14[3]
        self.ram4ks[3].bus_address12[2] = self.bus_address14[4]
        self.ram4ks[3].bus_address12[3] = self.bus_address14[5]
        self.ram4ks[3].bus_address12[4] = self.bus_address14[6]
        self.ram4ks[3].bus_address12[5] = self.bus_address14[7]
        self.ram4ks[3].bus_address12[6] = self.bus_address14[8]
        self.ram4ks[3].bus_address12[7] = self.bus_address14[9]
        self.ram4ks[3].bus_address12[8] = self.bus_address14[10]
        self.ram4ks[3].bus_address12[9] = self.bus_address14[11]
        self.ram4ks[3].bus_address12[10] = self.bus_address14[12]
        self.ram4ks[3].bus_address12[11] = self.bus_address14[13]

        # Update each RAM4K
        self.ram4ks[0].update()
        self.ram4ks[1].update()
        self.ram4ks[2].update()
        self.ram4ks[3].update()

        # Send output of each ram4k to a particular input of the 4-way mux 16:
        self.mux4_16.bus_a[0] = self.ram4ks[0].bus_Q16[0]
        self.mux4_16.bus_a[1] = self.ram4ks[0].bus_Q16[1]
        self.mux4_16.bus_a[2] = self.ram4ks[0].bus_Q16[2]
        self.mux4_16.bus_a[3] = self.ram4ks[0].bus_Q16[3]
        self.mux4_16.bus_a[4] = self.ram4ks[0].bus_Q16[4]
        self.mux4_16.bus_a[5] = self.ram4ks[0].bus_Q16[5]
        self.mux4_16.bus_a[6] = self.ram4ks[0].bus_Q16[6]
        self.mux4_16.bus_a[7] = self.ram4ks[0].bus_Q16[7]
        self.mux4_16.bus_a[8] = self.ram4ks[0].bus_Q16[8]
        self.mux4_16.bus_a[9] = self.ram4ks[0].bus_Q16[9]
        self.mux4_16.bus_a[10] = self.ram4ks[0].bus_Q16[10]
        self.mux4_16.bus_a[11] = self.ram4ks[0].bus_Q16[11]
        self.mux4_16.bus_a[12] = self.ram4ks[0].bus_Q16[12]
        self.mux4_16.bus_a[13] = self.ram4ks[0].bus_Q16[13]
        self.mux4_16.bus_a[14] = self.ram4ks[0].bus_Q16[14]
        self.mux4_16.bus_a[15] = self.ram4ks[0].bus_Q16[15]

        self.mux4_16.bus_b[0] = self.ram4ks[1].bus_Q16[0]
        self.mux4_16.bus_b[1] = self.ram4ks[1].bus_Q16[1]
        self.mux4_16.bus_b[2] = self.ram4ks[1].bus_Q16[2]
        self.mux4_16.bus_b[3] = self.ram4ks[1].bus_Q16[3]
        self.mux4_16.bus_b[4] = self.ram4ks[1].bus_Q16[4]
        self.mux4_16.bus_b[5] = self.ram4ks[1].bus_Q16[5]
        self.mux4_16.bus_b[6] = self.ram4ks[1].bus_Q16[6]
        self.mux4_16.bus_b[7] = self.ram4ks[1].bus_Q16[7]
        self.mux4_16.bus_b[8] = self.ram4ks[1].bus_Q16[8]
        self.mux4_16.bus_b[9] = self.ram4ks[1].bus_Q16[9]
        self.mux4_16.bus_b[10] = self.ram4ks[1].bus_Q16[10]
        self.mux4_16.bus_b[11] = self.ram4ks[1].bus_Q16[11]
        self.mux4_16.bus_b[12] = self.ram4ks[1].bus_Q16[12]
        self.mux4_16.bus_b[13] = self.ram4ks[1].bus_Q16[13]
        self.mux4_16.bus_b[14] = self.ram4ks[1].bus_Q16[14]
        self.mux4_16.bus_b[15] = self.ram4ks[1].bus_Q16[15]

        self.mux4_16.bus_c[0] = self.ram4ks[2].bus_Q16[0]
        self.mux4_16.bus_c[1] = self.ram4ks[2].bus_Q16[1]
        self.mux4_16.bus_c[2] = self.ram4ks[2].bus_Q16[2]
        self.mux4_16.bus_c[3] = self.ram4ks[2].bus_Q16[3]
        self.mux4_16.bus_c[4] = self.ram4ks[2].bus_Q16[4]
        self.mux4_16.bus_c[5] = self.ram4ks[2].bus_Q16[5]
        self.mux4_16.bus_c[6] = self.ram4ks[2].bus_Q16[6]
        self.mux4_16.bus_c[7] = self.ram4ks[2].bus_Q16[7]
        self.mux4_16.bus_c[8] = self.ram4ks[2].bus_Q16[8]
        self.mux4_16.bus_c[9] = self.ram4ks[2].bus_Q16[9]
        self.mux4_16.bus_c[10] = self.ram4ks[2].bus_Q16[10]
        self.mux4_16.bus_c[11] = self.ram4ks[2].bus_Q16[11]
        self.mux4_16.bus_c[12] = self.ram4ks[2].bus_Q16[12]
        self.mux4_16.bus_c[13] = self.ram4ks[2].bus_Q16[13]
        self.mux4_16.bus_c[14] = self.ram4ks[2].bus_Q16[14]
        self.mux4_16.bus_c[15] = self.ram4ks[2].bus_Q16[15]

        self.mux4_16.bus_d[0] = self.ram4ks[3].bus_Q16[0]
        self.mux4_16.bus_d[1] = self.ram4ks[3].bus_Q16[1]
        self.mux4_16.bus_d[2] = self.ram4ks[3].bus_Q16[2]
        self.mux4_16.bus_d[3] = self.ram4ks[3].bus_Q16[3]
        self.mux4_16.bus_d[4] = self.ram4ks[3].bus_Q16[4]
        self.mux4_16.bus_d[5] = self.ram4ks[3].bus_Q16[5]
        self.mux4_16.bus_d[6] = self.ram4ks[3].bus_Q16[6]
        self.mux4_16.bus_d[7] = self.ram4ks[3].bus_Q16[7]
        self.mux4_16.bus_d[8] = self.ram4ks[3].bus_Q16[8]
        self.mux4_16.bus_d[9] = self.ram4ks[3].bus_Q16[9]
        self.mux4_16.bus_d[10] = self.ram4ks[3].bus_Q16[10]
        self.mux4_16.bus_d[11] = self.ram4ks[3].bus_Q16[11]
        self.mux4_16.bus_d[12] = self.ram4ks[3].bus_Q16[12]
        self.mux4_16.bus_d[13] = self.ram4ks[3].bus_Q16[13]
        self.mux4_16.bus_d[14] = self.ram4ks[3].bus_Q16[14]
        self.mux4_16.bus_d[15] = self.ram4ks[3].bus_Q16[15]

        # Set the first 2 address lines to select lines of Mux4Way16
        self.mux4_16.pin_sel0 = self.bus_address14[0]
        self.mux4_16.pin_sel1 = self.bus_address14[1]

        # Update the Mux4Way16
        self.mux4_16.update()

        # Set the output of the Mux4Way16 to the output of the RAM16K
        self.bus_Q16[0] = self.mux4_16.bus_x[0]
        self.bus_Q16[1] = self.mux4_16.bus_x[1]
        self.bus_Q16[2] = self.mux4_16.bus_x[2]
        self.bus_Q16[3] = self.mux4_16.bus_x[3]
        self.bus_Q16[4] = self.mux4_16.bus_x[4]
        self.bus_Q16[5] = self.mux4_16.bus_x[5]
        self.bus_Q16[6] = self.mux4_16.bus_x[6]
        self.bus_Q16[7] = self.mux4_16.bus_x[7]
        self.bus_Q16[8] = self.mux4_16.bus_x[8]
        self.bus_Q16[9] = self.mux4_16.bus_x[9]
        self.bus_Q16[10] = self.mux4_16.bus_x[10]
        self.bus_Q16[11] = self.mux4_16.bus_x[11]
        self.bus_Q16[12] = self.mux4_16.bus_x[12]
        self.bus_Q16[13] = self.mux4_16.bus_x[13]
        self.bus_Q16[14] = self.mux4_16.bus_x[14]
        self.bus_Q16[15] = self.mux4_16.bus_x[15]


'''
class PC:
    def __init__(self, d16=[0 for i in range(16)], load=0, reset=0, inc=0, clk=0, Q16=[0 for i in range(16)]):
        self.bus_d16 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.pin_load = 0
        self.pin_reset = 0
        self.pin_inc = 0
        self.pin_clk = 0
        self.pin_Q16 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.register = Register16()
        self.zeros = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def update(self):
        inc1 = alu.Inc16(self.Q16)
        inc1.update()
        mux1 = lg.Mux16(self.d16, inc1.sum16, [self.inc for i in range(16)])
        mux1.update()
        mux2 = lg.Mux16(mux1.x16, self.zeros, [self.reset for i in range(16)])
        mux2.update()
        or1 = lg.Or(self.inc, self.load)
        or1.update()
        or2 = lg.Or(or1.x, self.reset)
        or2.update()
        self.register.d16 = mux2.x16
        self.register.load = or2.x
        self.register.clk = self.clk
        self.register.update()
        self.Q16 = self.register.Q16
        return(self.Q16)
'''


if __name__ == '__main__':
    import pdb 
    pdb.set_trace()
    print("Making a RAM8")
    my_RAM8 = RAM8()
    print("Making a RAM64")
    my_RAM64 = RAM64()
    print("Making a RAM512")
    my_RAM512 = RAM512()
    #print("Making a RAM4K")
    #my_RAM4K = RAM4K()
    #print("Making a RAM16K")
    #my_RAM16K = RAM16K()
    

    for ii in range(8):
        for jj in range(8):
            for kk in range(8):
                print(my_RAM512.ram64s[ii].ram8s[jj].registers[kk].bus_Q16)
    print("=======================================================================")

    my_RAM512.bus_address9 = [1, 1, 1, 1, 1, 1, 1, 1, 1]
    my_RAM512.bus_d16 = [1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0]
    my_RAM512.pin_load = 1
    my_RAM512.pin_clk = 0
    my_RAM512.update()
    my_RAM512.pin_clk = 1
    my_RAM512.update()

    for ii in range(8):
        for jj in range(8):
            for kk in range(8):
                print(my_RAM512.ram64s[ii].ram8s[jj].registers[kk].bus_Q16)
