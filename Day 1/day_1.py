import sys
import math

def fuel_needed(mass):
    return math.floor(mass/3)-2

fuel_list = []
for line in sys.stdin:
    fuel_list.append(fuel_needed(int(line)))
print(sum(fuel_list))

# PART 2
sum = sum(fuel_list)
for module in fuel_list:
    fuel = fuel_needed(module)
    while(True):
        #print(fuel)
        if fuel > 0:
            sum += fuel
            fuel = fuel_needed(fuel)
        else:
            break
print(sum)
