"""
Fundamental functions for building a computer... just Nand gate object.
"""
class Nand:
    def __init__(self, a, b, x=0):
        self.a = a
        self.b = b
        self.x = x

    def update(self):
        if (self.a and self.b) == 1:
            self.x = 0
        else:
            self.x = 1
        return(self.x)

            
        







            
