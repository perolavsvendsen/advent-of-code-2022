"""Advent of code 2022 - Day 9"""

from scipy.spatial.distance import pdist

def main():
    instructions = _read_instructions("input/9.txt")
    print(f"Day 1, part 1: {_make_moves(instructions, 2)}")
    print(f"Day 1, part 2: {_make_moves(instructions, 10)}")

class Rope:
    def __init__(self, knots_count, s=(0,0)):
        self.knots = [Knot(s) for _ in range(knots_count)]

    @property
    def head(self):
        return self.knots[0]

    @property
    def tail(self):
        return self.knots[-1]
    
    def move(self, direction):
        self.head.move(direction)
        for k, knot in enumerate(self.knots):
            if k == 0:
                continue
            knot.follow(self.knots[k-1].pos)

class Knot:
    def __init__(self, s=(0,0)):
        self._pos = s
        self._recorded_positions = [s]

    @property
    def pos(self):
        return self._pos

    @property
    def recorded_positions(self):
        return set(self._recorded_positions)

    def follow(self, target):
        self._pos = _follow(self.pos, target)
        self._recorded_positions.append(self.pos)

    def move(self, direction):
        self._pos = _move(self.pos, direction)

    def report_unique_positions(self):
        return len(set(self._recorded_positions))

def _make_moves(instructions, knots):
    rope = Rope(knots)
    for direction, steps in instructions:
        for step in range(steps):
            rope.move(direction)
    return rope.tail.report_unique_positions()

def _follow(p, target):
    """If distance is more than 1, move in the direction of target."""
    if _distance(p, target) <= 1:
        return p
    
    # move 1 step in direction of target
    p_x, p_y = p
    target_x, target_y = target

    # if in the same row/column, move in same row/column
    if p_x == target_x: # same row, move
        if p_y - target_y < -1:
            return _move(p, "R")
        if p_y - target_y > 1:
            return _move(p, "L")
    if p_y == target_y: # same colum, move up/down
        if p_x - target_x > 1:
            return _move(p, "U")
        if p_x - target_x < -1:
            return _move(p, "D")

    # if diagonal, move in both
    if p_x < target_x and p_y < target_y:
        return _move(_move(p, "D"), "R")
    if p_x < target_x and p_y > target_y:
        return _move(_move(p, "D"), "L")
    if p_x > target_x and p_y < target_y:
        return _move(_move(p, "U"), "R")
    if p_x > target_x and p_y > target_y:
        return _move(_move(p, "U"), "L")

    raise RuntimeError()

def _move(p, direction):
    if direction == "D":
        return tuple(sum(tup) for tup in zip(p, (1,0)))
    if direction == "U":
        return tuple(sum(tup) for tup in zip(p, (-1,0)))
    if direction == "R":
        return tuple(sum(tup) for tup in zip(p, (0,1)))
    if direction == "L":
        return tuple(sum(tup) for tup in zip(p, (0,-1)))

    raise ValueError("Illegal direction: %s", direction)

def _distance(p1, p2):
    return pdist([p1, p2], "chebyshev")    

def _read_instructions(fin):
    with open(fin, "r") as file:
        lines = [l.strip() for l in file.readlines()]

    instructions = []
    for line in lines:
        direction, step = line.strip().split()
        instructions.append((direction, int(step)))

    return instructions

if __name__ == "__main__":
    main()