from nand import Nand
from Not import Not


class And:
    def __init__(self):
        # components
        self.nand1 = Nand()
        self.not1 = Not()

        # connections
        self.nand1.x = self.not1.a
        self.a = self.nand1.a
        self.b = self.nand1.b
        self.x = self.not1.x

    def update(self):
        self.nand1.update()
        self.not1.update()


if __name__ == '__main__':
    print("Testing And gate")
    test_and = And()
    test_a = [0, 0, 1, 1]
    test_b = [0, 1, 0, 1]
    test_x = [0, 0, 0, 1]
    for ii in range(len(test_a)):
        test_and.a.val = test_a[ii]
        test_and.b.val = test_b[ii]
        test_and.update()
        if(test_and.x.val == test_x[ii]):
            print("success for test " + str(ii + 1) + " out of " + str(len(test_a)))
        else:
            raise Exception("Test failed")
