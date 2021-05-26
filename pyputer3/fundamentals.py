from nand import Nand
#import pdb; pdb.set_trace()

class NotGate:
    def __init__(self):
        self.pin_a = 0
        self.pin_x = 0
        
        self.nand = Nand()

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
        self.nand = Nand()

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
        self.nand = Nand()
    
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


class NotGateTestBench:
    def __init__(self):
        self.notGate = NotGate()
        self.truth_table = [[0, 1], [1, 0]]

    def test(self):
        for solution in self.truth_table:
            self.notGate.pin_a = solution[0]
            self.notGate.update()
            assert self.notGate.pin_x == solution[1]
        print("NotGate test success!")

class AndGateTestBench:
    def __init__(self):
        self.andGate = AndGate()
        self.truth_table = [[[0, 0], [0]], 
                            [[0, 1], [0]], 
                            [[1, 0], [0]], 
                            [[1, 1], [1]]]

    def test(self):
        for solution in self.truth_table:
            self.andGate.pin_a = solution[0][0]
            self.andGate.pin_b = solution[0][1]
            self.andGate.update()
            assert self.andGate.pin_x == solution[1][0]
        print("AndGate test success!")

class OrGateTestBench:
    def __init__(self):
        self.orGate = OrGate()
        self.truth_table = [[[0, 0], [0]], 
                            [[0, 1], [1]], 
                            [[1, 0], [1]], 
                            [[1, 1], [1]]]

    def test(self):
        for solution in self.truth_table:
            self.orGate.pin_a = solution[0][0]
            self.orGate.pin_b = solution[0][1]
            self.orGate.update()
            assert self.orGate.pin_x == solution[1][0]
        print("OrGate test success!")

class XorGateTestBench:
    def __init__(self):
        self.xorGate = XorGate()
        self.truth_table = [[[0, 0], [0]], 
                            [[0, 1], [1]], 
                            [[1, 0], [1]], 
                            [[1, 1], [0]]]

    def test(self):
        for solution in self.truth_table:
            self.xorGate.pin_a = solution[0][0]
            self.xorGate.pin_b = solution[0][1]
            self.xorGate.update()
            assert self.xorGate.pin_x == solution[1][0]
        print("XorGate test success!")

class MuxGateTestBench:
    def __init__(self):
        self.muxGate = MuxGate()
        self.truth_table = [[[0, 0, 0], [0]], 
                            [[0, 0, 1], [0]], 
                            [[0, 1, 0], [0]], 
                            [[0, 1, 1], [1]], 
                            [[1, 0, 0], [1]], 
                            [[1, 0, 1], [0]], 
                            [[1, 1, 0], [1]], 
                            [[1, 1, 1], [1]]]

    def test(self):
        for solution in self.truth_table:
            self.muxGate.pin_a = solution[0][0]
            self.muxGate.pin_b = solution[0][1]
            self.muxGate.pin_sel = solution[0][2]
            self.muxGate.update()
            assert self.muxGate.pin_x == solution[1][0]
        print("MuxGate test success!")

class DMuxGateTestBench:
    def __init__(self):
        self.dMux = DMuxGate()
        self.truth_table = [[[0, 0], [0, 0]],
                            [[0, 1], [0, 0]],
                            [[1, 0], [1, 0]],
                            [[1, 1], [0, 1]]]

    def test(self):
        for solution in self.truth_table:
            self.dMux.pin_a = solution[0][0]
            self.dMux.pin_sel = solution[0][1]
            self.dMux.update()
            assert self.dMux.pin_x == solution[1][0]
            assert self.dMux.pin_y == solution[1][1]
        print("DMuxGate test success!")

class Not16TestBench:
    def __init__(self, testCycles=100):
        self.not16 = Not16()
        self.truth_table = []
        for cycle in range(testCycles):
            test_bus_a = [random.choice([0, 1]) for ii in range(16)]
            test_bus_x = [self.notFunction(ii) for ii in test_bus_a]
            self.truth_table.append([test_bus_a, test_bus_x])

    def notFunction(self, pin_a_in):
        if(pin_a_in == 0):
            return(1)
        else:
            return(0)

    def test(self):
        for solution in self.truth_table:
            for ii in range(16):
                self.not16.pin_a_bus[ii] = solution[0][ii]
            self.not16.update()
            for ii in range(16):
                assert self.not16.pin_x_bus[ii] == solution[1][ii]

        print("Not16 test success!")

