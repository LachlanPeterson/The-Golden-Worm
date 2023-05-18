import menu

# Main Module to handle one call function.
# Other pages dont call functions, they just define different functions.

# This allows me to import other modules throughout my application
# as its menu based and repeats various functions from other modules.

# Instead of having one module filled with content, I've seperated the
# functions and variables for each 'menu option' in seperate modules ('pages').

# Start the Program with the initial function from the menu module
menu.initial_menu()
