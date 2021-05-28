# Build components leading up to, and including, final
# implementation of ALU.

from fundamentals import *

class HalfAdder:
    def __init__(self):
        # Inputs
        self.pin_a = 0
        self.pin_b = 0

        # Outputs
        self.pin_sum = 0
        self.pin_carry = 0

        # Constituent gates
        self.xorGate = XorGate()
        self.andGate = AndGate()

    def update(self):
        self.xorGate.pin_a = self.pin_a
        self.xorGate.pin_b = self.pin_b
        self.xorGate.update()

        self.andGate.pin_a = self.pin_a
        self.andGate.pin_b = self.pin_b 
        self.andGate.update()

        self.pin_sum = self.xorGate.pin_x
        self.pin_carry = self.andGate.pin_x

class FullAdder:
    def __init__(self):
        # Inputs
        self.pin_a = 0
        self.pin_b = 0
        self.pin_c = 0

        # Outputs
        self.pin_sum = 0
        self.pin_carry = 0

        # Constituent gates
        self.halfAdder0 = HalfAdder()
        self.halfAdder1 = HalfAdder()
        self.orGate = OrGate()

    def update(self):
        self.halfAdder0.pin_a = self.pin_a 
        self.halfAdder0.pin_b = self.pin_b 
        
        self.halfAdder0.update()

        self.halfAdder1.pin_a = self.halfAdder0.pin_sum
        self.halfAdder1.pin_b = self.pin_c 
        
        self.halfAdder1.update()

        self.orGate.pin_a = self.halfAdder0.pin_carry
        self.orGate.pin_b = self.halfAdder1.pin_carry 

        self.orGate.update()

        self.pin_sum = self.halfAdder1.pin_sum
        self.pin_carry = self.orGate.pin_x 

class Add16:
    def __init__(self):
        # Inputs
        self.pin_a_bus = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.pin_b_bus = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        # Outputs
        self.pin_sum_bus = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        # Constituent gates:
        self.ha0 = HalfAdder()
        self.fa1 = FullAdder()
        self.fa2 = FullAdder()
        self.fa3 = FullAdder()
        self.fa4 = FullAdder()
        self.fa5 = FullAdder()
        self.fa6 = FullAdder()
        self.fa7 = FullAdder()
        self.fa8 = FullAdder()
        self.fa9 = FullAdder()
        self.fa10 = FullAdder()
        self.fa11 = FullAdder()
        self.fa12 = FullAdder()
        self.fa13 = FullAdder()
        self.fa14 = FullAdder()
        self.fa15 = FullAdder()

    def update(self):
        self.ha0.pin_a = self.pin_a_bus[0]
        self.ha0.pin_b = self.pin_b_bus[0]
        self.ha0.update()
        self.pin_sum_bus[0] = self.ha0.pin_sum

        self.fa1.pin_a = self.pin_a_bus[1]
        self.fa1.pin_b = self.pin_b_bus[1]
        self.fa1.pin_c = self.ha0.pin_carry
        self.fa1.update()
        self.pin_sum_bus[1] = self.fa1.pin_sum

        self.fa2.pin_a = self.pin_a_bus[2]
        self.fa2.pin_b = self.pin_b_bus[2]
        self.fa2.pin_c = self.fa1.pin_carry
        self.fa2.update()
        self.pin_sum_bus[2] = self.fa2.pin_sum

        self.fa3.pin_a = self.pin_a_bus[3]
        self.fa3.pin_b = self.pin_b_bus[3]
        self.fa3.pin_c = self.fa2.pin_carry
        self.fa3.update()
        self.pin_sum_bus[3] = self.fa3.pin_sum

        self.fa4.pin_a = self.pin_a_bus[4]
        self.fa4.pin_b = self.pin_b_bus[4]
        self.fa4.pin_c = self.fa3.pin_carry
        self.fa4.update()
        self.pin_sum_bus[4] = self.fa4.pin_sum

        self.fa5.pin_a = self.pin_a_bus[5]
        self.fa5.pin_b = self.pin_b_bus[5]
        self.fa5.pin_c = self.fa4.pin_carry
        self.fa5.update()
        self.pin_sum_bus[5] = self.fa5.pin_sum

        self.fa6.pin_a = self.pin_a_bus[6]
        self.fa6.pin_b = self.pin_b_bus[6]
        self.fa6.pin_c = self.fa5.pin_carry
        self.fa6.update()
        self.pin_sum_bus[6] = self.fa6.pin_sum

        self.fa7.pin_a = self.pin_a_bus[7]
        self.fa7.pin_b = self.pin_b_bus[7]
        self.fa7.pin_c = self.fa6.pin_carry
        self.fa7.update()
        self.pin_sum_bus[7] = self.fa7.pin_sum

        self.fa8.pin_a = self.pin_a_bus[8]
        self.fa8.pin_b = self.pin_b_bus[8]
        self.fa8.pin_c = self.fa7.pin_carry
        self.fa8.update()
        self.pin_sum_bus[8] = self.fa8.pin_sum

        self.fa9.pin_a = self.pin_a_bus[9]
        self.fa9.pin_b = self.pin_b_bus[9]
        self.fa9.pin_c = self.fa8.pin_carry
        self.fa9.update()
        self.pin_sum_bus[9] = self.fa9.pin_sum

        self.fa10.pin_a = self.pin_a_bus[10]
        self.fa10.pin_b = self.pin_b_bus[10]
        self.fa10.pin_c = self.fa9.pin_carry
        self.fa10.update()
        self.pin_sum_bus[10] = self.fa10.pin_sum

        self.fa11.pin_a = self.pin_a_bus[11]
        self.fa11.pin_b = self.pin_b_bus[11]
        self.fa11.pin_c = self.fa10.pin_carry
        self.fa11.update()
        self.pin_sum_bus[11] = self.fa11.pin_sum

        self.fa12.pin_a = self.pin_a_bus[12]
        self.fa12.pin_b = self.pin_b_bus[12]
        self.fa12.pin_c = self.fa11.pin_carry
        self.fa12.update()
        self.pin_sum_bus[12] = self.fa12.pin_sum

        self.fa13.pin_a = self.pin_a_bus[13]
        self.fa13.pin_b = self.pin_b_bus[13]
        self.fa13.pin_c = self.fa12.pin_carry
        self.fa13.update()
        self.pin_sum_bus[13] = self.fa13.pin_sum

        self.fa14.pin_a = self.pin_a_bus[14]
        self.fa14.pin_b = self.pin_b_bus[14]
        self.fa14.pin_c = self.fa13.pin_carry
        self.fa14.update()
        self.pin_sum_bus[14] = self.fa14.pin_sum

        self.fa15.pin_a = self.pin_a_bus[15]
        self.fa15.pin_b = self.pin_b_bus[15]
        self.fa15.pin_c = self.fa14.pin_carry
        self.fa15.update()
        self.pin_sum_bus[15] = self.fa15.pin_sum

