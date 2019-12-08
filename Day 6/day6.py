from tree import Tree

def consolidate(tree_list):
    for tree1 in tree_list:
        for tree2 in tree_list:
            if tree1 == tree2:
                continue
            else:
                if tree1.add_orbiter(tree2,tree2):
                    tree_list.remove(tree2)
                    print("REMOVING")
                    print(len(tree_list))
                    return

orbits = open("input.txt","r").read().split()
temp_trees = [Tree("COM")]

for planets in orbits:
    orbitee_name = planets[:3]
    orbiter_name = planets[4:]
    added = False
    # Check if we should att it as child to an existing tree
    for tree in temp_trees:
        if tree.contains(Tree(orbitee_name)):
            added = tree.add_orbiter(Tree(orbitee_name), Tree(orbiter_name))
            break
    if not added:
        child = Tree(orbiter_name)
        t_tree = Tree(orbitee_name)
        t_tree.add_child(child)
        temp_trees.append(t_tree)

for tree in temp_trees:
    print(str(tree))
print(len(temp_trees))
print(len(orbits))

while len(temp_trees) > 1:
    consolidate(temp_trees)
print(str(temp_trees[0]))

# MP5
# 	B5J
# 		81G
# 			RDT
# 				8GY
