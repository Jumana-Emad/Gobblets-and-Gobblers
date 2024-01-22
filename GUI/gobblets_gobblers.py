import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
import os
from tkinter import messagebox
from tkinter import PhotoImage
import pygame
from pygame.locals import *
import random
class GameDetails:
    def __init__(self,game_mode,player1_name, player2_name , level, color):
        self.game_mode = game_mode
        if(game_mode == "pvp"):
            self.player1_name = player1_name
            self.player2_name = player2_name
            self.player1_color = color
            self.player2_color = (0,0,0) if color == (255,255,255) else (255,255,255)
            self.level = ""
        else:
            self.player1_name = player1_name 
            self.player2_name = "Computer AI"
            self.player1_color = color
            self.player2_color = (0,0,0) if color == (255,255,255) else (255,255,255)
            self.level = level

class ChooseWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Goblets and Gabblers")
        self.root.resizable(False, False) 
        self.gameMode = "pvp"
        self.root.configure(bg='#ADD8E6') 

        canvas = tk.Canvas(self.root, width=730, height=280, background="#ADD8E6")
        canvas.pack()

        # Draw the gobblet
        canvas.create_oval(230, 50, 400, 220, fill="#f36523", outline="#f36523")

        # Draw the text "Gobblet"
        canvas.create_text(230, 110, text="Gobblet", fill="#FFFFFF", font=("Arial", 60))

        # Draw the text "Gobbler's"
        canvas.create_text(430, 200, text="Gobbler's", fill="#FFFFFF", font=("Arial", 40))

        self.buttons = [
            tk.Button(self.root, text="Player vs Player", font=('normal', 20), background="#13c3f4", activebackground="#f36523", width=50, height=5, command=lambda: self.set_game_mode("pvp"),),
            tk.Button(self.root, text="Player vs Computer", font=('normal', 20), background="#13c3f4", activebackground="#f36523", width=50, height=5, command=lambda: self.set_game_mode("pvc"))
        ]

        for button in self.buttons:
            button.pack(pady=10)

    def set_game_mode(self, mode):
        self.gameMode = mode
        if mode == "pvp":
            self.root.destroy()
            self.new_window(PlayervsPlayer)
        if mode == "pvc":
            self.root.destroy()
            self.new_window(PlayervsComputer)

        #print(f"Selected Game Mode: {mode}")

    def new_window(self, _class):
        new_window = _class()
        new_window.run()

    def run(self):
        self.root.mainloop()


class PlayervsPlayer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Player vs Player")  
        self.root.resizable(False, False) 
        #self.gameMode = game_mode
        self.root.configure(bg='#ADD8E6') 
        self.root.protocol("WM_DELETE_WINDOW", self.back_to_choose)

        # Load an image
        self.image = ImageTk.PhotoImage(Image.open("finalvs.jpg").resize((730,400)))

        # Display the image using a Label
        self.image_label = tk.Label(self.root, image=self.image)
        self.image_label.grid(row=0, column=0, columnspan=5)  # Adjust columnspan to match the number of columns in the grid

        tk.Label(self.root, text="Black Player Name", width=18, height=4, font=('Helvetica', 18), background='#ADD8E6').grid(row=1, column=0, padx=10)
        self.e1 = tk.Entry(self.root, width=18, font=('Helvetica', 18))
        self.e1.grid(row=1, column=1)

        tk.Label(self.root, text="White Player Name", width=18, height=4, font=('Helvetica', 18), background='#ADD8E6').grid(row=1, column=3, padx=10)
        self.e2 = tk.Entry(self.root, width=18, font=('Helvetica', 18))
        self.e2.grid(row=1, column=4, padx=4)

        b1 = tk.Button(self.root, text="Start Game", font=('normal', 18), background="#13c3f4", activebackground="#f36523", width=15, height=3, command=lambda: self.new_window())
        b1.grid(row=3, column=2, pady=10)  

    
    def back_to_choose(self):
        self.root.destroy()
        ChooseWindow().run()

    def new_window(self):
        text = self.e1.get()
        text2 = self.e2.get()
        if text and text2:
            if text == text2:
                messagebox.showinfo("Same Name", 'Player names cannot be identical.')
            elif len(text) <= 12:
                if len(text2) <= 12:
                    self.root.destroy()
                    game_details = GameDetails("pvp", text, text2, 0 , (0,0,0))
                    new_window = Game(game_details)
                    new_window.run()
                else:
                    messagebox.showinfo("Name length", "White player's Name can be at most 12 letters long")               
            else:
                messagebox.showinfo("Name length", "Black player's Name can be at most 12 letters long")       
        else:
            messagebox.showinfo("Name", "Enter Names First")

    def run(self):
        self.root.mainloop()


