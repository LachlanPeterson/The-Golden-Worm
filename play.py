import os
import menu
import scores
from random import randint
from pytimedinput import timedInput
from colorama import Fore, Style

# Set Board size
board_width = 32
board_height = 15

# Play Area
play_area = (board_width - 2)*(board_height - 2)

# Board positions based off size
board = [
    (row, col) for row in range(board_height) for col in range(board_width)
    ]

# Worm
worm = [(board_height//2, 6), (board_height//2, 5), (board_height//2, 4)]
movement = {'up': (-1, 0), 'left': (0, -1), 'down': (1, 0), 'right': (0, 1)}
auto_move = movement['right']
# Worm auto direction = right, so I call the key from above dict to get value.

# Game Over
game_over = False

# Set Score and max score
score = 0
max_score = play_area - len(worm)


# Gold Nuggets
def generate_gold_position():
    global gold_position
    gold_position = ((randint(1, board_height - 2)),
                     (randint(1, board_width - 2)))

    # Regenerating gold position if its in worm
    if gold_position in worm:
        generate_gold_position()


# Print board function
def print_board():
    global gold_position
    for position in board:
        # Printing snake position
        if position == worm[0]:
            print(Fore.MAGENTA + '0', end='')
        elif position in worm[1:]:
            print(Fore.MAGENTA + 'o', end='')
        # If position of row is a value of 0 or (board_height -1),
        # or position of col is 0 or (board_height -1) then print border '#'
        elif (position[0] in (0, board_height - 1) or
              position[1] in (0, board_width - 1)):
            # printing border, need end as default is \n
            print(Fore.GREEN + '@', end='')
        # Checking if cell is equal to gold position
        elif position == gold_position:
            print(Fore.YELLOW + 'G', end='')
        else:
            # printing board space
            print(' ', end='')
        # Starting new line once you reach right col.
        if position[1] == board_width - 1:
            # Defaults new line.
            print('')


def worm_movement():
    global score
    global max_score
    global game_over
    global gold_position
    # Worm head = first tuple in worm, so to move worm we are adding
    # a new head = direciton + old head, then removing tail(last tuple).
    update_worm = worm[0][0] + auto_move[0], worm[0][1] + auto_move[1]
    # Inserting new head as first tuple in worm, meaning I have 4 tuples.
    worm.insert(0, update_worm)

    # If worm eats gold, body grows and new gold is generated.
    if worm[0] == gold_position:
        score += 1
        if score == max_score:
            # End game
            game_over = True
            worm_win()
        else:
            generate_gold_position()
    # If worm head is in: Itself, or the borders: Left & Right, Top & Bottom.
    elif (worm[0] in worm[1:] or worm[0][0] in (0, board_height - 1) or
          worm[0][1] in (0, board_width - 1)):
        worm_die()
    else:
        worm.pop(-1)


def worm_die():
    global game_over
    game_over = True

    # Passing score variable to scores module
    scores.update_highscores(score)

    # Death screen
    os.system('cls' if os.name == 'nt' else 'clear')
    print(menu.worm_death)
    print(menu.line_break)
    print(f'         You ate {Fore.YELLOW}{score}{Fore.WHITE} Golden Nuggets!')
    print(menu.line_break)
    print('  1. Retry')
    print('  2. Menu')
    print(menu.line_break)
    worm_die_input()


def worm_die_input():
    # Post death navigation
    game_nav = str(input(' > '))
    match game_nav:
        case '1' | 'Retry' | 'retry':
            os.system('cls' if os.name == 'nt' else 'clear')
            game_play()
        case '2' | 'Menu' | 'menu':
            os.system('cls' if os.name == 'nt' else 'clear')
            menu.main_menu()
        # Error Handling
        case _:
            print(menu.line_break)
            print(f" Please enter a valid input from the Menu:\n "
                  f"{Style.DIM}(Retry: '1' or 'Retry')\n "
                  f"(Menu: '2' or 'Menu'){Style.NORMAL}")
            print(menu.line_break)
            worm_die_input()


def worm_win():
    global game_over
    game_over = True

    # Passing score variable to scores module
    scores.update_highscores(score)

    # Win screen
    os.system('cls' if os.name == 'nt' else 'clear')
    print(menu.worm_win)
    print(menu.line_break)
    print(f'         You ate ALL {Fore.YELLOW}{score}{Fore.WHITE} '
          'Golden Nuggets!')
    print(menu.line_break)
    print(f" *{Fore.YELLOW}Greg{Fore.WHITE} rushes over to congratulate you*"
          f"\n\n I knew you could do it {Fore.YELLOW}{menu.name}{Fore.WHITE},"
          f" I believed \n in you as soon as you came to my {Fore.GREEN}Garden"
          f"{Fore.WHITE}.\n To think another worm evolved... how grand!\n")
    print(f" Well, there's not much left for you here my\n friend. I'll send"
          f" you on your way. Make sure\n to tell other {Fore.MAGENTA}"
          f"worms{Fore.WHITE} about my {Fore.GREEN}Garden!{Fore.WHITE} ")
    print(menu.line_break)
    print(f'  1. Leave the Garden')
    print(menu.line_break)
    worm_win_input()


def worm_win_input():
    # Post death navigation
    game_nav = str(input(' > '))
    match game_nav:
        case '1' | 'Leave' | 'leave':
            os.system('cls' if os.name == 'nt' else 'clear')
            # Goes to initial menu where user inputs name for Game Lore reasons
            menu.initial_menu()
        # Error Handling
        case _:
            print(menu.line_break)
            print(f" You decided to leave the {Fore.GREEN}Garden{Fore.WHITE} "
                  f"after\n thanking {Fore.YELLOW}Greg{Fore.WHITE} for all his"
                  f" help:\n {Style.DIM}('1' or 'Leave'){Style.NORMAL}")
            print(menu.line_break)
            worm_win_input()


# Resetting game
def game_reset():
    global score
    global game_over
    global worm
    global auto_move
    global gold_position
    score = 0
    game_over = False
    worm = [(board_height//2, 6), (board_height//2, 5), (board_height//2, 4)]
    auto_move = movement['right']
    generate_gold_position()


def game_play():
    global auto_move

    # Reset Game
    game_reset()

    # While game is game over is False (game is playing) run:
    while not game_over:
        # Reprint board, giving impression of movement
        os.system('cls' if os.name == 'nt' else 'clear')

        # Print Score
        print(f'{Fore.WHITE}Score: {Fore.YELLOW}{ score}')

        # Print Board, worm, gold and border
        print_board()

        # Player input for worm movement and timer between inputs
        player_input, _ = timedInput(
            Fore.WHITE + 'Press Movement Keys: ', timeout=0.2)
        # This timeout determines speed of game, increase to make slower
        match player_input:
            case 'w' | 'W':
                auto_move = movement['up']
            case 'a' | 'A':
                auto_move = movement['left']
            case 's' | 'S':
                auto_move = movement['down']
            case 'd' | 'D':
                auto_move = movement['right']
            # Errors handled as no invalid keys update worm.
            case _:
                pass

        # Updating new worm position after user input before game reprint
        worm_movement()
