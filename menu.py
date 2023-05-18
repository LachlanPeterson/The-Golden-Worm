from colorama import Fore, Style
import os
import rules
import scores
import play

line_break = ('+--------------------------------------------+')
menu_header = (f"          WELCOME TO THE {Fore.YELLOW}GOLDEN{Fore.MAGENTA} WORM{Fore.WHITE}")  #Spaces to center intro within menu break

# Print Hero Art and Welcome Message
def menu_hero():
    print(greg)
    print(line_break)
    print(menu_header)
    print(line_break)

# Introduction with Greg, prompt user for name and greets them before introducing the menu.
def introduction():
    # Introduction with Greg
    print(f" Hello, I am {Fore.YELLOW}Greg {Fore.WHITE}the Great Golden Worm! \n")
    print(f" I haven't seen you around my {Fore.GREEN}Garden.{Fore.WHITE}") 

def user_name():
    # User prompt for name input
    global name
    # Error Handling for inputs to be letters (no symbols or numbers)
    while True:
        name = input(" Tell me, what's your name little worm?\n\n > ")
        if name.isalpha():
            #  Prints name and greeting
            print (f"\n {Fore.MAGENTA + name}{Fore.WHITE}, what a splendid name for a worm! \n Welcome to my special {Fore.GREEN}Garden{Fore.WHITE} filled with \n {Fore.YELLOW}GOLD NUGGETS.{Fore.WHITE}\n") 
            break
        else:
            print(line_break)
            name_error = "Please enter only letters"
            name_error_center = name_error.center(46)
            print(name_error_center)
            print(line_break)
            

# Prompt to call in both initial and main menu function
def prompt():   
    print(f" What would you like to do now {Fore.MAGENTA + name}?{Fore.WHITE}")

# Prints Navigation Menu
def nav_menu():
    print(line_break)
    print('  1. Play')
    print('  2. Rules')
    print('  3. Scores')
    print('  4. Exit')
    print(line_break)

def menu_input():
    # Navigation to other Pages
    navigation = str(input(' > '))
    match navigation:
        case "1" | "Play" | "play":
            os.system('cls' if os.name == 'nt' else 'clear')
            play.game_play()

        case "2" | "Rules" | "rules":
            os.system('cls' if os.name == 'nt' else 'clear')
            rules.print_rules()

        case "3" | "Scores" | "scores":
            os.system('cls' if os.name == 'nt' else 'clear')
            scores.print_scores()
            
        case "4" | "Exit" | "exit":
            print(line_break)
            print(f' Come back to my {Fore.GREEN}Garden{Fore.WHITE} soon {Fore.MAGENTA + name}!{Fore.WHITE}')
            print(line_break)
            print(Fore.RED +'')
            exit = "THE PROGRAM WILL NOW TERMINATE."
            exit_center = exit.center(46)
            print(exit_center)
            print(Fore.WHITE + '')
            print(line_break)
            quit()

        # Error Handling
        case _:
            print(line_break)
            print(f" Please enter a valid input from the Menu:\n {Style.DIM}(E.g. If you want to Play: '1' or 'Play'){Style.NORMAL}")
            print(line_break)
            menu_input()
            

# Called by Main, runs introduction with Greg and takes name.
def initial_menu():
    menu_hero()
    introduction()
    user_name()
    prompt()
    nav_menu()
    menu_input()

# Used by modules to create interactive menu. No introduction function is defined. 
def main_menu():
    menu_hero()
    prompt()
    nav_menu()
    menu_input()


# Couldn't find Library that contained worm, so I converted the exact ASCII art function to a string value for the variable worm_art
greg = str(rf"""{Fore.YELLOW}
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
{Fore.WHITE}""")
           
worm_death = str(rf"""{Fore.MAGENTA}        
                                 (X)(X)
                {Fore.RED}  YOU {Fore.MAGENTA}          /     \
                {Fore.RED}  HAVE {Fore.MAGENTA}        /       |
                {Fore.RED}  DIED! {Fore.MAGENTA}      /   \  * |
                ________     /    /\__/
        _      /        \   /    /
       / \    /  ____    \_/    /
      //\ \  /  /    \         /
      V  \ \/  /      \       /
          \___/        \_____/ 
{Fore.WHITE}""")









