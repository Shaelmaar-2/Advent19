class Computer:

    def __init__(self, inputtape, phaseinput, thrustinput):
        self.tape = inputtape
        self.index = 0
        self.phaseInput = phaseinput
        self.thrustinput = thrustinput
        self.thrustoutput = 0
        self.halted = False
        self.finished = False

    def intcodecomp(self, dex, input):
        struct, param1, param2, param3 = self.paramparse(self.tape[dex])

        if struct == 99:
            self.finished = True
            return 0  # indicates halt condition

        if param1 == 0:
            param1 = self.tape[dex + 1]
        else:
            param1 = dex + 1

        if param2 == 0 and not (struct == 3 or struct == 4):
            param2 = self.tape[dex + 2]
        else:
            param2 = dex + 2

        if param3 == 0 and not ((struct == 5 or struct == 6) or (struct == 3 or struct == 4)):
            param3 = self.tape[dex + 3]
        else:
            param3 = dex + 3

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
        else:
            print("Opcode {} encountered at {}, halting.".format(self.tape[dex], dex))
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
            next = self.intcodecomp(self.index, self.thrustinput)
            self.index += next

    def nextthrustinput(self, new):
        self.thrustinput = new
        self.phaseInput = new
        self.halted = False
