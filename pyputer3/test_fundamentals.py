# Run as a test of the fundamental gates.

from fundamentals import *


class NotGateTestBench:
    def __init__(self):
        self.notGate = NotGate()
        self.truth_table = [[0, 1], [1, 0]]

    def test(self):
        for solution in self.truth_table:
            self.notGate.pin_a = solution[0]
            self.notGate.update()
            assert self.notGate.pin_x == solution[1]
        print("NotGate test success!")

class AndGateTestBench:
    def __init__(self):
        self.andGate = AndGate()
        self.truth_table = [[[0, 0], [0]], 
                            [[0, 1], [0]], 
                            [[1, 0], [0]], 
                            [[1, 1], [1]]]

    def test(self):
        for solution in self.truth_table:
            self.andGate.pin_a = solution[0][0]
            self.andGate.pin_b = solution[0][1]
            self.andGate.update()
            assert self.andGate.pin_x == solution[1][0]
        print("AndGate test success!")

class OrGateTestBench:
    def __init__(self):
        self.orGate = OrGate()
        self.truth_table = [[[0, 0], [0]], 
                            [[0, 1], [1]], 
                            [[1, 0], [1]], 
                            [[1, 1], [1]]]

    def test(self):
        for solution in self.truth_table:
            self.orGate.pin_a = solution[0][0]
            self.orGate.pin_b = solution[0][1]
            self.orGate.update()
            assert self.orGate.pin_x == solution[1][0]
        print("OrGate test success!")

class XorGateTestBench:
    def __init__(self):
        self.xorGate = XorGate()
        self.truth_table = [[[0, 0], [0]], 
                            [[0, 1], [1]], 
                            [[1, 0], [1]], 
                            [[1, 1], [0]]]

    def test(self):
        for solution in self.truth_table:
            self.xorGate.pin_a = solution[0][0]
            self.xorGate.pin_b = solution[0][1]
            self.xorGate.update()
            assert self.xorGate.pin_x == solution[1][0]
        print("XorGate test success!")

class MuxGateTestBench:
    def __init__(self):
        self.muxGate = MuxGate()
        self.truth_table = [[[0, 0, 0], [0]], 
                            [[0, 0, 1], [0]], 
                            [[0, 1, 0], [0]], 
                            [[0, 1, 1], [1]], 
                            [[1, 0, 0], [1]], 
                            [[1, 0, 1], [0]], 
                            [[1, 1, 0], [1]], 
                            [[1, 1, 1], [1]]]

    def test(self):
        for solution in self.truth_table:
            self.muxGate.pin_a = solution[0][0]
            self.muxGate.pin_b = solution[0][1]
            self.muxGate.pin_sel = solution[0][2]
            self.muxGate.update()
            assert self.muxGate.pin_x == solution[1][0]
        print("MuxGate test success!")

class DMuxGateTestBench:
    def __init__(self):
        self.dMux = DMuxGate()
        self.truth_table = [[[0, 0], [0, 0]],
                            [[0, 1], [0, 0]],
                            [[1, 0], [1, 0]],
                            [[1, 1], [0, 1]]]

    def test(self):
        for solution in self.truth_table:
            self.dMux.pin_a = solution[0][0]
            self.dMux.pin_sel = solution[0][1]
            self.dMux.update()
            assert self.dMux.pin_x == solution[1][0]
            assert self.dMux.pin_y == solution[1][1]
        print("DMuxGate test success!")

class Not16TestBench:
    def __init__(self, testCycles=100):
        self.not16 = Not16()
        self.truth_table = []
        for cycle in range(testCycles):
            test_bus_a = [random.choice([0, 1]) for ii in range(16)]
            test_bus_x = [self.notFunction(ii) for ii in test_bus_a]
            self.truth_table.append([test_bus_a, test_bus_x])

    def notFunction(self, pin_a_in):
        if(pin_a_in == 0):
            return(1)
        else:
            return(0)

    def test(self):
        for solution in self.truth_table:
            for ii in range(16):
                self.not16.pin_a_bus[ii] = solution[0][ii]
            self.not16.update()
            for ii in range(16):
                assert self.not16.pin_x_bus[ii] == solution[1][ii]

        print("Not16 test success!")

