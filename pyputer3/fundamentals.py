#! /usr/bin/python3

class NandGate:
    def __init__(self):
        self.pin_a = 0
        self.pin_b = 0
        self.pin_x = 0

    def update(self):
        if(self.pin_a and self.pin_b):
            self.pin_x = 0
        else:
            self.pin_x = 1


class NotGate:
    def __init__(self):
        self.pin_a = 0
        self.pin_x = 0
        
        self.nand = NandGate()

    def update(self):
        self.nand.pin_a = self.pin_a
        self.nand.pin_b = self.pin_a
        self.nand.update()

        self.pin_x = self.nand.pin_x

class AndGate:
    def __init__(self):
        self.pin_a = 0
        self.pin_b = 0
        self.pin_x = 0

        self.notGate = NotGate()
        self.nand = NandGate()

    def update(self):
        self.nand.pin_a = self.pin_a
        self.nand.pin_b = self.pin_b
        self.nand.update()

        self.notGate.pin_a = self.nand.pin_x
        self.notGate.update()
        
        self.pin_x = self.notGate.pin_x

class OrGate:
    def __init__(self):
        self.pin_a = 0
        self.pin_b = 0
        self.pin_x = 0

        self.not1 = NotGate()
        self.not2 = NotGate()
        self.nand = NandGate()
    
    def update(self):
        self.not1.pin_a = self.pin_a
        self.not2.pin_a = self.pin_b
        self.not1.update()
        self.not2.update()
        self.nand.pin_a = self.not1.pin_x
        self.nand.pin_b = self.not2.pin_x
        self.nand.update()
        self.pin_x = self.nand.pin_x 

class XorGate:
    def __init__(self):
        self.pin_a = 0
        self.pin_b = 0
        self.pin_x = 0

        self.not1 = NotGate()
        self.not2 = NotGate()
        self.and1 = AndGate()
        self.and2 = AndGate()
        self.orGate = OrGate()

    def update(self):
        self.not1.pin_a = self.pin_a
        self.not2.pin_a = self.pin_b
        self.not1.update()
        self.not2.update()
        self.and1.pin_a = self.pin_b
        self.and1.pin_b = self.not1.pin_x
        self.and2.pin_a = self.not2.pin_x
        self.and2.pin_b = self.pin_a
        self.and1.update()
        self.and2.update()
        self.orGate.pin_a = self.and1.pin_x
        self.orGate.pin_b = self.and2.pin_x
        self.orGate.update()
        self.pin_x = self.orGate.pin_x

class MuxGate:
    def __init__(self):
        self.pin_a = 0
        self.pin_b = 0
        self.pin_sel = 0
        self.pin_x = 0

        self.notGate = NotGate()
        self.and1 = AndGate()
        self.and2 = AndGate()
        self.orGate = OrGate()

    def update(self):
        self.notGate.pin_a = self.pin_sel
        self.notGate.update()
        self.and1.pin_a = self.pin_a
        self.and1.pin_b = self.notGate.pin_x
        self.and2.pin_a = self.pin_sel
        self.and2.pin_b = self.pin_b
        self.and1.update()
        self.and2.update()
        self.orGate.pin_a = self.and1.pin_x
        self.orGate.pin_b = self.and2.pin_x 
        self.orGate.update()
        self.pin_x = self.orGate.pin_x

class DMuxGate:
    def __init__(self):
        self.pin_a = 0
        self.pin_sel = 0
        self.pin_x = 0
        self.pin_y = 0

        self.notGate = NotGate()
        self.and1 = AndGate()
        self.and2 = AndGate()

    def update(self):
        self.notGate.pin_a = self.pin_sel
        self.notGate.update()
        self.and1.pin_a = self.pin_a
        self.and1.pin_b = self.notGate.pin_x
        self.and2.pin_a = self.pin_sel
        self.and2.pin_b = self.pin_a
        self.and1.update()
        self.and2.update()
        self.pin_x = self.and1.pin_x
        self.pin_y = self.and2.pin_x

class Not16:
    def __init__(self):
        self.pin_a_bus = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.pin_x_bus = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.not0 = NotGate()
        self.not1 = NotGate()
        self.not2 = NotGate()
        self.not3 = NotGate()
        self.not4 = NotGate()
        self.not5 = NotGate()
        self.not6 = NotGate()
        self.not7 = NotGate()
        self.not8 = NotGate()
        self.not9 = NotGate()
        self.not10 = NotGate()
        self.not11 = NotGate()
        self.not12 = NotGate()
        self.not13 = NotGate()
        self.not14 = NotGate()
        self.not15 = NotGate()

    def update(self):
        self.not0.pin_a = self.pin_a_bus[0]
        self.not1.pin_a = self.pin_a_bus[1]
        self.not2.pin_a = self.pin_a_bus[2]
        self.not3.pin_a = self.pin_a_bus[3]
        self.not4.pin_a = self.pin_a_bus[4]
        self.not5.pin_a = self.pin_a_bus[5]
        self.not6.pin_a = self.pin_a_bus[6]
        self.not7.pin_a = self.pin_a_bus[7]
        self.not8.pin_a = self.pin_a_bus[8]
        self.not9.pin_a = self.pin_a_bus[9]
        self.not10.pin_a = self.pin_a_bus[10]
        self.not11.pin_a = self.pin_a_bus[11]
        self.not12.pin_a = self.pin_a_bus[12]
        self.not13.pin_a = self.pin_a_bus[13]
        self.not14.pin_a = self.pin_a_bus[14]
        self.not15.pin_a = self.pin_a_bus[15]

        self.not0.update()
        self.not1.update()
        self.not2.update()
        self.not3.update()
        self.not4.update()
        self.not5.update()
        self.not6.update()
        self.not7.update()
        self.not8.update()
        self.not9.update()
        self.not10.update()
        self.not11.update()
        self.not12.update()
        self.not13.update()
        self.not14.update()
        self.not15.update()

        self.pin_x_bus[0] = self.not0.pin_x
        self.pin_x_bus[1] = self.not1.pin_x
        self.pin_x_bus[2] = self.not2.pin_x
        self.pin_x_bus[3] = self.not3.pin_x
        self.pin_x_bus[4] = self.not4.pin_x
        self.pin_x_bus[5] = self.not5.pin_x
        self.pin_x_bus[6] = self.not6.pin_x
        self.pin_x_bus[7] = self.not7.pin_x
        self.pin_x_bus[8] = self.not8.pin_x
        self.pin_x_bus[9] = self.not9.pin_x
        self.pin_x_bus[10] = self.not10.pin_x
        self.pin_x_bus[11] = self.not11.pin_x
        self.pin_x_bus[12] = self.not12.pin_x
        self.pin_x_bus[13] = self.not13.pin_x
        self.pin_x_bus[14] = self.not14.pin_x
        self.pin_x_bus[15] = self.not15.pin_x

