from src.node import Node
from src.actions import Actions


class DecisionTree:
    def __init__(self, node: Node):
        self.node: Node = node
        self.active_node: Node = node
        self.maxDepth: int = 500

    def run_actions_on_nodes(self):
        if self.node.solved:
            # Return the solution path as a list of tuples
            return self.get_solution_path()
        elif self.node.depth > self.maxDepth:
            print("max depth reached")
            return []
        elif self.node.exhausted and self.node.depth == 0:
            return []

        # debugging
        self.node.print_with_indent()

        # Run the actions and get the resulting node
        self.node = self.node.add_leaf()
        # run the actions and get the next node back
        next_node = Actions(self.node).run_next_action()
        # set the class node to the returned one
        self.node = next_node
        # Recursively call the method on the new active node
        return self.run_actions_on_nodes()

    def get_solution_path(self):
        # This method should return the path to the solution as a list of tuples
        path = []
        current_node = self.node
        while current_node:
            # Assuming each node has a method to get the action that led to it
            action = current_node.get_action()
            if action:
                path.append(action)
            current_node = current_node.get_parent_node()
        return path[::-1]
