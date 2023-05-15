# Set Board size
board_width = 38
board_height = 20

# Board positions based off size, no. of rows is determined by height and vice versa.
board = [(row, column) for row in range(board_height) for column in range(board_width)]

# Print board function
def print_board():
    for position in board:
        # if position of row is a value of 0 or (board_height -1), or position of column is 0 or (board_height -1) then print border '#'
        if position[0] in (0, board_height - 1) or position[1] in (0, board_width - 1):
            # printing border, need end as default is \n
            print('#', end = '')
        else:
            # printing board space
            print(' ', end = '')
        
        # Starting new line once you reach right column. 
        if position[1] == board_width -1:
            # Defaults new line.
            print('')
            
print_board()
