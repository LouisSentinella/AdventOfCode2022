from rucksack import Rucksack

def decrypt_move_order(encrypted_move_order, decryption_key):
    move_order = []
    for i in encrypted_move_order:
        move_order.append(decryption_key[i])
    return move_order


class Elf:

    def __init__(self, calories=None, encrypted_move_order=None, decryption_key=None, move_order=None, rucksack=None):
        if calories is None:
            calories = []
        self.calories = calories

        if encrypted_move_order is not None and decryption_key is not None:
            self.move_order = decrypt_move_order(encrypted_move_order, decryption_key)
        else:
            self.move_order = move_order

        self.rucksack = rucksack

        self.score = 0

    def get_calories(self):
        return self.calories

    def get_calories_total(self):
        return sum(self.calories)

    def set_calories(self, calories):
        self.calories = calories

    def get_move_order(self):
        return self.move_order

    def get_score(self):
        return self.score

    def add_score(self, score):
        self.score += score

    def set_score(self, score):
        self.score = score

    def set_rucksack(self, rucksack_contents):
        self.rucksack = Rucksack(rucksack_contents)

    def get_rucksack(self):
        return self.rucksack
class ElvenGroup:

    def __init__(self, elves):
        self.elves = elves

        self.rucksacks = [elf.rucksack for elf in self.elves]
        self.identification_badge = self.find_identification_badge()

    def find_identification_badge(self):
        common_items = [i for i in self.rucksacks[0].get_rucksack_contents() if i in self.rucksacks[1].get_rucksack_contents()]
        for i in self.rucksacks:
            common_items = [item for item in common_items if item in i.get_rucksack_contents()]

        return common_items[0]



