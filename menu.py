from art import text2art
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True) 


def print_menu():
    hero()
    introduction()
    main_menu()

# Print Hero Art and Welcome Message
def hero():
    print(worm_art)
    print(menu_break)
    print(intro_text)
    print(menu_break)

# Introduction with Greg, prompt user for name and greets them before introducing the menu.
def introduction():
    # Introduction with Greg
    print(f" Hello, I am {Fore.YELLOW}Greg {Fore.WHITE}the Great Golden Worm! \n")
    print(" I haven't seen you around this soil patch...") 

    # User prompt for name input
    name = input(" Tell me, what's your name child? ")
    #  Prints name and greeting
    print (f"\n {Fore.MAGENTA + name}{Fore.WHITE}, what a splendid name for a worm! \n Welcome to my special soil patch filled \n with {Fore.YELLOW}GOLD.\n") 

    # Menu Introduction and input
    print(f" What would you like to do now {Fore.MAGENTA + name}?")

# Prints Navigation Menu
def main_menu():
    print(menu_break)
    print('  1. Play')
    print('  2. Rules')
    print('  3. Scores')
    print('  4. Exit')
    print(menu_break)
    


# about_title = text2art("about")
    # print(about_title)
# title = text2art("G Worm")

intro_text = (f"          {Fore.MAGENTA}WELCOME TO THE {Fore.YELLOW}GOLDEN{Fore.MAGENTA} WORM")  #Spaces to center intro within menu break

menu_break = ('+--------------------------------------------+')


# Couldn't find a library that contained a worm art
# Therefore I converted the exact function to a string value for the variable worm_art
worm_art = str(rf"""{Fore.YELLOW}
                                 (o)(o)
                                /     \
                               /       |
                              /   \  * |
                ________     /    /\__/
        _      /        \   /    /
       / \    /  ____    \_/    /
      //\ \  /  /    \         /
      V  \ \/  /      \       /
          \___/        \_____/
""")
               





