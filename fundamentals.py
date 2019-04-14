"""
Fundamental functions for building a computer... just Nand gate object.
Google what a Nand gate is if you don't know.

This is the only object that is implemented in Python directly (uses an
if-else statement to derive output (x) from inputs (a and b)).

All other objects are created directly, or indirectly, from instances of
this Nand gate class. Suppose I create an instance called myNand. The inputs are set 
(set inputs myNand.a = 1 and myNand.b = 0, for example (1 and 0 are the only allowed inputs))
and the output (1 in this case) is placed on myNand.x after calling the myNand.update() method.

The update method defined here is the only method that is called by any
derived chip anywhere else in the program. Aka, the chips derived from this 
Nand gate can't use any built-in functions from Python. This is because there 
is no such thing as, say, a for-loop if all you have is transistors. The point
is to demonstrate how things like for-loops can exist in the first place from
fundamental logic gates.
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

            
        







            
