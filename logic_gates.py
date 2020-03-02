import fundamentals


class Not:
    def __init__(self, a=0, x=0):
        # Initialize member gates:
        self.nand = fundamentals.Nand(a=a, b=a, x=x)

        # Initialize pins for this chip:
        self.a = fundamentals.Pin(a)
        self.x = fundamentals.Pin(x)

        return(None)

    def update(self):
        # update input pins:
        self.nand.a = self.a
        self.nand.b = self.a

        # call Nand update:
        self.nand.update()

        # update output pins:
        self.x = self.nand.x
        return(None)


class And:
    def __init__(self, a, b, x=0):
        # Initialize member gates:
        self.nand = fundamentals.Nand()

        self.a = a
        self.b = b
        self.x = x
        return(None)

    def update(self):
        gate1 = fundamentals.Nand(self.a, self.b)
        gate1.update()
        gate2 = Not(gate1.x)
        gate2.update()
        self.x = gate2.x
        return(self.x)


class Or:
    def __init__(self, a, b, x=0):
        self.a = a
        self.b = b
        self.x = x
        return(None)

    def update(self):
        gate1 = Not(self.a)
        gate1.update()
        gate2 = Not(self.b)
        gate2.update()
        gate3 = fundamentals.Nand(gate1.x, gate2.x)
        gate3.update()
        self.x = gate3.x
        return(self.x)


class Xor:
    def __init__(self, a, b, x=0):
        self.a = a
        self.b = b
        self.x = x
        return(None)

    def update(self):
        not_a = Not(self.a)
        not_a.update()
        not_b = Not(self.b)
        not_b.update()
        and_1 = And(self.a, not_b.x)
        and_1.update()
        and_2 = And(not_a.x, self.b)
        and_2.update()
        or_gate = Or(and_1.x, and_2.x)
        or_gate.update()
        self.x = or_gate.x
        return(self.x)


class And3Way:
    def __init__(self, a, b, c, x=0):
        self.a = a
        self.b = b
        self.c = c
        self.x = x
        return(None)

    def update(self):
        and_1 = And(self.a, self.b)
        and_1.update()
        and_2 = And(and_1.x, self.c)
        and_2.update()
        self.x = and_2.x
        return(self.x)


