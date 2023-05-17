from art import text2art
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True) 
import os 
import menu

# VARIABLES

# Hero Text for Rules Section
scores_hero_art = text2art("Scores")

line_break = ('+--------------------------------------------+')

# Header text
scores_header = (f"         Only one {Fore.MAGENTA}worm{Fore.WHITE} has{Fore.YELLOW} Evolved...")


def scores_hero():
    print(scores_hero_art)
    print(line_break)
    print(scores_header)
    print(line_break)



def scores_prompt():
    print(line_break)
    scores_footer = "Will you take the Golden Challenge? (Yes or No)"
    scores_nav = scores_footer.center(44)
    print(scores_nav)
    print(line_break)

def scores_input():
    scores_nav = input(' > ')
    match scores_nav:
        case "Yes" | "yes":
            os.system('cls' if os.name == 'nt' else 'clear')
            menu.main_menu()
        case "No" | "no":
            print(line_break)
            believe_prompt = "I believe in you!"
            read_believe = believe_prompt.center(44)
            print(read_believe)
            print(line_break)
            scores_input()
        case _:
            print('other error')
            
    
def print_scores():
    scores_hero()
    # scores_list()
    scores_prompt()
    scores_input()



