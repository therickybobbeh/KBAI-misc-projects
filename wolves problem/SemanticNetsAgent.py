from src.decision_tree import *
from src.node import Node


class SemanticNetsAgent:
    def __init__(self):
        #If you want to do any initial processing, add it here.
        pass

    def solve(self, initial_sheep, initial_wolves):
        #Add your code here! Your solve method should receive
        #the initial number of sheep and wolves as integers,
        #and return a list of 2-tuples that represent the moves
        #required to get all sheep and wolves from the left
        #side of the river to the right.
        #
        #If it is impossible to move the animals over according
        #to the rules of the problem, return an empty list of
        #moves.



        #change this to initiate node

        #pass root node to decision tree


        #problem setup, add sheep and wolves to left bank, add a boat
        root_node = Node()
        for sheep in range(initial_sheep):
            root_node.bank_instance_left.set_sheep_count(initial_sheep)
        for wolf in range(initial_wolves):
            root_node.bank_instance_left.set_wolf_count(initial_wolves)
        root_node.bank_instance_left.add_boat()

        # make this return the tuple or whatever
        decision_tree =  DecisionTree(root_node)
        return decision_tree.run_actions_on_nodes()





        #TODO: proper return
        # return []

