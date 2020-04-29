
import re
from copy import copy
from collections import defaultdict
from itertools import permutations
import numpy as np
import cv2

from Computer import Computer

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
""" Day 6
with open("input6.txt", 'r') as txt:
    orbs = [orbit.split(')') for orbit in txt.readlines()]
    orbs = [(orbit[0].strip(), orbit[1].strip()) for orbit in orbs]
    bodies = set()
    for pair in orbs:
        bodies.add(pair[0])
        bodies.add(pair[1])

orbits = {}
map = defaultdict(set)

for pair in orbs:
    center, orbiter = pair
    orbits[orbiter] = center
    map[center].add(orbiter)


def orbitcount(leaforbiter):
    if leaforbiter == 'COM':
        return 0
    else:
        return 1 + orbitcount(orbits[leaforbiter])


def pathtocom(body):
    if body == "COM":
        return "COM"
    else:
        return pathtocom(orbits[body]) + "){}".format(body)


san = pathtocom("SAN").split(')')
me = pathtocom("YOU").split(')')

print(san)
print(me)

i = 0
while me[i] == san[i]:
    i += 1
i += 1
print(len(san) - i + len(me) - i)
"""
""" Day7 

with open("input7.txt", 'r') as txt:
    codes = [int(op) for op in txt.readlines()[0].split(',')]

toycodes = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,
            27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]

max = 0

for l in list(permutations(range(5, 10))):
    comp = Computer(copy(codes), l[0], 0)
    comp.run()
    comp2 = Computer(copy(codes), l[1], comp.thrustoutput)
    comp2.run()
    comp3 = Computer(copy(codes), l[2], comp2.thrustoutput)
    comp3.run()
    comp4 = Computer(copy(codes), l[3], comp3.thrustoutput)
    comp4.run()
    comp5 = Computer(copy(codes), l[4], comp4.thrustoutput)
    comp5.run()
    while not comp5.finished:
        comp.nextthrustinput(comp5.thrustoutput)
        comp.run()
        comp2.nextthrustinput(comp.thrustoutput)
        comp2.run()
        comp3.nextthrustinput(comp2.thrustoutput)
        comp3.run()
        comp4.nextthrustinput(comp3.thrustoutput)
        comp4.run()
        comp5.nextthrustinput(comp4.thrustoutput)
        comp5.run()

    if max < comp5.thrustoutput:
        max = comp5.thrustoutput
    print('----------------------')
print(max)
"""

"""Day 8
with open('input8.txt', 'r') as txt:
    layers = np.asarray([int(pixel) for pixel in txt.readline()]).reshape((-1, 150))

layerinfo = []
for x,layer in enumerate(layers):
    layerdict = defaultdict(int)
    for elem in layer:
        layerdict[elem] += 1
    layerinfo.append(layerdict)

layerinfo = sorted(layerinfo, key=lambda x: x[0])

print('part 1:', layerinfo[0][1] * layerinfo[0][2])

layers = layers.reshape((-1, 6, 25))
final = np.zeros((6, 25))

for i in range(len(final)):
    for j in range(len(final[i])):
        depth = 0
        while layers[depth][i][j] == 2 and depth < len(layers):
            depth += 1
        final[i][j] = 255 * layers[depth][i][j]

cv2.imshow('final bios', final)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
"""Day 10
toycodes = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
with open('inputs/input9.txt', 'r') as txt:
    codes = [int(code) for code in txt.readline().strip().split(',')]
comp = Computer(codes, 1, None)
comp.run()
"""

"""Day 10 --Incomplete--
with open('inputs/input10.txt', 'r') as txt:
    astroidbelt = [line.strip() for line in txt.readlines()]
astroids = {}
for i in range(len(astroidbelt)):
    for j in range(len(astroidbelt[i])):
        if astroidbelt[i][j] == "#":
            astroids[(i, j)] = set()
mslopes = defaultdict(int)
maxplace = None
max

for roid in astroids.keys():
    for roid2 in astroids.keys():
        if not roid2 == roid:
            if (roid2[0] - roid[0]) != 0:
                m = (roid2[1] - roid[1]) / (roid2[0] - roid[0])
            else:
                m = 'inf'
            xdir = ''
            ydir = ''
            if roid[0] <= roid2[0]:
                xdir = 'r'
            else:
                xdir = 'l'
            if roid[1] <= roid2[1]:
                ydir = 'u'
            else:
                ydir = 'd'
            if (m, (xdir, ydir)) not in astroids[roid]:
                astroids[roid].add((m, (xdir, ydir)))
# 17,14
"""
with open('inputs/input11.txt', 'r') as inp:
    instructions = [int(command) for command in inp.readline().strip().split(',')]
comp = Computer(instructions, 0, 0)
hull = defaultdict(int)
pos = [0, 0]
dirs = {0: -1, 1: 1, 2: 1, 3: -1}
dir = 0
tiles = 0
while not comp.finished:
    comp.run()
    if tuple(pos) not in hull:
        tiles += 1
    hull[tuple(pos)] = comp.thrustoutput
    comp.run()
    if comp.thrustoutput == 1:
        dir = (dir + 1) % 4
    else:
        dir = (dir - 1) % 4
    if dir in (1, 3):
        pos[1] += dirs[dir]
    else:
        pos[0] += dirs[dir]
    comp.nextthrustinput(hull[tuple(pos)])
print(len(hull))
