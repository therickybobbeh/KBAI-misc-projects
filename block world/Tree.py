from Node import Node
from Actions import Actions
from copy import deepcopy
from collections import deque

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
        self.goal_node.similarity = count = sum(len(sublist) for sublist in self.goal_node.table_state)


    def solve(self):
        self.generate_tree(self.root_node)
        # self.print_tree(self.root_node)
        return self.determine_optimal_path(self.root_node)


    # this only generates the tree, and sets the failed states appropriately
    # false indicates the node should be explored no more and move back up a node
    def generate_tree(self, node: Node):
        if node == self.goal_node:
            node.solved = True
            return False

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

    def determine_optimal_path(self, node: Node):
        # The BFS algorithm used here is an adaptation of the example used on this page
        # https://codereview.stackexchange.com/questions/135156/bfs-implementation-in-python-3
        queue = deque([(node, 0)])
        best_solved_node = None
        best_depth = float('inf')
        # Perform BFS until the queue is empty
        while queue:
            # Dequeue the next node and its depth from the front of the queue
            current_node, current_depth = queue.popleft()
            # Check if this node is solved
            if current_node.solved:
                if best_solved_node is None or current_depth < best_depth:
                    best_solved_node = current_node
                    best_depth = current_depth
                elif current_depth == best_depth:
                    # If depths are equal use the currently saved one
                    pass
            for child in current_node.child_nodes:
                queue.append((child, current_depth + 1))
        return self.get_path_moves(best_solved_node)

    @staticmethod
    def get_path_moves(node: Node):
        # Reconstruct the path by traversing from the solved node back to the root
        path_to_root = []
        current_node = node
        while current_node is not None:
            if current_node.last_move_made is not None:
                path_to_root.append(current_node.last_move_made)
            current_node = current_node.parent
        return path_to_root[::-1]


    def print_tree(self, node: Node, depth=0):
        indent = '  ' * depth
        print(f"{indent}Node: {node.table_state} (Solved: {node.solved},"
              f" Failed: {node.failed_state}, Score: {node.similarity}),"
              f"Move made to get to state: {node.last_move_made}")
        for child in node.child_nodes:
            self.print_tree(child, depth + 1)