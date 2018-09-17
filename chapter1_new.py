from fundamentals import Nand


class Not:
    def __init__(self, a, x=None):
        self.a = a
        self.x = x
        return(None)

    def update(self):
        gate1 = Nand(self.a,self.a)
        gate1.update()
        self.x = gate1.x
        return(self.x)

class And:
    def __init__(self, a, b, x=None):
        self.a = a
        self.b = b
        self.x = x
        return(None)

    def update(self):
        gate1 = Nand(self.a,self.b)
        gate1.update()
        gate2 = Not(gate1.x)
        gate2.update()
        self.x = gate2.x
        return(self.x)

class Or:
    def __init__(self, a, b, x=None):
        self.a = a
        self.b = b
        self.x = x
        return(None)

    def update(self):
        gate1 = Not(self.a)
        gate1.update()
        gate2 = Not(self.b)
        gate2.update()
        gate3 = Nand(gate1.x,gate2.x)
        gate3.update()
        self.x = gate3.x
        return(self.x)

class Xor:
    def __init__(self, a, b, x=None):
        self.a = a
        self.b = b
        self.x = x
        return(None)

    def update(self):
        not_a = Not(a)
        not_a.update()
        not_b = Not(b)
        not_b.update()
        and_1 = And(a,not_b.x)
        and_1.update()
        and_2 = And(not_a.x,b)
        and_2.update()
        or_gate = Or(and_1.x,and_2.x)
        or_gate.update()
        self.x = or_gate.x
        return(self.x)

class And3Way:
    def __init__(self, a, b, c, x=None):
        self.a = a
        self.b = b
        self.c = c
        self.x = x
        return(None)

    def update(self):
        and_1 = And(self.a,self.b)
        and_1.update()
        and_2 = And(and_1.x,self.c)
        and_2.update()
        self.x = and_2.x
        return(self.x)

class Mux:
    def __init__(self, a, b, sel, x=None):
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
        and_1 = And3Way(not_a.x,self.b,self.sel)
        and_1.update()
        and_2 = And3Way(self.a,not_b.x,not_sel.x)
        and_2.update()
        and_3 = And3Way(self.a,self.b,not_sel.x)
        and_3.update()
        and_4 = And3Way(self.a,self.b,self.sel)
        and_4.update()
        or_1 = Or(and_1.x,and_2.x)
        or_1.update()
        or_2 = Or(and_3.x,and_4.x)
        or_2.update()
        or_3 = Or(or_1.x,or_2.x)
        or_3.update()
        self.x = or_3.x
        return(self.x)

class DMux:
    def __init__(self, a, sel, x=None, y=None):
        self.a = a
        self.sel = sel
        self.x = x
        self.y = y
        return(None)

    def update(self):
        not_sel = Not(self.sel)
        not_sel.update()
        and_1 = And(self.a,not_sel.x)
        and_1.update()
        and_2 = And(self.a,self.sel)
        and_2.update()
        self.x = and_1.x
        self.y = and_2.x
        return(self.x,self.y)

class Not16:
    def __init__(self, a16, x16=[None for i in range(16)]):
        self.a16 = a16
        self.x16 = x16
        return(None)

    def update(self):
        not_gates = [Not(i) for i in self.a16]
        not_gates = [i.update() for i in not_gates]
        self.x16 = not_gates
        return(self.x16)

class And16:
    def __init__(self, a16, b16, x16=[None for i in range(16)]):
        self.a16 = a16
        self.b16 = b16
        self.x16 = x16
        self.input_list = [[a16[i],b16[i]] for i in range(16)]
        return(None)

    def update(self):
        and_gates = [And(i[0],i[1]) for i in self.input_list]
        and_gates = [i.update() for i in and_gates]
        self.x16 = and_gates
        return(self.x16)
        

a16 = [1,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0]
b16 = [0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0]
and_16 = And16(a16,b16)
and_16.update()
print(and_16.x16)





        
        