class And16TestBench:
    def __init__(self, testCycles=100):
        self.and16 = And16()
        self.truth_table = []
        for cycle in range(testCycles):
            test_bus_a = [random.choice([0, 1]) for ii in range(16)]
            test_bus_b = [random.choice([0, 1]) for ii in range(16)]
            test_bus_x = [self.andFunction(ii, jj) for ii, jj in zip(test_bus_a, test_bus_b)]
            self.truth_table.append([[test_bus_a, test_bus_b], [test_bus_x]])

    def andFunction(self, pin_a_in, pin_b_in):
        if(pin_a_in and pin_b_in):
            return(1)
        else:
            return(0)

    def test(self):
        for solution in self.truth_table:
            for ii in range(16):
                self.and16.pin_a_bus[ii] = solution[0][0][ii]
                self.and16.pin_b_bus[ii] = solution[0][1][ii]
            self.and16.update()
            for ii in range(16):
                assert self.and16.pin_x_bus[ii] == solution[1][0][ii]

        print("And16 test success!")

class Or16TestBench:
    def __init__(self, testCycles=100):
        self.or16 = Or16()
        self.truth_table = []
        for cycle in range(testCycles):
            test_bus_a = [random.choice([0, 1]) for ii in range(16)]
            test_bus_b = [random.choice([0, 1]) for ii in range(16)]
            test_bus_x = [self.orFunction(ii, jj) for ii, jj in zip(test_bus_a, test_bus_b)]
            self.truth_table.append([[test_bus_a, test_bus_b], [test_bus_x]])

    def orFunction(self, pin_a_in, pin_b_in):
        if(pin_a_in or pin_b_in):
            return(1)
        else:
            return(0)

    def test(self):
        for solution in self.truth_table:
            for ii in range(16):
                self.or16.pin_a_bus[ii] = solution[0][0][ii]
                self.or16.pin_b_bus[ii] = solution[0][1][ii]
            self.or16.update()
            for ii in range(16):
                assert self.or16.pin_x_bus[ii] == solution[1][0][ii]

        print("Or16 test success!")

class Mux16TestBench:
    def __init__(self, testCycles=100):
        self.mux16 = Mux16()
        self.truth_table = []
        for cycle in range(testCycles):
            test_bus_a = [random.choice([0, 1]) for ii in range(16)]
            test_bus_b = [random.choice([0, 1]) for ii in range(16)]
            test_sel = random.choice([0, 1])
            test_bus_x = [self.muxFunction(ii, jj, test_sel) for ii, jj in zip(test_bus_a, test_bus_b)]
            self.truth_table.append([[test_bus_a, test_bus_b, test_sel], [test_bus_x]])

    def muxFunction(self, pin_a_in, pin_b_in, pin_sel_in):
        if(pin_sel_in):
            return(pin_b_in)
        else:
            return(pin_a_in)

    def test(self):
        for solution in self.truth_table:
            for ii in range(16):
                self.mux16.pin_a_bus[ii] = solution[0][0][ii]
                self.mux16.pin_b_bus[ii] = solution[0][1][ii]
            self.mux16.pin_sel = solution[0][2]
            self.mux16.update()
            for ii in range(16):
                assert self.mux16.pin_x_bus[ii] == solution[1][0][ii]

        print("Mux16 test success!")

class Or8WayTestBench:
    def __init__(self, testCycles=100):
        self.or8way = Or8Way()
        self.truth_table = []
        for cycle in range(testCycles):
            test_input_bus = [random.choice([0, 1]) for ii in range(8)]
            if any(test_input_bus):
                test_pin_x = 1
            else:
                test_pin_x = 0
            self.truth_table.append([test_input_bus, test_pin_x])

    def test(self):
        for solution in self.truth_table:
            self.or8way.pin_a = solution[0][0]
            self.or8way.pin_b = solution[0][1]
            self.or8way.pin_c = solution[0][2]
            self.or8way.pin_d = solution[0][3]
            self.or8way.pin_e = solution[0][4]
            self.or8way.pin_f = solution[0][5]
            self.or8way.pin_g = solution[0][6]
            self.or8way.pin_h = solution[0][7]

            self.or8way.update()

            assert self.or8way.pin_x == solution[1]
        print("Or8Way test success!")

