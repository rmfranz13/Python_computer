from Not import Not
from And import And
from Or import Or


class Xor:
    def __init__(self):
        # components:
        self.not1 = Not()
        self.not2 = Not()
        self.and1 = And()
        self.and2 = And()
        self.or1 = Or()

        # connections:

        self.a = self.and1.a
        self.not2.a = self.and1.a
        self.b = self.and2.b
        self.not1.a = self.and2.b
        self.and1.b = self.not1.x
        self.and2.a = self.not2.x
        self.or1.a = self.and1.x
        self.or1.b = self.and2.x
        self.x = self.or1.x

    def update(self):
        self.not1.update()
        self.not2.update()
        self.and1.update()
        self.and2.update()
        self.or1.update()


if __name__ == '__main__':
    print("Testing Or gate")
    test_xor = Xor()
    test_a = [0, 0, 1, 1]
    test_b = [0, 1, 0, 1]
    test_x = [0, 1, 1, 0]
    for ii in range(len(test_a)):
        test_xor.a.val = test_a[ii]
        test_xor.b.val = test_b[ii]
        test_xor.update()
        if(test_xor.x.val == test_x[ii]):
            print("success for test " + str(ii + 1) + " out of " + str(len(test_a)))
        else:
            raise Exception("Test failed")
