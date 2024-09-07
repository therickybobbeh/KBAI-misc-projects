from src.node import Node


class RunAllRules:
    def __init__ (self, node: Node):
        self.node = node

    def bank_rules(self) -> bool:
        # wolves outnumber sheep on bank
        if (self.node.bank_instance_left.wolves > self.node.bank_instance_left.sheep or
                self.node.bank_instance_right.wolves > self.node.bank_instance_right.sheep):
            return False
        else:
            return True

    def boat_rules(self) -> bool:
        # boat can hold 2 animals
        total_animals = self.node.boat_instance.sheep + self.node.boat_instance.wolves
        if total_animals < 1 or total_animals >= 2:
            return False
        else:
            return True

    def different_than_parent(self) -> bool:
        #we are at root, may want to just end process?
        if self.node.get_parent_node() is None:
            return True
        if (
                self.node.bank_instance_left.get_wolf_count() == self.node.get_parent_node().bank_instance_left.get_wolf_count() and
                self.node.bank_instance_left.get_sheep_count() == self.node.get_parent_node().bank_instance_left.get_sheep_count() and
                self.node.bank_instance_right.get_wolf_count() == self.node.get_parent_node().bank_instance_right.get_wolf_count() and
                self.node.bank_instance_right.get_sheep_count() == self.node.get_parent_node().bank_instance_right.get_sheep_count() and
                self.node.boat_instance.get_wolf_count() == self.node.get_parent_node().boat_instance.get_wolf_count() and
                self.node.boat_instance.get_sheep_count() == self.node.get_parent_node().boat_instance.get_sheep_count()):
            return False
        return True


    def check_if_solved(self) -> None:
        if (self.node.bank_instance_left.get_wolf_count() == 0 and
                self.node.bank_instance_left.get_sheep_count() == 0
                # and self.node.boat_instance.get_wolf_count() == 0 and
                # self.node.boat_instance.get_sheep_count() == 0
                ):
            self.node.solved = True


    def check_if_dead_end(self) -> bool:
        pass

    def run(self) -> bool:
        self.check_if_solved()
        return self.bank_rules() and self.boat_rules() and self.different_than_parent()