class Mux4Way16TestBench:
    def __init__(self, testCycles=100):
        self.mux4way16 = Mux4Way16()
        self.truth_table = []
        for cycle in range(testCycles):
            test_a_bus = [random.choice([0, 1]) for ii in range(16)]
            test_b_bus = [random.choice([0, 1]) for ii in range(16)]
            test_c_bus = [random.choice([0, 1]) for ii in range(16)]
            test_d_bus = [random.choice([0, 1]) for ii in range(16)]
            test_sel0 = random.choice([0, 1])
            test_sel1 = random.choice([0, 1])

            test_x_bus = self.thisFunction(test_a_bus, test_b_bus, test_c_bus, test_d_bus, test_sel0, test_sel1)
            self.truth_table.append([[test_a_bus, test_b_bus, test_c_bus, test_d_bus, test_sel0, test_sel1], test_x_bus])

    def thisFunction(self, test_a_bus_in, test_b_bus_in, test_c_bus_in, test_d_bus_in, test_sel0_in, test_sel1_in):
        if(not(test_sel1_in) and not(test_sel0_in)):
            test_x_bus_out = test_a_bus_in
        elif(not(test_sel1_in) and test_sel0_in):
            test_x_bus_out = test_b_bus_in 
        elif(test_sel1_in and not(test_sel0_in)):
            test_x_bus_out = test_c_bus_in 
        elif(test_sel1_in and test_sel0_in):
            test_x_bus_out = test_d_bus_in
        else:
            print("Error: invalid values on sel lines in Mux4Way16TestBench")
            exit(1)
        return(test_x_bus_out)

    def test(self):
        for solution in self.truth_table:
            for ii in range(16):
                self.mux4way16.pin_a_bus[ii] = solution[0][0][ii]
                self.mux4way16.pin_b_bus[ii] = solution[0][1][ii]
                self.mux4way16.pin_c_bus[ii] = solution[0][2][ii]
                self.mux4way16.pin_d_bus[ii] = solution[0][3][ii]
            self.mux4way16.pin_sel0 = solution[0][4]
            self.mux4way16.pin_sel1 = solution[0][5]

            self.mux4way16.update()

            for ii in range(16):
                assert self.mux4way16.pin_x_bus[ii] == solution[1][ii]
        print("Mux4Way16 test success!!")

class Mux8Way16TestBench:
    def __init__(self, testCycles=100):
        self.mux8way16 = Mux8Way16()
        self.truth_table = []
        for cycle in range(testCycles):
            test_a_bus = [random.choice([0, 1]) for ii in range(16)]
            test_b_bus = [random.choice([0, 1]) for ii in range(16)]
            test_c_bus = [random.choice([0, 1]) for ii in range(16)]
            test_d_bus = [random.choice([0, 1]) for ii in range(16)]
            test_e_bus = [random.choice([0, 1]) for ii in range(16)]
            test_f_bus = [random.choice([0, 1]) for ii in range(16)]
            test_g_bus = [random.choice([0, 1]) for ii in range(16)]
            test_h_bus = [random.choice([0, 1]) for ii in range(16)]
            test_sel0 = random.choice([0, 1])
            test_sel1 = random.choice([0, 1])
            test_sel2 = random.choice([0, 1])

            test_x_bus = self.thisFunction(test_a_bus, test_b_bus, test_c_bus, test_d_bus, test_e_bus, test_f_bus, test_g_bus, test_h_bus, test_sel0, test_sel1, test_sel2)
            self.truth_table.append([[test_a_bus, test_b_bus, test_c_bus, test_d_bus, test_e_bus, test_f_bus, test_g_bus, test_h_bus, test_sel0, test_sel1, test_sel2], test_x_bus])

    def thisFunction(self, test_a_bus_in, test_b_bus_in, test_c_bus_in, test_d_bus_in, test_e_bus_in, test_f_bus_in, test_g_bus_in, test_h_bus_in, test_sel0_in, test_sel1_in, test_sel2_in):
        test_sel_array = [test_sel2_in, test_sel1_in, test_sel0_in]
        if(test_sel_array == [0, 0, 0]):
            test_x_bus_out = test_a_bus_in
        elif(test_sel_array == [0, 0, 1]):
            test_x_bus_out = test_b_bus_in 
        elif(test_sel_array == [0, 1, 0]):
            test_x_bus_out = test_c_bus_in 
        elif(test_sel_array == [0, 1, 1]):
            test_x_bus_out = test_d_bus_in
        elif(test_sel_array == [1, 0, 0]):
            test_x_bus_out = test_e_bus_in
        elif(test_sel_array == [1, 0, 1]):
            test_x_bus_out = test_f_bus_in
        elif(test_sel_array == [1, 1, 0]):
            test_x_bus_out = test_g_bus_in
        elif(test_sel_array == [1, 1, 1]):
            test_x_bus_out = test_h_bus_in
        else:
            print("Error: invalid values on sel lines in Mux4Way16TestBench")
            exit(1)
        return(test_x_bus_out)

    def test(self):
        for solution in self.truth_table:
            for ii in range(16):
                self.mux8way16.pin_a_bus[ii] = solution[0][0][ii]
                self.mux8way16.pin_b_bus[ii] = solution[0][1][ii]
                self.mux8way16.pin_c_bus[ii] = solution[0][2][ii]
                self.mux8way16.pin_d_bus[ii] = solution[0][3][ii]
                self.mux8way16.pin_e_bus[ii] = solution[0][4][ii]
                self.mux8way16.pin_f_bus[ii] = solution[0][5][ii]
                self.mux8way16.pin_g_bus[ii] = solution[0][6][ii]
                self.mux8way16.pin_h_bus[ii] = solution[0][7][ii]
            self.mux8way16.pin_sel0 = solution[0][8]
            self.mux8way16.pin_sel1 = solution[0][9]
            self.mux8way16.pin_sel2 = solution[0][10]

            self.mux8way16.update()

            for ii in range(16):
                assert self.mux8way16.pin_x_bus[ii] == solution[1][ii]
        print("Mux8Way16 test success!!")

