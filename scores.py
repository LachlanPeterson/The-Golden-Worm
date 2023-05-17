from art import text2art
from colorama import Fore
import os 
import menu
from play import max_score


# Hero Text for Rules Section
scores_hero_art = text2art("Scores")

# Header text
scores_header = (f"         Only one {Fore.MAGENTA}worm{Fore.WHITE} has{Fore.YELLOW} Evolved...{Fore.WHITE}")


def scores_hero():
    print(scores_hero_art)
    print(menu.line_break)
    print(scores_header)
    print(menu.line_break)

def scores_list():

    # Calc 2nd and 3rd scores
    second_score = (max_score // 8)
    third_score = (max_score // 16)

    # Create dictionaries for inital scores
    high_scores = [
        {'name': 'Greg', 'score': max_score},
        {'name': 'Jake', 'score': second_score},
        {'name': 'Lachlan', 'score': third_score}
    ]
    # Print individual scores

    print('')
    for placement in high_scores:
        print(f"      {placement['name']} has eaten {placement['score']} Gold Nuggets\n")


    




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
