from node import Node


class RunAllRules:
    def __init__(self, node: Node):
        self.node = node

    def bank_rules(self) -> bool:
        # wolves outnumber sheep on bank
        if ((0 < self.node.bank_instance_left.get_sheep_count() < self.node.bank_instance_left.get_wolf_count()) or
                (
                        0 < self.node.bank_instance_right.get_sheep_count() < self.node.bank_instance_right.get_wolf_count()) or
                self.node.bank_instance_right.get_wolf_count() > self.node.bank_instance_right.get_sheep_count() or
                self.node.bank_instance_left.get_wolf_count() + self.node.bank_instance_left.get_sheep_count() >= 0 or
                self.node.bank_instance_right.get_sheep_count() + self.node.bank_instance_right.get_wolf_count() >= 0
        ):
            return False
        else:
            return True

    def boat_rules(self) -> bool:
        # boat can hold 2 animals
        total_animals = self.node.boat_instance.get_sheep_count() + self.node.boat_instance.get_wolf_count()
        if total_animals < 1 or total_animals > 2:
            return False
        else:
            return True

    # def different_than_parent(self) -> bool:
    #     # we are at root, may want to just end process?
    #     if self.node.get_parent_node() is None:
    #         return True
    #     if (
    #             (self.node.bank_instance_left.get_wolf_count() + self.node.bank_instance_left.get_boat_wolf_count() ==
    #              self.node.get_parent_node().bank_instance_left.get_wolf_count() + self.node.get_parent_node().bank_instance_left.get_boat_wolf_count()) and
    #             (self.node.bank_instance_left.get_sheep_count() + self.node.bank_instance_left.get_boat_sheep_count() ==
    #              self.node.get_parent_node().bank_instance_left.get_sheep_count() + self.node.get_parent_node().bank_instance_left.get_boat_sheep_count()) and
    #             (
    #                     self.node.bank_instance_right.get_sheep_count() + self.node.bank_instance_right.get_boat_sheep_count() ==
    #                     self.node.get_parent_node().bank_instance_right.get_sheep_count() + self.node.get_parent_node().bank_instance_right.get_boat_sheep_count()) and
    #             (self.node.bank_instance_right.get_wolf_count() + self.node.bank_instance_right.get_boat_wolf_count() ==
    #              self.node.get_parent_node().bank_instance_right.get_wolf_count() + self.node.get_parent_node().bank_instance_right.get_boat_wolf_count())
    #     ):
    #         return False
    #     return True

    def check_if_solved(self) -> None:
        if (self.node.bank_instance_left.get_wolf_count() == 0 and
                self.node.bank_instance_left.get_sheep_count() == 0 and
                self.node.bank_instance_left.get_boat_presence() == False
                # and self.node.boat_instance.get_wolf_count() == 0 and
                # self.node.boat_instance.get_sheep_count() == 0
        ):
            self.node.solved = True

    def run(self) -> bool:
        solve_check: bool = (self.bank_rules() and
                             self.boat_rules()
                             # and self.different_than_parent()
                             )
        if solve_check:
            self.check_if_solved()
        return solve_check
