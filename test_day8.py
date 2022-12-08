from day8 import _read_data, _is_visible, _count_visible, _scenic_score, _count_trees_seeing, _max_scenic_score

TESTDATA = _read_data("testdata/8.txt")

def test_max_scenic_score():
    assert _max_scenic_score(TESTDATA) == 8

def test_scenic_score():
    assert TESTDATA[1,2] == 5
    assert _scenic_score(TESTDATA, 1, 2) == 4

    assert TESTDATA[3,2] == 5
    assert _scenic_score(TESTDATA, 3,2) == 8

    assert TESTDATA[0,4] == 3
    assert _scenic_score(TESTDATA, 0, 4) == 0

    assert TESTDATA[4,1] == 5
    assert _scenic_score(TESTDATA, 4, 1) == 0

def test_count_visible():
    assert _count_visible(TESTDATA) == 21

def test_count_trees_seeing():
    assert _count_trees_seeing(5, [3,5,3]) == 2
    assert _count_trees_seeing(5, [1,2]) == 2
    assert _count_trees_seeing(5, [1]) == 1
    assert _count_trees_seeing(5, [5,2]) == 1

def test_is_visible():
    col = [0,0,1,0,0]
    row = [0,0,1,0,0]
    assert _is_visible(1, 2, 2, row, col) is True

    col = [9,9,0,9,9]
    row = [9,9,0,9,9]
    assert _is_visible(0, 2, 2, row, col) is False

    col = [5,9,9,9,9]
    row = [5,9,9,9,9]
    assert _is_visible(5, 0, 0, row, col) is True

    col = [9,9,9,9,5]
    row = [9,9,9,9,5]
    assert _is_visible(5, 4, 4, row, col) is True

    col = [0,0,1,2,3,3,3,3,3,2,1,0]
    row = [9,9,9,9,9,3,9,9,9,9,9,9]
    assert _is_visible(3, 5, 5, row, col) is False