class And16:
    def __init__(self):
        self.pin_a_bus = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.pin_b_bus = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.pin_x_bus = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.and0 = AndGate()
        self.and1 = AndGate()
        self.and2 = AndGate()
        self.and3 = AndGate()
        self.and4 = AndGate()
        self.and5 = AndGate()
        self.and6 = AndGate()
        self.and7 = AndGate()
        self.and8 = AndGate()
        self.and9 = AndGate()
        self.and10 = AndGate()
        self.and11 = AndGate()
        self.and12 = AndGate()
        self.and13 = AndGate()
        self.and14 = AndGate()
        self.and15 = AndGate()

    def update(self):
        self.and0.pin_a = self.pin_a_bus[0]
        self.and1.pin_a = self.pin_a_bus[1]
        self.and2.pin_a = self.pin_a_bus[2]
        self.and3.pin_a = self.pin_a_bus[3]
        self.and4.pin_a = self.pin_a_bus[4]
        self.and5.pin_a = self.pin_a_bus[5]
        self.and6.pin_a = self.pin_a_bus[6]
        self.and7.pin_a = self.pin_a_bus[7]
        self.and8.pin_a = self.pin_a_bus[8]
        self.and9.pin_a = self.pin_a_bus[9]
        self.and10.pin_a = self.pin_a_bus[10]
        self.and11.pin_a = self.pin_a_bus[11]
        self.and12.pin_a = self.pin_a_bus[12]
        self.and13.pin_a = self.pin_a_bus[13]
        self.and14.pin_a = self.pin_a_bus[14]
        self.and15.pin_a = self.pin_a_bus[15]

        self.and0.pin_b = self.pin_b_bus[0]
        self.and1.pin_b = self.pin_b_bus[1]
        self.and2.pin_b = self.pin_b_bus[2]
        self.and3.pin_b = self.pin_b_bus[3]
        self.and4.pin_b = self.pin_b_bus[4]
        self.and5.pin_b = self.pin_b_bus[5]
        self.and6.pin_b = self.pin_b_bus[6]
        self.and7.pin_b = self.pin_b_bus[7]
        self.and8.pin_b = self.pin_b_bus[8]
        self.and9.pin_b = self.pin_b_bus[9]
        self.and10.pin_b = self.pin_b_bus[10]
        self.and11.pin_b = self.pin_b_bus[11]
        self.and12.pin_b = self.pin_b_bus[12]
        self.and13.pin_b = self.pin_b_bus[13]
        self.and14.pin_b = self.pin_b_bus[14]
        self.and15.pin_b = self.pin_b_bus[15]

        self.and0.update()
        self.and1.update()
        self.and2.update()
        self.and3.update()
        self.and4.update()
        self.and5.update()
        self.and6.update()
        self.and7.update()
        self.and8.update()
        self.and9.update()
        self.and10.update()
        self.and11.update()
        self.and12.update()
        self.and13.update()
        self.and14.update()
        self.and15.update()

        self.pin_x_bus[0] = self.and0.pin_x
        self.pin_x_bus[1] = self.and1.pin_x
        self.pin_x_bus[2] = self.and2.pin_x
        self.pin_x_bus[3] = self.and3.pin_x
        self.pin_x_bus[4] = self.and4.pin_x
        self.pin_x_bus[5] = self.and5.pin_x
        self.pin_x_bus[6] = self.and6.pin_x
        self.pin_x_bus[7] = self.and7.pin_x
        self.pin_x_bus[8] = self.and8.pin_x
        self.pin_x_bus[9] = self.and9.pin_x
        self.pin_x_bus[10] = self.and10.pin_x
        self.pin_x_bus[11] = self.and11.pin_x
        self.pin_x_bus[12] = self.and12.pin_x
        self.pin_x_bus[13] = self.and13.pin_x
        self.pin_x_bus[14] = self.and14.pin_x
        self.pin_x_bus[15] = self.and15.pin_x