class DMux4WayTestBench:
    def __init__(self):
        self.dmux4Way = DMux4Way()
        self.truth_table = [[[0, 0, 0], [0, 0, 0, 0]],
                            [[0, 0, 1], [0, 0, 0, 0]],
                            [[0, 1, 0], [0, 0, 0, 0]],
                            [[0, 1, 1], [0, 0, 0, 0]],
                            [[1, 0, 0], [1, 0, 0, 0]],
                            [[1, 0, 1], [0, 1, 0, 0]],
                            [[1, 1, 0], [0, 0, 1, 0]],
                            [[1, 1, 1], [0, 0, 0, 1]]]

    def test(self):
        for solution in self.truth_table:
            self.dmux4Way.pin_a = solution[0][0]
            self.dmux4Way.pin_sel0 = solution[0][1]
            self.dmux4Way.pin_sel1 = solution[0][2]

            self.dmux4Way.update()

            assert [self.dmux4Way.pin_w, self.dmux4Way.pin_x, self.dmux4Way.pin_y, self.dmux4Way.pin_z] == solution[1]

        print("DMux4Way test success!!")

class DMux8WayTestBench:
    def __init__(self):
        self.dmux8Way = DMux8Way()
        self.truth_table = [[[0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
                            [[0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0]],
                            [[0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
                            [[0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0]],
                            [[0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
                            [[0, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0]],
                            [[0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
                            [[0, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0]],
                            [[1, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]],
                            [[1, 0, 0, 1], [0, 1, 0, 0, 0, 0, 0, 0]],
                            [[1, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0, 0]],
                            [[1, 0, 1, 1], [0, 0, 0, 1, 0, 0, 0, 0]],
                            [[1, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0]],
                            [[1, 1, 0, 1], [0, 0, 0, 0, 0, 1, 0, 0]],
                            [[1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 1, 0]],
                            [[1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1]]]

    def test(self):
        for solution in self.truth_table:
            self.dmux8Way.pin_a = solution[0][0]
            self.dmux8Way.pin_sel0 = solution[0][1]
            self.dmux8Way.pin_sel1 = solution[0][2]
            self.dmux8Way.pin_sel2 = solution[0][3]

            self.dmux8Way.update()
            test_output = [self.dmux8Way.pin_s, self.dmux8Way.pin_t, self.dmux8Way.pin_u, self.dmux8Way.pin_v, self.dmux8Way.pin_w, self.dmux8Way.pin_x, self.dmux8Way.pin_y, self.dmux8Way.pin_z]
            assert test_output == solution[1]

        print("DMux8Way test success!!")

if __name__ == '__main__':
    import random
    import pdb 
    # pdb.set_trace()
    testCycles = 100 # For chips that have too many inputs to be exhaustively tested
    notGateTestBench = NotGateTestBench()
    notGateTestBench.test()
    andGateTestBench = AndGateTestBench()
    andGateTestBench.test()
    OrGateTestBench = OrGateTestBench()
    OrGateTestBench.test()
    xorGateTestBench = XorGateTestBench()
    xorGateTestBench.test()
    muxGateTestBench = MuxGateTestBench()
    muxGateTestBench.test()
    dmuxGateTestBench = DMuxGateTestBench()
    dmuxGateTestBench.test()
    not16TestBench = Not16TestBench(testCycles=testCycles)
    not16TestBench.test()
    and16TestBench = And16TestBench(testCycles=testCycles)
    and16TestBench.test()
    or16TestBench = Or16TestBench(testCycles=testCycles)
    or16TestBench.test()
    mux16TestBench = Mux16TestBench(testCycles=testCycles)
    mux16TestBench.test()
    or8WayTestBench = Or8WayTestBench(testCycles=testCycles)
    or8WayTestBench.test()
    mux4Way16TestBench = Mux4Way16TestBench(testCycles=testCycles)
    mux4Way16TestBench.test()
    mux8way16TestBench = Mux8Way16TestBench(testCycles=testCycles)
    mux8way16TestBench.test()
    dmux4WayTestBench = DMux4WayTestBench()
    dmux4WayTestBench.test()
    dmux8WayTestBench = DMux8WayTestBench()
    dmux8WayTestBench.test()