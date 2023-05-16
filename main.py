import menu
import os
import rules

# Main Page
menu.print_menu()


# Navigation to other Pages
navigation = str(input(' > '))

match navigation:
    case '1' | 'Play' | 'play':
        os.system('cls' if os.name == 'nt' else 'clear'),
        print("Game time") 

    case '2' | 'Rules' | 'rules':
        os.system('cls' if os.name == 'nt' else 'clear'),
        rules.print_rules()
        input(' > ')
        if input == 'Yes' or 'yes':
            os.system('cls' if os.name == 'nt' else 'clear'),
            


    case '3' | 'Scores' | 'scores':
        os.system('cls' if os.name == 'nt' else 'clear'),
        print("Score time") 

    case _:
        print("Failed") 
