from tree import Tree

orbits = open("input.txt","r").read().split()
com = Tree()

planet_list = []

for planets in orbits:
    #orbitee_name = planet[:3]
    orbiter_name = planets[4:]
    planet_list.append(Tree(orbiter_name))
    #print(orbitee, orbiter)

for planets in orbits:
    orbitee_name = planet[:3]
    orbiter_name = planets[4:]

    
