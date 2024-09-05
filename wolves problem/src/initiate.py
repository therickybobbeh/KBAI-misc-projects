# will run the actions after initiated
# will use numpy to create complex node that we can traverse
from multiprocessing.process import parent_process


# travers with 3d array
# [0][0,[x]][1,[y]]
# where x is the level into the decision tree, the first [0] is the depth it
# class Node:
# def  __init__(self, depth=0, towardsParent=[0], nextNode=[], depthInstance=0):
#     self.depth = depth #first number in array
#     self.depthInstance = depthInstance #second number in array
#     self.towardsParent = towardsParent #[depth, depthInstance]
#     self.nextNode = nextNode #[depth, depthInstance]
#
#     #actual objects
#     def createNode():
#         #make the boat
#         #make the 2 banks
#         #make the x number of sheep on each bank
#         # make the x number of wolves on each bank

import objects


class DecisionTree:

    def __init__(self, value, parent=None, pass_state=True, solved=False):
        self.depth: int = value
        self.leaves = []
        self.parent: int | None = parent
        #represents if the current node passed all rules after action was performed
        self.pass_state = pass_state
        self.solved = solved




        #crate instance of the classes
        self.bank_instance_left = objects.Bank()
        self.boat_instance_right = objects.Boat()
        self.sheep_instance = objects.Sheep()
        self.wolf_instance = objects.Wolf()




    #todo: this will not work yet. but lets use this in the actions -> rules flow after it passes all rules
    def add_leaf_node(self, leaf):
        leaf.parent = self
        self.leaf.append(leaf)
        leaf.depth = self.depth + 1

    def get_parent_node(self):
        return self.parent


    #TODO: comments
    def copy_node(self):
        # Create a new instance of DecisionTree
        new_node = DecisionTree(self.depth, self.parent, self.pass_state, self.solved)

        # Manually copy each attribute
        new_node.leaves = self.leaves[:]  # Shallow copy of the list
        new_node.bank_instance_left = self.bank_instance_left  # Assuming Bank is immutable or shallow copy is sufficient
        new_node.boat_instance_right = self.boat_instance_right  # Assuming Boat is immutable or shallow copy is sufficient
        new_node.sheep_instance = self.sheep_instance  # Assuming Sheep is immutable or shallow copy is sufficient
        new_node.wolf_instance = self.wolf_instance  # Assuming Wolf is immutable or shallow copy is sufficient

        return new_node





    # TODO: remove this later, debugging purposes
    ### begin citing code block
    def __repr__(self, level=0):
        string_return = "\t" * level + repr(self.leaves) + "\n"
        for leave in self.leaves:
            string_return += leave.__repr__(level + 1)
        return string_return


    def print_tree(self, level=0):
        print("  " * level + repr(self))
        for leave in self.leaves:
            self.print_tree(leave, level + 1)
    ### https://stackoverflow.com/questions/20242479/printing-a-tree-data-structure-in-python

    # will pass to action
    # each action will create a node, with an additional pasheepater for pass: true or false
    #







