from collections import defaultdict

class Computer:

    def __init__(self, inputtape, phaseinput, thrustinput):
        self.tape = inputtape + [0 for x in range(10000)]
        self.extra_mem = defaultdict(int)
        self.index = 0
        self.phaseInput = phaseinput
        self.thrustinput = thrustinput
        self.thrustoutput = 0
        self.halted = False
        self.finished = False
        self.relativebase = 0

    def intcodecomp(self, dex, input):
        struct, param1, param2, param3 = self.paramparse(self.tape[dex])

        if struct == 99:
            self.finished = True
            return 0  # indicates halt condition

        if param1 == 0:
            param1 = self.tape[dex + 1]
        elif param1 == 1:
            param1 = dex + 1
        else:
            param1 = self.tape[dex + 1] + self.relativebase

        if struct not in [3, 4, 9]:
            if param2 == 0:
                param2 = self.tape[dex + 2]
            elif param2 == 1:
                param2 = dex + 2
            else:
                param2 = self.tape[dex + 2] + self.relativebase
            if struct not in [5, 6]:
                if param3 == 0:
                    param3 = self.tape[dex + 3]
                elif param3 == 1:
                    param3 = dex + 3
                else:
                    param3 = self.tape[dex + 3] + self.relativebase

        if struct == 1:
            self.tape[param3] = self.tape[param1] + self.tape[param2]
            return 4
        elif struct == 2:
            self.tape[param3] = self.tape[param1] * self.tape[param2]
            return 4
        elif struct == 3 and input is not None:
            self.tape[param1] = input
            return 2
        elif struct == 4:
            # print(param1)
            print(self.tape[param1])
            self.thrustoutput = self.tape[param1]
            if self.thrustinput is not None:
                self.halted = True
            return 2
        elif struct == 5:
            if not self.tape[param1] == 0:
                self.index = self.tape[param2]
                return 0
            else:
                return 3
        elif struct == 6:
            if self.tape[param1] == 0:
                self.index = self.tape[param2]
                return 0
            else:
                return 3
        elif struct == 7:
            if self.tape[param1] < self.tape[param2]:
                self.tape[param3] = 1
                return 4
            else:
                self.tape[param3] = 0
                return 4
        elif struct == 8:
            if self.tape[param1] == self.tape[param2]:
                self.tape[param3] = 1
                return 4
            else:
                self.tape[param3] = 0
                return 4
        elif struct == 9:
            self.relativebase += self.tape[param1]
            return 2
        else:
            print("Opcode {} encountered at {}, halting.".format(struct, dex))
            self.finished = True
            # return None  # program failure halt condition

    def paramparse(self, instruction):
        struct = instruction % 100
        param1 = (instruction // 100) % 10
        param2 = (instruction // 1000) % 10
        param3 = (instruction // 10000) % 10

        return struct, param1, param2, param3

    def run(self):
        next = self.intcodecomp(self.index, self.phaseInput)
        self.index += next
        while not (self.finished or self.halted):
            if self.thrustinput is not None:
                next = self.intcodecomp(self.index, self.thrustinput)
            else:
                next = self.intcodecomp(self.index,self.phaseInput)
            self.index += next

    def nextthrustinput(self, new):
        self.thrustinput = new
        self.phaseInput = new
        self.halted = False

    def get_mem(self):
        pass
