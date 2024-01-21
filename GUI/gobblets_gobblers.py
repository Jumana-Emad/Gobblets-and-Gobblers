import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
import os
from tkinter import messagebox
from tkinter import PhotoImage
import pygame
from pygame.locals import *

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

        print(f"Selected Game Mode: {mode}")

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
            self.root.destroy()
            game_details = GameDetails("pvp", text, text2, 0 , (0,0,0))
            new_window = Game(game_details)
            new_window.run()
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
        self.b1.grid(row= 1,column=1)
        self.b2.grid(row=1,column = 2) 
        
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
            self.level = "Easy"

        if a == 2:
            self.b2.config(background= "#f36523")
            self.b1.config(background="#13c3f4")
            self.level = "Hard"    

        if a == 3:
            self.b3.config(background= "#f36523")
            self.b4.config(background="#ffffff")
            self.color = (0,0,0)

        if a == 4:
            self.b4.config(background= "#f36523")
            self.b3.config(background="#000000")
            self.color = (255,255,255)
        
        print(self.level,self.color)        


    def new_window(self):
        text = self.e1.get()
        if text:
            self.root.destroy()
            game_details = GameDetails("pvc", text, "", self.level , self.color)
            new_window = Game(game_details)
            new_window.run()
        else:
            messagebox.showinfo("Name", "Enter Name First")

    def run(self):
        self.root.mainloop()

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
        self.visible = True
        self.radius = radius
        self.position = position
        self.under = None

    def draw(self, screen):
        if self.visible:
            pygame.draw.circle(screen, self.color, self.position, self.radius)

    def toggle_visibility(self):
        self.visible = not self.visible    

