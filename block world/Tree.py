from Node import Node

class Tree:

    def __init__(self, root_node: Node, goal_node: Node):
        # make the root node and whatnot, root
        self.root_node: Node = root_node
        self.current_node: Node = root_node
        self.goal_node: Node = goal_node
        self.optimal_path = []
        # self.tree = []


        ## max depth on the trees should be the number of the elements in the list times 2 plus some number


    def solve(self):
        self.generate_tree(self.root_node)
        return self.determine_optimal_path()


    def generate_tree(self, root_node: Node):
        #TODO: needs work

        # first place the root node in the tree
        # then generate by running all action
        #

        # then run all rules
            #check if each stack top it can be placed on top of another stack
            # if not place on the table

        # see if any child has the failed state set to false, if so make that the active node
        # else: set it to the parent node until a child node has the state of false and the node does not equal
        # the solved state.
        # if the current node equals the root end the recursion
        pass

    def determine_optimal_path(self):

        # BFS

        # create some kind way to record the last path taken to a solved state. have a count that gets replaced
        # when it finds something with a smaller count

        # should go down from root and end when it exhaust all the nodes on the last child of the parent

        # first look at root, look for what children of its have solved = false
        # if it finds failed state = true then go down that path
        # if not backtrack to last node
        pass

    def print_tree(self):
        # print the tree
        pass