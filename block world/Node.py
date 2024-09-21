from typing import Union

class Node:
    def __init__(self, parent: Union['Node', None] = None,
                 child: Union[list['Node'], None]  | None = None,
                 failed_state: bool = False,
                 solved: bool = False,
                 table_state: Union[list[list[str]], None] = None,
                 similarity: int = 0
                ):
        self.parent: Node = parent
        self.child_nodes: list[Node] = child if child is not None else []
        self.failed_state: bool = failed_state
        self.solved: bool = solved
        self.similarity: int = similarity



        # use entropy to determin the tree how far from the state?

        #the entire table
        self.table_state: list[list[str]] = table_state if table_state is not None else []
        # self.table_state = table_state if table_state is not None else []




        # override the equals to check to just look for the lists
    def __eq__(self, other):
        if self.table_state is None or other.table_state is None:
            return self.table_state == other.table_state

        # Sort each sublist and the parent list for comparison
        # Uses O(n log n)
        # begin credit blok, used this for inspiration
        sorted_self = sorted([sorted(sublist) for sublist in self.table_state])
        sorted_other = sorted([sorted(sublist) for sublist in other.table_state])
        # https://stackoverflow.com/questions/7828867/how-to-efficiently-compare-two-unordered-lists-not-sets
        # end credit block
        return sorted_self == sorted_other







