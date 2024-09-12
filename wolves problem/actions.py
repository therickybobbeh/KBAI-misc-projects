import copy

from node import Node
from rules import RunAllRules

#
# class Actions:
#     def __init__(self, node: Node):
#         self.node = node
#         self.rules_checker = RunAllRules(node)
#
#     # START: actions that can preformed on nodes
#     def move_wolf_from_bank1_to_boat(self):
#         self.node.bank_instance_left.remove_wolf()
#         self.node.boat_instance.add_wolf()
#
#     def move_wolf_from_bank2_to_boat(self):
#         self.node.bank_instance_right.remove_wolf()
#         self.node.boat_instance.add_wolf()
#
#     def move_wolf_from_boat_to_bank1(self):
#         self.node.boat_instance.remove_wolf()
#         self.node.bank_instance_left.add_wolf()
#
#     def move_wolf_from_boat_to_bank2(self):
#         self.node.boat_instance.remove_wolf()
#         self.node.bank_instance_right.add_wolf()
#
#     def move_sheep_from_bank1_to_boat(self):
#         self.node.bank_instance_left.remove_sheep()
#         self.node.boat_instance.add_sheep()
#
#     def move_sheep_from_bank2_to_boat(self):
#         self.node.bank_instance_right.remove_sheep()
#         self.node.boat_instance.add_sheep()
#
#     def move_sheep_from_boat_to_bank1(self):
#         self.node.boat_instance.remove_sheep()
#         self.node.bank_instance_left.add_sheep()
#
#     def move_sheep_from_boat_to_bank2(self):
#         self.node.boat_instance.remove_sheep()
#         self.node.bank_instance_right.add_sheep()
#
#     def move_boat_from_bank1_to_bank2(self):
#         boat = self.node.boat_instance
#         self.node.bank_instance_left.remove_boat()
#         self.node.bank_instance_right.add_boat(boat)
#
#     def move_boat_from_bank2_to_bank1(self):
#         boat = self.node.boat_instance
#         self.node.bank_instance_right.remove_boat()
#         self.node.bank_instance_left.add_boat(boat)
#
#     def empty_boat(self, bank: int):
#         # Check if there are wolves in the boat
#         # 1 for left 2 for right in banks
#         if self.node.boat_instance.get_wolf_count() > 0:
#             if bank == 1:
#                 self.move_wolf_from_boat_to_bank1()
#             elif bank == 2:
#                 self.move_wolf_from_boat_to_bank2()
#
#         # Check if there are sheep in the boat
#         if self.node.boat_instance.get_sheep_count() > 0:
#             if bank == 1:
#                 self.move_sheep_from_boat_to_bank1()
#             elif bank == 2:
#                 self.move_sheep_from_boat_to_bank2()
#
#     # END actions setup
#
#     def move_1_wolf_from_left_to_right(self):
#         original_state = copy.deepcopy(self.node)
#         try:
#             if self.node.bank_instance_left.get_wolf_count() > 0:
#                 self.empty_boat(1)
#                 self.move_wolf_from_bank1_to_boat()
#                 self.move_boat_from_bank1_to_bank2()
#                 if self.rules_checker.run():
#                     raise Exception("Rule violation after moving 1 wolf to boat")
#                 self.node.back_and_fourth.append((0, 1))
#                 return True
#         except Exception as e:
#             self.node = original_state
#             print(f"Reverted due to: {e}")
#             return False
#         finally:
#             del original_state
#
#     def move_1_wolf_from_right_to_left(self) -> bool:
#         original_state = copy.deepcopy(self.node)
#         try:
#             if self.node.bank_instance_right.get_wolf_count() > 0:
#                 self.empty_boat(2)
#                 self.move_wolf_from_bank2_to_boat()
#                 self.move_boat_from_bank2_to_bank1()
#                 if self.rules_checker.run():
#                     raise Exception("Rule violation after moving 1 wolf to boat")
#                 self.node.back_and_fourth.append((0, 1))
#                 return True
#         except Exception as e:
#             self.node = original_state
#             print(f"Reverted due to: {e}")
#             return False
#         finally:
#             del original_state
#
#     def move_1_sheep_from_left_to_right(self) -> bool:
#         original_state = copy.deepcopy(self.node)
#         try:
#             if self.node.bank_instance_left.get_sheep_count() > 0:
#                 self.empty_boat(1)
#                 self.move_sheep_from_bank1_to_boat()
#                 self.move_boat_from_bank1_to_bank2()
#                 if self.rules_checker.run():
#                     raise Exception("Rule violation after moving 1 sheep to boat")
#                 self.node.back_and_fourth.append((1, 0))
#                 return True
#         except Exception as e:
#             self.node = original_state
#             print(f"Reverted due to: {e}")
#             return False
#         finally:
#             del original_state
#
#     def move_1_sheep_from_right_to_left(self) -> bool:
#         original_state = copy.deepcopy(self.node)
#         try:
#             if self.node.bank_instance_right.get_sheep_count() > 0:
#                 self.empty_boat(2)
#                 self.move_sheep_from_bank2_to_boat()
#                 self.move_boat_from_bank2_to_bank1()
#                 if self.rules_checker.run():
#                     raise Exception("Rule violation after moving 1 sheep to boat")
#                 self.node.back_and_fourth.append((1, 0))
#                 return True
#         except Exception as e:
#             self.node = original_state
#             print(f"Reverted due to: {e}")
#             return False
#         finally:
#             del original_state
#
#     def move_2_wolves_from_left_to_right(self) -> bool:
#         original_state = copy.deepcopy(self.node)
#         try:
#             if self.node.bank_instance_left.get_wolf_count() > 0:
#                 self.empty_boat(1)
#                 self.move_wolf_from_bank1_to_boat()
#                 self.move_wolf_from_bank1_to_boat()
#                 self.move_boat_from_bank1_to_bank2()
#                 if self.rules_checker.run():
#                     raise Exception("Rule violation after moving 2 wolf to boat")
#                 self.node.back_and_fourth.append((0, 2))
#                 return True
#         except Exception as e:
#             self.node = original_state
#             print(f"Reverted due to: {e}")
#             return False
#         finally:
#             del original_state
#
#     def move_2_wolves_from_right_to_left(self) -> bool:
#         original_state = copy.deepcopy(self.node)
#         try:
#             if self.node.bank_instance_right.get_wolf_count() > 0:
#                 self.empty_boat(2)
#                 self.move_wolf_from_bank2_to_boat()
#                 self.move_wolf_from_bank2_to_boat()
#                 self.move_boat_from_bank2_to_bank1()
#                 if self.rules_checker.run():
#                     raise Exception("Rule violation after moving 2 wolf to boat")
#                 self.node.back_and_fourth.append((0, 2))
#                 return True
#         except Exception as e:
#             self.node = original_state
#             print(f"Reverted due to: {e}")
#             return False
#         finally:
#             del original_state
#
#     def move_2_sheep_from_left_to_right(self) -> bool:
#         original_state = copy.deepcopy(self.node)
#         try:
#             if self.node.bank_instance_left.get_sheep_count() > 0:
#                 self.empty_boat(1)
#                 self.move_sheep_from_bank1_to_boat()
#                 self.move_sheep_from_bank1_to_boat()
#
#                 # if self.node.bank_instance_left.get_boat_presence() == 2:
#                 #     self.move_boat_from_bank1_to_bank2()
#                 self.move_boat_from_bank1_to_bank2()
#                 if self.rules_checker.run():
#                     raise Exception("Rule violation after moving 2 sheep to boat")
#                 self.node.back_and_fourth.append((2, 0))
#                 return True
#         except Exception as e:
#             self.node = original_state
#             print(f"Reverted due to: {e}")
#             return False
#         finally:
#             del original_state
#
#     def move_2_sheep_from_right_to_left(self) -> bool:
#         original_state = copy.deepcopy(self.node)
#         try:
#             if self.node.bank_instance_right.get_sheep_count() > 0:
#                 self.empty_boat(2)
#                 self.move_sheep_from_bank2_to_boat()
#                 self.move_sheep_from_bank2_to_boat()
#
#                 self.move_boat_from_bank2_to_bank1()
#                 if self.rules_checker.run():
#                     raise Exception("Rule violation after moving sheep 2 to boat")
#                 self.node.back_and_fourth.append((2, 0))
#                 return True
#         except Exception as e:
#             self.node = original_state
#             print(f"Reverted due to: {e}")
#             return False
#         finally:
#             del original_state
#
#     def move_1_wolf_and_1_sheep_from_left_to_right(self) -> bool:
#         original_state = copy.deepcopy(self.node)
#         try:
#             if self.node.bank_instance_left.get_sheep_count() > 0:
#                 self.empty_boat(1)
#                 self.move_sheep_from_bank1_to_boat()
#                 self.move_wolf_from_bank1_to_boat()
#                 self.move_boat_from_bank1_to_bank2()
#                 if self.rules_checker.run():
#                     raise Exception("Rule violation after moving sheep and wolf to boat")
#                 self.node.back_and_fourth.append((1, 1))
#                 return True
#         except Exception as e:
#             self.node = original_state
#             print(f"Reverted due to: {e}")
#             return False
#         finally:
#             del original_state
#
#     def move_1_wolf_and_1_sheep_from_right_to_left(self) -> bool:
#         original_state = copy.deepcopy(self.node)
#         try:
#             if self.node.bank_instance_right.get_sheep_count() > 0:
#                 self.empty_boat(2)
#                 self.move_sheep_from_bank2_to_boat()
#                 self.move_wolf_from_bank2_to_boat()
#                 self.move_boat_from_bank2_to_bank1()
#                 if self.rules_checker.run():
#                     raise Exception("Rule violation after moving sheep and wolf to boat")
#                 self.node.back_and_fourth.append((1, 1))
#                 return True
#         except Exception as e:
#             self.node = original_state
#             print(f"Reverted due to: {e}")
#             return False
#         finally:
#             del original_state
#
#     def back_to_parent_node(self):
#         self.node.exhausted = True
#         if self.node.get_parent_node() and self.node.depth != 0:
#             self.node.get_parent_node().actions_ran += 1
#             return self.node.get_parent_node()
#         else:
#             return self.node
#
#     def is_repetitive_pattern(self) -> bool:
#         ## get the current node actions_ran and all of the parents actions ran until it reaches a depth of 0
#         current_node = deepcopy(self.node)
#         actions_ran = []
#         # while current_node.depth >= 0:
#         while current_node.depth > 0:
#             actions_ran.append(current_node.actions_ran)
#             current_node = current_node.get_parent_node()
#
#         ## this may be complex
#
#         # when it finds a pattern, identify the length of the pattern and go back that many parent nodes
#         # in a loop, then set the active node back to that one
#
#         # check if the same move was made on the other side
#         current_pattern = actions_ran[-3:]
#         if current_pattern[0] == current_pattern[2]:
#             # compare the objects
#             two_moves_ago = self.node.get_parent_node().get_parent_node()
#             # compare how many on each side, boat has already moved so compare opposit bank
#             if (
#                     (
#                             self.node.bank_instance_left.get_wolf_count() + self.node.bank_instance_left.get_boat_wolf_count()) ==
#                     (
#                             two_moves_ago.bank_instance_left.get_wolf_count() + two_moves_ago.bank_instance_left.get_boat_wolf_count()) and
#                     (
#                             self.node.bank_instance_left.get_sheep_count() + self.node.bank_instance_left.get_boat_sheep_count()) ==
#                     (
#                             two_moves_ago.bank_instance_left.get_sheep_count() + two_moves_ago.bank_instance_left.get_boat_sheep_count()) and
#                     (
#                             self.node.bank_instance_right.get_sheep_count() + self.node.bank_instance_right.get_boat_sheep_count()) ==
#                     (
#                             two_moves_ago.bank_instance_right.get_sheep_count() + two_moves_ago.bank_instance_right.get_boat_sheep_count()) and
#                     (
#                             self.node.bank_instance_right.get_wolf_count() + self.node.bank_instance_right.get_boat_wolf_count()) ==
#                     (
#                             two_moves_ago.bank_instance_right.get_wolf_count() + two_moves_ago.bank_instance_right.get_boat_wolf_count())
#             ):
#                 self.node = two_moves_ago
#                 # self.node.actions_ran = + 1
#                 print("pattern found, going back 3 nodes")
#                 return True
#             return False
#
#     def run_actions(self) -> Node:
#         # check for patterns
#         if self.node.depth > 2:
#             if self.is_repetitive_pattern():
#                 # change the node in the above method to the last in the sequesnce
#                 return self.node
#
#         # You can re-order these to set preference/weight on more frequently ran actions
#         # can optimize by looking at what side boat is on
#         actions_case = {
#             0: self.move_1_sheep_from_left_to_right,
#             1: self.move_1_sheep_from_right_to_left,
#             2: self.move_1_wolf_from_left_to_right,
#             3: self.move_1_wolf_from_right_to_left,
#             4: self.move_2_sheep_from_left_to_right,
#             5: self.move_2_sheep_from_right_to_left,
#             6: self.move_2_wolves_from_left_to_right,
#             7: self.move_2_wolves_from_right_to_left,
#             8: self.move_1_wolf_and_1_sheep_from_left_to_right,
#             9: self.move_1_wolf_and_1_sheep_from_right_to_left,
#         }
#
#         # If all actions are exhausted, go back to parent node
#
#         # Iterate over all actions
#         while self.node.actions_ran < len(actions_case):
#             action = actions_case.get(self.node.actions_ran)
#
#             # Debugging: Print current action
#             # print(f"Actions ran: {self.node.actions_ran}")
#
#             if action:
#                 if action():
#                     self.node.actions_ran += 1
#                     if self.node.depth > 2:
#                         if self.is_repetitive_pattern():
#                             # change the node in the above method to the last in the sequesnce
#                             return self.node
#                     return self.node
#                 else:
#                     self.node.actions_ran += 1
#             else:
#                 self.node.actions_ran += 1
#
#         if self.node.actions_ran == len(actions_case):
#             return self.back_to_parent_node()




