from itertools import permutations
import math
import numpy as np

def get_params(firstcode):
    opcode = int(firstcode[-1])
    mode1 = 0
    mode2 = 0
    mode3 = 0
    if len(firstcode) > 2:
        mode1 = int(firstcode[-3])
    if len(firstcode) > 3:
        mode2 = int(firstcode[-4])
    if len(firstcode) > 4:
        mode3 = int(firstcode[-5])
    return opcode,mode1,mode2,mode3

def execute(intcode):
    i = 0
    relbase = 0
    input = 1
    orientation = ['u'] # Must be mutable within methods
    dimensions = 100
    panels = np.zeros((dimensions,dimensions), dtype=int)
    position = [int(dimensions/2) , int(dimensions/2)]
    panels.itemset((position[0],position[1]),1)
    outputs_arr = []
    covered_panels = set()
    for x in range(dimensions-1):
        for y in range(dimensions-1):
            print(panels[x][y], end=" ")
        print()
    while True:
        #print(i)
        firstcode = str(intcode[i])
        opcode, mode1, mode2, mode3 = get_params(firstcode)
        #print("{}: [{}, {}, {}, {}]".format(i, firstcode, intcode[i+1], intcode[i+2], intcode[i+3], intcode[i+4]))
        #print(opcode,mode1,mode2,mode3)
        # Get value at address (if relevant)
        if mode1 == 1: #VAL
            par1 = intcode[i+1]
        elif mode1 == 2: #REL
            #print("RELBASE")
            par1 = intcode[relbase + intcode[i+1]]
        else:
            par1 = intcode[intcode[i+1]]

        if mode2 == 1:
            par2 = intcode[i+2]
        elif mode2 == 2:
            #print("RELBASE")
            par2 = intcode[relbase + intcode[i+2]]
        else:
            par2 = intcode[intcode[i+2]]

        if firstcode[-2:] == "99":
            print("HALT")
            break

        if opcode == 1:
            out = intcode[i+3]
            if mode3 == 2:
                out += relbase
            ##print("ADDING {} + {}. Placing it at address {}".format(par1,par2, out))
            intcode[out] = par1 + par2
            i += 4
        elif opcode == 2:
            out = intcode[i+3]
            if mode3 == 2:
                out += relbase
            ##print("MUL {} * {}. Placing it at address {}".format(par1,par2, out))
            intcode[out] = par1 * par2
            i += 4

        elif opcode == 3:
            ##print("INPUTTING {} AT {}".format(input,intcode[i+1]))
            if mode1 == 2:
                ##print("INPUTTING {} AT {}".format(input,relbase))
                intcode[relbase] = input
                i += 2
            intcode[intcode[i+1]] = input
            i += 2
        elif opcode == 4:
            if len(outputs_arr) == 0:
                #print("First output value: {}".format(par1))
                outputs_arr.append(par1)
            else:
                outputs_arr.append(par1)
                values = (outputs_arr[0],outputs_arr[1])
                input = move_robot(orientation, panels, position, values, covered_panels)
                outputs_arr.clear()
            ##print("OUTPUT IS:")
            ##print(par1, end=" ")
            i += 2


        elif opcode == 5:
            if par1 != 0:
                ##print("TRUE: Changing i to {}".format(par2))
                i = par2
            else:
                i += 3
        elif opcode == 6:
            if par1 == 0:
                ##print("FALSE: Changing i to {}".format(par2))
                i = par2
            else:
                i += 3

        elif opcode == 7:
            out = intcode[i+3]
            if mode3 == 2:
                out += relbase
            if par1 < par2:
                ##print("TRUE {} < {}".format(par1, par2))
                intcode[out] = 1
            else:
                ##print("FALSE {} < {}".format(par1, par2))
                intcode[out] = 0
            i += 4
        elif opcode == 8:
            out = intcode[i+3]
            if mode3 == 2:
                out += relbase
            if par1 == par2:
                ##print("TRUE {} == {}".format(par1, par2))
                intcode[out] = 1
            else:
                ##print("FALSE {} == {}".format(par1, par2))
                intcode[out] = 0
            i += 4

        elif opcode == 9:
            ##print("new relbase = {}".format(relbase+par1))
            relbase += par1
            i+=2
    # print("Covered panels: {}".format(covered_panels))
    print(len(covered_panels))
    for i in range(dimensions):
        for j in range(dimensions):
            if panels[i][j] == 1:
                print("#", end=" ")
            else:
                print(" ", end=" ")
        print()
    np.set_printoptions(threshold=np.inf)

def move_robot(orientation, panels, position, values, covered_panels):
    # Paint
    covered_panels.add((position[0],position[1]))
    panels.itemset((position[0], position[1]), values[0])
    # UP
    if orientation[0] == 'u':
        if values[1] == 0:
            orientation[0] = 'l'
        else:
            orientation[0] = 'r'
    # DOWN
    elif orientation[0] == 'd':
        if values[1] == 0:
            orientation[0] = 'r'
        else:
            orientation[0] = 'l'
    # LEFT
    elif orientation[0] == 'l':
        if values[1] == 0:
            orientation[0] = 'd'
        else:
            orientation[0] = 'u'
    # RIGHT

    elif orientation[0] == 'r':
        if values[1] == 0:
            orientation[0] = 'u'
        else:
            orientation[0] = 'd'

    if orientation[0] == 'u':
        position[0] -=1
    elif orientation[0] == 'd':
        position[0] +=1
    elif orientation[0] == 'r':
        position[1] +=1
    elif orientation[0] == 'l':
        position[1] -=1

    return panels[position[0]][position[1]]

f = open("input.txt","r")
intcode = f.read().split(",")
intcode = list(map(int, intcode))
intcode.extend([0]*1000000) # EXTEND MEMORY

execute(intcode)
