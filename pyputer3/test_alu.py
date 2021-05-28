# Test classes leading up to and including ALU 

from alu import *

class HalfAdderTestBench:
    def __init__(self):
        self.halfAdder = HalfAdder()
        self.truth_table = [[[0, 0], [0, 0]], 
                            [[0, 1], [0, 1]], 
                            [[1, 0], [0, 1]], 
                            [[1, 1], [1, 0]]]

    def test(self):
        for solution in self.truth_table:
            self.halfAdder.pin_a = solution[0][0]
            self.halfAdder.pin_b = solution[0][1]

            self.halfAdder.update()
            
            assert self.halfAdder.pin_carry == solution[1][0]
            assert self.halfAdder.pin_sum == solution[1][1]
        
        print("HalfAdder test success!!!")


class FullAdderTestBench:
    def __init__(self):
        self.fullAdder = FullAdder()
        self.truth_table = [[[0, 0, 0], [0, 0]], 
                            [[0, 0, 1], [0, 1]], 
                            [[0, 1, 0], [0, 1]], 
                            [[0, 1, 1], [1, 0]], 
                            [[1, 0, 0], [0, 1]], 
                            [[1, 0, 1], [1, 0]], 
                            [[1, 1, 0], [1, 0]],
                            [[1, 1, 1], [1, 1]]]

    def test(self):
        for solution in self.truth_table:
            self.fullAdder.pin_a = solution[0][0]
            self.fullAdder.pin_b = solution[0][1]
            self.fullAdder.pin_c = solution[0][2]

            self.fullAdder.update()

            assert self.fullAdder.pin_sum == solution[1][1]
            assert self.fullAdder.pin_carry == solution[1][0]

        print("FullAdder test success!!!")


class Add16TestBench:
    def __init__(self, testCycles=100):
        self.add16 = Add16()
        self.truth_table = []
        for ii in range(testCycles):
            test_a_bus = [random.choice([0, 1]) for jj in range(16)]
            test_b_bus = [random.choice([0, 1]) for jj in range(16)]
            test_sum_bus = self.addition_method(test_a_bus, test_b_bus)
            self.truth_table.append([[test_a_bus, test_b_bus], test_sum_bus])

    def test(self):
        for solution in self.truth_table:
            self.add16.pin_a_bus = solution[0][0]
            self.add16.pin_b_bus = solution[0][1]
            self.add16.update()
            assert self.add16.pin_sum_bus == solution[1]

        print("Add16 test success!!!")

    def full_adder_tester(self, a, b, c):
        test_list = [a, b, c]
        if(test_list == [0, 0, 0]):
            sum_out = 0
            carry_out = 0
        elif(test_list == [0, 0, 1] or test_list == [0, 1, 0] or test_list == [1, 0, 0]):
            sum_out = 1
            carry_out = 0
        elif(test_list == [0, 1, 1] or test_list == [1, 0, 1] or test_list == [1, 1, 0]):
            sum_out = 0
            carry_out = 1
        else:
            sum_out = 1
            carry_out = 1

        return([sum_out, carry_out])

    def addition_method(self, a_bus_in, b_bus_in):
        test_sum_list = []
        next_sum, next_carry = self.full_adder_tester(a_bus_in[0], b_bus_in[0], 0)
        test_sum_list.append(next_sum)
        for ii in range(1,16):
            next_sum, next_carry = self.full_adder_tester(a_bus_in[ii], b_bus_in[ii], next_carry)
            test_sum_list.append(next_sum)
        return(test_sum_list)


class Incr16TestBench:
    def __init__(self, testCycles=100):
        self.incr16 = Incr16()
        self.add16 = Add16TestBench()
        self.constant_incr = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.truth_table = []
        for ii in range(testCycles):
            test_a_bus = [random.choice([0, 1]) for jj in range(16)]
            test_x_bus = self.add16.addition_method(self.constant_incr, test_a_bus)
            self.truth_table.append([test_a_bus, test_x_bus])

    def test(self):
        for solution in self.truth_table:
            self.incr16.pin_a_bus = solution[0]
            self.incr16.update()
            assert self.incr16.pin_x_bus == solution[1]

        print("Incr16 test success!!!")
        



if __name__ == '__main__':
    import random 
    import pdb 
    testCycles = 100
    halfAdderTestBench = HalfAdderTestBench()
    halfAdderTestBench.test()
    fullAdderTestBench = FullAdderTestBench()
    fullAdderTestBench.test()
    add16TestBench = Add16TestBench(testCycles=testCycles)
    add16TestBench.test()
    inc16TestBench = Incr16TestBench(testCycles=testCycles)
    inc16TestBench.test()