class Or16:
    def __init__(self):
        self.pin_a_bus = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.pin_b_bus = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.pin_x_bus = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.or0 = OrGate()
        self.or1 = OrGate()
        self.or2 = OrGate()
        self.or3 = OrGate()
        self.or4 = OrGate()
        self.or5 = OrGate()
        self.or6 = OrGate()
        self.or7 = OrGate()
        self.or8 = OrGate()
        self.or9 = OrGate()
        self.or10 = OrGate()
        self.or11 = OrGate()
        self.or12 = OrGate()
        self.or13 = OrGate()
        self.or14 = OrGate()
        self.or15 = OrGate()

    def update(self):
        self.or0.pin_a = self.pin_a_bus[0]
        self.or1.pin_a = self.pin_a_bus[1]
        self.or2.pin_a = self.pin_a_bus[2]
        self.or3.pin_a = self.pin_a_bus[3]
        self.or4.pin_a = self.pin_a_bus[4]
        self.or5.pin_a = self.pin_a_bus[5]
        self.or6.pin_a = self.pin_a_bus[6]
        self.or7.pin_a = self.pin_a_bus[7]
        self.or8.pin_a = self.pin_a_bus[8]
        self.or9.pin_a = self.pin_a_bus[9]
        self.or10.pin_a = self.pin_a_bus[10]
        self.or11.pin_a = self.pin_a_bus[11]
        self.or12.pin_a = self.pin_a_bus[12]
        self.or13.pin_a = self.pin_a_bus[13]
        self.or14.pin_a = self.pin_a_bus[14]
        self.or15.pin_a = self.pin_a_bus[15]

        self.or0.pin_b = self.pin_b_bus[0]
        self.or1.pin_b = self.pin_b_bus[1]
        self.or2.pin_b = self.pin_b_bus[2]
        self.or3.pin_b = self.pin_b_bus[3]
        self.or4.pin_b = self.pin_b_bus[4]
        self.or5.pin_b = self.pin_b_bus[5]
        self.or6.pin_b = self.pin_b_bus[6]
        self.or7.pin_b = self.pin_b_bus[7]
        self.or8.pin_b = self.pin_b_bus[8]
        self.or9.pin_b = self.pin_b_bus[9]
        self.or10.pin_b = self.pin_b_bus[10]
        self.or11.pin_b = self.pin_b_bus[11]
        self.or12.pin_b = self.pin_b_bus[12]
        self.or13.pin_b = self.pin_b_bus[13]
        self.or14.pin_b = self.pin_b_bus[14]
        self.or15.pin_b = self.pin_b_bus[15]

        self.or0.update()
        self.or1.update()
        self.or2.update()
        self.or3.update()
        self.or4.update()
        self.or5.update()
        self.or6.update()
        self.or7.update()
        self.or8.update()
        self.or9.update()
        self.or10.update()
        self.or11.update()
        self.or12.update()
        self.or13.update()
        self.or14.update()
        self.or15.update()

        self.pin_x_bus[0] = self.or0.pin_x
        self.pin_x_bus[1] = self.or1.pin_x
        self.pin_x_bus[2] = self.or2.pin_x
        self.pin_x_bus[3] = self.or3.pin_x
        self.pin_x_bus[4] = self.or4.pin_x
        self.pin_x_bus[5] = self.or5.pin_x
        self.pin_x_bus[6] = self.or6.pin_x
        self.pin_x_bus[7] = self.or7.pin_x
        self.pin_x_bus[8] = self.or8.pin_x
        self.pin_x_bus[9] = self.or9.pin_x
        self.pin_x_bus[10] = self.or10.pin_x
        self.pin_x_bus[11] = self.or11.pin_x
        self.pin_x_bus[12] = self.or12.pin_x
        self.pin_x_bus[13] = self.or13.pin_x
        self.pin_x_bus[14] = self.or14.pin_x
        self.pin_x_bus[15] = self.or15.pin_x

class Mux16:
    def __init__(self):
        self.pin_a_bus = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.pin_b_bus = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.pin_sel = 0
        self.pin_x_bus = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.mux0 = MuxGate()
        self.mux1 = MuxGate()
        self.mux2 = MuxGate()
        self.mux3 = MuxGate()
        self.mux4 = MuxGate()
        self.mux5 = MuxGate()
        self.mux6 = MuxGate()
        self.mux7 = MuxGate()
        self.mux8 = MuxGate()
        self.mux9 = MuxGate()
        self.mux10 = MuxGate()
        self.mux11 = MuxGate()
        self.mux12 = MuxGate()
        self.mux13 = MuxGate()
        self.mux14 = MuxGate()
        self.mux15 = MuxGate()

    def update(self):
        self.mux0.pin_sel = self.pin_sel
        self.mux1.pin_sel = self.pin_sel
        self.mux2.pin_sel = self.pin_sel
        self.mux3.pin_sel = self.pin_sel
        self.mux4.pin_sel = self.pin_sel
        self.mux5.pin_sel = self.pin_sel
        self.mux6.pin_sel = self.pin_sel
        self.mux7.pin_sel = self.pin_sel
        self.mux8.pin_sel = self.pin_sel
        self.mux9.pin_sel = self.pin_sel
        self.mux10.pin_sel = self.pin_sel
        self.mux11.pin_sel = self.pin_sel
        self.mux12.pin_sel = self.pin_sel
        self.mux13.pin_sel = self.pin_sel
        self.mux14.pin_sel = self.pin_sel
        self.mux15.pin_sel = self.pin_sel

        self.mux0.pin_a = self.pin_a_bus[0]
        self.mux1.pin_a = self.pin_a_bus[1]
        self.mux2.pin_a = self.pin_a_bus[2]
        self.mux3.pin_a = self.pin_a_bus[3]
        self.mux4.pin_a = self.pin_a_bus[4]
        self.mux5.pin_a = self.pin_a_bus[5]
        self.mux6.pin_a = self.pin_a_bus[6]
        self.mux7.pin_a = self.pin_a_bus[7]
        self.mux8.pin_a = self.pin_a_bus[8]
        self.mux9.pin_a = self.pin_a_bus[9]
        self.mux10.pin_a = self.pin_a_bus[10]
        self.mux11.pin_a = self.pin_a_bus[11]
        self.mux12.pin_a = self.pin_a_bus[12]
        self.mux13.pin_a = self.pin_a_bus[13]
        self.mux14.pin_a = self.pin_a_bus[14]
        self.mux15.pin_a = self.pin_a_bus[15]

        self.mux0.pin_b = self.pin_b_bus[0]
        self.mux1.pin_b = self.pin_b_bus[1]
        self.mux2.pin_b = self.pin_b_bus[2]
        self.mux3.pin_b = self.pin_b_bus[3]
        self.mux4.pin_b = self.pin_b_bus[4]
        self.mux5.pin_b = self.pin_b_bus[5]
        self.mux6.pin_b = self.pin_b_bus[6]
        self.mux7.pin_b = self.pin_b_bus[7]
        self.mux8.pin_b = self.pin_b_bus[8]
        self.mux9.pin_b = self.pin_b_bus[9]
        self.mux10.pin_b = self.pin_b_bus[10]
        self.mux11.pin_b = self.pin_b_bus[11]
        self.mux12.pin_b = self.pin_b_bus[12]
        self.mux13.pin_b = self.pin_b_bus[13]
        self.mux14.pin_b = self.pin_b_bus[14]
        self.mux15.pin_b = self.pin_b_bus[15]

        self.mux0.update()
        self.mux1.update()
        self.mux2.update()
        self.mux3.update()
        self.mux4.update()
        self.mux5.update()
        self.mux6.update()
        self.mux7.update()
        self.mux8.update()
        self.mux9.update()
        self.mux10.update()
        self.mux11.update()
        self.mux12.update()
        self.mux13.update()
        self.mux14.update()
        self.mux15.update()

        self.pin_x_bus[0] = self.mux0.pin_x
        self.pin_x_bus[1] = self.mux1.pin_x
        self.pin_x_bus[2] = self.mux2.pin_x
        self.pin_x_bus[3] = self.mux3.pin_x
        self.pin_x_bus[4] = self.mux4.pin_x
        self.pin_x_bus[5] = self.mux5.pin_x
        self.pin_x_bus[6] = self.mux6.pin_x
        self.pin_x_bus[7] = self.mux7.pin_x
        self.pin_x_bus[8] = self.mux8.pin_x
        self.pin_x_bus[9] = self.mux9.pin_x
        self.pin_x_bus[10] = self.mux10.pin_x
        self.pin_x_bus[11] = self.mux11.pin_x
        self.pin_x_bus[12] = self.mux12.pin_x
        self.pin_x_bus[13] = self.mux13.pin_x
        self.pin_x_bus[14] = self.mux14.pin_x
        self.pin_x_bus[15] = self.mux15.pin_x