class PlayervsComputer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Player vs Computer")  
        self.root.resizable(False, False) 
      #  self.gameMode = "game_mode"
        self.color = (0,0,0)
        self.level = "Easy"
        self.selColor = "#f36523"
        self.selLevel = ""
        self.root.configure(bg='#ADD8E6') 
        self.root.protocol("WM_DELETE_WINDOW", self.back_to_choose)

        tk.Label(self.root, text="Player Name", width=18, height=4, font=('Helvetica', 18), background='#ADD8E6').grid(row=0, column=0, padx=10)
        self.e1 = tk.Entry(self.root, width=18, font=('Helvetica', 18))
        self.e1.grid(row=0, column=1)
        
        tk.Label(self.root, text="Level", width=18, height=4, font=('Helvetica', 18), background='#ADD8E6').grid(row=1, column=0, padx=10)

        self.b1 = tk.Button(self.root, text=" Easy", font=('normal', 18), background="#f36523", activebackground="#f36523", width=15, height=3, command=lambda: self.changebg(1))
        self.b2 = tk.Button(self.root, text="Hard", font=('normal', 18), background="#13c3f4", activebackground="#f36523", width=15, height=3, command=lambda: self.changebg(2))
        self.b6 = tk.Button(self.root, text="Impossible", font=('normal', 18), background="#13c3f4", activebackground="#f36523", width=15, height=3, command=lambda: self.changebg(5))
        
        self.b1.grid(row= 1,column=1)
        self.b2.grid(row=1,column = 2)
        self.b6.grid(row=1,column = 3, padx = 10) 
        
        tk.Label(self.root, text="Your Color", width=18, height=4, font=('Helvetica', 18), background='#ADD8E6').grid(row=2, column=0, padx=10)

        self.b3 = tk.Button(self.root, text="Black", font=('normal', 18), background="#f36523",foreground="#ffffff",activeforeground="#000000", activebackground="#f36523", width=15, height=3, command=lambda: self.changebg(3))
        self.b4 = tk.Button(self.root, text="White", font=('normal', 18), background="#ffffff",foreground="#000000",activeforeground="#ffffff", activebackground="#f36523", width=15, height=3, command=lambda: self.changebg(4))
        self.b3.grid(row= 2,column=1)
        self.b4.grid(row=2,column = 2) 

        self.b5 = tk.Button(self.root, text="Start Game", font=('normal', 18), background="#13c3f4", activebackground="#f36523", width=15, height=3, command=lambda: self.new_window())
        self.b5.grid(row=3, column=1, pady=10)  

    
    def back_to_choose(self):
        self.root.destroy()
        ChooseWindow().run()

    def changebg(self, a):
        if a == 1:
            self.b1.config(background= "#f36523")
            self.b2.config(background="#13c3f4")
            self.b6.config(background="#13c3f4")
            self.level = "Easy"

        if a == 2:
            self.b2.config(background= "#f36523")
            self.b1.config(background="#13c3f4")
            self.b6.config(background="#13c3f4")
            self.level = "Hard"    

        if a == 3:
            self.b3.config(background= "#f36523")
            self.b4.config(background="#ffffff")
            self.color = (0,0,0)

        if a == 4:
            self.b4.config(background= "#f36523")
            self.b3.config(background="#000000")
            self.color = (255,255,255)
        
        if a == 5:
            self.b6.config(background= "#f36523")
            self.b2.config(background="#13c3f4")
            self.b1.config(background="#13c3f4")
            self.level = "Impossible"  
        #print(self.level,self.color)          


    def new_window(self):
        text = self.e1.get()
        if text:
            if len(text) <= 12:
                self.root.destroy()
                game_details = GameDetails("pvc", text, "", self.level , self.color)
                new_window = Game(game_details)
                new_window.run()
            else:
                messagebox.showinfo("Name length", "Name can be at most 12 letters long")   
        else:
            messagebox.showinfo("Name", "Enter Name First")

    def run(self):
        self.root.mainloop()

