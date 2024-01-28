from Gobblet_Game import Game
from smart_Bot import *

while True:
    game = Game()
    winner = None
    print('Let the games begin!')

    # create players
    players = []
    txt = f'Enter your name'
    name = input(txt)
    players.append(Human(0, name, game))
    txt = f'Enter 1 for Easy difficulty, 2 for Medium, 3 for Hard'
    difficulty = input(txt)
    if difficulty == '1':
        players.append(Easy_Bot(1, 'Bot', game))
    elif difficulty == '2':
        players.append(Medium_Bot(1, 'Bot', game))
    elif difficulty == '3':
        players.append(Hard_Bot(1, 'Bot', game))
         
    i = 0
    # start a match
    while winner is None:
        # select gobbler
        current_player = players[game.current_player_idx]
        print(game.Draw_board())
        # if game.current_player_idx == 1:
        #     current_player.play()
        while winner is None:
            if i == 1:
                brpt = 0
            selected_gobbler_size = current_player.select_gobbler()
            success = game.select_gobbler_object(selected_gobbler_size)
            if success:
                print(f'{current_player.repr} selects gobbler {selected_gobbler_size}.')
                break
            else:
                print(('Try again!'))
                


        # play gobbler
        # print(game.Draw_board())
        while winner is None:

            board_position = current_player.select_board_position()

            i+=1
            success, winner = game.select_gobbler_position(board_position, selected_gobbler_size)
            if success:
                print(f'{current_player.repr} moves gobbler {selected_gobbler_size} to {board_position}.')
                break
            else:
                print('Try again!')

    # announce winner
    print(game.Draw_board())
    winner = players[winner]
    print(f'{winner.repr} has won!')

    # play again?
    play_again = input('Play again? (y/n): ')
    if play_again != 'y':
        break

print('Thank you for playing.')

