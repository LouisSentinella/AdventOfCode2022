import string


def get_item_priority(item):
    priorities = string.ascii_lowercase + string.ascii_uppercase
    return priorities.index(item) + 1


class Rucksack:

    def __init__(self, rucksack_contents):
        self.compartments = [rucksack_contents[:len(rucksack_contents) // 2],
                             rucksack_contents[len(rucksack_contents) // 2:]]

    def find_compartment_similarity(self):
        return [i for i in self.compartments[0] if i in self.compartments[1]][0]

    def get_rucksack_contents(self, compartmented=False):
        if compartmented:
            return self.compartments
        else:
            return self.compartments[0] + self.compartments[1]
