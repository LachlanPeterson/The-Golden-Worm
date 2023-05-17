from art import text2art
from colorama import Fore
import os 
import menu
import csv
from collections import OrderedDict
from play import max_score, score


# Hero Text for Rules Section
scores_hero_art = text2art("Scores")

# Header text
scores_header = (f"         Only one {Fore.MAGENTA}worm{Fore.WHITE} has{Fore.YELLOW} Evolved...{Fore.WHITE}")

# Calc 2nd and 3rd scores for highscores list
second_score = 2 # (max_score // 8)
third_score = 1 # (max_score // 16)

# Create dictionaries for inital scores
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

def scores_list():
    # Print individual scores
    print('')
    # Looping individual key-value pairs to print high-scores.
    for k, v in high_scores.items():
        print(f"      {k} has eaten {v} Gold Nuggets\n")

    
# Receives score from play.py and update highscores accordingly   
def update_highscores(player_score):

    with open('app-user-scores.csv', 'a') as f:
        writer = csv.writer(f)
        # # WANT TO PRINT name, score above inputs
        # if not os.path.isfile('./app-user-scores.csv'):
        #     writer.writerow(["name","score"])
        writer.writerow([menu.name,player_score])


    global high_scores
    for v in high_scores.values():
        if player_score >= v:
            # Create new k:v pair and insert into dictionary
            high_scores[menu.name] = player_score
            
            # Sorts high scores based on score value
            sorted_highscores = sorted(high_scores.items(),key=lambda item: item[1],reverse=True)
            if len(sorted_highscores) > 3:
                # Removes smallest tuple from high scores
                sorted_highscores.pop(-1)
            high_scores = dict(sorted_highscores)
            break


def scores_prompt():
    print(menu.line_break)
    scores_footer = "Will you take the Golden Challenge? (Yes or No)"
    scores_nav = scores_footer.center(44)
    print(scores_nav)
    print(menu.line_break)

def scores_input():
    scores_nav = input(' > ')
    match scores_nav:
        case "Yes" | "yes":
            os.system('cls' if os.name == 'nt' else 'clear')
            menu.main_menu()
        case "No" | "no":
            print(menu.line_break)
            believe_prompt = "I believe in you!"
            read_believe = believe_prompt.center(44)
            print(read_believe)
            print(menu.line_break)
            scores_input()
        case _:
            print('other error')
            
def print_scores():
    scores_hero()
    scores_list()
    scores_prompt()
    scores_input()
