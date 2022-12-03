class RockPaperScissorsGame:

    def __init__(self, player_one, player_two):
        self.player_one = player_one
        self.player_two = player_two

    def single_round(self, player_one_shape, player_two_shape):
        shape_score_map = {"rock": 1, "paper": 2, "scissors": 3}
        game_result_map = {"rock": {"rock": 3, "paper": 0, "scissors": 6}, "paper": {"rock": 6, "paper": 3, "scissors": 0}, "scissors": {"rock": 0, "paper": 6, "scissors": 3}}

        shape_score_one = shape_score_map[player_one_shape]
        shape_score_two = shape_score_map[player_two_shape]

        game_score_one = game_result_map[player_one_shape][player_two_shape]
        game_score_two = game_result_map[player_two_shape][player_one_shape]

        player_one_score = shape_score_one + game_score_one
        player_two_score = shape_score_two + game_score_two

        return player_one_score, player_two_score

    def move_calculator(self, opponent_move, desired_outcome):
        game_result_map = {"rock": {"draw" : "rock", "win" : "paper", "loss" : "scissors"},
                           "paper": {"loss" : "rock", "draw" : "paper", "win" : "scissors"},
                           "scissors": {"win" : "rock", "loss" : "paper", "draw" : "scissors"}}

        return game_result_map[opponent_move][desired_outcome]

    def run_game(self):

        for player_one_move, player_two_move in zip(self.player_one.get_move_order(), self.player_two.get_move_order()):

            player_one_score, player_two_score = self.single_round(player_one_move, player_two_move)

            self.player_one.add_score(player_one_score)
            self.player_two.add_score(player_two_score)

    def get_game_results(self):
        print("Player One:", self.player_one.get_score())
        print("Player Two:", self.player_two.get_score())

