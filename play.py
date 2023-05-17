import os
import menu
from pytimedinput import timedInput
from random import randint
from colorama import Fore
 
# Set Board size
board_width = 32
board_height = 15

# Play Area
play_area = (board_width - 2)*(board_height - 2)

# Board positions based off size, no. of rows is determined by height and vice versa.
board = [(row, column) for row in range(board_height) for column in range(board_width)]

# Worm
worm = [(board_height//2,6),(board_height//2,5),(board_height//2,4)]
movement = {'up': (-1,0), 'left': (0,-1), 'down': (1,0), 'right': (0,1)}
auto_move = movement['right']
# Worm auto direction = right, so I call the key from above dict to get the value.

# Game Over
game_over = False

# Set Score and max score
score = 0
max_score = play_area -len(worm)

# Gold Nuggets
def generate_gold_position():
    global gold_position
    gold_position = (randint(1, board_height - 2)), (randint(1, board_width -2))
    # Regenerating gold position if its in worm 
    if gold_position in worm:
        generate_gold_position()

# Print board function
def print_board():
    for position in board:
        # Printing snake position
        if position == worm[0]:
            print(Fore.MAGENTA + '0', end = '')
        elif position in worm[1:]:
            print(Fore.MAGENTA + 'o', end = '')
        # if position of row is a value of 0 or (board_height -1), or position of column is 0 or (board_height -1) then print border '#'
        elif position[0] in (0, board_height - 1) or position[1] in (0, board_width - 1):
            # printing border, need end as default is \n
            print(Fore.GREEN + '@', end = '')
        # Checking if cell is equal to gold position
        elif position == gold_position:
            print(Fore.YELLOW + 'G', end = '')
        else:
            # printing board space
            print(' ', end = '')
        
        # Starting new line once you reach right column. 
        if position[1] == board_width -1:
            # Defaults new line.
            print('')

def worm_movement():
    # Referencing global score variable
    global score
    global max_score
    global game_over
    # Worm head = first tuple in worm, so to move worm we are adding a new head = direciton + old head, then removing tail(last tuple).
    update_worm = worm[0][0] + auto_move[0], worm[0][1] + auto_move[1]
    # Inserting new head as first tuple in worm, meaning I have 4 tuples.
    worm.insert(0,update_worm)
    # You can see there are now 4 tuples with print(worm), so you need to pop last tuple in list.

    # If worm eats gold, body grows and new gold is generated. 
    if worm[0] == gold_position:
        score += 1
        if score == max_score:
            # End game
            game_over = True
            print('You won and turned gold!')
        else:    
            generate_gold_position()
    # If worm head is in: Itself, or the borders: Left&Right, Top&Bottom
    elif worm[0] in worm[1:] or worm[0][0] in (0, board_height - 1) or worm[0][1] in (0, board_width - 1):
        worm_die()
         
    else:
        worm.pop(-1)
        # If you print(worm) there are 3 tuples.

def worm_die():
    global game_over
    game_over = True
    print(f'You ate {score} Golden Nuggets!')
    game_nav = input('Press 1 to retry, press 2 for menu: ')
    match game_nav:
        case '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            game_play()
        case '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            menu.main_menu()


def game_reset():
    # Resetting game.
    global score
    global game_over
    global worm
    global auto_move
    
    score = 0
    game_over = False
    worm = [(board_height//2,6),(board_height//2,5),(board_height//2,4)]
    auto_move = movement['right']



def game_play():
    global auto_move
    
    # Reset Game
    game_reset()

    # Generate initial gold position
    generate_gold_position()

    # While game is game over is False (game is playing) run:
    while game_over == False:
        # Reprint board, giving impression of movement
        os.system('cls' if os.name == 'nt' else 'clear')

        # Print Score
        print(f'{Fore.WHITE}Score: {Fore.YELLOW}{ score}')

        # Print Board, worm, gold and border
        print_board()
        
        # Player input for worm movement
        player_input,_ = timedInput(Fore.WHITE +'Press Movement Keys: ', timeout = 0.2)
        match player_input:
            case 'w' | 'W':
                auto_move = movement['up']
            case 'a' | 'A':
                auto_move = movement['left']
            case 's' | 'S':
                auto_move = movement['down']
            case 'd' | 'D':
                auto_move = movement['right']
            
        # Updating new worm position after user input before game reprint 
        worm_movement()
