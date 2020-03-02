"""
Fundamental functions for building a computer... just pin and nand gate objects.
Google what a Nand gate is if you don't know.

These are the only objects that implemented in Python directly (pin is just a 
getter and setter for modelling a physical pin which can either be set to 1 or 0, 
and nand uses an if-else statement to derive output (x) from inputs (a and b)).

All other objects are created directly, or indirectly, from instances of
these objects. Suppose I create an instance called myNand. The inputs are set
(set inputs myNand.a = 1 and myNand.b = 0, for example (1 and 0 are the only allowed inputs))
and the output (1 in this case) is placed on myNand.x after calling the myNand.update() method.

The update method defined here is the only method that is called by any
derived chip anywhere else in the program. Aka, the chips derived from this
Nand gate can't use any built-in functions from Python. This is because there
is no such thing as, say, a for-loop if all you have is transistors. The point
is to demonstrate how things like for-loops can exist in the first place from
fundamental logic gates.
"""


class Pin:
    def __init__(self, init_value=0):
        self.__value = init_value

    @property
    def value(self):
        return(self.__value)

    @value.setter
    def value(self, new_value):
        self.__value = new_value


class Nand:
    def __init__(self, a=0, b=0, x=0):
        self.a = Pin(a)
        self.b = Pin(b)
        self.x = Pin(x)

    def update(self):
        if (self.a and self.b) == 1:
            self.x.value = 0
        else:
            self.x.value = 1