class Actions:
    def __init__(self, node):
        self.node = node
        self.rules_checker = RunAllRules(node)

    # START: actions that can be performed on nodes
    def move_wolf_from_bank1_to_boat(self):
        self.node.bank_instance_left.remove_wolf()
        self.node.boat_instance.add_wolf()

    def move_wolf_from_bank2_to_boat(self):
        self.node.bank_instance_right.remove_wolf()
        self.node.boat_instance.add_wolf()

    def move_wolf_from_boat_to_bank1(self):
        self.node.boat_instance.remove_wolf()
        self.node.bank_instance_left.add_wolf()

    def move_wolf_from_boat_to_bank2(self):
        self.node.boat_instance.remove_wolf()
        self.node.bank_instance_right.add_wolf()

    def move_sheep_from_bank1_to_boat(self):
        self.node.bank_instance_left.remove_sheep()
        self.node.boat_instance.add_sheep()

    def move_sheep_from_bank2_to_boat(self):
        self.node.bank_instance_right.remove_sheep()
        self.node.boat_instance.add_sheep()

    def move_sheep_from_boat_to_bank1(self):
        self.node.boat_instance.remove_sheep()
        self.node.bank_instance_left.add_sheep()

    def move_sheep_from_boat_to_bank2(self):
        self.node.boat_instance.remove_sheep()
        self.node.bank_instance_right.add_sheep()

    def move_boat_from_bank1_to_bank2(self):
        boat = self.node.boat_instance
        self.node.bank_instance_left.remove_boat()
        self.node.bank_instance_right.add_boat(boat)

    def move_boat_from_bank2_to_bank1(self):
        boat = self.node.boat_instance
        self.node.bank_instance_right.remove_boat()
        self.node.bank_instance_left.add_boat(boat)

    def empty_boat(self, bank: int):
        # Empty the boat according to which bank it’s at
        if self.node.boat_instance.get_wolf_count() > 0:
            if bank == 1:
                self.move_wolf_from_boat_to_bank1()
            elif bank == 2:
                self.move_wolf_from_boat_to_bank2()

        if self.node.boat_instance.get_sheep_count() > 0:
            if bank == 1:
                self.move_sheep_from_boat_to_bank1()
            elif bank == 2:
                self.move_sheep_from_boat_to_bank2()

    # END actions setup


    def move_1_wolf_from_left_to_right(self):
            original_state = copy.deepcopy(self.node)
            try:
                if self.node.bank_instance_left.get_wolf_count() > 0:
                    self.empty_boat(1)
                    self.move_wolf_from_bank1_to_boat()
                    self.move_boat_from_bank1_to_bank2()
                    self.move_wolf_from_boat_to_bank2()
                    if self.rules_checker.run():
                        raise Exception("Rule violation after moving 1 wolf to boat")
                    self.node.back_and_fourth.append((0, 1))
                    return True
            except Exception as e:
                self.node = original_state
                print(f"Reverted due to: {e}")
                return False
            finally:
                del original_state

    def move_1_wolf_from_right_to_left(self) -> bool:
        original_state = copy.deepcopy(self.node)
        try:
            if self.node.bank_instance_right.get_wolf_count() > 0:
                self.empty_boat(2)
                self.move_wolf_from_bank2_to_boat()
                self.move_boat_from_bank2_to_bank1()
                self.move_wolf_from_boat_to_bank1()
                if self.rules_checker.run():
                    raise Exception("Rule violation after moving 1 wolf to boat")
                self.node.back_and_fourth.append((0, 1))
                return True
        except Exception as e:
            self.node = original_state
            print(f"Reverted due to: {e}")
            return False
        finally:
            del original_state

    def move_1_sheep_from_left_to_right(self) -> bool:
        original_state = copy.deepcopy(self.node)
        try:
            if self.node.bank_instance_left.get_sheep_count() > 0:
                self.empty_boat(1)
                self.move_sheep_from_bank1_to_boat()
                self.move_boat_from_bank1_to_bank2()
                self.move_sheep_from_boat_to_bank2()
                if self.rules_checker.run():
                    raise Exception("Rule violation after moving 1 sheep to boat")
                self.node.back_and_fourth.append((1, 0))
                return True
        except Exception as e:
            self.node = original_state
            print(f"Reverted due to: {e}")
            return False
        finally:
            del original_state

    def move_1_sheep_from_right_to_left(self) -> bool:
        original_state = copy.deepcopy(self.node)
        try:
            if self.node.bank_instance_right.get_sheep_count() > 0:
                self.empty_boat(2)
                self.move_sheep_from_bank2_to_boat()
                self.move_boat_from_bank2_to_bank1()
                self.move_wolf_from_boat_to_bank1()
                if self.rules_checker.run():
                    raise Exception("Rule violation after moving 1 sheep to boat")
                self.node.back_and_fourth.append((1, 0))
                return True
        except Exception as e:
            self.node = original_state
            print(f"Reverted due to: {e}")
            return False
        finally:
            del original_state

    def move_2_wolves_from_left_to_right(self) -> bool:
        original_state = copy.deepcopy(self.node)
        try:
            if self.node.bank_instance_left.get_wolf_count() > 0:
                self.empty_boat(1)
                self.move_wolf_from_bank1_to_boat()
                self.move_wolf_from_bank1_to_boat()
                self.move_boat_from_bank1_to_bank2()
                self.move_wolf_from_boat_to_bank2()
                self.move_wolf_from_boat_to_bank2()
                if self.rules_checker.run():
                    raise Exception("Rule violation after moving 2 wolf to boat")
                self.node.back_and_fourth.append((0, 2))
                return True
        except Exception as e:
            self.node = original_state
            print(f"Reverted due to: {e}")
            return False
        finally:
            del original_state

    def move_2_wolves_from_right_to_left(self) -> bool:
        original_state = copy.deepcopy(self.node)
        try:
            if self.node.bank_instance_right.get_wolf_count() > 0:
                self.empty_boat(2)
                self.move_wolf_from_bank2_to_boat()
                self.move_wolf_from_bank2_to_boat()
                self.move_boat_from_bank2_to_bank1()
                self.move_wolf_from_boat_to_bank1()
                self.move_wolf_from_boat_to_bank1()
                if self.rules_checker.run():
                    raise Exception("Rule violation after moving 2 wolf to boat")
                self.node.back_and_fourth.append((0, 2))
                return True
        except Exception as e:
            self.node = original_state
            print(f"Reverted due to: {e}")
            return False
        finally:
            del original_state

    def move_2_sheep_from_left_to_right(self) -> bool:
        original_state = copy.deepcopy(self.node)
        try:
            if self.node.bank_instance_left.get_sheep_count() > 0:
                self.empty_boat(1)
                self.move_sheep_from_bank1_to_boat()
                self.move_sheep_from_bank1_to_boat()

                # if self.node.bank_instance_left.get_boat_presence() == 2:
                #     self.move_boat_from_bank1_to_bank2()
                self.move_boat_from_bank1_to_bank2()
                self.move_sheep_from_boat_to_bank2()
                self.move_sheep_from_boat_to_bank2()
                if self.rules_checker.run():
                    raise Exception("Rule violation after moving 2 sheep to boat")
                self.node.back_and_fourth.append((2, 0))
                return True
        except Exception as e:
            self.node = original_state
            print(f"Reverted due to: {e}")
            return False
        finally:
            del original_state

    def move_2_sheep_from_right_to_left(self) -> bool:
        original_state = copy.deepcopy(self.node)
        try:
            if self.node.bank_instance_right.get_sheep_count() > 0:
                self.empty_boat(2)
                self.move_sheep_from_bank2_to_boat()
                self.move_sheep_from_bank2_to_boat()
                self.move_boat_from_bank2_to_bank1()
                self.move_sheep_from_boat_to_bank1()
                self.move_sheep_from_boat_to_bank1()
                if self.rules_checker.run():
                    raise Exception("Rule violation after moving sheep 2 to boat")
                self.node.back_and_fourth.append((2, 0))
                return True
        except Exception as e:
            self.node = original_state
            print(f"Reverted due to: {e}")
            return False
        finally:
            del original_state

    def move_1_wolf_and_1_sheep_from_left_to_right(self) -> bool:
        original_state = copy.deepcopy(self.node)
        try:
            if self.node.bank_instance_left.get_sheep_count() > 0:
                self.empty_boat(1)
                self.move_sheep_from_bank1_to_boat()
                self.move_wolf_from_bank1_to_boat()
                self.move_boat_from_bank1_to_bank2()
                self.move_sheep_from_boat_to_bank2()
                self.move_wolf_from_boat_to_bank2()
                if self.rules_checker.run():
                    raise Exception("Rule violation after moving sheep and wolf to boat")
                self.node.back_and_fourth.append((1, 1))
                return True
        except Exception as e:
            self.node = original_state
            print(f"Reverted due to: {e}")
            return False
        finally:
            del original_state

    def move_1_wolf_and_1_sheep_from_right_to_left(self) -> bool:
        original_state = copy.deepcopy(self.node)
        try:
            if self.node.bank_instance_right.get_sheep_count() > 0:
                self.empty_boat(2)
                self.move_sheep_from_bank2_to_boat()
                self.move_wolf_from_bank2_to_boat()
                self.move_boat_from_bank2_to_bank1()
                self.move_wolf_from_boat_to_bank1()
                self.move_sheep_from_boat_to_bank1()
                if self.rules_checker.run():
                    raise Exception("Rule violation after moving sheep and wolf to boat")
                self.node.back_and_fourth.append((1, 1))
                return True
        except Exception as e:
            self.node = original_state
            print(f"Reverted due to: {e}")
            return False
        finally:
            del original_state

    def back_to_parent_node(self):
        self.node.exhausted = True
        if self.node.get_parent_node() and self.node.depth != 0:
            self.node.get_parent_node().actions_ran += 1
            return self.node.get_parent_node()
        else:
            return self.node

    def back_to_parent_node(self):
        self.node.exhausted = True
        parent = self.node.get_parent_node()
        if parent and self.node.depth != 0:
            parent.actions_ran += 1
            return parent
        return self.node

    def is_repetitive_pattern(self) -> bool:
        current_node = copy.deepcopy(self.node)
        actions_ran = []
        while current_node.depth > 0:
            actions_ran.append(current_node.actions_ran)
            current_node = current_node.get_parent_node()

        # Look for a repetitive pattern in the last 3 moves
        current_pattern = actions_ran[-3:]
        if len(current_pattern) < 3:
            return False

        # Check if the pattern repeats by comparing node states two moves ago
        two_moves_ago = self.node.get_parent_node().get_parent_node()
        if (
                (
                        self.node.bank_instance_left.get_wolf_count() + self.node.bank_instance_left.get_boat_wolf_count()) ==
                (
                        two_moves_ago.bank_instance_left.get_wolf_count() + two_moves_ago.bank_instance_left.get_boat_wolf_count()) and
                (
                        self.node.bank_instance_left.get_sheep_count() + self.node.bank_instance_left.get_boat_sheep_count()) ==
                (
                        two_moves_ago.bank_instance_left.get_sheep_count() + two_moves_ago.bank_instance_left.get_boat_sheep_count()) and
                (
                        self.node.bank_instance_right.get_sheep_count() + self.node.bank_instance_right.get_boat_sheep_count()) ==
                (
                        two_moves_ago.bank_instance_right.get_sheep_count() + two_moves_ago.bank_instance_right.get_boat_sheep_count()) and
                (
                        self.node.bank_instance_right.get_wolf_count() + self.node.bank_instance_right.get_boat_wolf_count()) ==
                (
                        two_moves_ago.bank_instance_right.get_wolf_count() + two_moves_ago.bank_instance_right.get_boat_wolf_count())
        ):
            self.node = self.node.get_parent_node()
            self.node.actions_ran += 1
            print("Pattern found, reverting back 1 moves.")
            return True
        return False


    def run_actions(self) -> Node:
        # Check for repetitive patterns
        if self.node.depth > 2:
            if self.is_repetitive_pattern():
                return self.node

        actions_case = {
            0: self.move_1_sheep_from_left_to_right,
            1: self.move_1_sheep_from_right_to_left,
            2: self.move_1_wolf_from_left_to_right,
            3: self.move_1_wolf_from_right_to_left,
            4: self.move_2_sheep_from_left_to_right,
            5: self.move_2_sheep_from_right_to_left,
            6: self.move_2_wolves_from_left_to_right,
            7: self.move_2_wolves_from_right_to_left,
            8: self.move_1_wolf_and_1_sheep_from_left_to_right,
            9: self.move_1_wolf_and_1_sheep_from_right_to_left,
        }

        # Iterate through actions until all are exhausted
        while self.node.actions_ran < len(actions_case):
            action = actions_case.get(self.node.actions_ran)

            if action and action():  # Execute the action
                self.node.actions_ran += 1
                # Re-check for repetitive patterns after each move
                if self.node.depth > 2 and self.is_repetitive_pattern():
                    return self.node
                return self.node
            else:
                self.node.actions_ran += 1  # Move to the next action

        # If all actions are exhausted, go back to the parent node
        if self.node.actions_ran == len(actions_case):
            return self.back_to_parent_node()
