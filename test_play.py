import play

# Mock Board Size
board_width = 32
board_height = 15

# Mock Board positions
board = [
    (row, col) for row in range(board_height) for col in range(board_width)
    ]

# Mock Worm
worm = [(board_height//2, 6), (board_height//2, 5), (board_height//2, 4)]


# Test generate_gold_position function
# Case 1 - Test whether gold_position is generated inside border
def test_generate_gold_position_not_in_border():
    play.generate_gold_position()
    assert (play.gold_position[0] not in (0, board_height - 1) or
            play.gold_position[1] not in (0, board_width - 1))
    # Expected results: gold_position randomly generated outside border


# Case 2 - Test whether gold position is not in the worm
def test_generate_gold_position_not_in_worm():
    play.generate_gold_position()
    assert play.gold_position not in worm
    # Expected results: gold_position randomly generated outside worm


# Test game_reset function
# Case 1 -  Test whether score is reset to 0
def test_game_reset_score(monkeypatch):
    # Using monkeypatch to set score to 50 before running function
    monkeypatch.setattr(play, "score", 50)
    play.game_reset()
    assert play.score == 0
    # Expected results: score is reset from to 0 after game_reset function


# Case 2 - Test whether game_over is reset to False
def test_game_reset_game_over_false(monkeypatch):
    # Using monkeypatch to set game_over to True before running function
    monkeypatch.setattr(play, "game_over", True)
    play.game_reset()
    assert play.game_over is False
    # Expected results: game_over is reset to False after function
