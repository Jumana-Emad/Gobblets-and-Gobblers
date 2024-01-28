
class Node:
    def __init__(self, data):
        self.piece_no = data
        self.next_node = None

class Gobbler_piece:
    def __init__(self, player: int, piece_no: int):
        self.piece_no = piece_no  # integers 1-12
        if self.piece_no<4 :
            self.piece_size=4-((piece_no)%4)
        elif self.piece_no%4==0 :
            self.piece_size=((piece_no)%4)
        else:    
         self.piece_size=4-((piece_no)%4) # integer 0-3 piece 1 is the biggest size
        self.player = player  # integer -2-2
        
        self.board_position = None  # integers 0-15 or None
        self.board_position_previous = None # so that it can be placed back where it came from
        self.board_previous_positions = [] # A list that saves the previous positions of a goblet
        self.under_on_board =None
        if(self.piece_size ==3 ):
            self.is_on_top=True
        else:
            self.is_on_top = False
        
counter=0

class Game:
    def __init__(self):
        self.player_name = ['player 0', 'player 1']
        self.winner = None

        # create the gobblers
        number_of_gobbler_pieces = 12
        self.gobblers = []
        for player in range(2):  # number of players
            piece_no = 1
            for gobbler in range(number_of_gobbler_pieces):
                gobbler = Gobbler_piece(player, piece_no)
                self.gobblers.append(gobbler)
                piece_no += 1

        self.current_player_idx = 0
        self.selected_gobbler_piece = None
        self.board = [None for _ in range(16)]
        # for _ in range(16):
        #     self.board.append([])

        self.winning_combinations = [
            [0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15],
            [0, 4, 8, 12], [1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15],[0,5,10,15],[3,6,9,12]
        ]
 #the rules for selecting gobbler piece
    def select_gobbler_object(self, gobbler_piece: int, minimax = False) -> bool:
        if minimax:
            aaa = 0
        if self.winner is not None and not minimax:
            return False
        if self.selected_gobbler_piece:
            return False
        if self.Original_input(gobbler_piece, 0, 11) is None:
            return False
        matching_gobblers = [g for g in self.gobblers if g.player == self.current_player_idx][self.Original_input(gobbler_piece, 0, 11)]
        if not matching_gobblers.is_on_top:
            return False
       # if (not matching_gobblers.is_on_top) and (matching_gobblers.under is None) and (matching_gobblers.board_position is None)   : 
       #    return False
        self.selected_gobbler_piece = matching_gobblers
        if self.selected_gobbler_piece.board_position is not None  :
            
         if self.current_player_idx == 0 and not minimax:
            print("AAA")
        #  if self.board[self.selected_gobbler_piece.board_position].under_on_board == self.selected_gobbler_piece:
        #      return False
         if self.selected_gobbler_piece.under_on_board is not None:
             if self.board[self.selected_gobbler_piece.board_position].under_on_board == self.selected_gobbler_piece:
                return False
             self.board[self.selected_gobbler_piece.board_position]=self.selected_gobbler_piece.under_on_board
             self.board[self.selected_gobbler_piece.board_position].board_position=self.selected_gobbler_piece.board_position
             self.selected_gobbler_piece.under_on_board=None
            #  self.board[self.selected_gobbler_piece.board_position].is_on_top=False
         else :self.board[self.selected_gobbler_piece.board_position]=None
          
        # self.selected_gobbler_piece.board_position_previous = self.selected_gobbler_piece.board_position
        self.selected_gobbler_piece.board_previous_positions.append(self.selected_gobbler_piece.board_position)
        self.selected_gobbler_piece.board_position = None
        self._update_on_top()
        return True

    def select_gobbler_position(self, board_position: int, piece: int, minimax = False) -> bool:
        board_position = self.Original_input(board_position, 0, 15)
        # matching_gobblers = [g for g in self.gobblers if g.player == self.current_player_idx][self.original_input(piece, 0, 11)]
        # self.selected_gobbler_piece = matching_gobblers
        # if not matching_gobblers.is_on_top:
        #      return False
        if not self.selected_gobbler_piece:
            return False, None
        elif self.selected_gobbler_piece.board_previous_positions[-1] == board_position :
            return False, None
        # elif self.selected_gobbler_piece.board_position_previous == board_position :
        #     return False, None
        elif board_position is None:
            return False, None
        
        elif (self.board[board_position] and self.selected_gobbler_piece.piece_size <= self.board[board_position].piece_size):
            return False, None
       
        if self.board[board_position] is not None:
         self.selected_gobbler_piece.under_on_board=self.board[board_position]
         #self.selected_gobbler_piece.under_on_board.on_board_position=None
         self.board[board_position]=self.selected_gobbler_piece
         self.selected_gobbler_piece.board_position = board_position
        else:
            self.board[board_position]=self.selected_gobbler_piece
            self.selected_gobbler_piece.board_position = board_position
    
    
        
        self._update_on_top()
        if not minimax:
            self.current_player_idx = int(not self.current_player_idx)
        self.selected_gobbler_piece = None
        return True, self._check_for_winner()
    #def update_under(self):
        
    def _update_on_top(self):
        """
        checks all of the gobblers on the board and
        updates their is_on_top flag
        """
        first_stack=[]
        second_stack=[]
        third_stack=[]
        for position in self.board:
            if position is not None:  
                position.is_on_top = True
                if position.under_on_board is not None:
                    position.under_on_board.is_on_top = False
        for g in  self.gobblers:
            if g.board_position is None and g.player == self.current_player_idx :
                if g.piece_no<=4:
                    first_stack.append(g)
                elif g.piece_no<=8:
                    second_stack.append(g)
                elif g.piece_no<=12:
                    third_stack.append(g)
        first_stack = sorted(first_stack,reverse=True, key=lambda g: g.piece_no)
        second_stack = sorted(second_stack,reverse=True, key=lambda g: g.piece_no)
        third_stack = sorted(third_stack,reverse=True, key=lambda g: g.piece_no)

        # first_stack[-1].is_on_top= True
        for i in first_stack:
            if i == first_stack[-1]:
                i.is_on_top= True
            else:
                i.is_on_top = False
        # second_stack[-1].is_on_top=True
        for i in second_stack:
            if i == second_stack[-1]:
                i.is_on_top= True
            else:
                i.is_on_top = False
        # third_stack[-1].is_on_top=True
        for i in third_stack:
            if i == third_stack[-1]:
                i.is_on_top= True
            else:
                i.is_on_top = False

    # def set_player_names(self, player_names: list) -> list[bool, str]:
    #     player_name_0 = player_names[0]
    #     player_name_1 = player_names[1]
    #     name_len_requirement = 3
    #     if len(player_name_0) < name_len_requirement or len(player_name_1) < name_len_requirement:
    #         return False, f'Player names must be at least {name_len_requirement} characters long.'
    #     elif player_name_0 == player_name_1:
    #         return False, 'Player names cannot be identical.'
    #     else:
    #         self.player_names = player_names
    #         return True, 'Let the games begin!'
    def _check_for_winner(self) -> int:
        """
        checks if there is a winner
        if so, returns winner (int)
        if not, returns None
        """
        # check all of the winning combinations for a winner

        for combo in self.winning_combinations:
            # initialize a list to keep track of the
            # owner of each piece
            result_to_check = []
            for position in combo:
                if self.board[position]:
                    # record the player of the current piece in a list
                    result_to_check.append(self.board[position].player)
                else:
                    result_to_check.append(None)
            # if there is only one non-None unique value, then
            # we have a winner
            unique_values = list(set(result_to_check))
            if len(unique_values) == 1 and unique_values[0] is not None:
                self.winner = unique_values[0]
                return self.winner
        return None
            #still shearching
        #for i ,j in enumerate(self.board):
         #   if j==0:
         #       return 1
            #tie case
       # return 0


    def Draw_board(self) -> str:
        new_board = ''
        k = 0
        for cell in self.board:
            if cell:
                str_to_add = f'|{cell.piece_no}({cell.player})'
            else:
                str_to_add = f'|____'
            new_board += str_to_add
            k += 1
            if k > 3:
                new_board += '|\n'
                k = 0
        new_board += '-----------------------'
        return new_board

    def Original_input(self, value: int, minimum: int, maximum: int) -> int:
        return (int(value))-1 if minimum <= ((int(value))-1) <= maximum else None

    def get_possible_moves(self,board,gobblers,selected_gobbler_num,prevposition)->list:
        r1=[g.board_position for g in gobblers if g.is_on_top and g.piece_size < selected_gobbler_num ]
        # r2=[i for i ,cell in enumerate(board) if len(cell) == 0 and i != prevposition ]
        r2=[i for i in range(16) if board[i] is None and i != prevposition ]
        r3=r1+r2
        return r3
    def get_list_selected_gobblers(self,gobblers)->list:
        r1 = [g for g in gobblers if g.is_on_top and g.player == self.current_player_idx and g.board_position is not None ]
        # r2 = [g for g in gobblers if g.board_position is None and g.board_position_previous is None and g.player == self.current_player_idx and g.is_on_top]
        r2 = [g for g in gobblers if g.board_position is None and (not g.board_previous_positions or g.board_previous_positions[-1] is None) and g.player == self.current_player_idx and g.is_on_top]
        r3=r1+r2
        return r3
    def winner_case(self)->int:
        for move in self.winning_combinations:
            result = []
            for pcell in move:
                if self.board[pcell]:
                    result.append(self.board[pcell].player)
                else:
                    result.append(None)
            unique_result= list(set(result))
            if len(unique_result) == 1 and unique_result[0] is not None:
                if unique_result[0]:
                    self.winner = 2
                else:
                    self.winner = -2
                return self.winner
        #return None
        # still searching
        # for i ,cell in enumerate(self.board):
        #   if len(cell)==0:
        #         return 1
        for i in self.board:
            if i == None:
                return 1
         #tie case
        return 0

  
    def maximizer(self,board,depth,alpha,beta):
            global max_gobbler
            global max_move

            self.current_player_idx = 1
            best_score = float('-inf')
            for r in self.get_list_selected_gobblers(self.gobblers):
                max_gobbler=r.piece_no
                # for move in self.get_possible_moves(self.board, self.gobblers,r.piece_size,r.board_position_previous):
                for move in self.get_possible_moves(self.board, self.gobblers,r.piece_size,r.board_previous_positions):
                    max_move=move  
                    if move is None:
                        continue  
                    self.select_gobbler_object(r.piece_no, True)
                    self.select_gobbler_position(move+1, r.piece_size,True) 

                    returned_value = self.minimax(board, depth - 1, False,alpha,beta,False)
                    # print(self.Draw_board()) 
                    score=returned_value[0]
                    compared=returned_value[3]
                    if compared>alpha:
                        alpha=score
                    self.current_player_idx = 1

                    if r.board_position is not None:
                        if r.under_on_board is not None:
                            r.under_on_board.is_on_top = True
                        self.board[r.board_position] = r.under_on_board
                    r.under_on_board = None

                    # r.board_position = r.board_position_previous
                    r.board_position = r.board_previous_positions[-1]
                    if r.board_position is not None:
                        r.under_on_board = self.board[r.board_position]
                        self.board[r.board_position] = r
                    r.board_previous_positions.pop()
                    self._update_on_top()
                    if (score > best_score):
                        bestGobbler = r
                        bestPosition = move
                        best_score = score
                        
                    if alpha>= beta:
                         return best_score, bestGobbler, bestPosition ,alpha 
            
            return best_score, bestGobbler, bestPosition ,alpha
    def minimizer(self,board,depth,alpha,beta):
            global max_gobbler
            global max_move
            self.current_player_idx = 0
            best_score = float('inf')  # Change to positive infinity for minimizing
            # r1=[g.piece_no for g in self.get_list_selected_gobblers(self.gobblers)]
            # if(11 in r1):
            #     jemmy=2
            # print(r1)
            for r in self.get_list_selected_gobblers(self.gobblers):
                    # print(self.get_possible_moves(self.board, self.gobblers,r.piece_no,r.board_position_previous))
                    # print(r.piece_no)
                    # print(r.player)
                    # for move in self.get_possible_moves(self.board, self.gobblers,r.piece_size,r.board_position_previous):
                    for move in self.get_possible_moves(self.board, self.gobblers,r.piece_size,r.board_previous_positions):
                        if move is None:
                            continue
                        if max_move ==0 and max_gobbler == 4 and r.piece_no==12 and move == 1:
                            jemmy=1
                        self.select_gobbler_object(r.piece_no, True)
                        self.select_gobbler_position(move+1, r.piece_size,True)
                        # self._update_on_top()
                        # print(self.Draw_board())
                        returned_value = self.minimax(board, depth - 1, True,alpha,beta,False)
                        score=returned_value[0]
                        compared=returned_value[3]
                        if compared<beta:
                            beta=score

                        if score == -2 or score == 2:
                            jemmy=1
                        self.current_player_idx = 0
                        if r.board_position is not None:
                            if r.under_on_board is not None:
                                r.under_on_board.is_on_top = True
                            self.board[r.board_position] = r.under_on_board
                        r.under_on_board = None
                        # self.board[move].pop()
                        # r.board_position = r.board_position_previous
                        r.board_position = r.board_previous_positions[-1]
                        if r.board_position is not None:
                            r.under_on_board = self.board[r.board_position]
                            self.board[r.board_position] = r
                        r.board_previous_positions.pop()
                        self._update_on_top()
                        if (score < best_score):
                            bestGobbler = r
                            bestPosition = move
                            best_score = score
                        if alpha>= beta:
                            return best_score, bestGobbler, bestPosition ,beta 

            return best_score, bestGobbler, bestPosition,beta


    def minimax(self, board: list, depth: int, isMaximizing: bool,alpha,beta,firstTime=True):
        result = self.evaluate_function()
        # result = self.winner_case()
        self.winner = None
        bestGobbler = None
        bestPosition = None
        global counter
     


        if  depth == 0:
            counter=counter+1
            return result, bestGobbler, bestPosition,result

        if isMaximizing:  
            best_score, bestGobbler, bestPosition,alpha=self.maximizer(board,depth,alpha,beta)  
            print(counter)   
            return best_score, bestGobbler, bestPosition,alpha

        else: 
            best_score, bestGobbler, bestPosition,beta=self.minimizer(board,depth,alpha,beta)     
            return best_score, bestGobbler, bestPosition,beta
        
    def evaluate_function(self):
            if self.current_player_idx == 0:
                bot_player_idx = 1
            elif self.current_player_idx == 1:
                bot_player_idx = 0
            if self._check_for_winner() == bot_player_idx:
                return float('inf')
            if self._check_for_winner() == self.current_player_idx:
                return float('-inf')
            
            piece_place_wgt = 1
            threat_wgt = 5
            block_wgt = 5

            bot_score = piece_place_wgt * self.piece_place(bot_player_idx) + threat_wgt * self.threats(bot_player_idx) + block_wgt * self.threats(self.current_player_idx)
            player_score = piece_place_wgt * self.piece_place(self.current_player_idx) + threat_wgt * self.threats(self.current_player_idx) + block_wgt * self.threats(bot_player_idx)

            return bot_score - player_score
 
    # to give a score to the pieces on the board based on (number, size, postion)
    def piece_place(self, player_idx):   
        result = 0
        for i in range(4):
            for j in range(4):
                if self.board[4*i+j] and self.board[4*i+j].player == player_idx:
                    if(i == 0 or i==3) and (j==0 or j ==3):
                        result += 2 * ( 0.25 * self.board[4*i+j].piece_size)
                    elif i == 0 or i==3 or j==0 or j ==3:
                        result += (0.25 * self.board[4*i+j].piece_size)
                    else:
                        result += 3 * (0.25 * self.board[4*i+j].piece_size)
        return result

    def threats( self,player_idx):

        result = 0

        #horizontal
        for i in range(4):
            count = 0
            for j in range(4):
                if self.board[4*i+j] :
                    if self.board[4*i+j].player == player_idx:
                        count += 1
                    else:
                        count -= 1
            if count == 3:
                result += 1

        #vertical
        for i in range(4):
            count = 0
            for j in range(4):
                if self.board[4*j+i]:
                    if self.board[4*j+i].player == player_idx:
                        count += 1
                    else:
                        count -= 1

            if count == 3:
                result += 1

        #  forward diagonal
        count = 0
        for i in range(4):
            if self.board[5*i] :
                if self.board[5*i].player == player_idx:
                    count += 1
                else:
                    count -= 1
        if count == 3:
            result += 1


        # backward diagonal
        count = 0
        for i in range(4):
            if self.board[3*i+3]:
                if self.board[3*i+3].player == player_idx:
                    count += 1
                else:
                    count -= 1
        if count == 3:
            result += 1
        return result


    @property
    def winner_name(self) -> str:
        return self.player_name[self.winner] if self.winner is not None else None
    @property
    def current_player_name(self) -> str:
        return self.player_name[self.current_player_idx]
