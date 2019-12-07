from itertools import permutations
# PART 2

def get_params(firstcode):
    opcode = int(firstcode[-1])
    mode1 = int(firstcode[-3])
    mode2 = 0
    mode3 = 0
    if len(firstcode) > 3:
        mode2 = int(firstcode[-4])
    if len(firstcode) > 4:
        mode3 = int(firstcode[-5])
    return opcode,mode1,mode2,mode3

def execute(intcode, i, opcode, mode1, mode2, input):
    if opcode == 3:
        #print("INPUTTING {} AT {}".format(input,intcode[i+1]))
        intcode[intcode[i+1]] = input
        return 2
    elif opcode == 4:
        if mode1 == 0:
            par1 = intcode[intcode[i+1]]
        else:
            par1 = intcode[i+1]
        #print("OUTPUT IS:")
        #print(par1)
        return 2
    else:
        # Get value at address (if relevant)
        if mode1 == 0:
            par1 = intcode[intcode[i+1]]
        else:
            par1 = intcode[i+1]
        if mode2 == 0:
            par2 = intcode[intcode[i+2]]
        else:
            par2 = intcode[i+2]

        ####

        if opcode == 1:
            out = intcode[i+3]
            #print("ADDING {} + {}. Placing it at address {}".format(par1,par2, out))
            intcode[out] = par1 + par2
            return 4
        elif opcode == 2:
            out = intcode[i+3]
            #print("MUL {} * {}. Placing it at address {}".format(par1,par2, out))
            intcode[out] = par1 * par2
            return 4
        if opcode == 5:
            if par1 != 0:
                #print("TRUE: Changing i to {}".format(par2))
                return par2 - i
            else:
                return 3
        if opcode == 6:
            if par1 == 0:
                #print("FALSE: Changing i to {}".format(par2))
                return par2 - i
            else:
                return 3
        if opcode == 7:
            out = intcode[i+3]
            if par1 < par2:
                #print("TRUE {} < {}".format(par1, par2))
                intcode[out] = 1
            else:
                #print("FALSE {} < {}".format(par1, par2))
                intcode[out] = 0
            return 4
        if opcode == 8:
            out = intcode[i+3]
            if par1 == par2:
                #print("TRUE {} == {}".format(par1, par2))
                intcode[out] = 1
            else:
                #print("FALSE {} == {}".format(par1, par2))
                intcode[out] = 0
            return 4


def run(input1, input2, intcode, i, first):
    #print("i = {}".format(i))
    #print(intcode)
    #print(len(intcode))
    while(True):
        #print()
        if first:
            input = input1
        else:
            input = input2
        if i > len(intcode):
            #print("End of intcodes")
            break

        firstcode = str(intcode[i])
        #print("{}: [{}, {}, {}]".format(i, firstcode, intcode[i+1], intcode[i+2], intcode[i+3]))
        if len(firstcode) == 1:
            opcode = int(firstcode)
            if opcode == 3:
                first = False
            elif opcode == 4:
                #print("Fetching first address {}".format(intcode[i+1]))
                par1 = intcode[intcode[i+1]]
                #print("OUTPUT IS:")
                #print(par1)
                i+=2
                return par1, i
            #print("opcode {}".format(opcode))
            i += execute(intcode, i, opcode, 0, 0, input)
        else:
            if int(firstcode[-1]) == 9:
                #print("HALT")
                return -999999, i
            opcode, mode1, mode2, mode3 = get_params(firstcode)
            if opcode == 4:
                if mode1 == 0:
                    #print("Fetching first address {}".format(intcode[i+1]))
                    par1 = intcode[intcode[i+1]]
                else:
                    par1 = intcode[i+1]
                #print("OUTPUT IS:")
                #print(par1)
                i+=2
                return par1, i
            #print("opcode {}, modes: {}, {}".format(opcode, mode1, mode2))
            i += execute(intcode, i, opcode, mode1, mode2, input)


f = open("input.txt","r")
intcode = f.read().split(",")
intcode = list(map(int, intcode))

maxv = 0
for p in permutations(range(5, 10)):
    intcode_a = intcode.copy()
    intcode_b = intcode.copy()
    intcode_c = intcode.copy()
    intcode_d = intcode.copy()
    intcode_e = intcode.copy()

    va, ia = run(p[0],0,intcode_a, 0, True)
    vb, ib = run(p[1],va,intcode_b, 0, True)
    vc, ic = run(p[2],vb,intcode_c, 0, True)
    vd, id = run(p[3],vc,intcode_d, 0, True)
    ve, ie = run(p[4],vd,intcode_e, 0, True)

    while True:
        ##print(v)
        va, ia = run(p[0],ve,intcode_a, ia, False)
        vb, ib = run(p[1],va,intcode_b, ib, False)
        vc, ic = run(p[2],vb,intcode_c, ic, False)
        vd, id = run(p[3],vc,intcode_d, id, False)
        ve, ie = run(p[4],vd,intcode_e, ie, False)
        #print(ve)
        if ve > maxv:
            maxv = ve
        if ve == -999999:
            break

print(maxv)
