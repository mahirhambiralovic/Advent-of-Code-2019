from itertools import permutations
import math
import numpy as np
import sys
import time

def print_grid(grid):
    for y in range(29):
        for x in range(49):
            if int(grid[x][y]) == 0:
                print(" ", end=" ")
            elif int(grid[x][y]) == 1:
                print("#", end=" ")
            elif int(grid[x][y]) == 2:
                print("O", end=" ")
            elif int(grid[x][y]) == 3:
                print("_", end=" ")
            elif int(grid[x][y]) == 4:
                print("@", end=" ")
        print()

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
    playing_mode = False
    displaying = True
    score = 0
    ball_position = (0,0)
    paddle_position = (0,0)
    i = 0
    relbase = 0
    input1 = 1
    dimensions = 50
    temp_outputs = []
    grid = np.zeros((dimensions,dimensions))
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
            print("FINAL SCORE = {}".format(score))
            print("HALT")
            return grid

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
            if displaying:
                print_grid(grid)
                time.sleep(0.050)
            if playing_mode:
                direction = input("a for left, d for right")
                if direction == "a":
                    input1 = -1
                elif direction == "d":
                    input1 = 1
                else:
                    input1 = 0
            else:
                if ball_position[0] > paddle_position[0]:
                    input1 = 1
                elif ball_position[0] < paddle_position[0]:
                    input1 = -1
                else:
                    input1 = 0
            ##print("INPUTTING {} AT {}".format(input,intcode[i+1]))
            if mode1 == 2:
                ##print("INPUTTING {} AT {}".format(input,relbase))
                intcode[relbase] = input1
                i += 2
            intcode[intcode[i+1]] = input1
            i += 2
        elif opcode == 4:
            if len(temp_outputs) < 2:
                #print("Adding output value: {}".format(par1))
                temp_outputs.append(par1)
            else:
                #print("Adding LAST output value: {}".format(par1))
                temp_outputs.append(par1)
                grid.itemset((temp_outputs[0],temp_outputs[1]), temp_outputs[2])
                if temp_outputs[2] == 3:
                    paddle_position = (temp_outputs[0],temp_outputs[1])
                if temp_outputs[2] == 4:
                    ball_position = (temp_outputs[0],temp_outputs[1])
                if temp_outputs[0] == -1 and temp_outputs[1] == 0:
                    score = temp_outputs[2]
                #outputs.append((temp_outputs[0],temp_outputs[1],temp_outputs[2]))
                #input1 = move_robot(orientation, panels, position, values, covered_panels)
                temp_outputs.clear()
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


f = open("input.txt","r")
intcode = f.read().split(",")
intcode = list(map(int, intcode))
intcode.extend([0]*100000) # EXTEND MEMORY
intcode[0] = 2
#print(intcode)
grid = execute(intcode)

#print(intcode)
