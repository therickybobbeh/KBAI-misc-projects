from Node import Node
from copy import deepcopy


class Actions:
    def __init__(self):
        pass

    # start actions block
    @staticmethod
    def pop_off_top_and_place_on_stack(node: Node, from_stack_index: int, to_stack_index: int) -> Node:
        # if not node.table_state[from_stack_index]:
        #     return None
        new_state = deepcopy(node.table_state)
        element = new_state[from_stack_index].pop()
        # Remove the empty stacks by taking index and filtering at end
        if len(new_state[from_stack_index]) == 0:
            new_state[from_stack_index] = []
            move_made = ("Table", f"{element}")
        else:
            move_made = (f"{element}", f"{new_state[to_stack_index][-1]}")
        # Keep the index but empty the stack
        new_state[to_stack_index].append(element)
        new_state = [stack for stack in new_state if stack]
        return Node(parent=node, table_state=new_state, last_move_made=move_made)

    @staticmethod
    def pop_off_top_and_place_on_table(node: Node, from_stack_index: int) -> Node:
        # if not node.table_state[from_stack_index]:
        #     return None
        new_state = deepcopy(node.table_state)
        element = new_state[from_stack_index].pop()
        # Remove the empty stacks by taking index and filtering at end
        if len(new_state[from_stack_index]) == 0:
            new_state[from_stack_index] = []
        new_state.append([element])
        new_state = [stack for stack in new_state if stack]
        move_made = (f"{element}","Table")
        return Node(parent=node, table_state=new_state, last_move_made=move_made)

    #end actions

    # start rules block

    @staticmethod
    def check_does_not_equal_prior_nodes(node: Node):
        current_node: Node | None = node.parent
        # check the parent until there is no parent
        while current_node is not None:
            if node == current_node:
                node.failed_state = True
                return False
            current_node = current_node.parent
        return True


    # end rules block

    @staticmethod
    def calculate_similarity_to_goal_state(node: Node, goal_state: Node) -> int:
        total_similarity = 0
        initial_state = node.table_state
        goal_state_list = goal_state.table_state
        # Loop through each sublist in the initial state
        for init_sublist in initial_state:
            max_similarity = 0
            # Compare the sublist to each sublist in the goal state
            for goal_sublist in goal_state_list:
                similarity = 0
                # Compare elements in position until a mismatch is found
                for i, el in enumerate(init_sublist):
                    if i >= len(goal_sublist) or el != goal_sublist[i]:
                        break  # Stop when we find the first mismatch
                    similarity += 1  # Add to similarity for matching elements
                max_similarity = max(max_similarity, similarity)
            # Add the maximum similarity for this sublist to the total
            total_similarity += max_similarity

        return total_similarity