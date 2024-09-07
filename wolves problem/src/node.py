import copy
from src import objects as objects


class Node:
    def __init__(self, depth, leaves=None, parent: 'Node' = None,
                 actions_ran=0, solved=False, exhausted=False, bank_left=objects.Bank,
                 bank_right=objects.Bank, boat=objects.Boat, back_and_fourth = []):
        if leaves is None:
            leaves = []
        self.depth: int = depth
        self.leaves: list = leaves
        self.parent: Node = parent
        self.actions_ran: int = actions_ran
        self.solved: bool = solved
        self.exhausted: bool = exhausted
        # (x,y) where x is sheep and y is wolf
        self.back_and_fourth = back_and_fourth

        self.bank_instance_left = bank_left
        self.bank_instance_right = bank_right
        self.boat_instance = boat

    def add_leaf(self) -> 'Node':
        leaf = copy.deepcopy(self)
        leaf.parent = self
        self.leaves.append(leaf)
        leaf.depth = self.depth + 1
        return leaf

    def get_parent_node(self):
        return self.parent

    def get_depth(self):
        return self.depth

    def get_pass_state(self):
        return self.actions_ran

    def get_solved(self):
        return self.solved


    def __repr__(self):
        return (f"Node(depth={self.depth}, actions_ran={self.actions_ran}, "
                f"solved={self.solved}, exhausted={self.exhausted}, "
                f"bank_left={self.bank_instance_left}, "
                f"bank_right={self.bank_instance_right}, "
                f"boat={self.boat_instance})")

    def print_with_indent(self):
        indent = '---' * self.depth
        print(f"{indent}Node at depth {self.depth}: {self}")