class Or8Way:
    def __init__(self):
        self.pin_a = 0
        self.pin_b = 0
        self.pin_c = 0
        self.pin_d = 0
        self.pin_e = 0
        self.pin_f = 0
        self.pin_g = 0
        self.pin_h = 0

        self.or00 = OrGate()
        self.or01 = OrGate()
        self.or02 = OrGate()
        self.or03 = OrGate()
        self.or10 = OrGate()
        self.or11 = OrGate()
        self.or20 = OrGate()

    def update(self):
        self.or00.pin_a = self.pin_a
        self.or00.pin_b = self.pin_b
        self.or01.pin_a = self.pin_c
        self.or01.pin_b = self.pin_d
        self.or02.pin_a = self.pin_e
        self.or02.pin_b = self.pin_f
        self.or03.pin_a = self.pin_g
        self.or03.pin_b = self.pin_h

        self.or00.update()
        self.or01.update()
        self.or02.update()
        self.or03.update()

        self.or10.pin_a = self.or00.pin_x
        self.or10.pin_b = self.or01.pin_x
        self.or11.pin_a = self.or02.pin_x
        self.or11.pin_b = self.or03.pin_x

        self.or10.update()
        self.or11.update()

        self.or20.pin_a = self.or10.pin_x
        self.or20.pin_b = self.or11.pin_x

        self.or20.update()

        self.pin_x = self.or20.pin_x


