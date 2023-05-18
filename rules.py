from art import text2art
from colorama import Fore, Style
import os
import menu

# Hero Text for Rules Section
rules_hero_art = text2art("Rules")

# Header text
rules_header = (f"          {Fore.YELLOW}Golden {Fore.WHITE}rules of "
                f"the {Fore.GREEN}Garden{Fore.WHITE}")


def rules_hero():
    print(rules_hero_art)
    print(menu.line_break)
    print(rules_header)
    print(menu.line_break)


def rules_list():
    # Rule 1
    print(f" {Fore.YELLOW}1. {Fore.WHITE}Movement is controlled by "
          "W,A,S,D Keys:\n    W = Left, A = Right, S = Up, D = Down\n")
    # Rule 2
    print(f" {Fore.YELLOW}2. {Fore.WHITE}Don't try to leave the {Fore.GREEN}"
          f"Garden{Fore.WHITE} or run\n    into your body... "
          f"you will {Fore.RED}die!\n")
    # Rule 3
    print(f" {Fore.YELLOW}3. {Fore.WHITE}On a positive{Fore.WHITE} note, "
          f"eating {Fore.YELLOW}Gold{Fore.WHITE} will\n    make you grow and "
          "add to your score.\n")
    # Rule 4
    print(f" {Fore.YELLOW}4. {Fore.WHITE}If you manage to eat enough"
          f"{Fore.YELLOW} Gold{Fore.WHITE} and\n    you can no longer grow in "
          f"the garden...\n\n    You will evolve from a {Fore.MAGENTA}Regular "
          f"Worm{Fore.WHITE} to\n    a Glamorous {Fore.YELLOW}Golden Worm"
          f"{Fore.WHITE} like me!")


def rules_prompt():
    print(menu.line_break)
    rules_footer = "Do you understand the rules?"
    rules_nav = rules_footer.center(46)
    print(rules_nav)
    print(menu.line_break)


def rules_input():
    rules_nav = input(' > ')
    match rules_nav:
        case "Yes" | "yes":
            os.system('cls' if os.name == 'nt' else 'clear')
            menu.main_menu()
        case "No" | "no":
            print(menu.line_break)
            no_prompt = "Have another read, you'll get it!"
            read_again = no_prompt.center(46)
            print(read_again)
            print(menu.line_break)
            rules_input()
        # Error Handling
        case _:
            print(menu.line_break)
            print(f" Please enter a valid input:  {Style.DIM}('Yes' or 'No')"
                  f"{Style.NORMAL}")
            print(menu.line_break)
            rules_input()


def print_rules():
    rules_hero()
    rules_list()
    rules_prompt()
    rules_input()
