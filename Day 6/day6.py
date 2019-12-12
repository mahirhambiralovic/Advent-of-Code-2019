f = open("input.txt", "r")
map = f.read().split()

# Since a body can only directly orbit one other body,
# we can set ut all the pairs in a tree, and then traverse
# all of the nodes. Finally adding up all the values

orbits = []

final_tree = []

for orbit in map:
    #P is for primary, S is for secondary.
    pBody = orbit[0:3]
    sBody = orbit[4:7]
    orbits.append([pBody, sBody])

total = [0] # Lists are mutable
def assembleOrbits(body, depth, total):
    orbitees = []
    for orbit in orbits:
        if orbit[0] == body:
            total[0] += depth
            orbitees.append(body)
            orbitees.append(assembleOrbits(orbit[1], depth + 1, total))
    if len(orbitees) == 0:
        return body, []
    return orbitees

final_tree = assembleOrbits("COM", 1, total)

#print(final_tree)
print(total[0])

def get_to_santa(tree, distance, found, complete):
    if not found[0]:
        distance = 0
    else:
        old_distance = distance
    if complete[0]:
        return distance
    if len(tree) == 0:
        return distance
    print()
    print(tree[0])
    del tree[0]
    print(tree[0])
    print(distance, found[0])

    for body in tree:
        if body[0] == "YOU" or body[0] == "SAN":
            print("HERE")
            if not complete[0] and not found[0]:
                print("found[0] {}".format(body[0]))
                found[0] = True
            elif not complete[0]:
                complete[0] = True
                print() # plussa distance
                distance = get_to_santa(body[1], distance, found, complete)
            else:
                return distance
        elif len(body[1]) > 1:
            distance = get_to_santa(body, distance+1, found, complete)
    if not found[0]:
        distance = 0

    if complete[0]:
        return distance
    print("exiting")
    return distance +1

found = [False]
complete = [False]
distance = get_to_santa(final_tree, 0, found, complete)
print(distance)