class Easy_Bot:
    def __init__(self, player_number, game):
        self.player_number = player_number
        self.game = game

    def select_gobbler(self):
        if self.player_number == 0:
            available_gobblers = [g for g in self.game.left_gobblets if g.is_on_top]
        else:
            available_gobblers = [g for g in self.game.right_gobblets if g.is_on_top]

        random_idx = random.randint(0, len(available_gobblers) - 1)
        #print(random_idx, available_gobblers)
        available_gobblers[random_idx].color = (243, 101, 35) if self.player_number == 0 else (19, 195, 244)
        return available_gobblers[random_idx]

    def select_board_position(self):
        return random.randint(0, 15)

class Medium_Bot:
    def __init__(self,player_number,name,game):
        super().__init__(player_number, name, game)
        self.game=game
        self.gobbler = ""
        self.position = ""
    def play(self):
        # game=Game()
        result, self.gobbler, self.position=self.game.minimax(self.game.board,2,True,True)
        print(self.game.Draw_board())
    def select_gobbler(self):
        print("Gobbler: ", self.gobbler)
        return self.gobbler
    def select_board_position(self):
        print("Position: ", self.position)
        return self.position
        
class Hard_Bot:
    def __init__(self,player_number,name,game):
        super().__init__(player_number, name, game)
        self.play()
        # self.gobbler
        # self.position
    def play(self):
        game=Game()
        result, self.gobbler, self.position=game.minimax(game.board,6,True,True)
        print(game.Draw_board())

class Gobbler_piece:
    def __init__(self, player, piece_no,color,radius,position):
        self.player = player  # integer 0-1
        #index 0 is the biggest in stack 1 , 1 is the smaller , 2 smaller and 3 smallest , etc
        self.piece_no = piece_no  # integers 0-11 
        self.size = piece_no % 4 #size 0 is the biggest, 3 is the smallest
        self.board_position = None  # integers 0-15 or None
        self.board_position_previous = None  # so that it can be placed back where it came from
        self.is_on_top = True
        self.color = color
        self.radius = radius
        self.position = position
        self.under = None

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius)
  

