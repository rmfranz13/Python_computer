#! /usr/bin/python3

# Basic Nand gate underlying everything in boolean logic

# Additionally DFF, the fundamental sequential or 'memory' unit, 
# placed here because it's assumed fundamental by the book but is itself 
# constructed from nand gates

class Nand:
    def __init__(self):
        self.pin_a = 0
        self.pin_b = 0
        self.pin_x = 0

    def update(self):
        if(self.pin_a and self.pin_b):
            self.pin_x = 0
        else:
            self.pin_x = 1


class DFF:
    def __init__(self):
        # Inputs
        self.d = 0
        self.clk = 0

        self.q = 0
        self.q_bar = 0

        self.nandNot = Nand()
        self.nand00 = Nand()
        self.nand01 = Nand()
        self.nand10 = Nand()
        self.nand11 = Nand()

    def update(self):
        pass