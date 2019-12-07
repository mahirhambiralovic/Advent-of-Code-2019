from itertools import permutations

# PART 1
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
            #print("Fetching first address {}".format(intcode[i+1]))
            par1 = intcode[intcode[i+1]]
        else:
            par1 = intcode[i+1]
        #print("OUTPUT IS:")
        #print(par1)
        return 2
    else:
        # Get value at address (if relevant)
        if mode1 == 0:
            #print("Fetching first address {}".format(intcode[i+1]))
            par1 = intcode[intcode[i+1]]
        else:
            #print("First param is by value {}".format(intcode[i+1]))
            par1 = intcode[i+1]
        if mode2 == 0:
            #print("Fetching second address {}".format(intcode[i+2]))
            par2 = intcode[intcode[i+2]]
        else:
            #print("Second param is by value {}".format(intcode[i+2]))
            par2 = intcode[i+2]

        ####
        #print("par1 {}, par2 {}".format(par1,par2))

        if opcode == 1:
            out = intcode[i+3]
            #print("ADDING {} + {}. Placing it at address {}".format(par1,par2, out))
            intcode[out] = par1 + par2
            #print("CHECK. Address {} is now {}".format(out,intcode[out]))
            return 4
        elif opcode == 2:
            out = intcode[i+3]
            #print("MUL {} * {}. Placing it at address {}".format(par1,par2, out))
            intcode[out] = par1 * par2
            #print("CHECK. Address {} is now {}".format(out,intcode[out]))
            return 4
        if opcode == 5:
            if par1 != 0:
                #print("TRUE: Changing i to {}".format(par2))
                return par2 - i
            else:
                #print("Doing nothing, moving i 2 steps")
                return 3
        if opcode == 6:
            if par1 == 0:
                #print("FALSE: Changing i to {}".format(par2))
                return par2 - i
            else:
                #print("Doing nothing, moving i 2 steps")
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


def run(input1, input2, intcode):
    i=0
    first = True
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
        #print("{}: [{}, {}, {}, {}]".format(i, firstcode, intcode[i+1], intcode[i+2], intcode[i+3], intcode[i+4]))
        if len(firstcode) == 1:
            opcode = int(firstcode)
            if opcode == 3:
                first = False
            elif opcode == 4:
                #print("Fetching first address {}".format(intcode[i+1]))
                par1 = intcode[intcode[i+1]]
                #print("OUTPUT IS:")
                #print(par1)
                return par1
            #print("opcode {}".format(opcode))
            i += execute(intcode, i, opcode, 0, 0, input)
        else:
            if int(firstcode[-1]) == 9:
                print("HALT")
                break
            opcode, mode1, mode2, mode3 = get_params(firstcode)
            if opcode == 4:
                if mode1 == 0:
                    #print("Fetching first address {}".format(intcode[i+1]))
                    par1 = intcode[intcode[i+1]]
                else:
                    par1 = intcode[i+1]
                #print("OUTPUT IS:")
                #print(par1)
                return par1
            #print("opcode {}, modes: {}, {}".format(opcode, mode1, mode2))
            i += execute(intcode, i, opcode, mode1, mode2, input)


f = open("input.txt","r")
intcode = f.read().split(",")
intcode = list(map(int, intcode))
maxv = 0
for p in permutations(range(0, 5)):
        v = run(p[4],run(p[3],run(p[2],run(p[1],run(p[0],0,intcode.copy()),intcode.copy()),intcode.copy()),intcode.copy()),intcode.copy())
        if v > maxv:
            maxv = v
print(maxv)
