
import re

""" day one
def calc(load):
    if calcless(load) <= 0:
        return 0
    else:
        return calcless(load) + calc(calcless(load))


def calcless(load):
    return load//3 - 2


with open('input1.txt','r') as txt:
    lst = txt.readlines()
lst = [int(l) for l in lst]

print(sum([calc(elem) for elem in lst]))
"""
""" day 2
out = 0
input = 0;
while(out != 19690720):
    with open('input2.txt', 'r') as txt:
        codes = txt.readlines()
    codes = [int(code) for code in codes[0].split(',')]

    codes[1] = input // 100
    codes[2] = input % 100

    noun = codes[1]
    verb = codes[2]


    for i in range(0, len(codes), 4):
        if codes[i] == 99:
            break
        elif codes[i] == 1:
            codes[codes[i+3]] = codes[codes[i+1]] + codes[codes[i+2]]
        elif codes[i] == 2:
            codes[codes[i+3]] = codes[codes[i+1]] * codes[codes[i+2]]
        else:
            print("Opcode {} encountered at {}, halting.".format(codes[i], i))
    out = codes[0]
    input += 1

print(noun, verb)
"""
""" day 3
toypath1 = [('R',8),("U",5),('L',5),('D',3)]
toypath2 = [('U',7),("R",6),('D',4),('L',4)]

toypath3 = [('R',2),('U',4)]
toypath4 = [('U',2),('R',4)]


with open("input3.txt","r")as txt:
    wirePaths = txt.readlines()
    wirePaths = [path.strip() for path in wirePaths]
path1, path2 = [(path[0], int(path[1:])) for path in wirePaths[0].split(',')], \
               [(path[0], int(path[1:])) for path in wirePaths[1].split(',')]


sec1 = set()
step1 = {}
sec2 = set()
step2 = {}

pos = [0, 0]

step = 1

for move in path1:
    direction, length = move
    if direction == 'R':
        for x in range(0, length):
            if (pos[0] + 1, pos[1]) not in sec1:
                sec1.add((pos[0] + 1, pos[1]))
                step1[(pos[0] + 1, pos[1])] = step
            pos[0] += 1
            step += 1
    elif direction == "L":
        for x in range(0, length):
            if (pos[0] - 1, pos[1]) not in sec1:
                sec1.add((pos[0] - 1, pos[1]))
                step1[(pos[0] - 1, pos[1])] = step
            pos[0] -= 1
            step += 1
    elif direction == 'U':
        for x in range(0, length):
            if (pos[0], pos[1] + 1) not in sec1:
                sec1.add((pos[0], pos[1] + 1))
                step1[(pos[0], pos[1] + 1)] = step
            pos[1] += 1
            step += 1
    else:
        for x in range(0, length):
            if (pos[0], pos[1] - 1) not in sec1:
                sec1.add((pos[0], pos[1] - 1))
                step1[(pos[0], pos[1] - 1)] = step
            pos[1] -= 1
            step += 1
pos = [0, 0]
step = 1

for move in path2:
    direction, length = move
    if direction == 'R':
        for x in range(0, length):
            if (pos[0] + 1, pos[1]) not in sec2:
                sec2.add((pos[0] + 1, pos[1]))
                step2[(pos[0] + 1, pos[1])] = step
            step += 1
            # else:
            #     intersections[2].add((pos[0] + 1, pos[1]))
            pos[0] += 1
    elif direction == "L":
        for x in range(0, length):
            if (pos[0] - 1, pos[1]) not in sec2:
                sec2.add((pos[0] - 1, pos[1]))
                step2[(pos[0] - 1, pos[1])] = step
            step += 1
            # else:
            #     intersections[2].add((pos[0] - 1, pos[1]))
            pos[0] -= 1
    elif direction == 'U':
        for x in range(0, length):
            if (pos[0], pos[1] + 1) not in sec2:
                sec2.add((pos[0], pos[1] + 1))
                step2[(pos[0], pos[1] + 1)] = step
            step += 1
            # else:
            #     intersections[2].add((pos[0], pos[1] + 1))
            pos[1] += 1
    else:
        for x in range(0, length):
            if (pos[0], pos[1] - 1) not in sec2:
                sec2.add((pos[0], pos[1] - 1))
                step2[(pos[0], pos[1] - 1)] = step
            step += 1
            # else:
            #     intersections[2].add((pos[0], pos[1] - 1))
            pos[1] -= 1

print(min([abs(sect[0]) + abs(sect[1]) for sect in sec1 & sec2]))
print(min([step1[sect] + step2[sect] for sect in sec1 & sec2]))
"""

""" day 4
def inOrder(x):
    for i in range(0,len(x)-1):
        if int(x[i+1]) < int(x[i]):
            return False
    return True


def hasDouble(x):
    for i in range(10):
        for j in range(len(x)-1):
            if int(x[j]) == int(x[j+1]):
                return True
    return False


possSet = set()
oPossSet = set()

for x in range(245182, 790573):
    if(inOrder(str(x)) and hasDouble(str(x))):
        possSet.add(x)
for y in possSet:
    for x in range(2, 10):
        if re.search('[{}][{}]'.format(x,x), str(y)) and not re.search('[{}][{}][{}]'.format(x, x, x), str(y)):
            oPossSet.add(y)
print(len(oPossSet))

"""

"""Day 5
class Computer:

    def __init__(self, inputtape, inp):
        self.tape = inputtape
        self.index = 0
        self.firstInput = inp

    # def printinstruction(self, dex, oginstruction, struct, param1, param2, param3):
    # 
    #     if struct == 99:
    #         print('halt')
    #         return
    # 
    #     id = {1: 'add', 2: 'mult', 3: 'write', 4: 'print'}
    #     print("original instruction: ", oginstruction,"at index: {}".format(dex))
    # 
    #     if struct not in [3, 4]:
    #         print("Tape[{}]: {} {} Tape[{}]: {} to Tape[{}]".format(param1, self.tape[param1], id[struct], param2, self.tape[param2], param3))
    #     else:
    #         print("{} Tape[{}]".format(id[struct], param1))

    def intcodecomp(self, dex, input):
        struct, param1, param2, param3 = self.paramparse(self.tape[dex])

        if struct == 99:
            return None  # indicates halt condition

        if param1 == 0:
            param1 = self.tape[dex + 1]
        else:
            param1 = dex + 1

        if param2 == 0:
            param2 = self.tape[dex + 2]
        else:
            param2 = dex + 2

        if param3 == 0:
            param3 = self.tape[dex + 3]
        else:
            param3 = dex + 3

        # self.printinstruction(dex,self.tape[dex], struct, param1, param2, param3)

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
            return None  # program failure halt condition

    def paramparse(self, instruction):

        struct = instruction % 100
        param1 = (instruction // 100) % 10
        param2 = (instruction // 1000) % 10
        param3 = (instruction // 10000) % 10

        return struct, param1, param2, param3

    def run(self):
        next = self.intcodecomp(self.index, self.firstInput)
        while next is not None:
            self.index += next
            next = self.intcodecomp(self.index, None)


with open('input5.txt', 'r') as txt:
    codes = txt.readlines()
codes = [int(code) for code in codes[0].split(',')]
codes2 = [elem for elem in codes]

tape = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
        1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
        999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]

cpart1 = Computer(codes, 1)
cpart2 = Computer(codes2, 5)
cpart1.run()
cpart2.run()
"""
