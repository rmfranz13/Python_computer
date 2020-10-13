from pin import Pin
from connection import Connection
from nand import Nand


class Not:
    def __init__(self):
        # input/output pins:
        self.__a = Pin()
        self.__x = Pin()

        # components
        self.__nand1 = Nand()

        # connections:
        self.__connection1 = Connection([self.__a, self.__nand1.b, self.__nand1.a])
        self.__connection2 = Connection([self.__x, self.__nand1.x])

    def update(self):
        self.__connection1.update()
        self.__nand1.update()
        self.__connection2.update()

    @property
    def nand1(self):
        return(self.__nand1)

    @nand1.setter
    def nand1(self, _nand1):
        self.__nand1 = _nand1

    @property
    def a(self):
        self.__connection1.update()
        return(self.__a)

    @a.setter
    def a(self, _a):
        self.__a = _a
        self.__connection1.update()

    @property
    def x(self):
        self.__connection2.update()
        return(self.__x)

    @x.setter
    def x(self, _x):
        self.__x = _x
        self.__connection2.update()

    @property
    def connection1(self):
        return(self.__connection1)

    @connection1.setter
    def connection1(self, _connection1):
        self.__connection1 = _connection1

    @property
    def connection2(self):
        return(self.__connection2)

    @connection2.setter
    def connection2(self, _connection2):
        self.__connection2 = _connection2


if __name__ == '__main__':
    print("Testing Not gate")
    my_not = Not()
    test_inputs = [0, 1]
    test_outputs = [1, 0]
    for ii in range(len(test_inputs)):
        my_not.a.val = test_inputs[ii]
        my_not.update()
        if(my_not.x.val == test_outputs[ii]):
            print("success for test " + str(ii + 1) + " out of " + str(len(test_inputs)))
        else:
            raise Exception("Test failed")
