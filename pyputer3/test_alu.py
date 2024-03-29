#! /usr/bin/python3

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
    print("\n")
    # pdb.set_trace()
    testCycles = 100
    halfAdderTestBench = HalfAdderTestBench()
    halfAdderTestBench.test()
    fullAdderTestBench = FullAdderTestBench()
    fullAdderTestBench.test()
    add16TestBench = Add16TestBench(testCycles=testCycles)
    add16TestBench.test()
    inc16TestBench = Incr16TestBench(testCycles=testCycles)
    inc16TestBench.test()

    print("\n\n>>>> ALU TEST >>>>>")
    print("Press enter to run each ALU function on a random inputs (same x16 and y16 for each test).")
    input("Judge correctness for yourself.\n")

    # Test ALU "manually" (doesn't explicitly handle all inputs)
    alu = ALU()
    control_bit_test = {'zero': [1, 0, 1, 0, 1, 0], 
                        'one': [1, 1, 1, 1, 1, 1],
                        'negative_one': [1, 1, 1, 0, 1, 0],
                        'x': [0, 0, 1, 1, 0, 0],
                        'y': [1, 1, 0, 0, 0, 0],
                        'not_x': [0, 0, 1, 1, 0, 1],
                        'not_y': [1, 1, 0, 0, 0, 1],
                        'negative_x': [0, 0, 1, 1, 1, 1],
                        'negative_y': [1, 1, 0, 0, 1, 1],
                        'inc_x': [0, 1, 1, 1, 1, 1],
                        'inc_y': [1, 1, 0, 1, 1, 1],
                        'dec_x': [0, 0, 1, 1, 1, 0],
                        'dec_y': [1, 1, 0, 0, 1, 0],
                        'add': [0, 0, 0, 0, 1, 0],
                        'x_sub_y': [0, 1, 0, 0, 1, 1],
                        'y_sub_x': [0, 0, 0, 1, 1, 1],
                        'and': [0, 0, 0, 0, 0, 0],
                        'or': [0, 1, 0, 1, 0, 1]}

    test_x_bus = [random.choice([0, 1]) for ii in range(16)]
    test_y_bus = [random.choice([0, 1]) for ii in range(16)]

    # Print text_x_bus and test_y_bus
    print("ALU inputs under test: ")
    print("x16 = " + str(test_x_bus))
    print("y16 = " + str(test_y_bus))
    print("\n")
    print("ALU  outputs for each ALU function:")
    print("\n")

    for key in control_bit_test.keys():
        func = key
        control_bits = control_bit_test[key]

        alu.x16 = test_x_bus
        alu.y16 = test_y_bus
        alu.zx = control_bits[0]
        alu.nx = control_bits[1]
        alu.zy = control_bits[2]
        alu.ny = control_bits[3]
        alu.f = control_bits[4]
        alu.no = control_bits[5]

        alu.update()

        print("ALU FUNCTION: " + func)
        print("out16 = " + str(alu.out16) + ", zr = " + str(alu.zr) + ", ng = " + str(alu.ng))