class Mux4Way16:
    def __init__(self):
        self.pin_a_bus = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.pin_b_bus = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.pin_c_bus = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.pin_d_bus = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.pin_sel0 = 0
        self.pin_sel1 = 0

        self.pin_x_bus = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.mux00 = Mux16()
        self.mux01 = Mux16()
        self.mux10 = Mux16()

    def update(self):
        self.mux00.pin_a_bus[0] = self.pin_a_bus[0]
        self.mux00.pin_a_bus[1] = self.pin_a_bus[1]
        self.mux00.pin_a_bus[2] = self.pin_a_bus[2]
        self.mux00.pin_a_bus[3] = self.pin_a_bus[3]
        self.mux00.pin_a_bus[4] = self.pin_a_bus[4]
        self.mux00.pin_a_bus[5] = self.pin_a_bus[5]
        self.mux00.pin_a_bus[6] = self.pin_a_bus[6]
        self.mux00.pin_a_bus[7] = self.pin_a_bus[7]
        self.mux00.pin_a_bus[8] = self.pin_a_bus[8]
        self.mux00.pin_a_bus[9] = self.pin_a_bus[9]
        self.mux00.pin_a_bus[10] = self.pin_a_bus[10]
        self.mux00.pin_a_bus[11] = self.pin_a_bus[11]
        self.mux00.pin_a_bus[12] = self.pin_a_bus[12]
        self.mux00.pin_a_bus[13] = self.pin_a_bus[13]
        self.mux00.pin_a_bus[14] = self.pin_a_bus[14]
        self.mux00.pin_a_bus[15] = self.pin_a_bus[15]

        self.mux00.pin_b_bus[0] = self.pin_b_bus[0]
        self.mux00.pin_b_bus[1] = self.pin_b_bus[1]
        self.mux00.pin_b_bus[2] = self.pin_b_bus[2]
        self.mux00.pin_b_bus[3] = self.pin_b_bus[3]
        self.mux00.pin_b_bus[4] = self.pin_b_bus[4]
        self.mux00.pin_b_bus[5] = self.pin_b_bus[5]
        self.mux00.pin_b_bus[6] = self.pin_b_bus[6]
        self.mux00.pin_b_bus[7] = self.pin_b_bus[7]
        self.mux00.pin_b_bus[8] = self.pin_b_bus[8]
        self.mux00.pin_b_bus[9] = self.pin_b_bus[9]
        self.mux00.pin_b_bus[10] = self.pin_b_bus[10]
        self.mux00.pin_b_bus[11] = self.pin_b_bus[11]
        self.mux00.pin_b_bus[12] = self.pin_b_bus[12]
        self.mux00.pin_b_bus[13] = self.pin_b_bus[13]
        self.mux00.pin_b_bus[14] = self.pin_b_bus[14]
        self.mux00.pin_b_bus[15] = self.pin_b_bus[15]

        self.mux00.pin_sel = self.pin_sel0

        self.mux01.pin_a_bus[0] = self.pin_c_bus[0]
        self.mux01.pin_a_bus[1] = self.pin_c_bus[1]
        self.mux01.pin_a_bus[2] = self.pin_c_bus[2]
        self.mux01.pin_a_bus[3] = self.pin_c_bus[3]
        self.mux01.pin_a_bus[4] = self.pin_c_bus[4]
        self.mux01.pin_a_bus[5] = self.pin_c_bus[5]
        self.mux01.pin_a_bus[6] = self.pin_c_bus[6]
        self.mux01.pin_a_bus[7] = self.pin_c_bus[7]
        self.mux01.pin_a_bus[8] = self.pin_c_bus[8]
        self.mux01.pin_a_bus[9] = self.pin_c_bus[9]
        self.mux01.pin_a_bus[10] = self.pin_c_bus[10]
        self.mux01.pin_a_bus[11] = self.pin_c_bus[11]
        self.mux01.pin_a_bus[12] = self.pin_c_bus[12]
        self.mux01.pin_a_bus[13] = self.pin_c_bus[13]
        self.mux01.pin_a_bus[14] = self.pin_c_bus[14]
        self.mux01.pin_a_bus[15] = self.pin_c_bus[15]

        self.mux01.pin_b_bus[0] = self.pin_d_bus[0]
        self.mux01.pin_b_bus[1] = self.pin_d_bus[1]
        self.mux01.pin_b_bus[2] = self.pin_d_bus[2]
        self.mux01.pin_b_bus[3] = self.pin_d_bus[3]
        self.mux01.pin_b_bus[4] = self.pin_d_bus[4]
        self.mux01.pin_b_bus[5] = self.pin_d_bus[5]
        self.mux01.pin_b_bus[6] = self.pin_d_bus[6]
        self.mux01.pin_b_bus[7] = self.pin_d_bus[7]
        self.mux01.pin_b_bus[8] = self.pin_d_bus[8]
        self.mux01.pin_b_bus[9] = self.pin_d_bus[9]
        self.mux01.pin_b_bus[10] = self.pin_d_bus[10]
        self.mux01.pin_b_bus[11] = self.pin_d_bus[11]
        self.mux01.pin_b_bus[12] = self.pin_d_bus[12]
        self.mux01.pin_b_bus[13] = self.pin_d_bus[13]
        self.mux01.pin_b_bus[14] = self.pin_d_bus[14]
        self.mux01.pin_b_bus[15] = self.pin_d_bus[15]

        self.mux01.pin_sel = self.pin_sel0

        self.mux00.update()
        self.mux01.update()

        self.mux10.pin_a_bus[0] = self.mux00.pin_x_bus[0]
        self.mux10.pin_a_bus[1] = self.mux00.pin_x_bus[1]
        self.mux10.pin_a_bus[2] = self.mux00.pin_x_bus[2]
        self.mux10.pin_a_bus[3] = self.mux00.pin_x_bus[3]
        self.mux10.pin_a_bus[4] = self.mux00.pin_x_bus[4]
        self.mux10.pin_a_bus[5] = self.mux00.pin_x_bus[5]
        self.mux10.pin_a_bus[6] = self.mux00.pin_x_bus[6]
        self.mux10.pin_a_bus[7] = self.mux00.pin_x_bus[7]
        self.mux10.pin_a_bus[8] = self.mux00.pin_x_bus[8]
        self.mux10.pin_a_bus[9] = self.mux00.pin_x_bus[9]
        self.mux10.pin_a_bus[10] = self.mux00.pin_x_bus[10]
        self.mux10.pin_a_bus[11] = self.mux00.pin_x_bus[11]
        self.mux10.pin_a_bus[12] = self.mux00.pin_x_bus[12]
        self.mux10.pin_a_bus[13] = self.mux00.pin_x_bus[13]
        self.mux10.pin_a_bus[14] = self.mux00.pin_x_bus[14]
        self.mux10.pin_a_bus[15] = self.mux00.pin_x_bus[15]

        self.mux10.pin_b_bus[0] = self.mux01.pin_x_bus[0]
        self.mux10.pin_b_bus[1] = self.mux01.pin_x_bus[1]
        self.mux10.pin_b_bus[2] = self.mux01.pin_x_bus[2]
        self.mux10.pin_b_bus[3] = self.mux01.pin_x_bus[3]
        self.mux10.pin_b_bus[4] = self.mux01.pin_x_bus[4]
        self.mux10.pin_b_bus[5] = self.mux01.pin_x_bus[5]
        self.mux10.pin_b_bus[6] = self.mux01.pin_x_bus[6]
        self.mux10.pin_b_bus[7] = self.mux01.pin_x_bus[7]
        self.mux10.pin_b_bus[8] = self.mux01.pin_x_bus[8]
        self.mux10.pin_b_bus[9] = self.mux01.pin_x_bus[9]
        self.mux10.pin_b_bus[10] = self.mux01.pin_x_bus[10]
        self.mux10.pin_b_bus[11] = self.mux01.pin_x_bus[11]
        self.mux10.pin_b_bus[12] = self.mux01.pin_x_bus[12]
        self.mux10.pin_b_bus[13] = self.mux01.pin_x_bus[13]
        self.mux10.pin_b_bus[14] = self.mux01.pin_x_bus[14]
        self.mux10.pin_b_bus[15] = self.mux01.pin_x_bus[15]

        self.mux10.pin_sel = self.pin_sel1 

        self.mux10.update()

        self.pin_x_bus[0] = self.mux10.pin_x_bus[0]
        self.pin_x_bus[1] = self.mux10.pin_x_bus[1]
        self.pin_x_bus[2] = self.mux10.pin_x_bus[2]
        self.pin_x_bus[3] = self.mux10.pin_x_bus[3]
        self.pin_x_bus[4] = self.mux10.pin_x_bus[4]
        self.pin_x_bus[5] = self.mux10.pin_x_bus[5]
        self.pin_x_bus[6] = self.mux10.pin_x_bus[6]
        self.pin_x_bus[7] = self.mux10.pin_x_bus[7]
        self.pin_x_bus[8] = self.mux10.pin_x_bus[8]
        self.pin_x_bus[9] = self.mux10.pin_x_bus[9]
        self.pin_x_bus[10] = self.mux10.pin_x_bus[10]
        self.pin_x_bus[11] = self.mux10.pin_x_bus[11]
        self.pin_x_bus[12] = self.mux10.pin_x_bus[12]
        self.pin_x_bus[13] = self.mux10.pin_x_bus[13]
        self.pin_x_bus[14] = self.mux10.pin_x_bus[14]
        self.pin_x_bus[15] = self.mux10.pin_x_bus[15]      

