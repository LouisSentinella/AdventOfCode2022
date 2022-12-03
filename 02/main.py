from elfy.elf import Elf, decrypt_move_order
from elfy.rock_paper_scissors import RockPaperScissorsGame

player_one_moves = []
player_two_moves = []
for line in open("input.txt", "r"):
    player_one_move, player_two_move = line.split()
    player_one_moves.append(player_one_move)
    player_two_moves.append(player_two_move)

player_one = Elf(encrypted_move_order=player_one_moves, decryption_key={'A': 'rock', 'B': 'paper', 'C': 'scissors'})
player_two = Elf(encrypted_move_order=player_two_moves, decryption_key={'X': 'rock', 'Y': 'paper', 'Z': 'scissors'})

game = RockPaperScissorsGame(player_one, player_two)
game.run_game()
game.get_game_results()

desired_outcomes = decrypt_move_order(player_two_moves, {'X': 'loss', 'Y': 'draw', 'Z': 'win'})
player_two_moves = [game.move_calculator(opponent_move, outcome) for opponent_move, outcome in zip(player_one.get_move_order(), desired_outcomes)]

player_one = Elf(encrypted_move_order=player_one_moves, decryption_key={'A': 'rock', 'B': 'paper', 'C': 'scissors'})
player_two = Elf(move_order=player_two_moves)

game = RockPaperScissorsGame(player_one, player_two)
game.run_game()
game.get_game_results()

