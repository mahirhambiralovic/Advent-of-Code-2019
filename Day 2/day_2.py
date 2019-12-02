# PART 1
def execute(intcode):
    i=0
    while(True):
        if i > len(intcode)-3:
            print("End of intcodes")
            break
        opcode = intcode[i]
        inpos_1 = intcode[i+1]
        inpos_2 = intcode[i+2]
        outpos = intcode[i+3]
        if opcode == 1:
            intcode[outpos] = intcode[inpos_1] + intcode[inpos_2]
        elif opcode == 2:
            intcode[outpos] = intcode[inpos_1] * intcode[inpos_2]
        elif opcode == 99:
            #print("HALT")
            break
        else:
            #print("PANIC - Wrong opcode at position [{}]".format(i))
            break
        i+=4
    return intcode[0]

f = open("input.txt","r")
intcode = f.read().split(",")
intcode = list(map(int, intcode))
print(intcode)

for noun in range(100):
    result = 0
    for verb in range(100):
        t_intcode = intcode.copy()
        t_intcode[1] = noun
        t_intcode[2] = verb
        result = execute(t_intcode)
        if result == 19690720:
            print(result)
            break
        # For efficiency, break when number goes above
        elif result > 19690720:
            break
    if result == 19690720:
        print("{}{}".format(noun,verb))
        break