class Mux8Way16:
    def __init__(self):
        self.pin_a_bus = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.pin_b_bus = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.pin_c_bus = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.pin_d_bus = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.pin_e_bus = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.pin_f_bus = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.pin_g_bus = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.pin_h_bus = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        
        self.pin_sel0 = 0
        self.pin_sel1 = 0
        self.pin_sel2 = 0

        self.pin_x_bus = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.mux4way0 = Mux4Way16()
        self.mux4way1 = Mux4Way16()

        self.mux20 = Mux16()

    def update(self):
        self.mux4way0.pin_a_bus[0] = self.pin_a_bus[0]
        self.mux4way0.pin_a_bus[1] = self.pin_a_bus[1]
        self.mux4way0.pin_a_bus[2] = self.pin_a_bus[2]
        self.mux4way0.pin_a_bus[3] = self.pin_a_bus[3]
        self.mux4way0.pin_a_bus[4] = self.pin_a_bus[4]
        self.mux4way0.pin_a_bus[5] = self.pin_a_bus[5]
        self.mux4way0.pin_a_bus[6] = self.pin_a_bus[6]
        self.mux4way0.pin_a_bus[7] = self.pin_a_bus[7]
        self.mux4way0.pin_a_bus[8] = self.pin_a_bus[8]
        self.mux4way0.pin_a_bus[9] = self.pin_a_bus[9]
        self.mux4way0.pin_a_bus[10] = self.pin_a_bus[10]
        self.mux4way0.pin_a_bus[11] = self.pin_a_bus[11]
        self.mux4way0.pin_a_bus[12] = self.pin_a_bus[12]
        self.mux4way0.pin_a_bus[13] = self.pin_a_bus[13]
        self.mux4way0.pin_a_bus[14] = self.pin_a_bus[14]
        self.mux4way0.pin_a_bus[15] = self.pin_a_bus[15]

        self.mux4way0.pin_b_bus[0] = self.pin_b_bus[0]
        self.mux4way0.pin_b_bus[1] = self.pin_b_bus[1]
        self.mux4way0.pin_b_bus[2] = self.pin_b_bus[2]
        self.mux4way0.pin_b_bus[3] = self.pin_b_bus[3]
        self.mux4way0.pin_b_bus[4] = self.pin_b_bus[4]
        self.mux4way0.pin_b_bus[5] = self.pin_b_bus[5]
        self.mux4way0.pin_b_bus[6] = self.pin_b_bus[6]
        self.mux4way0.pin_b_bus[7] = self.pin_b_bus[7]
        self.mux4way0.pin_b_bus[8] = self.pin_b_bus[8]
        self.mux4way0.pin_b_bus[9] = self.pin_b_bus[9]
        self.mux4way0.pin_b_bus[10] = self.pin_b_bus[10]
        self.mux4way0.pin_b_bus[11] = self.pin_b_bus[11]
        self.mux4way0.pin_b_bus[12] = self.pin_b_bus[12]
        self.mux4way0.pin_b_bus[13] = self.pin_b_bus[13]
        self.mux4way0.pin_b_bus[14] = self.pin_b_bus[14]
        self.mux4way0.pin_b_bus[15] = self.pin_b_bus[15]

        self.mux4way0.pin_c_bus[0] = self.pin_c_bus[0]
        self.mux4way0.pin_c_bus[1] = self.pin_c_bus[1]
        self.mux4way0.pin_c_bus[2] = self.pin_c_bus[2]
        self.mux4way0.pin_c_bus[3] = self.pin_c_bus[3]
        self.mux4way0.pin_c_bus[4] = self.pin_c_bus[4]
        self.mux4way0.pin_c_bus[5] = self.pin_c_bus[5]
        self.mux4way0.pin_c_bus[6] = self.pin_c_bus[6]
        self.mux4way0.pin_c_bus[7] = self.pin_c_bus[7]
        self.mux4way0.pin_c_bus[8] = self.pin_c_bus[8]
        self.mux4way0.pin_c_bus[9] = self.pin_c_bus[9]
        self.mux4way0.pin_c_bus[10] = self.pin_c_bus[10]
        self.mux4way0.pin_c_bus[11] = self.pin_c_bus[11]
        self.mux4way0.pin_c_bus[12] = self.pin_c_bus[12]
        self.mux4way0.pin_c_bus[13] = self.pin_c_bus[13]
        self.mux4way0.pin_c_bus[14] = self.pin_c_bus[14]
        self.mux4way0.pin_c_bus[15] = self.pin_c_bus[15]
        
        self.mux4way0.pin_d_bus[0] = self.pin_d_bus[0]
        self.mux4way0.pin_d_bus[1] = self.pin_d_bus[1]
        self.mux4way0.pin_d_bus[2] = self.pin_d_bus[2]
        self.mux4way0.pin_d_bus[3] = self.pin_d_bus[3]
        self.mux4way0.pin_d_bus[4] = self.pin_d_bus[4]
        self.mux4way0.pin_d_bus[5] = self.pin_d_bus[5]
        self.mux4way0.pin_d_bus[6] = self.pin_d_bus[6]
        self.mux4way0.pin_d_bus[7] = self.pin_d_bus[7]
        self.mux4way0.pin_d_bus[8] = self.pin_d_bus[8]
        self.mux4way0.pin_d_bus[9] = self.pin_d_bus[9]
        self.mux4way0.pin_d_bus[10] = self.pin_d_bus[10]
        self.mux4way0.pin_d_bus[11] = self.pin_d_bus[11]
        self.mux4way0.pin_d_bus[12] = self.pin_d_bus[12]
        self.mux4way0.pin_d_bus[13] = self.pin_d_bus[13]
        self.mux4way0.pin_d_bus[14] = self.pin_d_bus[14]
        self.mux4way0.pin_d_bus[15] = self.pin_d_bus[15]
        
        self.mux4way0.pin_sel0 = self.pin_sel0
        self.mux4way0.pin_sel1 = self.pin_sel1 

        self.mux4way1.pin_a_bus[0] = self.pin_e_bus[0]
        self.mux4way1.pin_a_bus[1] = self.pin_e_bus[1]
        self.mux4way1.pin_a_bus[2] = self.pin_e_bus[2]
        self.mux4way1.pin_a_bus[3] = self.pin_e_bus[3]
        self.mux4way1.pin_a_bus[4] = self.pin_e_bus[4]
        self.mux4way1.pin_a_bus[5] = self.pin_e_bus[5]
        self.mux4way1.pin_a_bus[6] = self.pin_e_bus[6]
        self.mux4way1.pin_a_bus[7] = self.pin_e_bus[7]
        self.mux4way1.pin_a_bus[8] = self.pin_e_bus[8]
        self.mux4way1.pin_a_bus[9] = self.pin_e_bus[9]
        self.mux4way1.pin_a_bus[10] = self.pin_e_bus[10]
        self.mux4way1.pin_a_bus[11] = self.pin_e_bus[11]
        self.mux4way1.pin_a_bus[12] = self.pin_e_bus[12]
        self.mux4way1.pin_a_bus[13] = self.pin_e_bus[13]
        self.mux4way1.pin_a_bus[14] = self.pin_e_bus[14]
        self.mux4way1.pin_a_bus[15] = self.pin_e_bus[15]
         
        self.mux4way1.pin_b_bus[0] = self.pin_f_bus[0]
        self.mux4way1.pin_b_bus[1] = self.pin_f_bus[1]
        self.mux4way1.pin_b_bus[2] = self.pin_f_bus[2]
        self.mux4way1.pin_b_bus[3] = self.pin_f_bus[3]
        self.mux4way1.pin_b_bus[4] = self.pin_f_bus[4]
        self.mux4way1.pin_b_bus[5] = self.pin_f_bus[5]
        self.mux4way1.pin_b_bus[6] = self.pin_f_bus[6]
        self.mux4way1.pin_b_bus[7] = self.pin_f_bus[7]
        self.mux4way1.pin_b_bus[8] = self.pin_f_bus[8]
        self.mux4way1.pin_b_bus[9] = self.pin_f_bus[9]
        self.mux4way1.pin_b_bus[10] = self.pin_f_bus[10]
        self.mux4way1.pin_b_bus[11] = self.pin_f_bus[11]
        self.mux4way1.pin_b_bus[12] = self.pin_f_bus[12]
        self.mux4way1.pin_b_bus[13] = self.pin_f_bus[13]
        self.mux4way1.pin_b_bus[14] = self.pin_f_bus[14]
        self.mux4way1.pin_b_bus[15] = self.pin_f_bus[15]
        
        self.mux4way1.pin_c_bus[0] = self.pin_g_bus[0]
        self.mux4way1.pin_c_bus[1] = self.pin_g_bus[1]
        self.mux4way1.pin_c_bus[2] = self.pin_g_bus[2]
        self.mux4way1.pin_c_bus[3] = self.pin_g_bus[3]
        self.mux4way1.pin_c_bus[4] = self.pin_g_bus[4]
        self.mux4way1.pin_c_bus[5] = self.pin_g_bus[5]
        self.mux4way1.pin_c_bus[6] = self.pin_g_bus[6]
        self.mux4way1.pin_c_bus[7] = self.pin_g_bus[7]
        self.mux4way1.pin_c_bus[8] = self.pin_g_bus[8]
        self.mux4way1.pin_c_bus[9] = self.pin_g_bus[9]
        self.mux4way1.pin_c_bus[10] = self.pin_g_bus[10]
        self.mux4way1.pin_c_bus[11] = self.pin_g_bus[11]
        self.mux4way1.pin_c_bus[12] = self.pin_g_bus[12]
        self.mux4way1.pin_c_bus[13] = self.pin_g_bus[13]
        self.mux4way1.pin_c_bus[14] = self.pin_g_bus[14]
        self.mux4way1.pin_c_bus[15] = self.pin_g_bus[15]

        self.mux4way1.pin_d_bus[0] = self.pin_h_bus[0]
        self.mux4way1.pin_d_bus[1] = self.pin_h_bus[1]
        self.mux4way1.pin_d_bus[2] = self.pin_h_bus[2]
        self.mux4way1.pin_d_bus[3] = self.pin_h_bus[3]
        self.mux4way1.pin_d_bus[4] = self.pin_h_bus[4]
        self.mux4way1.pin_d_bus[5] = self.pin_h_bus[5]
        self.mux4way1.pin_d_bus[6] = self.pin_h_bus[6]
        self.mux4way1.pin_d_bus[7] = self.pin_h_bus[7]
        self.mux4way1.pin_d_bus[8] = self.pin_h_bus[8]
        self.mux4way1.pin_d_bus[9] = self.pin_h_bus[9]
        self.mux4way1.pin_d_bus[10] = self.pin_h_bus[10]
        self.mux4way1.pin_d_bus[11] = self.pin_h_bus[11]
        self.mux4way1.pin_d_bus[12] = self.pin_h_bus[12]
        self.mux4way1.pin_d_bus[13] = self.pin_h_bus[13]
        self.mux4way1.pin_d_bus[14] = self.pin_h_bus[14]
        self.mux4way1.pin_d_bus[15] = self.pin_h_bus[15]
        
        self.mux4way1.pin_sel0 = self.pin_sel0 
        self.mux4way1.pin_sel1 = self.pin_sel1 

        self.mux4way0.update()
        self.mux4way1.update()

        self.mux20.pin_a_bus[0] = self.mux4way0.pin_x_bus[0]
        self.mux20.pin_a_bus[1] = self.mux4way0.pin_x_bus[1]
        self.mux20.pin_a_bus[2] = self.mux4way0.pin_x_bus[2]
        self.mux20.pin_a_bus[3] = self.mux4way0.pin_x_bus[3]
        self.mux20.pin_a_bus[4] = self.mux4way0.pin_x_bus[4]
        self.mux20.pin_a_bus[5] = self.mux4way0.pin_x_bus[5]
        self.mux20.pin_a_bus[6] = self.mux4way0.pin_x_bus[6]
        self.mux20.pin_a_bus[7] = self.mux4way0.pin_x_bus[7]
        self.mux20.pin_a_bus[8] = self.mux4way0.pin_x_bus[8]
        self.mux20.pin_a_bus[9] = self.mux4way0.pin_x_bus[9]
        self.mux20.pin_a_bus[10] = self.mux4way0.pin_x_bus[10]
        self.mux20.pin_a_bus[11] = self.mux4way0.pin_x_bus[11]
        self.mux20.pin_a_bus[12] = self.mux4way0.pin_x_bus[12]
        self.mux20.pin_a_bus[13] = self.mux4way0.pin_x_bus[13]
        self.mux20.pin_a_bus[14] = self.mux4way0.pin_x_bus[14]
        self.mux20.pin_a_bus[15] = self.mux4way0.pin_x_bus[15]
        
        self.mux20.pin_b_bus[0] = self.mux4way1.pin_x_bus[0]
        self.mux20.pin_b_bus[1] = self.mux4way1.pin_x_bus[1]
        self.mux20.pin_b_bus[2] = self.mux4way1.pin_x_bus[2]
        self.mux20.pin_b_bus[3] = self.mux4way1.pin_x_bus[3]
        self.mux20.pin_b_bus[4] = self.mux4way1.pin_x_bus[4]
        self.mux20.pin_b_bus[5] = self.mux4way1.pin_x_bus[5]
        self.mux20.pin_b_bus[6] = self.mux4way1.pin_x_bus[6]
        self.mux20.pin_b_bus[7] = self.mux4way1.pin_x_bus[7]
        self.mux20.pin_b_bus[8] = self.mux4way1.pin_x_bus[8]
        self.mux20.pin_b_bus[9] = self.mux4way1.pin_x_bus[9]
        self.mux20.pin_b_bus[10] = self.mux4way1.pin_x_bus[10]
        self.mux20.pin_b_bus[11] = self.mux4way1.pin_x_bus[11]
        self.mux20.pin_b_bus[12] = self.mux4way1.pin_x_bus[12]
        self.mux20.pin_b_bus[13] = self.mux4way1.pin_x_bus[13]
        self.mux20.pin_b_bus[14] = self.mux4way1.pin_x_bus[14]
        self.mux20.pin_b_bus[15] = self.mux4way1.pin_x_bus[15]
        
        self.mux20.pin_sel = self.pin_sel2

        self.mux20.update()

        self.pin_x_bus[0] = self.mux20.pin_x_bus[0]
        self.pin_x_bus[1] = self.mux20.pin_x_bus[1]
        self.pin_x_bus[2] = self.mux20.pin_x_bus[2]
        self.pin_x_bus[3] = self.mux20.pin_x_bus[3]
        self.pin_x_bus[4] = self.mux20.pin_x_bus[4]
        self.pin_x_bus[5] = self.mux20.pin_x_bus[5]
        self.pin_x_bus[6] = self.mux20.pin_x_bus[6]
        self.pin_x_bus[7] = self.mux20.pin_x_bus[7]
        self.pin_x_bus[8] = self.mux20.pin_x_bus[8]
        self.pin_x_bus[9] = self.mux20.pin_x_bus[9]
        self.pin_x_bus[10] = self.mux20.pin_x_bus[10]
        self.pin_x_bus[11] = self.mux20.pin_x_bus[11]
        self.pin_x_bus[12] = self.mux20.pin_x_bus[12]
        self.pin_x_bus[13] = self.mux20.pin_x_bus[13]
        self.pin_x_bus[14] = self.mux20.pin_x_bus[14]
        self.pin_x_bus[15] = self.mux20.pin_x_bus[15]