class And16TestBench:
    def __init__(self, testCycles=100):
        self.and16 = And16()
        self.truth_table = []
        for cycle in range(testCycles):
            test_bus_a = [random.choice([0, 1]) for ii in range(16)]
            test_bus_b = [random.choice([0, 1]) for ii in range(16)]
            test_bus_x = [self.andFunction(ii, jj) for ii, jj in zip(test_bus_a, test_bus_b)]
            self.truth_table.append([[test_bus_a, test_bus_b], [test_bus_x]])

    def andFunction(self, pin_a_in, pin_b_in):
        if(pin_a_in and pin_b_in):
            return(1)
        else:
            return(0)

    def test(self):
        for solution in self.truth_table:
            for ii in range(16):
                self.and16.pin_a_bus[ii] = solution[0][0][ii]
                self.and16.pin_b_bus[ii] = solution[0][1][ii]
            self.and16.update()
            for ii in range(16):
                assert self.and16.pin_x_bus[ii] == solution[1][0][ii]

        print("And16 test success!")

class Or16TestBench:
    def __init__(self, testCycles=100):
        self.or16 = Or16()
        self.truth_table = []
        for cycle in range(testCycles):
            test_bus_a = [random.choice([0, 1]) for ii in range(16)]
            test_bus_b = [random.choice([0, 1]) for ii in range(16)]
            test_bus_x = [self.orFunction(ii, jj) for ii, jj in zip(test_bus_a, test_bus_b)]
            self.truth_table.append([[test_bus_a, test_bus_b], [test_bus_x]])

    def orFunction(self, pin_a_in, pin_b_in):
        if(pin_a_in or pin_b_in):
            return(1)
        else:
            return(0)

    def test(self):
        for solution in self.truth_table:
            for ii in range(16):
                self.or16.pin_a_bus[ii] = solution[0][0][ii]
                self.or16.pin_b_bus[ii] = solution[0][1][ii]
            self.or16.update()
            for ii in range(16):
                assert self.or16.pin_x_bus[ii] == solution[1][0][ii]

        print("Or16 test success!")

class Mux16TestBench:
    def __init__(self, testCycles=100):
        self.mux16 = Mux16()
        self.truth_table = []
        for cycle in range(testCycles):
            test_bus_a = [random.choice([0, 1]) for ii in range(16)]
            test_bus_b = [random.choice([0, 1]) for ii in range(16)]
            test_sel = random.choice([0, 1])
            test_bus_x = [self.muxFunction(ii, jj, test_sel) for ii, jj in zip(test_bus_a, test_bus_b)]
            self.truth_table.append([[test_bus_a, test_bus_b, test_sel], [test_bus_x]])

    def muxFunction(self, pin_a_in, pin_b_in, pin_sel_in):
        if(pin_sel_in):
            return(pin_b_in)
        else:
            return(pin_a_in)

    def test(self):
        for solution in self.truth_table:
            for ii in range(16):
                self.mux16.pin_a_bus[ii] = solution[0][0][ii]
                self.mux16.pin_b_bus[ii] = solution[0][1][ii]
            self.mux16.pin_sel = solution[0][2]
            self.mux16.update()
            for ii in range(16):
                assert self.mux16.pin_x_bus[ii] == solution[1][0][ii]

        print("Mux16 test success!")

class Or8WayTestBench:
    def __init__(self, testCycles=100):
        self.or8way = Or8Way()
        self.truth_table = []
        for cycle in range(testCycles):
            test_input_bus = [random.choice([0, 1]) for ii in range(8)]
            if any(test_input_bus):
                test_pin_x = 1
            else:
                test_pin_x = 0
            self.truth_table.append([test_input_bus, test_pin_x])

    def test(self):
        for solution in self.truth_table:
            self.or8way.pin_a = solution[0][0]
            self.or8way.pin_b = solution[0][1]
            self.or8way.pin_c = solution[0][2]
            self.or8way.pin_d = solution[0][3]
            self.or8way.pin_e = solution[0][4]
            self.or8way.pin_f = solution[0][5]
            self.or8way.pin_g = solution[0][6]
            self.or8way.pin_h = solution[0][7]

            self.or8way.update()

            assert self.or8way.pin_x == solution[1]
        print("Or8Way test success!")