class Game:
    
    def __init__(self, game_details):
        self.game_details = game_details
        pygame.init()
        print(game_details.game_mode, game_details.player1_name , game_details.player2_name, game_details.player1_color, game_details.level)
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
        print(self.game_details.player1_color)
        self.nextTurn = self.game_details.player1_name if self.game_details.player1_color == (0,0,0) else self.game_details.player2_name
        self.text_color = self.left_color
        self.text_surface = self.pfont.render(self.nextTurn + "'s Turn", True, self.text_color)  # White color
        self.fade_start_time = 0
        self.fade_duration = 0 

    def on_button_click(self, row, col):
        index = 4 * row + col
        print(index)
        for i in range(12):
            if(self.current_player == 0):
                if self.left_gobblets[i].color == self.left_color:
                    if self.left_gobblets[i].board_position != None:
                        print("gwa el placedindex")
                        PlacedIndex = self.left_gobblets[i].board_position
                        if(self.left_gobblets[i].under != None):
                            print("gwa el placedindex under")
                            self.board[PlacedIndex] = self.left_gobblets[i].under
                        else:
                            print("gwa el placedindex else")
                            print(PlacedIndex)
                            self.board[PlacedIndex] = " "
                
                    print(index)
                    print(self.board[index])
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
                        self.set_error("*Can't gobble a bigger Gobblet")
                        # self.error = "*Can't gobble a bigger Gobblet"
                        # # Set up timing variables
                        # self.fade_start_time = pygame.time.get_ticks()
                        # self.fade_duration = 2000  # 2 seconds
                        # print(self.error)
                        # self.error_txt = self.efont.render(self.error , True, (255,0,0))  # red color
                        # self.error_txt.set_alpha(255)
                         

                            
            else:                    
                if self.right_gobblets[i].color == self.right_color:
                    if self.right_gobblets[i].board_position != None:
                        print("gwa el placedindex")
                        PlacedIndex = self.right_gobblets[i].board_position
                        if(self.right_gobblets[i].under != None):
                            print("gwa el placedindex under")
                            self.board[PlacedIndex] = self.right_gobblets[i].under
                        else:
                            print("gwa el placedindex else")
                            print(PlacedIndex)
                            self.board[PlacedIndex] = " "
                            
                    print(self.board[index])
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
                        self.set_error("*Can't gobble a bigger Gobblet")

    def set_error(self,error):
            self.error = error
            print(self.error)
            # Set up timing variables
            self.fade_start_time = pygame.time.get_ticks()
            self.fade_duration = 2000  # 2 seconds
            self.error_txt = self.efont.render(self.error , True, (255,0,0))  # red color
            self.error_txt.set_alpha(255)
    
    def check_winner(self):
        for i in range(3):
            if self.board[i * 3] == self.board[i * 3 + 1] == self.board[i * 3 + 2] != " ":
                return True  # Row
            if self.board[i] == self.board[i + 3] == self.board[i + 6] != " ":
                return True  # Column

        if self.board[0] == self.board[4] == self.board[8] != " ":
            return True  # Diagonal
        if self.board[2] == self.board[4] == self.board[6] != " ":
            return True  # Diagonal

        return False

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

    def reset_game(self):
        self.current_player = "X"
        self.board = [" " for _ in range(16)]
    # Main game loop
   # running = True
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

    def run(self):
       
        self.generate_gobblets()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    ChooseWindow().run()
                    quit()
                elif event.type == MOUSEBUTTONDOWN:
                    mouseX, mouseY = event.pos
                    print(event.pos)
                    print(self.clicked)
                    for i in range(12):
                        if(self.current_player == 0 and self.left_gobblets[i].color == self.left_color):
                            self.clicked = True
                        elif (self.current_player == 1 and self.right_gobblets[i].color == self.right_color):
                            self.clicked = True
                    for i in range(12):            
                            if (self.current_player == 0 and self.left_gobblets[i].is_on_top == True and  mouseY - 40 < self.left_gobblets[i].position[1] < mouseY + 40 and mouseX - 35 < self.left_gobblets[i].position[0] < mouseX + 35 ):
                                print("yay")
                                if not self.clicked and self.current_player == self.left_gobblets[i].player:
                                    print("fo2")
                                    # self.left_gobblets[i].color = (0,0,255)
                                    self.left_gobblets[i].color = self.left_color
                                    #print(self.left_gobblets[i].color)
                                break
                            elif(self.current_player == 1 and self.right_gobblets[i].is_on_top == True and  mouseY - 40 < self.right_gobblets[i].position[1] < mouseY + 40 and mouseX - 35 < self.right_gobblets[i].position[0] < mouseX + 35 ):
                                #print("yay")
                                if not self.clicked and self.current_player == self.right_gobblets[i].player:
                                    print("nos")
                                    self.right_gobblets[i].color = self.right_color
                                    #print(self.left_gobblets[i].color)
                                break        
                            else:
                                if self.left_gobblets[i].color == self.left_color or self.right_gobblets[i].color == self.right_color:
                                        print("color")
                                        self.clicked = True
                                           
                    print(self.clicked)   
                    if(100 < mouseX < 500 and mouseY < 400):
                            print("d5lt")
                            for i in range(12):
                                if(self.current_player == 0):
                                    if (self.left_gobblets[i].is_on_top == True and self.left_gobblets[i].color == self.left_color and self.clicked):
                                        print("d5lt2")
                                        clicked_row = mouseY // 100
                                        clicked_col = (mouseX-100) // 100
                                        print(clicked_row,clicked_col)
                                        if (self.left_gobblets[i].position[1]//100 == clicked_row and (self.left_gobblets[i].position[0]-100)//100 == clicked_col):
                                            print("Can't move in the same position")
                                            self.set_error("*Can't move in the same position")
                                        else:
                                            self.on_button_click(clicked_row, clicked_col) 
                                            break
                                elif(self.current_player == 1):
                                    if (self.right_gobblets[i].is_on_top == True and self.right_gobblets[i].color == self.right_color and self.clicked):
                                        print("d5lt3")
                                        clicked_row = mouseY // 100
                                        clicked_col = (mouseX-100) // 100
                                        print(clicked_row,clicked_col)
                                        self.on_button_click(clicked_row, clicked_col) 
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
                    # text = self.font.render(self.board[row * 4 + col], True, (0, 0, 0))
                    # self.screen.blit(text, ((col+1) * 100 + 30, row * 100 + 20))
             # Check if fade duration has elapsed
            if pygame.time.get_ticks() - self.fade_start_time >= self.fade_duration:
                self.error_txt.set_alpha(0)

            self.screen.blit(self.error_txt,(20,420))        
            self.screen.blit(self.text_surface, (180, 450))
            pygame.display.flip()
            self.clock.tick(60)

# Instantiate the ChooseWindow class and run the game
if __name__ == "__main__":
    game = ChooseWindow()
    game.run()
