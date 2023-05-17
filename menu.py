from colorama import Fore
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
    print(" I haven't seen you around this soil patch...") 

    # User prompt for name input
    global name
    name = input(" Tell me, what's your name child? ")
    #  Prints name and greeting
    print (f"\n {Fore.MAGENTA + name}{Fore.WHITE}, what a splendid name for a worm! \n Welcome to my special soil patch filled \n with {Fore.YELLOW}GOLD.{Fore.WHITE}\n") 

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

    # Navigation to other Pages
    navigation = str(input(' > '))
    match navigation:
        case "1" | "Play" | "play":
            os.system('cls' if os.name == 'nt' else 'clear'),
            play.game_play()

        case "2" | "Rules" | "rules":
            os.system('cls' if os.name == 'nt' else 'clear'),
            rules.print_rules()

        case "3" | "Scores" | "scores":
            os.system('cls' if os.name == 'nt' else 'clear'),
            scores.print_scores()
            

        case "4" | "Exit" | "exit":
            print(line_break)
            print(f' Come back to my soil patch soon {Fore.MAGENTA + name}!{Fore.WHITE}')
            print(line_break)
            print(Fore.RED +'')
            exit = "THE PROGRAM WILL NOW TERMINATE."
            exit_center = exit.center(44)
            print(exit_center)
            print(Fore.WHITE + '')
            print(line_break)
            quit()
        case _:
            print('other error')
            


def initial_menu():
    menu_hero()
    introduction()
    prompt()
    nav_menu()

def main_menu():
    menu_hero()
    prompt()
    nav_menu()


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
                {Fore.BLACK}  YOU {Fore.MAGENTA}          /     \
                {Fore.BLACK}  HAVE {Fore.MAGENTA}        /       |
                {Fore.RED}  DIED! {Fore.MAGENTA}      /   \  * |
                ________     /    /\__/
        _      /        \   /    /
       / \    /  ____    \_/    /
      //\ \  /  /    \         /
      V  \ \/  /      \       /
          \___/        \_____/ 
{Fore.WHITE}""")









