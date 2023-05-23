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
        self.nandNot.pin_a = self.d 
        self.nandNot.pin_b = self.d 
        self.nandNot.update()

        self.nand00.pin_a = self.d 
        self.nand00.pin_b = self.clk 
        self.nand00.update()

        self.nand01.pin_a = self.nandNot.pin_x 
        self.nand01.pin_b = self.clk 
        self.nand01.update()

        self.nand10.pin_a = self.nand00.pin_x 
        self.nand10.pin_b = self.nand11.pin_x 
        self.nand10.update()

        self.nand11.pin_a = self.nand10.pin_x 
        self.nand11.pin_b = self.nand01.pin_x 
        self.nand11.update()

        self.q = self.nand10.pin_x 
        self.q_bar = self.nand11.pin_x 

if __name__ == '__main__':
    import random 
    NUM_TESTS = 20
    myDFF = DFF()
    test_d = [random.choice([0, 1]) for ii in range(2*NUM_TESTS)]
    test_q = []
    test_qbar = []
    clk_line = []
    for ii in range(0, 2*NUM_TESTS, 2):
        data = test_d[ii]
        myDFF.d = data 
        myDFF.clk = 0 
        myDFF.update()
        test_q.append(myDFF.q)
        test_qbar.append(myDFF.q_bar)
        clk_line.append(myDFF.clk)
        data = test_d[ii+1]
        myDFF.d = data
        myDFF.clk = 1 
        myDFF.update()
        test_q.append(myDFF.q)
        test_qbar.append(myDFF.q_bar)
        clk_line.append(myDFF.clk)
        

        
    print("Clock line:   " + str(clk_line))
    print("Data inputs:  " + str(test_d))
    print("Q outputs:    " + str(test_q))
    print("Qbar outputs: " + str(test_qbar))