class Or4Way:
    def __init__(self, a, b, c, d, x=0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.x = x
        return(None)

    def update(self):
        or_1 = Or(self.a, self.b)
        or_1.update()
        or_2 = Or(self.c, self.d)
        or_2.update()
        or_3 = Or(or_1.x, or_2.x)
        or_3.update()
        self.x = or_3.x
        return(self.x)


class Mux:
    def __init__(self, a, b, sel, x=0):
        self.a = a
        self.b = b
        self.sel = sel
        self.x = x
        return(None)

    def update(self):
        not_a = Not(self.a)
        not_a.update()
        not_b = Not(self.b)
        not_b.update()
        not_sel = Not(self.sel)
        not_sel.update()
        and_1 = And3Way(not_a.x, self.b, self.sel)
        and_1.update()
        and_2 = And3Way(self.a, not_b.x, not_sel.x)
        and_2.update()
        and_3 = And3Way(self.a, self.b, not_sel.x)
        and_3.update()
        and_4 = And3Way(self.a, self.b, self.sel)
        and_4.update()
        or_1 = Or(and_1.x, and_2.x)
        or_1.update()
        or_2 = Or(and_3.x, and_4.x)
        or_2.update()
        or_3 = Or(or_1.x, or_2.x)
        or_3.update()
        self.x = or_3.x
        return(self.x)


class DMux:
    def __init__(self, a, sel, x=0, y=0):
        self.a = a
        self.sel = sel
        self.x = x
        self.y = y
        return(None)

    def update(self):
        not_sel = Not(self.sel)
        not_sel.update()
        and_1 = And(self.a, not_sel.x)
        and_1.update()
        and_2 = And(self.a, self.sel)
        and_2.update()
        self.x = and_1.x
        self.y = and_2.x
        return(self.x, self.y)


class Not16:
    def __init__(self, a16, x16=[0 for i in range(16)]):
        self.a16 = a16
        self.x16 = x16
        return(None)

    def update(self):
        not_gates = [Not(i) for i in self.a16]
        not_gates = [i.update() for i in not_gates]
        self.x16 = not_gates
        return(self.x16)


class And16:
    def __init__(self, a16, b16, x16=[0 for i in range(16)]):
        self.a16 = a16
        self.b16 = b16
        self.x16 = x16
        self.input_list = [[a16[i], b16[i]] for i in range(16)]
        return(None)

    def update(self):
        and_gates = [And(i[0], i[1]) for i in self.input_list]
        and_gates = [i.update() for i in and_gates]
        self.x16 = and_gates
        return(self.x16)


class Or16:
    def __init__(self, a16, b16, x16=[0 for i in range(16)]):
        self.a16 = a16
        self.b16 = b16
        self.x16 = x16
        self.input_list = [[a16[i], b16[i]] for i in range(16)]
        return(None)

    def update(self):
        or_gates = [Or(i[0], i[1]) for i in self.input_list]
        or_gates = [i.update() for i in or_gates]
        self.x16 = or_gates
        return(self.x16)


class Mux16:
    def __init__(self, a16, b16, sel16, x16=[0 for i in range(16)]):
        self.a16 = a16
        self.b16 = b16
        self.sel16 = sel16
        self.x16 = x16
        self.input_list = [[a16[i], b16[i], sel16[i]] for i in range(16)]
        return(None)

    def update(self):
        muxes = [Mux(i[0], i[1], i[2]) for i in self.input_list]
        muxes = [i.update() for i in muxes]
        self.x16 = muxes
        return(muxes)


class Or8Way:
    def __init__(self, a, b, c, d, e, f, g, h, x=0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.g = g
        self.h = h
        self.x = x
        return(None)

    def update(self):
        or1 = Or(self.a, self.b)
        or1.update()
        or2 = Or(self.c, self.d)
        or2.update()
        or3 = Or(self.e, self.f)
        or3.update()
        or4 = Or(self.g, self.h)
        or4.update()
        or5 = Or(or1.x, or2.x)
        or5.update()
        or6 = Or(or3.x, or4.x)
        or6.update()
        or7 = Or(or5.x, or6.x)
        or7.update()
        self.x = or7.x
        return(or7.x)


class Mux4Way16:
    def __init__(self, a16, b16, c16, d16, sel2, x16=[0 for i in range(16)]):
        self.a16 = a16
        self.b16 = b16
        self.c16 = c16
        self.d16 = d16
        self.sel1 = [sel2[0] for i in range(16)]
        self.sel2 = [sel2[1]for i in range(16)]
        self.x16 = x16
        return(None)

    def update(self):
        mux16_1 = Mux16(self.a16, self.b16, self.sel2)
        mux16_1.update()
        mux16_2 = Mux16(self.c16, self.d16, self.sel2)
        mux16_2.update()
        mux16_3 = Mux16(mux16_1.x16, mux16_2.x16, self.sel1)
        mux16_3.update()
        self.x16 = mux16_3.x16
        return(self.x16)


class Mux8Way16:
    def __init__(self, a16, b16, c16, d16, e16, f16, g16, h16, sel3, x16=[0 for i in range(16)]):
        self.a16 = a16
        self.b16 = b16
        self.c16 = c16
        self.d16 = d16
        self.e16 = e16
        self.f16 = f16
        self.g16 = g16
        self.h16 = h16
        self.sel0 = [sel3[0] for i in range(16)]
        self.sel1 = sel3[1]
        self.sel2 = sel3[2]
        self.x16 = x16

    def update(self):
        mux416_1 = Mux4Way16(self.a16, self.b16, self.c16, self.d16, [self.sel1, self.sel2])
        mux416_1.update()
        mux416_2 = Mux4Way16(self.e16, self.f16, self.g16, self.h16, [self.sel1, self.sel2])
        mux416_2.update()
        mux16 = Mux16(mux416_1.x16, mux416_2.x16, self.sel0)
        mux16.update()
        self.x16 = mux16.x16
        return(self.x16)


class DMux4Way:
    def __init__(self, a, sel2, w=0, x=0, y=0, z=0):
        self.a = a
        self.sel2 = sel2
        self.w = w
        self.x = x
        self.y = y
        self.z = z
        return(None)

    def update(self):
        dmux_1 = DMux(self.a, self.sel2[0])
        dmux_1.update()
        dmux_2 = DMux(dmux_1.x, self.sel2[1])
        dmux_2.update()
        dmux_3 = DMux(dmux_1.y, self.sel2[1])
        dmux_3.update()
        self.w = dmux_2.x
        self.x = dmux_2.y
        self.y = dmux_3.x
        self.z = dmux_3.y
        return(self.w, self.x, self.y, self.z)


class DMux8Way:
    def __init__(self, a, sel3, x0=0, x1=0, x2=0, x3=0, x4=0, x5=0, x6=0, x7=0):
        self.a = a
        self.sel3 = sel3
        self.x0 = x0
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.x4 = x4
        self.x5 = x5
        self.x6 = x6
        self.x7 = x7
        return(None)

    def update(self):
        dmux_1 = DMux(self.a, self.sel3[0])
        dmux_1.update()
        dmux4_1 = DMux4Way(dmux_1.x, [self.sel3[1], self.sel3[2]])
        dmux4_1.update()
        dmux4_2 = DMux4Way(dmux_1.y, [self.sel3[1], self.sel3[2]])
        dmux4_2.update()
        self.x0 = dmux4_1.w
        self.x1 = dmux4_1.x
        self.x2 = dmux4_1.y
        self.x3 = dmux4_1.z
        self.x4 = dmux4_2.w
        self.x5 = dmux4_2.x
        self.x6 = dmux4_2.y
        self.x7 = dmux4_2.z
        return(self.x0, self.x1, self.x2, self.x3, self.x4, self.x5, self.x6, self.x7)


if __name__ == "__main__":
    my_Not = Not()
    my_Not.a = 0
    my_Not.update()
    my_Not.a = 1
    my_Not.update()
