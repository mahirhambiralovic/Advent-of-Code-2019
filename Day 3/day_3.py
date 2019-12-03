f = open("input.txt","r")
l1 = f.readline().strip("\n").split(",")
l1_covered_points = []
current_pos = (0,0)
for instruction in l1:
    dir = instruction[0]
    steps = int(instruction[1:])
    if dir == "R":
        for i in range(steps):
            current_pos = (current_pos[0] +1, current_pos[1])
            l1_covered_points.append(current_pos)
    if dir == "L":
        for i in range(steps):
            current_pos = (current_pos[0] -1, current_pos[1])
            l1_covered_points.append(current_pos)
    if dir == "U":
        for i in range(steps):
            current_pos = (current_pos[0], current_pos[1]+1)
            l1_covered_points.append(current_pos)
    if dir == "D":
        for i in range(steps):
            current_pos = (current_pos[0], current_pos[1]-1)
            l1_covered_points.append(current_pos)

l2 = f.read().strip("\n").split(",")[:-1]
l2_covered_points = []
current_pos = (0,0)
for instruction in l2:
    dir = instruction[0]
    steps = int(instruction[1:])

    if dir == "R":
        for i in range(steps):
            current_pos = (current_pos[0] +1, current_pos[1])
            l2_covered_points.append(current_pos)
    if dir == "L":
        for i in range(steps):
            current_pos = (current_pos[0] -1, current_pos[1])
            l2_covered_points.append(current_pos)
    if dir == "U":
        for i in range(steps):
            current_pos = (current_pos[0], current_pos[1]+1)
            l2_covered_points.append(current_pos)
    if dir == "D":
        for i in range(steps):
            current_pos = (current_pos[0], current_pos[1]-1)
            l2_covered_points.append(current_pos)

matches = set(l1_covered_points) - (set(l1_covered_points) - set(l2_covered_points))
minimum = 999999999
for x in matches:
    val = abs(x[0]) + abs(x[1])
    if val < minimum:
        minimum = val
print(minimum)

# PART 2
minimum = 999999999
for pos in matches:
    #print(pos)
    i1 = l1_covered_points.index(pos)+1
    i2 = l2_covered_points.index(pos)+1
    val = abs(i1 + i2)
    if val < minimum:
        minimum = val
print(minimum)
