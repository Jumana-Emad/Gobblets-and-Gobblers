class Evaluation:
    def __init__(self, ai: Player, opponent: Player, game: Game):
        # Initialize an instance of the Evaluation class with references to AI, opponent, and the game.
        self.opponent = opponent
        self.ai = ai
        self.game = game

    def evaluate_board(self):
        # Evaluate the current state of the game board and return a score indicating desirability for the AI player.
        if self.game.winner == self.ai.player_number:
            # Return positive infinity if the AI player wins.
            return float('inf')
        if self.game.winner == self.opponent.player_number:
            # Return negative infinity if the opponent wins.
            return float('-inf')

        # Define weights for different evaluation factors.
        piece_count_weight = 1
        threat_weight = 3
        blocking_weight = 5

        ai_score = 0
        opponent_score = 0

        # Evaluate based on piece count.
        ai_score += piece_count_weight * self.count_pieces(self.ai.player_number)
        opponent_score += piece_count_weight * self.count_pieces(self.opponent.player_number)

        # Evaluate based on threats.
        ai_score += threat_weight * self.count_threats(self.opponent.player_number)
        opponent_score += threat_weight * self.count_threats(self.ai.player_number)

        # Evaluate based on blocking moves.
        ai_score += blocking_weight * self.count_blocks(self.ai.player_number)
        opponent_score += blocking_weight * self.count_blocks(self.opponent.player_number)

        # Return the difference between AI score and opponent score.
        return ai_score - opponent_score

    def count_pieces(self, player_number):
        # Count the number of on-top pieces belonging to a specific player on the game board.
        result = 0
        for gobbler in self.game.gobblers:
            if gobbler.player == player_number and gobbler.is_on_top:
                result += 1
        return result

    def count_threats(self, player_number):
        # Count the number of potential winning combinations (threats) for a player on the game board.
        result = 0

        # Iterate through winning combinations.
        for combo in self.game.winning_combinations:
            count = 0
            for position in combo:
                gobbler = self.game.board[position][-1] if self.game.board[position] else None
                if gobbler and gobbler.player != player_number:
                    count += 1
            # If the opponent has three pieces in a row, it's a threat.
            if count == 3:
                result += 1

        return result

    def count_blocks(self, player_number):
        # Count the number of potential blocking moves for a player on the game board.
        result = 0

        # Iterate through winning combinations.
        for combo in self.game.winning_combinations:
            count_p = 0
            count_o = 0
            for position in combo:
                gobbler = self.game.board[position][-1] if self.game.board[position] else None
                if gobbler:
                    if gobbler.player == player_number:
                        count_p += 1
                    else:
                        count_o += 1
            # If the opponent has three pieces in a row with one empty space, it's a blocking move.
            if count_o == 3 and count_p == 1:
                result += 1

        return result
