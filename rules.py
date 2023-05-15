from art import text2art
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True) 
from menu import menu_break

# Hero Text for Rules Section
rules_hero_art = text2art("Rules")

# Header text
rules_hero_text = (f"        {Fore.YELLOW}Golden {Fore.WHITE}rules of the soil patch")
# Tried to center the above function with colour but couldn't.
# rules_txt = "Rules of the soil patch!"
# rules_header = rules_txt.center(44)

def rules_hero():
    print(rules_hero_art)
    print(menu_break)
    print(rules_hero_text)
    print(menu_break)

def rules_list():
    # Rule 1
    print(f" {Fore.YELLOW}1. {Fore.WHITE}Movement is controlled by W,A,S,D Keys:\n    W = Left, A = Right, S = Up, D = Down\n")
   
    # Rule 2
    print(f" {Fore.YELLOW}2. {Fore.WHITE}Don't try to leave the soil patch or run\n    into your body... you will {Fore.RED}die!\n")

     # Rule 3
    print(f" {Fore.YELLOW}3. {Fore.WHITE}On a {Fore.GREEN}positive{Fore.WHITE} note, eating {Fore.YELLOW}Gold{Fore.WHITE} will\n    make you grow and add to your score.\n")

    # Rule 4
    print(f" {Fore.YELLOW}4. {Fore.WHITE}If you manage to eat enough{Fore.YELLOW} Gold{Fore.WHITE} and\n    you can no longer grow in my patch...\n\n    You will evolve from a {Fore.MAGENTA}Regular Worm{Fore.WHITE} to\n    a{Fore.YELLOW} Glamorous Golden Worm{Fore.WHITE} like me!")

def rules_input():
    pass


def print_rules():
    rules_hero()
    rules_list()
    print(menu_break)

# print_rules()





