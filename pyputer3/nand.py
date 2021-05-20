#! /usr/bin/python3

# Basic Nand gate underlying everything else

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