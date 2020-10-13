from pin import Pin


class Nand:
    def __init__(self):
        # input pins
        self.a = Pin()
        self.b = Pin()
        # output pins
        self.x = Pin()

    def update(self):
        if((self.a.val == 1) and (self.b.val == 1)):
            self.x.val = 0
        else:
            self.x.val = 1


if __name__ == '__main__':
    print("Testing nand gate:")
    test_nand = Nand()
    test_inputs = [[0, 0],
                   [0, 1],
                   [1, 0],
                   [1, 1]]
    test_outputs = [1, 1, 1, 0]
    for ii in range(len(test_inputs)):
        test_nand.a.val = test_inputs[ii][0]
        test_nand.b.val = test_inputs[ii][1]
        test_nand.update()
        if(test_nand.x.val == test_outputs[ii]):
            print("success for test " + str(ii))
        else:
            raise Exception("Test failure")
