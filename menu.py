from art import text2art
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True) 

def hero():
    print(worm_art)
    print(menu_break)
    print(intro_text)
    print(menu_break)

def nav_menu():
    print(menu_break)
    print('  1. Play')
    print('  2. About')
    print('  3. Scores')
    print('  4. Exit')
    print(menu_break)


# about_title = text2art("about")
    # print(about_title)
# title = text2art("G Worm")


intro_text = (f"          {Fore.MAGENTA}WELCOME TO THE {Fore.YELLOW}GOLDEN{Fore.MAGENTA} WORM")  #Spaces to center intro within menu break

menu_break = ('+--------------------------------------------+')

#Couldn't find a library that contained a worm like the following:
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
               





