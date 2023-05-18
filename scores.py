import os
import csv
import menu
from art import text2art
from colorama import Fore, Style
from play import max_score

# Hero Text for Rules Section
scores_hero_art = text2art("Scores")

# Header text
scores_header = (f"         Only one {Fore.MAGENTA}worm{Fore.WHITE} has"
                 f"{Fore.YELLOW} Evolved...{Fore.WHITE}")

# Calc 2nd and 3rd scores for highscores list
second_score = (max_score // 8)
third_score = (max_score // 16)

# Default Scores to beat
high_scores = {
    'Greg': max_score,
    'Jake': second_score,
    'Lachlan': third_score
    }


def scores_hero():
    print(scores_hero_art)
    print(menu.line_break)
    print(scores_header)
    print(menu.line_break)


# Default scores list taken from high_scores dictionary
def scores_list():
    print('')
    # Looping individual key-value pairs to print high-scores.
    for k, v in high_scores.items():
        print(f"      {k} has eaten {Fore.YELLOW}{v}{Fore.WHITE} "
              "Gold Nuggets\n")

    print(f'            {Style.DIM}(Each worms TOP Score){Style.NORMAL}')


# Receives score from play.py and update highscores accordingly - print to csv
def update_highscores(player_score):
    file_loc = "app-user-scores.csv"
    if not os.path.exists(file_loc):
        with open(file_loc, 'w') as f:
            writer = csv.writer(f)
            # Create new file
            writer.writerow(["name", "score"])
            writer.writerow([menu.name, player_score])
    else:
        with open(file_loc, 'a') as f:
            writer = csv.writer(f)
            writer.writerow([menu.name, player_score])

    global high_scores
    for v in high_scores.values():
        if player_score >= v:
            # Create new k:v pair and insert into dictionary
            high_scores[menu.name] = player_score
            # Sorts high scores based on score value
            sorted_highscores = sorted(
                high_scores.items(), key=lambda item: item[1], reverse=True
                )
            if len(sorted_highscores) > 3:
                # Removes smallest tuple from high scores
                sorted_highscores.pop(-1)
            # high_scores is now a dictionary from the sorted_highscores tuples
            # allowing the above for loop to work next time the function
            # update_highscores() is called.
            high_scores = dict(sorted_highscores)
            break


def scores_prompt():
    print(menu.line_break)
    print('  1. Menu')
    print(menu.line_break)


def scores_input():
    scores_nav = str(input(' > '))
    match scores_nav:
        case "1" | "Menu" | "menu":
            os.system('cls' if os.name == 'nt' else 'clear')
            menu.main_menu()
        # Error Handling
        case _:
            print(menu.line_break)
            print(f" Please enter a valid input:  "
                  f"{Style.DIM}('1' or 'Menu'){Style.NORMAL}")
            print(menu.line_break)
            scores_input()


def print_scores():
    scores_hero()
    scores_list()
    scores_prompt()
    scores_input()
