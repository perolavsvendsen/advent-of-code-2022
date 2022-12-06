from day6 import _find

def test_find():
    assert _find("bvwbjplbgvbhsrlpgdmjqwftvncz", 4) == 5
    assert _find("nppdvjthqldpwncqszvftbrmjlhg", 4) == 6
    assert _find("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 4) == 10
    assert _find("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 4) == 11

    assert _find("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14) == 19
    assert _find("bvwbjplbgvbhsrlpgdmjqwftvncz", 14) == 23
    assert _find("nppdvjthqldpwncqszvftbrmjlhg", 14) == 23
    assert _find("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14) == 29
    assert _find("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14) == 26