class Game:
    
    def __init__(self, game_details):
        self.game_details = game_details
        pygame.init()
        #print(game_details.game_mode, game_details.player1_name , game_details.player2_name, game_details.player1_color, game_details.level)
        self.left_color = (243, 101, 35)
        self.right_color = (19, 195, 244)
        self.left_gobblets = []
        self.right_gobblets = []
        self.screen = pygame.display.set_mode((600, 500))
        pygame.display.set_caption("Gobblets and Gobblers")
        self.clicked = False
        self.current_player = 0
        self.board = [" " for _ in range(16)]
        self.player1 = "player1"
        self.player2 = "player2"
        self.error = ""
        self.efont = pygame.font.Font(None, 16)
        self.error_txt = self.efont.render(self.error , True, (255,0,0))  # red color

        self.pfont = pygame.font.Font(None, 36)  # Use a default font
        self.clock = pygame.time.Clock()

        # Create a text surface
        #print(self.game_details.player1_color)
        self.nextTurn = self.game_details.player1_name if self.game_details.player1_color == (0,0,0) else self.game_details.player2_name
        self.text_color = self.left_color
        self.text_surface = self.pfont.render(self.nextTurn + "'s Turn", True, self.text_color)  # White color
        self.fade_start_time = 0
        self.fade_duration = 0 
        
        # Set up the Winner pop-up window
        popup_width, popup_height = 400, 200
        self.popup_screen = pygame.Surface((popup_width, popup_height))
        self.popup_rect = self.popup_screen.get_rect(center=(600 // 2, 500 // 2))

        # Set up fonts and text for the pop-up window
        self.popup_font = pygame.font.Font(None, 28)
        self.popup_message = self.popup_font.render("Congratulations! You Won!", True, (0, 255, 0))
        self.popup_message_rect = self.popup_message.get_rect(center=(140, popup_height // 3))

        self.play_again_button = pygame.Rect(popup_width // 4, 2 * popup_height // 3, popup_width // 2, popup_height // 4)

        self.winner_no = None
        self.winner = ""
        self.win_win = False

        self.winning_combinations = [
            [0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15],
            [0, 4, 8, 12], [1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15],[0,5,10,15],[3,6,9,12]
        ]
    def retry_comp(self):
        print("retrying")
        if self.game_details.level == "Easy":
            index = Easy_Bot(self.current_player,self).select_board_position()
            clicked_row = index //4
            clicked_col = index %4
            self.move_pos(clicked_row,clicked_col)
        elif self.game_details.level == "Hard":
            index = Medium_Bot().select_board_position()
            clicked_row = index //4
            clicked_col = index %4
            self.move_pos(clicked_row,clicked_col)
        elif self.game_details.level == "Impossible":
            index = Hard_Bot().select_board_position()
            clicked_row = index //4
            clicked_col = index %4
            self.move_pos(clicked_row,clicked_col)
                                
    def move_pos(self, row, col):
        index = 4 * row + col
        for i in range(12):
            if(self.current_player == 0):
                if self.left_gobblets[i].color == self.left_color:
                    if self.left_gobblets[i].board_position != None:       
                        PlacedIndex = self.left_gobblets[i].board_position
                        if(self.left_gobblets[i].under != None):
                            self.board[PlacedIndex] = self.left_gobblets[i].under
                        else:
                            self.board[PlacedIndex] = " "
                    if self.left_gobblets[i].board_position == None:
                        if self.board[index] == " ":
                                self.clicked = False
                                self.left_gobblets[i].board_position = index
                                self.left_gobblets[i].position = (150+ 100*col,50+ 100*row)
                                self.left_gobblets[i].color = (0,0,0) 
                                if(self.left_gobblets[i].under != None):
                                    self.left_gobblets[i].under.is_on_top = True
                                    self.left_gobblets[i].under = None   
                                self.left_gobblets[i].is_on_top = True
                                self.left_gobblets[i].under = None 
                                self.board[index] = self.left_gobblets[i] 
                                self.switch_player()       
                                break
                        elif self.check_possible_win() == True:
                            if self.board[index].size > self.left_gobblets[i].size:
                                    self.clicked = False
                                    self.left_gobblets[i].board_position = index
                                    self.left_gobblets[i].position = (150+ 100*col,50+ 100*row)
                                    self.left_gobblets[i].color = (0,0,0) 
                                    if(self.left_gobblets[i].under != None):
                                        self.left_gobblets[i].under.is_on_top = True
                                        self.left_gobblets[i].under = None
                                    temp = self.board[index]
                                    self.left_gobblets[i].under = temp
                                    self.left_gobblets[i].is_on_top = True
                                    self.left_gobblets[i].under.is_on_top = False     
                                    self.board[index] = self.left_gobblets[i]
                                    self.switch_player()  
                                    break
                            else:
                                if self.game_details.game_mode == "pvc" and self.game_details.player2_color == (0,0,0):
                                    self.retry_comp()
                                else:        
                                    self.set_error("*Can't gobble a bigger Gobblet")

                        else:
                            if self.game_details.game_mode == "pvc" and self.game_details.player2_color == (0,0,0):
                                        self.retry_comp()
                            else: 
                                self.set_error("*new gobblet must place on an empty square")
                    else:
                            if self.board[index] == " ":
                                self.clicked = False
                                self.left_gobblets[i].board_position = index
                                self.left_gobblets[i].position = (150+ 100*col,50+ 100*row)
                                self.left_gobblets[i].color = (0,0,0) 
                                if(self.left_gobblets[i].under != None):
                                    self.left_gobblets[i].under.is_on_top = True
                                    self.left_gobblets[i].under = None   
                                self.left_gobblets[i].is_on_top = True
                                self.left_gobblets[i].under = None 
                                self.board[index] = self.left_gobblets[i] 
                                self.switch_player()       
                                break
                            elif self.board[index].size > self.left_gobblets[i].size:
                                    self.clicked = False
                                    self.left_gobblets[i].board_position = index
                                    self.left_gobblets[i].position = (150+ 100*col,50+ 100*row)
                                    self.left_gobblets[i].color = (0,0,0) 
                                    if(self.left_gobblets[i].under != None):
                                        self.left_gobblets[i].under.is_on_top = True
                                        self.left_gobblets[i].under = None
                                    temp = self.board[index]
                                    self.left_gobblets[i].under = temp
                                    self.left_gobblets[i].is_on_top = True
                                    self.left_gobblets[i].under.is_on_top = False     
                                    self.board[index] = self.left_gobblets[i]
                                    self.switch_player()  
                                    break
                            else:
                                if self.game_details.game_mode == "pvc" and self.game_details.player2_color == (0,0,0):
                                        self.retry_comp()
                                else: 
                                    self.set_error("*Can't gobble a bigger Gobblet")
                               
            else:                    
                if self.right_gobblets[i].color == self.right_color:

                    if self.right_gobblets[i].board_position != None:
                        PlacedIndex = self.right_gobblets[i].board_position
                        if(self.right_gobblets[i].under != None):
                            self.board[PlacedIndex] = self.right_gobblets[i].under
                        else:
                            self.board[PlacedIndex] = " "
                    
                    if self.right_gobblets[i].board_position == None:
                        if self.board[index] == " ":
                                self.clicked = False
                                self.right_gobblets[i].board_position = index 
                                self.right_gobblets[i].position = (150+ 100*col,50+ 100*row)
                                self.right_gobblets[i].color = (255,255,255) 
                                if(self.right_gobblets[i].under != None):
                                    self.right_gobblets[i].under.is_on_top = True
                                    self.right_gobblets[i].under = None
                                self.right_gobblets[i].is_on_top = True
                                self.right_gobblets[i].under = None
                                self.board[index] = self.right_gobblets[i]
                                self.switch_player()
                                break
                        elif self.check_possible_win() == True:
                            if self.board[index].size > self.right_gobblets[i].size:
                                self.clicked = False
                                self.right_gobblets[i].board_position = index 
                                self.right_gobblets[i].position = (150+ 100*col,50+ 100*row)
                                self.right_gobblets[i].color = (255,255,255) 
                                if(self.right_gobblets[i].under != None):
                                    self.right_gobblets[i].under.is_on_top = True
                                    self.right_gobblets[i].under = None
                                temp = self.board[index]
                                self.right_gobblets[i].under = temp
                                self.right_gobblets[i].is_on_top = True
                                self.right_gobblets[i].under.is_on_top = False
                                self.board[index] = self.right_gobblets[i]
                                self.switch_player()
                                break                    
                            else:
                                if self.game_details.game_mode == "pvc" and self.game_details.player2_color == (255,255,255):
                                        self.retry_comp()
                                else: 
                                    self.set_error("*Can't gobble a bigger Gobblet")
                        else:
                            if self.game_details.game_mode == "pvc" and self.game_details.player2_color == (255,255,255):
                                        self.retry_comp()
                            else: 
                                self.set_error("*new gobblet must place on an empty square")
                    else:
                        if self.board[index] == " ":
                                self.clicked = False
                                self.right_gobblets[i].board_position = index 
                                self.right_gobblets[i].position = (150+ 100*col,50+ 100*row)
                                self.right_gobblets[i].color = (255,255,255) 
                                if(self.right_gobblets[i].under != None):
                                    self.right_gobblets[i].under.is_on_top = True
                                    self.right_gobblets[i].under = None
                                self.right_gobblets[i].is_on_top = True
                                self.right_gobblets[i].under = None
                                self.board[index] = self.right_gobblets[i]
                                self.switch_player()
                                break
                        elif self.board[index].size > self.right_gobblets[i].size:
                                self.clicked = False
                                self.right_gobblets[i].board_position = index 
                                self.right_gobblets[i].position = (150+ 100*col,50+ 100*row)
                                self.right_gobblets[i].color = (255,255,255) 
                                if(self.right_gobblets[i].under != None):
                                    self.right_gobblets[i].under.is_on_top = True
                                    self.right_gobblets[i].under = None
                                temp = self.board[index]
                                self.right_gobblets[i].under = temp
                                self.right_gobblets[i].is_on_top = True
                                self.right_gobblets[i].under.is_on_top = False
                                self.board[index] = self.right_gobblets[i]
                                self.switch_player()
                                break                    
                        else:
                            if self.game_details.game_mode == "pvc" and self.game_details.player2_color == (255,255,255):
                                        self.retry_comp()
                            else: 
                                self.set_error("*Can't gobble a bigger Gobblet")
        
            
        if self._check_for_winner()!= None:
            me = 0 if self.current_player == 1 else 1
            #print(f"Player {me} wins!")
            self.Celebrate()

    def check_possible_win(self) -> bool:
        """
        checks if there is a possible win next turn
        if so, returns True
        if not, returns False
        """
        # check all of the winning combinations for a winner
        for combo in self.winning_combinations:
            # initialize a list to keep track of the
            # owner of each piece
            result_to_check = []
            #print("combo" )
            for position in combo:
               # print(position)
                if self.board[position] != " ":
                    # record the player of the current piece in a list
                    #print("checking", me)
                    result_to_check.append(self.board[position].player)

                # else:
                #     result_to_check.append(None)
            #print(result_to_check)        
            # if there is only one non-None unique value, then
            # we have a winner
            unique_values = list(set(result_to_check))
            #print(result_to_check, unique_values)
            if len(unique_values) == 1 and len(result_to_check) == 3:
                if(unique_values[0] != self.current_player):
                    return True
        return None

    def _check_for_winner(self) -> int:
        """
        checks if there is a winner
        if so, returns winner (int)
        if not, returns None
        """
        #me = 0 if self.current_player == 1 else 1 
        # check all of the winning combinations for a winner
        for combo in self.winning_combinations:
            # initialize a list to keep track of the
            # owner of each piece
            result_to_check = []
            #print("combo" )
            for position in combo:
               # print(position)
                if self.board[position] != " ":
                    # record the player of the current piece in a list
                    #print("checking", me)
                    result_to_check.append(self.board[position].player)

                else:
                    result_to_check.append(None)
            #print(result_to_check)        
            # if there is only one non-None unique value, then
            # we have a winner
            unique_values = list(set(result_to_check))
            if len(unique_values) == 1 and unique_values[0] is not None:
                self.winner_no = unique_values[0]
                return self.winner_no
        return None

    def Celebrate(self):
        if self.winner_no == 0:
            if self.game_details.player1_color == (0,0,0):
                self.winner = self.game_details.player1_name
                
            else:
                self.winner = self.game_details.player2_name

        else:
            if self.game_details.player1_color == (255,255,255):
                self.winner = self.game_details.player1_name
            else:
                self.winner = self.game_details.player2_name
                
        self.popup_message = self.popup_font.render("Congratulations " + self.winner +"! You Won!", True, (0, 255, 0))
        self.win_win = True        

    def set_error(self,error):
            self.error = error
            #print(self.error)
            # Set up timing variables
            self.fade_start_time = pygame.time.get_ticks()
            self.fade_duration = 2000  # 2 seconds
            self.error_txt = self.efont.render(self.error , True, (255,0,0))  # red color
            self.error_txt.set_alpha(255)
    
    def switch_player(self):
        if self.current_player == 1:
            self.current_player = 0
            pygame.display.set_caption("Black's Turn")
            self.nextTurn = self.game_details.player1_name if self.nextTurn == self.game_details.player2_name else self.game_details.player2_name
            self.text_color = self.left_color
            self.text_surface= self.pfont.render(self.nextTurn + "'s Turn", True, self.text_color)

        else: 
            self.current_player = 1 
            pygame.display.set_caption("White's Turn")
            self.nextTurn = self.game_details.player1_name if self.nextTurn == self.game_details.player2_name else self.game_details.player2_name
            #self.nextTurn = self.game_details.player1_name if self.game_details.player1_color == (255,255,255) else self.game_details.player1_name
            self.text_color =  self.right_color
            self.text_surface= self.pfont.render(self.nextTurn + "'s Turn", True, self.text_color)
        if self.game_details.game_mode == "pvc":
            if (self.game_details.player2_color == (0,0,0) and self.current_player == 0) or (self.game_details.player2_color == (255,255,255) and self.current_player == 1):   
                    self.Bot_turn()

    def reset_game(self):
        pygame.quit()
        ChooseWindow().run()
        quit()
        #self.current_player = "X"
        #self.board = [" " for _ in range(16)]
    # Main game loop
    # running = True
    
    def check_clicked(self):
        for i in range(12):
            if(self.current_player == 0 and self.left_gobblets[i].color == self.left_color):
                self.clicked = True
            elif (self.current_player == 1 and self.right_gobblets[i].color == self.right_color):
                self.clicked = True

    def generate_gobblets(self):
        for i in range(3):
            for j in range(4):   
                    gobbler=  Gobbler_piece(0,i*4 +j ,(0, 0, 0), 40-j*10, (100//2, 72+(i)*(400//3)))
                    if(j%4 != 0):
                        gobbler.is_on_top = False
                    self.left_gobblets.append(gobbler)

        for i in range(3):
            for j in range(4):   
                    gobbler=  Gobbler_piece(1,i*4 +j ,(255, 255, 255), 40-j*10, (500+100//2, 72+(i)*(400//3)))
                    if(j%4 != 0):
                        gobbler.is_on_top = False
                    self.right_gobblets.append(gobbler)

        for j in range(12):
            if j%4 != 3:
                self.left_gobblets[j].under = self.left_gobblets[j+1]   
                self.right_gobblets[j].under = self.right_gobblets[j+1]        
    
    def Bot_turn(self):
        if(self.game_details.game_mode == "pvc" ):
            if (self.game_details.player2_color == (0,0,0) and self.current_player == 0) or (self.game_details.player2_color == (255,255,255) and self.current_player == 1):
                if(self.game_details.level == "Easy"):
                    bot = Easy_Bot(self.current_player,self)
                elif(self.game_details.level == "Hard"):
                    bot = Medium_Bot(self.current_player,self)
                elif(self.game_details.level == "Impossible"):
                    bot = Hard_Bot(self.current_player,self)
                chosen_piece = bot.select_gobbler()
                self.clicked = True
                chosen_index = bot.select_board_position()
        
            while (self.game_details.player2_color == (0,0,0) and self.current_player == 0) or (self.game_details.player2_color == (255,255,255) and self.current_player == 1):                
                    for i in range(12):
                        if(self.current_player == 0):
                            if (self.left_gobblets[i].is_on_top == True and self.left_gobblets[i].color == self.left_color and self.clicked):
                                clicked_row = chosen_index //4
                                clicked_col = chosen_index %4
                                # print(clicked_row,clicked_col)
                                #print(clicked_row,clicked_col)
                                if (self.left_gobblets[i].position[1]//100 == clicked_row and (self.left_gobblets[i].position[0]-100)//100 == clicked_col):
                                    #print("Can't move in the same position")
                                    #self.set_error("*Can't move in the same position")
                                    chosen_index = bot.select_board_position()
                                else:
                                    #print(chosen_index,clicked_row,clicked_col)
                                    self.move_pos(clicked_row, clicked_col) 
                                    break
                        elif(self.current_player == 1):
                                    if (self.right_gobblets[i].is_on_top == True and self.right_gobblets[i].color == self.right_color and self.clicked):
                                        #print("d5lt3")
                                        clicked_row = chosen_index //4
                                        clicked_col = chosen_index %4
                                        # print(clicked_row,clicked_col)
                                        if (self.right_gobblets[i].position[1]//100 == clicked_row and (self.right_gobblets[i].position[0]-100)//100 == clicked_col):
                                            #print("Can't move in the same position")
                                            #self.set_error("*Can't move in the same position")
                                            chosen_index = bot.select_board_position()
                                        else:
                                            self.move_pos(clicked_row, clicked_col) 
                                        break
    def run(self):
        self.generate_gobblets()
        self.Bot_turn()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    ChooseWindow().run()
                    quit()
                elif self.win_win and event.type == MOUSEBUTTONDOWN:
                    mouseX, mouseY = event.pos
                    #print(self.play_again_button.center[1], mouseY ,self.play_again_button.center[0], mouseX)
                    if  200 <= mouseX <= 380 and 290 <= mouseY <= 320:
                        self.reset_game()
                        #print("Play Again clicked")
                        self.win_win = False    
                elif event.type == MOUSEBUTTONDOWN:
                    mouseX, mouseY = event.pos
                    #print(event.pos)
                    #print(self.clicked)
                    self.check_clicked()
                    # for i in range(12):
                    #     if(self.current_player == 0 and self.left_gobblets[i].color == self.left_color):
                    #         self.clicked = True
                    #     elif (self.current_player == 1 and self.right_gobblets[i].color == self.right_color):
                    #         self.clicked = True
                    for i in range(12):            
                            if (self.current_player == 0 and self.left_gobblets[i].is_on_top == True and  mouseY - 40 < self.left_gobblets[i].position[1] < mouseY + 40 and mouseX - 35 < self.left_gobblets[i].position[0] < mouseX + 35 ):
                                #print("yay")
                                if not self.clicked and self.current_player == self.left_gobblets[i].player:
                                    #print("fo2")
                                    # self.left_gobblets[i].color = (0,0,255)
                                    self.left_gobblets[i].color = self.left_color
                                    #print(self.left_gobblets[i].color)
                                    if self.left_gobblets[i].under != None and self.left_gobblets[i].under.player != self.left_gobblets[i].player:
                                            temp = self.board.copy()
                                            self.board[self.left_gobblets[i].board_position] = self.left_gobblets[i].under
                                            if self._check_for_winner() == 1:
                                                self.set_error("*Watchout white gobblet underneath")                     
                                                self.board = temp.copy()
                                break
                            elif(self.current_player == 1 and self.right_gobblets[i].is_on_top == True and  mouseY - 40 < self.right_gobblets[i].position[1] < mouseY + 40 and mouseX - 35 < self.right_gobblets[i].position[0] < mouseX + 35 ):
                                #print("yay")
                                if not self.clicked and self.current_player == self.right_gobblets[i].player:
                                    #print("nos")
                                    self.right_gobblets[i].color = self.right_color
                                    #print(self.left_gobblets[i].color)
                                    if self.right_gobblets[i].under != None and self.right_gobblets[i].under.player != self.right_gobblets[i].player:
                                            temp = self.board.copy()
                                            self.board[self.right_gobblets[i].board_position] = self.right_gobblets[i].under                                       
                                            if self._check_for_winner() == self.right_gobblets[i].under.player:
                                                self.set_error("*Watchout black gobblet underneath")                                        
                                                self.board = temp.copy()
                                       
                                break        
                            else:
                                if self.left_gobblets[i].color == self.left_color or self.right_gobblets[i].color == self.right_color:
                                        #print("color")
                                        self.clicked = True
                                           
                    #print(self.clicked)   
                    if(100 < mouseX < 500 and mouseY < 400):
                            #print("d5lt")
                            for i in range(12):
                                if(self.current_player == 0):
                                    if (self.left_gobblets[i].is_on_top == True and self.left_gobblets[i].color == self.left_color and self.clicked):
                                        #print("d5lt2")
                                        clicked_row = mouseY // 100
                                        clicked_col = (mouseX-100) // 100
                                        #print(clicked_row,clicked_col)
                                        if (self.left_gobblets[i].position[1]//100 == clicked_row and (self.left_gobblets[i].position[0]-100)//100 == clicked_col):
                                            #print("Can't move in the same position")
                                            self.set_error("*Can't move in the same position")
                                        else:
                                            self.move_pos(clicked_row, clicked_col) 
                                            break
                                elif(self.current_player == 1):
                                    if (self.right_gobblets[i].is_on_top == True and self.right_gobblets[i].color == self.right_color and self.clicked):
                                        #print("d5lt3")
                                        clicked_row = mouseY // 100
                                        clicked_col = (mouseX-100) // 100
                                        #print(clicked_row,clicked_col)
                                        if (self.right_gobblets[i].position[1]//100 == clicked_row and (self.right_gobblets[i].position[0]-100)//100 == clicked_col):
                                            #print("Can't move in the same position")
                                            self.set_error("*Can't move in the same position")
                                        else:
                                            self.move_pos(clicked_row, clicked_col) 
                                        break

            self.screen.fill((173,216,230))
            for i in range(11, -1, -1):
                #print(self.left_gobblets[i].color)
                if(i % 4 == 3):
                    self.left_gobblets[i].draw(self.screen)
                    self.right_gobblets[i].draw(self.screen)
            for i in range(11, -1, -1):
                #print(self.left_gobblets[i].color)
                if(i % 4 == 2):
                    self.left_gobblets[i].draw(self.screen)
                    self.right_gobblets[i].draw(self.screen)
            for i in range(11, -1, -1):
                #print(self.left_gobblets[i].color)
                if(i % 4 == 1):
                    self.left_gobblets[i].draw(self.screen)
                    self.right_gobblets[i].draw(self.screen)
            for i in range(11, -1, -1):
                #print(self.left_gobblets[i].color)
                if(i % 4 == 0):
                    self.left_gobblets[i].draw(self.screen)
                    self.right_gobblets[i].draw(self.screen)
        
            for row in range(4):
                for col in range(4):
                    pygame.draw.rect(self.screen, (0, 0, 0), ((col+1) * 100, row * 100, 100, 100), 1)
                
             # Check if fade duration has elapsed
            if pygame.time.get_ticks() - self.fade_start_time >= self.fade_duration:
                self.error_txt.set_alpha(0)

            self.screen.blit(self.error_txt,(20,420))        
            self.screen.blit(self.text_surface, (180, 450))

            # Draw the pop-up window if needed
            if self.win_win:
                pygame.draw.rect(self.screen, (100, 100, 100), self.popup_rect)
                self.popup_screen.fill((0, 0, 0))
                self.popup_screen.blit(self.popup_message, self.popup_message_rect)
                pygame.draw.rect(self.popup_screen, (50, 50, 200), self.play_again_button)
                self.play_again_text = self.popup_font.render("Play Again", True, (255, 255, 255))
                self.play_again_text_rect = self.play_again_text.get_rect(center=self.play_again_button.center)
                self.popup_screen.blit(self.play_again_text, self.play_again_text_rect)
                self.screen.blit(self.popup_screen, self.popup_rect)
            
            pygame.display.flip()
            self.clock.tick(60)

# Instantiate the ChooseWindow class and run the game
if __name__ == "__main__":
    game = ChooseWindow()
    game.run()
