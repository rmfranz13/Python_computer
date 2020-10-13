from nand import Nand
from Not import Not


class Or:
    def __init__(self):
        # components
        self.not1 = Not()
        self.not2 = Not()
        self.nand1 = Nand()

        # connections
        self.nand1.a = self.not1.x
        self.nand1.b = self.not2.x
        self.a = self.not1.a
        self.b = self.not2.a
        self.x = self.nand1.x

    def update(self):
        self.not1.update()
        self.not2.update()
        self.nand1.update()


if __name__ == '__main__':
    print("Testing Or gate")
    test_or = Or()
    test_a = [0, 0, 1, 1]
    test_b = [0, 1, 0, 1]
    test_x = [0, 1, 1, 1]
    for ii in range(len(test_a)):
        test_or.a.val = test_a[ii]
        test_or.b.val = test_b[ii]
        test_or.update()
        if(test_or.x.val == test_x[ii]):
            print("success for test " + str(ii + 1) + " out of " + str(len(test_a)))
        else:
            raise Exception("Test failed")
