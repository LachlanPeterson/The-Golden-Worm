from play import generate_gold_position

# MOCK Board Size
board_width = 32
board_height = 15

# MOCK Board positions
board = [
    (row, col) for row in range(board_height) for col in range(board_width)
    ]

# MOCK Worm
worm = [(board_height//2, 6), (board_height//2, 5), (board_height//2, 4)]


# Test generate_gold_position
# Case 1 - Test whether gold position is not in the border
def test_generate_gold_position_not_in_border():
    gold_position = generate_gold_position()
    assert (gold_position[0] not in (0, board_height - 1) or
            gold_position[1] not in (0, board_width - 1))


# Case 2 - Test whether gold position is not in the worm
def test_generate_gold_position_not_in_worm():
    gold_position = generate_gold_position()
    assert gold_position not in worm