class Mux4Way16TestBench:
    def __init__(self, testCycles=100):
        self.mux4way16 = Mux4Way16()
        self.truth_table = []
        for cycle in range(testCycles):
            test_a_bus = [random.choice([0, 1]) for ii in range(16)]
            test_b_bus = [random.choice([0, 1]) for ii in range(16)]
            test_c_bus = [random.choice([0, 1]) for ii in range(16)]
            test_d_bus = [random.choice([0, 1]) for ii in range(16)]
            test_sel0 = random.choice([0, 1])
            test_sel1 = random.choice([0, 1])

            test_x_bus = self.thisFunction(test_a_bus, test_b_bus, test_c_bus, test_d_bus, test_sel0, test_sel1)
            self.truth_table.append([[test_a_bus, test_b_bus, test_c_bus, test_d_bus, test_sel0, test_sel1], test_x_bus])

    def thisFunction(self, test_a_bus_in, test_b_bus_in, test_c_bus_in, test_d_bus_in, test_sel0_in, test_sel1_in):
        if(not(test_sel1_in) and not(test_sel0_in)):
            test_x_bus_out = test_a_bus_in
        elif(not(test_sel1_in) and test_sel0_in):
            test_x_bus_out = test_b_bus_in 
        elif(test_sel1_in and not(test_sel0_in)):
            test_x_bus_out = test_c_bus_in 
        elif(test_sel1_in and test_sel0_in):
            test_x_bus_out = test_d_bus_in
        else:
            print("Error: invalid values on sel lines in Mux4Way16TestBench")
            exit(1)
        return(test_x_bus_out)

    def test(self):
        for solution in self.truth_table:
            for ii in range(16):
                self.mux4way16.pin_a_bus[ii] = solution[0][0][ii]
                self.mux4way16.pin_b_bus[ii] = solution[0][1][ii]
                self.mux4way16.pin_c_bus[ii] = solution[0][2][ii]
                self.mux4way16.pin_d_bus[ii] = solution[0][3][ii]
            self.mux4way16.pin_sel0 = solution[0][4]
            self.mux4way16.pin_sel1 = solution[0][5]

            self.mux4way16.update()

            for ii in range(16):
                assert self.mux4way16.pin_x_bus[ii] == solution[1][ii]
        print("Mux4Way16 test success!!")

class Mux8Way16TestBench:
    def __init__(self, testCycles=100):
        self.mux8way16 = Mux8Way16()
        self.truth_table = []
        for cycle in range(testCycles):
            test_a_bus = [random.choice([0, 1]) for ii in range(16)]
            test_b_bus = [random.choice([0, 1]) for ii in range(16)]
            test_c_bus = [random.choice([0, 1]) for ii in range(16)]
            test_d_bus = [random.choice([0, 1]) for ii in range(16)]
            test_e_bus = [random.choice([0, 1]) for ii in range(16)]
            test_f_bus = [random.choice([0, 1]) for ii in range(16)]
            test_g_bus = [random.choice([0, 1]) for ii in range(16)]
            test_h_bus = [random.choice([0, 1]) for ii in range(16)]
            test_sel0 = random.choice([0, 1])
            test_sel1 = random.choice([0, 1])
            test_sel2 = random.choice([0, 1])

            test_x_bus = self.thisFunction(test_a_bus, test_b_bus, test_c_bus, test_d_bus, test_e_bus, test_f_bus, test_g_bus, test_h_bus, test_sel0, test_sel1, test_sel2)
            self.truth_table.append([[test_a_bus, test_b_bus, test_c_bus, test_d_bus, test_e_bus, test_f_bus, test_g_bus, test_h_bus, test_sel0, test_sel1, test_sel2], test_x_bus])

    def thisFunction(self, test_a_bus_in, test_b_bus_in, test_c_bus_in, test_d_bus_in, test_e_bus_in, test_f_bus_in, test_g_bus_in, test_h_bus_in, test_sel0_in, test_sel1_in, test_sel2_in):
        test_sel_array = [test_sel2_in, test_sel1_in, test_sel0_in]
        if(test_sel_array == [0, 0, 0]):
            test_x_bus_out = test_a_bus_in
        elif(test_sel_array == [0, 0, 1]):
            test_x_bus_out = test_b_bus_in 
        elif(test_sel_array == [0, 1, 0]):
            test_x_bus_out = test_c_bus_in 
        elif(test_sel_array == [0, 1, 1]):
            test_x_bus_out = test_d_bus_in
        elif(test_sel_array == [1, 0, 0]):
            test_x_bus_out = test_e_bus_in
        elif(test_sel_array == [1, 0, 1]):
            test_x_bus_out = test_f_bus_in
        elif(test_sel_array == [1, 1, 0]):
            test_x_bus_out = test_g_bus_in
        elif(test_sel_array == [1, 1, 1]):
            test_x_bus_out = test_h_bus_in
        else:
            print("Error: invalid values on sel lines in Mux4Way16TestBench")
            exit(1)
        return(test_x_bus_out)

    def test(self):
        for solution in self.truth_table:
            for ii in range(16):
                self.mux8way16.pin_a_bus[ii] = solution[0][0][ii]
                self.mux8way16.pin_b_bus[ii] = solution[0][1][ii]
                self.mux8way16.pin_c_bus[ii] = solution[0][2][ii]
                self.mux8way16.pin_d_bus[ii] = solution[0][3][ii]
                self.mux8way16.pin_e_bus[ii] = solution[0][4][ii]
                self.mux8way16.pin_f_bus[ii] = solution[0][5][ii]
                self.mux8way16.pin_g_bus[ii] = solution[0][6][ii]
                self.mux8way16.pin_h_bus[ii] = solution[0][7][ii]
            self.mux8way16.pin_sel0 = solution[0][8]
            self.mux8way16.pin_sel1 = solution[0][9]
            self.mux8way16.pin_sel2 = solution[0][10]

            self.mux8way16.update()

            for ii in range(16):
                assert self.mux8way16.pin_x_bus[ii] == solution[1][ii]
        print("Mux8Way16 test success!!")

