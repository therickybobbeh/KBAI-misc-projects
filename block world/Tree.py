from Node import Node
from Actions import Actions
from copy import deepcopy

class Tree:

    def __init__(self, root_node: Node, goal_node: Node):
        # make the root node and whatnot, root
        self.root_node: Node = root_node

        self.goal_node: Node = goal_node
        self.optimal_path = []
        # self.tree = []

        self.root_node.similarity = Actions.calculate_similarity_to_goal_state(self.root_node, self.goal_node)
        ## max depth on the trees should be the number of the elements in the list times 2 plus some number
        self.current_node: Node = root_node
        # may not need
        self.goal_node.similarity = count = sum(len(sublist) for sublist in self.goal_node.table_state)


    def solve(self):
        self.generate_tree(self.root_node)
        self.print_tree(self.root_node)
        return self.determine_optimal_path()


    # this only generates the tree, and sets the failed states appropriately
    def generate_tree(self, node: Node):
        if node == self.goal_node:
            node.solved = True
            return True

        for selected_stack_index, stack in enumerate(node.table_state):
            for other_stack_index in range(len(node.table_state)):
                if selected_stack_index != other_stack_index:
                    child_node = Actions.pop_off_top_and_place_on_stack(node, selected_stack_index, other_stack_index)
                    # node.child_nodes.append(child_node)
                    if self.check_child_node_after_action(child_node, node, 1):
                        return True

            # Move top block to the table
            child_node = Actions.pop_off_top_and_place_on_table(node, selected_stack_index)
            if self.check_child_node_after_action(child_node, node, 2):
                return True

        node.failed_state = True
        return False

    def check_child_node_after_action(self, child_node: Node, parent_node: Node, case: int):
        if child_node and not child_node.failed_state:
            # Ensure the child is a deep copy, with its parent set properly
            child_node.parent = parent_node
            child_node.similarity = Actions.calculate_similarity_to_goal_state(child_node, self.goal_node)
            parent_node.child_nodes.append(child_node)
            # Check if the child is a better state and recursively generate the tree
            if Actions.check_does_not_equal_prior_nodes(child_node):
                # check for if its comparing on table move or stack on move, 1 for stack, 2 for table
                if case == 1:
                    if child_node.similarity > parent_node.similarity:
                        if self.generate_tree(child_node):
                            return True
                if case == 2:
                    if child_node.similarity >= parent_node.similarity:
                        if self.generate_tree(child_node):
                            return True
            return False
        else:
            parent_node.failed_state = True
            return False

    def determine_optimal_path(self):

        # BFS

        # create some kind way to record the last path taken to a solved state. have a count that gets replaced
        # when it finds something with a smaller count

        # should go down from root and end when it exhaust all the nodes on the last child of the parent

        # first look at root, look for what children of its have solved = false
        # if it finds failed state = true then go down that path
        # if not backtrack to last node
        pass

    def print_tree(self, node: Node, depth=0):
        indent = '  ' * depth
        print(f"{indent}Node: {node.table_state} (Solved: {node.solved}, Failed: {node.failed_state}, Score: {node.similarity})")
        for child in node.child_nodes:
            self.print_tree(child, depth + 1)