class DMux4Way:
    def __init__(self):
        self.pin_a = 0

        self.pin_sel0 = 0
        self.pin_sel1 = 0

        self.pin_w = 0
        self.pin_x = 0
        self.pin_y = 0
        self.pin_z = 0

        self.dmux00 = DMuxGate()
        self.dmux10 = DMuxGate()
        self.dmux11 = DMuxGate()

    def update(self):
        self.dmux00.pin_a = self.pin_a
        self.dmux00.pin_sel = self.pin_sel0
        self.dmux00.update()

        self.dmux10.pin_a = self.dmux00.pin_x
        self.dmux11.pin_a = self.dmux00.pin_y
        self.dmux10.pin_sel = self.pin_sel1
        self.dmux11.pin_sel = self.pin_sel1
        self.dmux10.update()
        self.dmux11.update()

        self.pin_w = self.dmux10.pin_x
        self.pin_x = self.dmux10.pin_y
        self.pin_y = self.dmux11.pin_x
        self.pin_z = self.dmux11.pin_y

class DMux8Way:
    def __init__(self):
        self.pin_a = 0
        
        self.pin_sel0 = 0
        self.pin_sel1 = 0
        self.pin_sel2 = 0

        self.pin_s = 0
        self.pin_t = 0
        self.pin_u = 0
        self.pin_v = 0
        self.pin_w = 0
        self.pin_x = 0
        self.pin_y = 0
        self.pin_z = 0

        self.dmux00 = DMuxGate()
        self.dmux10 = DMux4Way()
        self.dmux11 = DMux4Way()

    def update(self):
        self.dmux00.pin_a = self.pin_a
        self.dmux00.pin_sel = self.pin_sel0
        self.dmux00.update()

        self.dmux10.pin_a = self.dmux00.pin_x
        self.dmux10.pin_sel0 = self.pin_sel1
        self.dmux10.pin_sel1 = self.pin_sel2
        self.dmux11.pin_a = self.dmux00.pin_y
        self.dmux11.pin_sel0 = self.pin_sel1
        self.dmux11.pin_sel1 = self.pin_sel2

        self.dmux10.update()
        self.dmux11.update()

        self.pin_s = self.dmux10.pin_w
        self.pin_t = self.dmux10.pin_x
        self.pin_u = self.dmux10.pin_y
        self.pin_v = self.dmux10.pin_z
        self.pin_w = self.dmux11.pin_w
        self.pin_x = self.dmux11.pin_x
        self.pin_y = self.dmux11.pin_y
        self.pin_z = self.dmux11.pin_z
