class Node:
    def __init__(self, parent: 'Node' | None = None,
                 child: 'Node' | None = None,
                 failed_state: bool = False,
                 table_state: list[list] = None,
                ):
        self.parent: Node = parent
        self.child: Node = child
        self.failed_state: bool = failed_state


        # use entropy to determin the tree how far from the state?

        #the entire table
        self.table_state: list[list] = table_state


        # override the equals to check to just look for the lists
    def __eq__(self, other):
        if self.table_state is None or other.table_state is None:
            # TODO: check
            return self.table_state == other.table_state

        # Sort each sublist and the parent list for comparison
        sorted_self = sorted([sorted(sublist) for sublist in self.table_state])
        sorted_other = sorted([sorted(sublist) for sublist in other.table_state])

        return sorted_self == sorted_other







