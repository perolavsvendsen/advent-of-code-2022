from day9 import _read_instructions, _make_moves, _move, _distance, _follow, Rope, Knot

TESTDATA_1 = _read_instructions("testdata/9-1.txt")
TESTDATA_2 = _read_instructions("testdata/9-2.txt")

def test_read_instructions():
    assert isinstance(TESTDATA_1, list)
    assert TESTDATA_1[0] == ("R", 4)

def test_distance():
    assert _distance((0,0), (0,0)) == 0
    assert _distance((0,0), (0,1)) == 1
    assert _distance((0,0), (1,0)) == 1
    assert _distance((0,0), (1,1)) == 1
    assert _distance((0,0), (2,0)) == 2
    assert _distance((-2,0), (0,0)) == 2
    assert _distance((0,0), (2,0)) == 2
    assert _distance((-1,-1), (-1,-1)) == 0
    assert _distance((-1,-1), (-1,0)) == 1

def test_move():
    assert _move((0,0), "U") == (-1,0)
    assert _move((0,0), "D") == (1,0)
    assert _move((0,0), "R") == (0,1)
    assert _move((0,0), "L") == (0,-1)
    assert _move((1,5), "L") == (1,4)
    assert _move((-1,-1), "L") == (-1, -2)

def test_follow():
    assert _follow((0,0), (0,0)) == (0,0)
    assert _follow((0,0), (1,1)) == (0,0) # distance is 1, don't move
    assert _follow((0,0), (2,2)) == (1,1) # distance is 2, move diagonally down/right
    assert _follow((0,0), (-1, -1)) == (0,0) # distance is 1, don't move
    assert _follow((0,0), (-2, -2)) == (-1,-1) # distance is 2, move diagonally up/left
    assert _follow((0,0), (2,0)) == (1,0) #distance is 2, move down one

def test_move_rope_part1():
    rope = Rope(2)
    assert len(rope.knots) == 2
    for direction, steps in TESTDATA_1:
        for i, step in enumerate(range(steps)):
            rope.move(direction)
    assert rope.tail.report_unique_positions() == 13

def test_move_rope_part1():
    rope = Rope(10)
    assert len(rope.knots) == 10
    for direction, steps in TESTDATA_2:
        for i, step in enumerate(range(steps)):
            rope.move(direction)
    assert rope.tail.report_unique_positions() == 36