"""Advent of Code 2022 - Day 2"""


def play(fin):

    combinations = {
        "ax": {"score": 1 + 3},  # rock-rock # draw
        "ay": {"score": 2 + 6},  # rock-paper # win
        "az": {"score": 3 + 0},  # rock-scissor # loose
        "bx": {"score": 1 + 0},  # paper-rock # loose
        "by": {"score": 2 + 3},  # paper-paper # draw
        "bz": {"score": 3 + 6},  # paper-scissor # win
        "cx": {"score": 1 + 6},  # scissor-rock # win
        "cy": {"score": 2 + 0},  # scissor-paper # loose
        "cz": {"score": 3 + 3},  # scissor-scissor # draw
    }

    with open(fin, "r") as file:
        rounds = [r.strip().lower().replace(" ", "") for r in file.readlines()]

    round_scores = [combinations[round]["score"] for round in rounds]

    total_score = sum(round_scores)

    return round_scores, total_score


def play_part2(fin):
    """Play according to the instructions in the second round."""
    with open(fin, "r") as file:
        rounds = ["".join(round.lower().strip().split()) for round in file.readlines()]

    round_scores = []

    choose = {
        "a": {
            "x": {"choose": "c", "score": 3 + 0},  # loose
            "y": {"choose": "a", "score": 1 + 3},  # draw
            "z": {"choose": "b", "score": 2 + 6},  # win
        },
        "b": {
            "x": {"choose": "a", "score": 1 + 0},  # loose
            "y": {"choose": "b", "score": 2 + 3},  # draw
            "z": {"choose": "c", "score": 3 + 6},  # win
        },
        "c": {
            "x": {"choose": "b", "score": 2 + 0},  # loose
            "y": {"choose": "c", "score": 3 + 3},  # draw
            "z": {"choose": "a", "score": 1 + 6},  # win
        },
    }

    for hand, requirement in rounds:
        score = choose[hand][requirement]["score"]
        round_scores.append(score)

    total_score = sum(round_scores)

    return round_scores, total_score


def test_part1():

    fin = "2_tests.txt"
    round_scores, total_score = play(fin)

    assert round_scores == [8, 1, 6]
    assert total_score == 15

    print("Part 1: ✅")


def test_part2():
    fin = "2_tests.txt"

    round_scores, total_scores = play_part2(fin)

    assert round_scores == [4, 1, 7]
    assert total_scores == 12

    print("Part 2: ✅")


def main():
    fin = "2a.txt"

    round_scores, total_score = play(fin)

    print(f"Total score, part 1: {total_score}")

    round_scores, total_score = play_part2(fin)
    print(f"Total score, part 2: {total_score}")


if __name__ == "__main__":
    test_part1()
    test_part2()
    main()