class Incr16:
    def __init__(self):
        # Inputs:
        self.pin_a_bus = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        # Outputs:
        self.pin_x_bus = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        # Constituent gates:
        self.add16 = Add16()

    def update(self):
        self.add16.pin_a_bus = self.pin_a_bus
        self.add16.pin_b_bus = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.add16.update()

        self.pin_x_bus = self.add16.pin_sum_bus


class ALU:
    def __init__(self):
        # Inputs:
        self.x16 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.y16 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.zx = 0
        self.nx = 0
        self.zy = 0
        self.ny = 0
        self.f = 0
        self.no = 0

        # Outputs:
        self.out16 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.zr = 0
        self.ng = 0

        # Constituent chips:
        self.notZX = Not16()
        self.andZX = And16()
        self.notZY = Not16()
        self.andZY = And16()
        self.notNX = Not16()
        self.muxNX = Mux16()
        self.notNY = Not16()
        self.muxNY = Mux16()
        self.add16 = Add16()
        self.and16 = And16()
        self.muxF  = Mux16()
        self.notNO = Not16()
        self.muxNO = Mux16()
        self.or0ZR = Or8Way()
        self.or1ZR = Or8Way()
        self.or2ZR = OrGate()
        self.notZR = NotGate()

    def update(self):
        self.notZX.pin_a_bus[0] = self.zx
        self.notZX.pin_a_bus[1] = self.zx
        self.notZX.pin_a_bus[2] = self.zx
        self.notZX.pin_a_bus[3] = self.zx
        self.notZX.pin_a_bus[4] = self.zx
        self.notZX.pin_a_bus[5] = self.zx
        self.notZX.pin_a_bus[6] = self.zx
        self.notZX.pin_a_bus[7] = self.zx
        self.notZX.pin_a_bus[8] = self.zx
        self.notZX.pin_a_bus[9] = self.zx
        self.notZX.pin_a_bus[10] = self.zx
        self.notZX.pin_a_bus[11] = self.zx
        self.notZX.pin_a_bus[12] = self.zx
        self.notZX.pin_a_bus[13] = self.zx
        self.notZX.pin_a_bus[14] = self.zx
        self.notZX.pin_a_bus[15] = self.zx
        self.notZX.update()

        self.andZX.pin_a_bus = self.notZX.pin_x_bus
        self.andZX.pin_b_bus = self.x16
        self.andZX.update()

        self.notZY.pin_a_bus[0] = self.zy
        self.notZY.pin_a_bus[1] = self.zy
        self.notZY.pin_a_bus[2] = self.zy
        self.notZY.pin_a_bus[3] = self.zy
        self.notZY.pin_a_bus[4] = self.zy
        self.notZY.pin_a_bus[5] = self.zy
        self.notZY.pin_a_bus[6] = self.zy
        self.notZY.pin_a_bus[7] = self.zy
        self.notZY.pin_a_bus[8] = self.zy
        self.notZY.pin_a_bus[9] = self.zy
        self.notZY.pin_a_bus[10] = self.zy
        self.notZY.pin_a_bus[11] = self.zy
        self.notZY.pin_a_bus[12] = self.zy
        self.notZY.pin_a_bus[13] = self.zy
        self.notZY.pin_a_bus[14] = self.zy
        self.notZY.pin_a_bus[15] = self.zy
        self.notZY.update()

        self.andZY.pin_a_bus = self.notZY.pin_x_bus
        self.andZY.pin_b_bus = self.y16
        self.andZY.update()

        self.notNX.pin_a_bus = self.andZX.pin_x_bus
        self.notNX.update()

        self.muxNX.pin_a_bus = self.andZX.pin_x_bus
        self.muxNX.pin_b_bus = self.notNX.pin_x_bus
        self.muxNX.pin_sel = self.nx
        self.muxNX.update()

        self.notNY.pin_a_bus = self.andZY.pin_x_bus
        self.notNY.update()

        self.muxNY.pin_a_bus = self.andZY.pin_x_bus
        self.muxNY.pin_b_bus = self.notNY.pin_x_bus
        self.muxNY.pin_sel = self.ny
        self.muxNY.update()

        self.add16.pin_a_bus = self.muxNX.pin_x_bus
        self.add16.pin_b_bus = self.muxNY.pin_x_bus
        self.add16.update()

        self.and16.pin_a_bus = self.muxNX.pin_x_bus
        self.and16.pin_b_bus = self.muxNY.pin_x_bus
        self.and16.update()

        self.muxF.pin_a_bus = self.and16.pin_x_bus
        self.muxF.pin_b_bus = self.add16.pin_sum_bus
        self.muxF.pin_sel = self.f
        self.muxF.update()

        self.notNO.pin_a_bus = self.muxF.pin_x_bus
        self.notNO.update()
        
        self.muxNO.pin_a_bus = self.muxF.pin_x_bus
        self.muxNO.pin_b_bus = self.notNO.pin_x_bus
        self.muxNO.pin_sel = self.no
        self.muxNO.update()

        self.out16 = self.muxNO.pin_x_bus

        self.or0ZR.pin_a = self.out16[0]
        self.or0ZR.pin_b = self.out16[1]
        self.or0ZR.pin_c = self.out16[2]
        self.or0ZR.pin_d = self.out16[3]
        self.or0ZR.pin_e = self.out16[4]
        self.or0ZR.pin_f = self.out16[5]
        self.or0ZR.pin_g = self.out16[6]
        self.or0ZR.pin_g = self.out16[7]
        self.or0ZR.update()

        self.or1ZR.pin_a = self.out16[8]
        self.or1ZR.pin_b = self.out16[9]
        self.or1ZR.pin_c = self.out16[10]
        self.or1ZR.pin_d = self.out16[11]
        self.or1ZR.pin_e = self.out16[12]
        self.or1ZR.pin_f = self.out16[13]
        self.or1ZR.pin_g = self.out16[14]
        self.or1ZR.pin_h = self.out16[15]
        self.or1ZR.update()

        self.or2ZR.pin_a = self.or0ZR.pin_x
        self.or2ZR.pin_b = self.or1ZR.pin_x
        self.or2ZR.update()

        self.notZR.pin_a = self.or2ZR.pin_x
        self.notZR.update()
        
        self.zr = self.notZR.pin_x

        self.ng = self.out16[15]

