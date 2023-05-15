import menu
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True) 

# Print Hero Art and Welcome Message
menu.hero()

# Introduction with George
print(f" Hello, I am {Fore.YELLOW}George {Fore.WHITE}the Great Golden Worm! \n")
print(" I haven't seen you around this soil patch...") 

# User prompt for name input
name = input(" Tell me, what's your name child? ")
#  Prints name and greeting
print (f"\n {Fore.MAGENTA + name}{Fore.WHITE}, what a splendid name for a worm! \n Welcome to my special soil patch filled \n with {Fore.YELLOW}GOLD.\n") 

# Menu Introduction and input
print(f" What would you like to do now {Fore.MAGENTA + name}?")
menu.nav_menu()
nav = input(' > ')



