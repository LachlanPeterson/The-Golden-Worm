# from art import text2art
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True) 

def hero():
    print(worm_art)
    print(menu_break)
    # print(menu.title)
    print(intro)
    print(menu_break)

# title = text2art("G Worm")


intro = (f"         {Fore.MAGENTA}Welcome to the {Fore.YELLOW}Golden{Fore.MAGENTA} Worm!")  #Spaces to center intro within menu break

menu_break = ('+-------------------------------------------+')

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
               





