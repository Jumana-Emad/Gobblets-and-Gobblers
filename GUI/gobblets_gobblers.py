import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
import os
from tkinter import messagebox
from tkinter import PhotoImage

class ChooseWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Goblets and Gabblers")
        self.root.resizable(False, False) 
        self.gameMode = "pvp"
        self.root.configure(bg='#ADD8E6') 
        '''
        # Load an image
        self.image = ImageTk.PhotoImage(Image.open("intro.jpeg").resize((730,300)))
        
        # Display the image using a Label
        self.image_label = tk.Label(self.root, image=self.image)
        self.image_label.pack(pady=10)
'''
        # Create a canvas widget to draw on
        canvas = Canvas(self.root, width=730, height=280, background="#ADD8E6")
        canvas.pack()

        # Draw the gobblet
        canvas.create_oval(230, 50, 400, 220, fill="#f36523", outline="#f36523")

        # Draw the text "Gobblet"
        canvas.create_text(230, 110, text="Gobblet", fill="#FFFFFF", font=("Arial", 60))

        # Draw the text "Gobbler's"
        canvas.create_text(430, 200, text="Gobbler's", fill="#FFFFFF", font=("Arial", 40))
        
        self.buttons = [ tk.Button(self.root, text="Player vs Player", font=('normal', 20),background= "#13c3f4" ,activebackground= "#f36523",width=50, height=5, command=lambda: self.set_game_mode("pvp"),),
            tk.Button(self.root, text="Player vs Computer", font=('normal', 20),background= "#13c3f4",activebackground= "#f36523", width=50, height=5, command=lambda: self.set_game_mode("pvc"))
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
    def new_window(self,  _class):
        new_window = _class()
        new_window.run()

    def run(self):
        self.root.mainloop()

class PlayervsPlayer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Player vs Player")  
        self.root.resizable(False, False) 
        self.gameMode = "pvp"
        self.root.configure(bg='#ADD8E6') 
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

        b1 = tk.Button(self.root, text="Start Game", font=('normal', 18), background="#13c3f4", activebackground="#f36523", width=15, height=3)
        b1.grid(row=3, column=2, pady=10)  


    def new_window(self,  _class):
        if self.e1.get() and self.e2.get():
            self.root.destroy()
            new_window = _class()
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
        self.gameMode = "pvc"
        self.color ="Black"
        self.level = "Easy"
        self.selColor = "#f36523"
        self.selLevel = ""
        self.root.configure(bg='#ADD8E6') 

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

        self.b5 = tk.Button(self.root, text="Start Game", font=('normal', 18), background="#13c3f4", activebackground="#f36523", width=15, height=3,)
        self.b5.grid(row=3, column=1, pady=10)  

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
            self.color = "Black"

        if a == 4:
            self.b4.config(background= "#f36523")
            self.b3.config(background="#000000")
            self.color = "White"
        
        print(self.level,self.color)        


    
    
    def new_window(self,  _class):

        if self.e1.get():
            self.root.destroy()
            new_window = _class()
            new_window.run()
        else:
            messagebox.showinfo("Name", "Enter Name First")

    def run(self):
        self.root.mainloop()
        

# Instantiate the TicTacToe class and run the game
if __name__ == "__main__":
    game = ChooseWindow()
    game.run()
