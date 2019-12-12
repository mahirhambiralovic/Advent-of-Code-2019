class Tree:
    def __init__(self,name):
        self.children = []
        self.name = name

    def add_child(self,tree):
        self.children.append(tree)

    def remove_child(self,tree):
        self.children.remove(tree)

    def contains(self, query_tree):
        if len(self.children) == 0:
            return False
        for peeking_tree in self.children:
            #print(peeking_tree.name)
            if peeking_tree.name == query_tree.name:
                return True
            else:
                return Tree.contains(peeking_tree, query_tree)

    def __str__(self, level=0):
        ret = "\t"*level+self.name+"\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret
#
# a = Tree("A")
# b = Tree("B")
# c = Tree("C")
# d = Tree("D")
#
# a.add_child(b)
# a.add_child(c)
# c.add_child(d)
# a.print()
