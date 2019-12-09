from itertools import permutations
# PART 2

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

def execute(intcode, i, opcode, mode1, mode2, mode3, input, relbase):
    # Get value at address (if relevant)
    if mode1 == 1: #VAL
        par1 = intcode[i+1]
    elif mode1 == 2: #REL
        ##print("RELBASE")
        par1 = intcode[relbase + intcode[i+1]]
    else:
        par1 = intcode[intcode[i+1]]

    if mode2 == 1:
        par2 = intcode[i+2]
    elif mode2 == 2:
        ##print("RELBASE")
        par2 = intcode[relbase + intcode[i+2]]
    else:
        par2 = intcode[intcode[i+2]]

    if opcode == 1:
        out = intcode[i+3]
        if mode3 == 2:
            out += relbase
        #print("ADDING {} + {}. Placing it at address {}".format(par1,par2, out))
        intcode[out] = par1 + par2
        return 4
    elif opcode == 2:
        out = intcode[i+3]
        if mode3 == 2:
            out += relbase
        #print("MUL {} * {}. Placing it at address {}".format(par1,par2, out))
        intcode[out] = par1 * par2
        return 4

    elif opcode == 3:
        #print("INPUTTING {} AT {}".format(input,intcode[i+1]))
        if mode1 == 2:
            #print("INPUTTING {} AT {}".format(input,relbase))
            intcode[relbase] = input
            return 2
        intcode[intcode[i+1]] = input
        return 2
    elif opcode == 4:
        #print("OUTPUT IS:")
        print(par1, end=" ")
        return 2


    elif opcode == 5:
        if par1 != 0:
            #print("TRUE: Changing i to {}".format(par2))
            return par2 - i
        else:
            return 3
    elif opcode == 6:
        if par1 == 0:
            #print("FALSE: Changing i to {}".format(par2))
            return par2 - i
        else:
            return 3

    elif opcode == 7:
        out = intcode[i+3]
        if mode3 == 2:
            out += relbase
        if par1 < par2:
            #print("TRUE {} < {}".format(par1, par2))
            intcode[out] = 1
        else:
            #print("FALSE {} < {}".format(par1, par2))
            intcode[out] = 0
        return 4
    elif opcode == 8:
        out = intcode[i+3]
        if mode3 == 2:
            out += relbase
        if par1 == par2:
            #print("TRUE {} == {}".format(par1, par2))
            intcode[out] = 1
        else:
            #print("FALSE {} == {}".format(par1, par2))
            intcode[out] = 0
        return 4

    elif opcode == 9:
        #print("new relbase = {}".format(relbase+par1))
        return relbase + par1


f = open("input.txt","r")
intcode = f.read().split(",")
intcode = list(map(int, intcode))
intcode.extend([0]*1000000) # EXTEND MEMORY
i=0
relbase = 0
input = 2
while(True):
    #print()
    if i > len(intcode):
        #print("End of intcodes")
        break
    firstcode = str(intcode[i])
    #print("{}: [{}, {}, {}, {}]".format(i, firstcode, intcode[i+1], intcode[i+2], intcode[i+3], intcode[i+4]))
    if int(firstcode[-2:]) == 99:
        #print("HALT")
        break
    opcode, mode1, mode2, mode3 = get_params(firstcode)
    #print("opcode {}, modes: {}, {}, {}".format(opcode, mode1, mode2, mode3))
    if opcode == 9:
        relbase = execute(intcode, i, opcode, mode1, mode2, mode3, input, relbase)
        i += 2
    else:
        i += execute(intcode, i, opcode, mode1, mode2, mode3, input, relbase)
