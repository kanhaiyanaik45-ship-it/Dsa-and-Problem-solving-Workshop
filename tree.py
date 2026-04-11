# class Tree:
#     def __init__(self, data):
#         self.data = data #instance variable
#         self.children = []

#     def addChild(self, child):
#         self.children.append(child)

#     def  __str__(self, level =0):
#         ret = "   "* level + str (self.data) + "\n"
#         for child in self.children:
#             ret += child.__str__(level+1)
#         return ret

# rootNode = Tree("Drinks")
# hot  = Tree("hot")
# cold = Tree("cold")
# tea = Tree("tea")
# coffie = Tree("coffie")
# nonAlcoholic = Tree("NonAlcoholic")
# alcoholic = Tree("alcoholic")

# rootNode.addChild(hot)
# rootNode.addChild(cold)
# hot.addChild(tea)
# hot.addChild(coffie)
# cold.addChild(nonAlcoholic)
# cold.addChild(alcoholic)

# print(rootNode)



# class Tree:
#     def __init__(self, data):
#         self.data = data #instance variable
#         self.children = []

#     def addChild(self, child):
#         self.children.append(child)

#     def  __str__(self, level =0):
#         ret = "   "* level + str (self.data) + "\n"
#         for child in self.children:
#             ret += child.__str__(level+1)
#         return ret

# rootNode = Tree("N1")
# n2 = Tree("N2")
# n3 = Tree("N3")
# n4 = Tree("N4")
# n5 = Tree("N5")
# n6 = Tree("N6")
# n7 = Tree("N7")
# n8 = Tree("N8")
# n9 = Tree("N9")

# rootNode.addChild(n2)
# rootNode.addChild(n3)
# n2.addChild(n4)
# n2.addChild(n5)
# n3.addChild(n6)
# n3.addChild(n7)
# n4.addChild(n8)
# n4.addChild(n9)

# print(rootNode)
