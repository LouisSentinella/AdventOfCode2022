from elfy.rucksack import Rucksack


def decrypt_move_order(encrypted_move_order, decryption_key):
    move_order = []
    for i in encrypted_move_order:
        move_order.append(decryption_key[i])
    return move_order


def is_pair_contained(pair_one, pair_two):
    """
    Checks if pair_one contains pair_two
    """
    if pair_one[0] <= pair_two[0]:
        if pair_one[-1] >= pair_two[-1]:
            return True
    return False


class Elf:

    def __init__(self):
        self.calories = None
        self.move_order = None
        self.rucksack = None
        self.cleaning_assignment = None
        self.score = 0

    def get_calories(self):
        return self.calories

    def get_calories_total(self):
        return sum(self.calories)

    def set_calories(self, calories):
        self.calories = calories

    def get_move_order(self):
        return self.move_order

    def set_move_order(self, move_order):
        self.move_order = move_order

    def set_move_order_encrypted(self, encrypted_move_order, decryption_key):
        self.move_order = decrypt_move_order(encrypted_move_order, decryption_key)

    def get_score(self):
        return self.score

    def add_score(self, score):
        self.score += score

    def set_score(self, score):
        self.score = score

    def pack_rucksack(self, rucksack_contents):
        self.rucksack = Rucksack(rucksack_contents)

    def get_rucksack(self):
        return self.rucksack

    def assign_cleaning(self, lower, upper):
        self.cleaning_assignment = [i for i in range(lower, upper + 1)]


class ElvenGroup:

    def __init__(self, elves):
        self.elves = elves

        if self.elves[0].rucksack is not None:
            self.rucksacks = [elf.rucksack for elf in self.elves]
            self.identification_badge = self.find_identification_badge()

    def find_identification_badge(self):
        common_items = [i for i in self.rucksacks[0].get_rucksack_contents() if
                        i in self.rucksacks[1].get_rucksack_contents()]
        for i in self.rucksacks:
            common_items = [item for item in common_items if item in i.get_rucksack_contents()]

        return common_items[0]

    def find_redundant_cleaning(self):
        for ix, i_elf in enumerate(self.elves):
            for jx, j_elf in enumerate(self.elves):
                if ix is not jx:
                    if is_pair_contained(i_elf.cleaning_assignment, j_elf.cleaning_assignment):
                        return True
        return False

    def identify_cleaning_overlap(self):
        for ix, i_elf in enumerate(self.elves):
            for jx, j_elf in enumerate(self.elves):
                if ix is not jx:
                    combined_cleaning = i_elf.cleaning_assignment + j_elf.cleaning_assignment
                    if len(set(combined_cleaning)) < len(combined_cleaning):
                        return True
        return False
