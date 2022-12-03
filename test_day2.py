from day2 import play, play_part2

fin = "testdata/2.txt"

def test_part1():

    round_scores, total_score = play(fin)

    assert round_scores == [8, 1, 6]
    assert total_score == 15

def test_part2():

    round_scores, total_scores = play_part2(fin)

    assert round_scores == [4, 1, 7]
    assert total_scores == 12