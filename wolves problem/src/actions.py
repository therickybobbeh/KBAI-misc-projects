import copy

from src.node import Node
from src.rules import RunAllRules


class Actions:
    def __init__(self, node: Node):
        self.node = node
        self.rules_checker = RunAllRules(node)

    # START: actions that can preformed on nodes
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
        self.node.bank_instance_left.remove_boat()
        self.node.bank_instance_right.add_boat()

    def move_boat_from_bank2_to_bank1(self):
        self.node.bank_instance_right.remove_boat()
        self.node.bank_instance_left.add_boat()

    # END actions setup

    #TODO: add checks for all of these to make see what is on the boat
    # check before when we load the boat up for the action.
    def move_1_wolf_from_left_to_right(self):
        original_state = copy.deepcopy(self.node)
        try:
            if (self.node.bank_instance_left.wolf_count > 0 and
                    self.node.boat_instance.get_animal_count() < 2):
                self.move_sheep_from_boat_to_bank1()
                if not self.rules_checker.run():
                    raise Exception("Rule violation after moving sheep to bank1")
            self.move_wolf_from_bank1_to_boat()
            if not self.rules_checker.run():
                raise Exception("Rule violation after moving wolf to boat")
            self.move_boat_from_bank1_to_bank2()
            if not self.rules_checker.run():
                raise Exception("Rule violation after moving boat to bank2")
            self.move_wolf_from_boat_to_bank2()
            if not self.rules_checker.run():
                raise Exception("Rule violation after moving wolf to bank2")
            self.node.back_and_fourth.append((1, 0))
            return True
        except Exception as e:
            self.node = original_state
            print(f"Reverted due to: {e}")
            return False

    def move_1_wolf_from_right_to_left(self) -> bool:
        original_state = copy.deepcopy(self.node)
        try:
            if (self.node.bank_instance_right.wolf_count > 0 and
                    self.node.boat_instance.get_animal_count() < 2):
                self.move_sheep_from_boat_to_bank2()
                if not self.rules_checker.run():
                    raise Exception("Rule violation after moving sheep to bank2")
            self.move_wolf_from_bank2_to_boat()
            if not self.rules_checker.run():
                raise Exception("Rule violation after moving wolf to boat")
            self.move_boat_from_bank2_to_bank1()
            if not self.rules_checker.run():
                raise Exception("Rule violation after moving boat to bank1")
            self.move_wolf_from_boat_to_bank1()
            if not self.rules_checker.run():
                raise Exception("Rule violation after moving wolf to bank1")
            self.node.back_and_fourth.append((1, 0))
            return True
        except Exception as e:
            self.node = original_state
            print(f"Reverted due to: {e}")
            return False

    def move_1_sheep_from_left_to_right(self) -> bool:
        original_state = copy.deepcopy(self.node)
        try:
            ## if there is too many animals on boat, get one off
            if (self.node.bank_instance_right.get_sheep_count() > 0 and
                    self.node.boat_instance.get_animal_count() < 2):
                self.move_wolf_from_boat_to_bank1()
                if not self.rules_checker.run():
                    raise Exception("Rule violation after moving sheep to bank2")
            self.move_sheep_from_bank1_to_boat()
            if not self.rules_checker.run():
                raise Exception("Rule violation after moving sheep to boat")
            self.move_boat_from_bank1_to_bank2()
            if not self.rules_checker.run():
                raise Exception("Rule violation after moving boat to bank2")
            self.move_sheep_from_boat_to_bank2()
            if not self.rules_checker.run():
                raise Exception("Rule violation after moving sheep to bank2")
            self.node.back_and_fourth.append((1, 0))
            return True
        except Exception as e:
            self.node = original_state
            print(f"Reverted due to: {e}")
            return False

    def move_1_sheep_from_right_to_left(self) -> bool:
        original_state = copy.deepcopy(self.node)
        try:
            if (self.node.bank_instance_right.sheep_count > 0 and
                    self.node.boat_instance.get_animal_count() < 2):
                self.move_wolf_from_boat_to_bank2()
                if not self.rules_checker.run():
                    raise Exception("Rule violation after moving sheep to bank2")
            self.move_sheep_from_bank2_to_boat()
            if not self.rules_checker.run():
                raise Exception("Rule violation after moving sheep to boat")
            self.move_boat_from_bank2_to_bank1()
            if not self.rules_checker.run():
                raise Exception("Rule violation after moving boat to bank1")
            self.move_sheep_from_boat_to_bank1()
            if not self.rules_checker.run():
                raise Exception("Rule violation after moving sheep to bank1")
            self.node.back_and_fourth.append((1, 0))
            return True
        except Exception as e:
            self.node = original_state
            print(f"Reverted due to: {e}")
            return False


    def move_2_wolves_from_left_to_right(self) -> bool:
        original_state = copy.deepcopy(self.node)
        try:
            # when there is 1 sheep, 2 sheep, and 1 wolf

            # if there is 1 sheep
            if (self.node.bank_instance_left.get_wolf_count() > 0 and
                self.node.boat_instance.get_animal_count() < 2 and
                self.node.boat_instance.get_sheep_count() == 1
            ):
                self.move_sheep_from_boat_to_bank1()
                if not self.rules_checker.run():
                    raise Exception("Rule violation after moving sheep to bank1")
                self.move_wolf_from_bank1_to_boat()
                if not self.rules_checker.run():
                    raise Exception("Rule violation after moving wolf to boat")
                self.move_wolf_from_bank1_to_boat()
                if not self.rules_checker.run():
                    raise Exception("Rule violation after moving wolf to bank1")
            # if 2 sheep
            elif (self.node.bank_instance_left.get_wolf_count() > 0 and
                self.node.boat_instance.get_animal_count() < 2 and
                self.node.boat_instance.get_sheep_count() == 2
            ):
                self.move_sheep_from_boat_to_bank1()
                if not self.rules_checker.run():
                    raise Exception("Rule violation after moving sheep1 to bank1")
                self.move_sheep_from_boat_to_bank1()
                if not self.rules_checker.run():
                    raise Exception("Rule violation after moving sheep2 to bank1")
                # TODO: going to fail since the boat is empty for a sec
                if not self.rules_checker.run():
                    raise Exception("Rule violation after moving wolf to boat")
                self.move_wolf_from_bank1_to_boat()
                if not self.rules_checker.run():
                    raise Exception("Rule violation after moving wolf to bank1")
             #if 1 wolf
            elif (self.node.bank_instance_left.get_wolf_count() > 0 and
                self.node.boat_instance.get_animal_count() < 2 and
                self.node.boat_instance.get_wolf_count() == 1
            ):
                self.move_wolf_from_bank1_to_boat()
                if not self.rules_checker.run():
                    raise Exception("Rule violation after moving wolf to boat")
            elif (self.node.bank_instance_left.get_wolf_count() > 0 and
                self.node.boat_instance.get_animal_count() < 2 and
                self.node.boat_instance.get_wolf_count() == 2
            ):
                raise Exception("We just moved these over")
            #move boat
            self.move_boat_from_bank1_to_bank2()
            self.node.back_and_fourth((0,2))
        except Exception as e:
            self.node = original_state
            print(f"Reverted due to: {e}")
            return False

    def move_2_wolves_from_right_to_left(self) -> bool:
        original_state = copy.deepcopy(self.node)
        try:
            # when there is 1 sheep, 2 sheep, and 1 wolf

            # if there is 1 sheep
            if (self.node.bank_instance_right.get_wolf_count() > 0 and
                    self.node.boat_instance.get_animal_count() < 2 and
                    self.node.boat_instance.get_sheep_count() == 1
            ):
                self.move_sheep_from_boat_to_bank2()
                if not self.rules_checker.run():
                    raise Exception("Rule violation after moving sheep to bank2")
                self.move_wolf_from_bank2_to_boat()
                if not self.rules_checker.run():
                    raise Exception("Rule violation after moving wolf to boat")
                self.move_wolf_from_bank2_to_boat()
                if not self.rules_checker.run():
                    raise Exception("Rule violation after moving wolf to bank2")
            # if 2 sheep
            elif (self.node.bank_instance_right.get_wolf_count() > 0 and
                  self.node.boat_instance.get_animal_count() < 2 and
                  self.node.boat_instance.get_sheep_count() == 2
            ):
                self.move_sheep_from_boat_to_bank2()
                if not self.rules_checker.run():
                    raise Exception("Rule violation after moving sheep1 to bank2")
                self.move_sheep_from_boat_to_bank2()
                if not self.rules_checker.run():
                    raise Exception("Rule violation after moving sheep2 to bank2")
                # TODO: going to fail since the boat is empty for a sec
                if not self.rules_checker.run():
                    raise Exception("Rule violation after moving wolf to boat")
                self.move_wolf_from_bank2_to_boat()
                if not self.rules_checker.run():
                    raise Exception("Rule violation after moving wolf to bank2")
            # if 1 wolf
            elif (self.node.bank_instance_right.get_wolf_count() > 0 and
                  self.node.boat_instance.get_animal_count() < 2 and
                  self.node.boat_instance.get_wolf_count() == 1
            ):
                self.move_wolf_from_bank2_to_boat()
                if not self.rules_checker.run():
                    raise Exception("Rule violation after moving wolf to boat")
            elif (self.node.bank_instance_right.get_wolf_count() > 0 and
                  self.node.boat_instance.get_animal_count() < 2 and
                  self.node.boat_instance.get_wolf_count() == 2
            ):
                raise Exception("We just moved these over")
            # move boat
            self.move_boat_from_bank2_to_bank1()
            self.node.back_and_fourth((0, 2))
        except Exception as e:
            self.node = original_state
            print(f"Reverted due to: {e}")
            return False


    # move 2 sheep from shore 1 to shore 2
    def move_2_sheep_from_left_to_right(self) -> bool:
        original_state = copy.deepcopy(self.node)
        try:
            # when there is 1 sheep, 2 sheep, and 1 wolf

            # if there is 1 sheep
            if (self.node.bank_instance_left.get_sheep_count() > 0 and
                    self.node.boat_instance.get_animal_count() < 2 and
                    self.node.boat_instance.get_sheep_count() == 1
            ):
                self.move_sheep_from_boat_to_bank1()
                if not self.rules_checker.run():
                    raise Exception("Rule violation after moving sheep to bank1")
                self.move_sheep_from_bank1_to_boat()
                if not self.rules_checker.run():
                    raise Exception("Rule violation after moving sheep to boat")
                self.move_sheep_from_bank1_to_boat()
                if not self.rules_checker.run():
                    raise Exception("Rule violation after moving sheep to bank1")
            # if 2 sheep
            elif (self.node.bank_instance_left.get_sheep_count() > 0 and
                  self.node.boat_instance.get_animal_count() < 2 and
                  self.node.boat_instance.get_sheep_count() == 2
            ):
                self.move_sheep_from_boat_to_bank1()
                if not self.rules_checker.run():
                    raise Exception("Rule violation after moving sheep1 to bank1")
                self.move_sheep_from_boat_to_bank1()
                if not self.rules_checker.run():
                    raise Exception("Rule violation after moving sheep2 to bank1")
                # TODO: going to fail since the boat is empty for a sec
                if not self.rules_checker.run():
                    raise Exception("Rule violation after moving sheep to boat")
                self.move_sheep_from_bank1_to_boat()
                if not self.rules_checker.run():
                    raise Exception("Rule violation after moving sheep to bank1")
            # if 1 sheep
            elif (self.node.bank_instance_left.get_sheep_count() > 0 and
                  self.node.boat_instance.get_animal_count() < 2 and
                  self.node.boat_instance.get_sheep_count() == 1
            ):
                self.move_sheep_from_bank1_to_boat()
                if not self.rules_checker.run():
                    raise Exception("Rule violation after moving sheep to boat")
            elif (self.node.bank_instance_left.get_sheep_count() > 0 and
                  self.node.boat_instance.get_animal_count() < 2 and
                  self.node.boat_instance.get_sheep_count() == 2
            ):
                raise Exception("We just moved these over")
            # move boat
            self.move_boat_from_bank1_to_bank2()
            self.node.back_and_fourth((0, 2))
        except Exception as e:
            self.node = original_state
            print(f"Reverted due to: {e}")
            return False
    # move 2 sheep from shore 2 to shore 1

    def back_to_parent_node(self):
        self.node.exhausted = True
        if self.node.get_parent_node():
            return self.node.get_parent_node()
        else:
            return self.node


    def move_2_sheep_from_right_to_left(self) -> bool:
        original_state = copy.deepcopy(self.node)
        try:

            # if there is 1 wolves
            if (self.node.bank_instance_right.get_wolf_count() > 0 and
                    self.node.boat_instance.get_animal_count() < 2 and
                    self.node.boat_instance.get_wolves_count() == 1
            ):
                self.move_wolf_from_boat_to_bank2()
                if not self.rules_checker.run():
                    raise Exception("Rule violation after moving wolf to bank2")
                self.move_wolf_from_bank2_to_boat()
                if not self.rules_checker.run():
                    raise Exception("Rule violation after moving wolf to boat")
                self.move_wolf_from_bank2_to_boat()
                if not self.rules_checker.run():
                    raise Exception("Rule violation after moving wolf to bank2")
            # if 2 wolf
            elif (self.node.bank_instance_right.get_wolf_count() > 0 and
                  self.node.boat_instance.get_animal_count() < 2 and
                  self.node.boat_instance.get_wolf_count() == 2
            ):
                self.move_wolf_from_boat_to_bank2()
                if not self.rules_checker.run():
                    raise Exception("Rule violation after moving wolf1 to bank2")
                self.move_wolf_from_boat_to_bank2()
                if not self.rules_checker.run():
                    raise Exception("Rule violation after moving wolf2 to bank2")
                # TODO: going to fail since the boat is empty for a sec
                if not self.rules_checker.run():
                    raise Exception("Rule violation after moving wolf to boat")
                self.move_wolf_from_bank2_to_boat()
                if not self.rules_checker.run():
                    raise Exception("Rule violation after moving wolf to bank2")
            # if 1 wolf
            elif (self.node.bank_instance_right.get_wolf_count() > 0 and
                  self.node.boat_instance.get_animal_count() < 2 and
                  self.node.boat_instance.get_wolf_count() == 1
            ):
                self.move_wolf_from_bank2_to_boat()
                if not self.rules_checker.run():
                    raise Exception("Rule violation after moving wolf to boat")
            elif (self.node.bank_instance_right.get_wolf_count() > 0 and
                  self.node.boat_instance.get_animal_count() < 2 and
                  self.node.boat_instance.get_wolf_count() == 2
            ):
                raise Exception("We just moved these over")
            # move boat
            self.move_boat_from_bank2_to_bank1()
            self.node.back_and_fourth((0, 2))
        except Exception as e:
            self.node = original_state
            print(f"Reverted due to: {e}")
            return False

    # TODO: this needs to pass coppies into each, otherwise we are editing the node
    def run_next_action(self) -> Node:
        pass
        # You can re-order these to set preference/ weight on more frequently ran actions
        actions_case = {
            0: self.move_1_sheep_from_left_to_right(),
            1: self.move_1_sheep_from_right_to_left(),
            2: self.move_1_wolf_from_left_to_right(),
            3: self.move_1_wolf_from_right_to_left(),
            4: self.move_2_sheep_from_left_to_right(),
            5: self.move_2_sheep_from_right_to_left(),
            6: self.move_2_wolves_from_left_to_right(),
            7: self.move_2_wolves_from_right_to_left()

        }

        # Iterate over all actions, should return a node
        for action_index in range(len(actions_case)):
            if self.node.exhausted:
                self.back_to_parent_node()
                break
            action = actions_case.get(self.node.actions_ran)
            if action:
                action()
                # if RunAllRules(self.node).run():
                #     return self.node
                # elif self.node.actions_ran == len(actions_case):
                #     self.node.exhausted = True
                #     return self.node
                # else:
                #     self.node.actions_ran += 1