class DMux4WayTestBench:
    def __init__(self):
        self.dmux4Way = DMux4Way()
        self.truth_table = [[[0, 0, 0], [0, 0, 0, 0]],
                            [[0, 0, 1], [0, 0, 0, 0]],
                            [[0, 1, 0], [0, 0, 0, 0]],
                            [[0, 1, 1], [0, 0, 0, 0]],
                            [[1, 0, 0], [1, 0, 0, 0]],
                            [[1, 0, 1], [0, 1, 0, 0]],
                            [[1, 1, 0], [0, 0, 1, 0]],
                            [[1, 1, 1], [0, 0, 0, 1]]]

    def test(self):
        for solution in self.truth_table:
            self.dmux4Way.pin_a = solution[0][0]
            self.dmux4Way.pin_sel0 = solution[0][1]
            self.dmux4Way.pin_sel1 = solution[0][2]

            self.dmux4Way.update()

            assert [self.dmux4Way.pin_w, self.dmux4Way.pin_x, self.dmux4Way.pin_y, self.dmux4Way.pin_z] == solution[1]

        print("DMux4Way test success!!")

class DMux8WayTestBench:
    def __init__(self):
        self.dmux8Way = DMux8Way()
        self.truth_table = [[[0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
                            [[0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0]],
                            [[0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
                            [[0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0]],
                            [[0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
                            [[0, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0]],
                            [[0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
                            [[0, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0]],
                            [[1, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]],
                            [[1, 0, 0, 1], [0, 1, 0, 0, 0, 0, 0, 0]],
                            [[1, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0, 0]],
                            [[1, 0, 1, 1], [0, 0, 0, 1, 0, 0, 0, 0]],
                            [[1, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0]],
                            [[1, 1, 0, 1], [0, 0, 0, 0, 0, 1, 0, 0]],
                            [[1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 1, 0]],
                            [[1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1]]]

    def test(self):
        for solution in self.truth_table:
            self.dmux8Way.pin_a = solution[0][0]
            self.dmux8Way.pin_sel0 = solution[0][1]
            self.dmux8Way.pin_sel1 = solution[0][2]
            self.dmux8Way.pin_sel2 = solution[0][3]

            self.dmux8Way.update()
            test_output = [self.dmux8Way.pin_s, self.dmux8Way.pin_t, self.dmux8Way.pin_u, self.dmux8Way.pin_v, self.dmux8Way.pin_w, self.dmux8Way.pin_x, self.dmux8Way.pin_y, self.dmux8Way.pin_z]
            assert test_output == solution[1]

        print("DMux8Way test success!!")

if __name__ == '__main__':
    import random
    import pdb 
    # pdb.set_trace()
    testCycles = 100 # For chips that have too many inputs to be exhaustively tested
    notGateTestBench = NotGateTestBench()
    notGateTestBench.test()
    andGateTestBench = AndGateTestBench()
    andGateTestBench.test()
    OrGateTestBench = OrGateTestBench()
    OrGateTestBench.test()
    xorGateTestBench = XorGateTestBench()
    xorGateTestBench.test()
    muxGateTestBench = MuxGateTestBench()
    muxGateTestBench.test()
    dmuxGateTestBench = DMuxGateTestBench()
    dmuxGateTestBench.test()
    not16TestBench = Not16TestBench(testCycles=testCycles)
    not16TestBench.test()
    and16TestBench = And16TestBench(testCycles=testCycles)
    and16TestBench.test()
    or16TestBench = Or16TestBench(testCycles=testCycles)
    or16TestBench.test()
    mux16TestBench = Mux16TestBench(testCycles=testCycles)
    mux16TestBench.test()
    or8WayTestBench = Or8WayTestBench(testCycles=testCycles)
    or8WayTestBench.test()
    mux4Way16TestBench = Mux4Way16TestBench(testCycles=testCycles)
    mux4Way16TestBench.test()
    mux8way16TestBench = Mux8Way16TestBench(testCycles=testCycles)
    mux8way16TestBench.test()
    dmux4WayTestBench = DMux4WayTestBench()
    dmux4WayTestBench.test()
    dmux8WayTestBench = DMux8WayTestBench()
    dmux8WayTestBench.test()