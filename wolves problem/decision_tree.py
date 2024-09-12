from node import Node
from actions import Actions


class DecisionTree:
    def __init__(self, node: Node):
        self.node: Node = node
        self.maxDepth: int = 500

    def run_actions_on_nodes(self):
        # if len(self.node.leaves):
        #     self.node.actions_ran = len(self.node.leaves)
        if self.node.solved:
            # Return the solution path as a list of tuples
            return self.node.actions_ran
        elif self.node.depth > self.maxDepth:
            print("max depth reached")
            return []
        elif self.node.exhausted and self.node.depth == 0:
            print("impossible scenario")
        # elif self.node.actions_ran > 10:
        #     print("too many actions, impossible scenario")
        #     return []

        # set actions ran based on leve count
        # self.node.actions_ran = len(self.node.leaves)



        # debugging
        self.node.print_with_indent()

        # Run the actions and get the resulting node
        self.node = self.node.add_leaf()
        # run the actions and get the next node back
        # set the class node to the returned one
        self.node = Actions(self.node).run_actions()

        print('pause')

        # self.check_if_solved()


        # Recursively call the method on the new active node
        return self.run_actions_on_nodes()


    # def check_if_solved(self) -> None:
    #     if (self.node.bank_instance_left.get_wolf_count() == 0 and
    #             self.node.bank_instance_left.get_sheep_count() == 0 and
    #             self.node.bank_instance_left.get_boat_presence() == False
    #             # and self.node.boat_instance.get_wolf_count() == 0 and
    #             # self.node.boat_instance.get_sheep_count() == 0
    #     ):
    #         self.node.solved = True