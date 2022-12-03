def decrypt_move_order(encrypted_move_order, decryption_key):
    move_order = []
    for i in encrypted_move_order:
        move_order.append(decryption_key[i])
    return move_order


class Elf:

    def __init__(self, calories=None, encrypted_move_order=None, decryption_key=None, move_order=None):
        if calories is None:
            calories = []
        self.calories = calories

        if encrypted_move_order is not None and decryption_key is not None:
            self.move_order = decrypt_move_order(encrypted_move_order, decryption_key)
        else:
            self.move_order = move_order

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

