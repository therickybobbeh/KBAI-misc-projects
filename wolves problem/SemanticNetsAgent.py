from src.initiate import *

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


        #problem setup
        decision_tree = DecisionTree(value=0)
        bank_instance_left = decision_tree.bank_instance_left
        for sheep in range(initial_sheep):
            bank_instance_left.add_sheep(objects.Sheep)
        for wolf in range(initial_wolves):
            bank_instance_left.add_wolf(objects.Wolf)

        # run all states until all either solve/ fail or for a max depth




        #TODO: proper return
        return []

