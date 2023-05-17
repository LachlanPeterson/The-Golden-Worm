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
scores_header = (f"        *FILLER*{Fore.YELLOW}Golden {Fore.WHITE}rules of the soil patch")


def scores_hero():
    print(scores_hero_art)
    print(line_break)
    print(scores_header)
    print(line_break)

# def rules_list():
#     # Rule 1
#     print(f" {Fore.YELLOW}1. {Fore.WHITE}Movement is controlled by W,A,S,D Keys:\n    W = Left, A = Right, S = Up, D = Down\n")
   
#     # Rule 2
#     print(f" {Fore.YELLOW}2. {Fore.WHITE}Don't try to leave the soil patch or run\n    into your body... you will {Fore.RED}die!\n")

#      # Rule 3
#     print(f" {Fore.YELLOW}3. {Fore.WHITE}On a {Fore.GREEN}positive{Fore.WHITE} note, eating {Fore.YELLOW}Gold{Fore.WHITE} will\n    make you grow and add to your score.\n")

#     # Rule 4
#     print(f" {Fore.YELLOW}4. {Fore.WHITE}If you manage to eat enough{Fore.YELLOW} Gold{Fore.WHITE} and\n    you can no longer grow in my patch...\n\n    You will evolve from a {Fore.MAGENTA}Regular Worm{Fore.WHITE} to\n    a{Fore.YELLOW} Glamorous Golden Worm{Fore.WHITE} like me!")

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
            
    
def print_scores():
    scores_hero()
    # scores_list()
    scores_prompt()
    scores_input()



