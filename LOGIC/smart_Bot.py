from Gobblet_Game import Game
import random

class Player:
    def __init__(self, player_number, name, game):
        self.player_number = player_number
        self.name = name
        self.repr = f'{name}({player_number})'
        self.game = game

class Human(Player):
    def __init__(self, player_number, name, game):
        super().__init__(player_number, name, game)

    def select_gobbler(self):
        text = f'{self.repr}, select a gobbler to move (1-12): '
        return input(text)

    def select_board_position(self):
        text = f'{self.repr}, where would you '\
                f'like to place gobbler {self.game.selected_gobbler_piece.piece_no} (1-16)? '
        return input(text)

class Easy_Bot(Player):
    def __init__(self, player_number, name, game):
        super().__init__(player_number, name, game)

    def select_gobbler(self):
        available_gobblers = [g for g in self.game.gobblers if g.player == self.player_number and g.is_on_top]
        random_idx = random.randint(0, len(available_gobblers) - 1)

        return available_gobblers[random_idx].piece_no

    def select_board_position(self):
        return random.randint(0, 15)

class Medium_Bot(Player):
    def __init__(self,player_number,name,game):
        super().__init__(player_number, name, game)
        self.game=game
        self.gobbler = ""
        self.position = ""
    def select_gobbler(self):
        alpha=float('-inf')
        beta=float('inf') 
        result, self.gobbler, self.position,alpha=self.game.minimax(self.game.board,3,True,alpha,beta,True)
        # print(self.game.Draw_board())
        print("Gobbler: ", self.gobbler)
        return self.gobbler.piece_no
    def select_board_position(self):
        print("Position: ", self.position)
        return self.position + 1
        
class Hard_Bot(Player):
    def __init__(self,player_number,name,game):
        super().__init__(player_number, name, game)
        self.game=game
        self.gobbler = ""
        self.position = ""
    def select_gobbler(self):
        alpha=float('-inf')
        beta=float('inf') 
        result, self.gobbler, self.position,alpha=self.game.minimax(self.game.board,2,True,alpha,beta,True)
        # print(self.game.Draw_board())
        print("Gobbler: ", self.gobbler)
        return self.gobbler.piece_no
    def select_board_position(self):
        print("Position: ", self.position)
        return self.position + 1
#while True:
