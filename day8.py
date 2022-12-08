"""Advent of code 2022 - Day 8"""

import numpy as np

def main():

    data = _read_data("input/8.txt")

    print(f"Day 8, part 1: {_count_visible(data)}")
    print(f"Day 8, part 2: {_max_scenic_score(data)}")

def _max_scenic_score(data):
    scenic_scores = []
    for row_i, row in enumerate(data):
        for col_i, col in enumerate(row):
            scenic_scores.append(_scenic_score(data, row_i, col_i))
    return max(scenic_scores)

def _count_visible(data):
    visibles = 0
    for row_i, row in enumerate(data): # vertical id
        for col_i, value in enumerate(row): # horizontal id
            col = data[:,col_i]
            if _is_visible(value, row_i, col_i, row, col):
                visibles += 1
    return visibles

def _scenic_score(data, row_i, col_i):
    row = data[row_i]
    col = data[:,col_i]
    val = data[row_i, col_i]

    if row_i == 0 or row_i == len(row-1):
        return 0
    if col_i == 0 or col_i == len(col-1):
        return 0

    seeing_up = _count_trees_seeing(val, reversed(col[:row_i]))
    seeing = seeing_up

    seeing_down = _count_trees_seeing(val, col[row_i+1:])
    seeing *= seeing_down

    seeing_left = _count_trees_seeing(val, reversed(row[:col_i]))
    seeing *= seeing_left

    seeing_right = _count_trees_seeing(val, row[col_i+1:])
    seeing *= seeing_right

    return seeing


def _count_trees_seeing(value, array):
    seeing_count = 0
    for seetree in array:
        seeing_count += 1
        if seetree >= value:
            break
    return seeing_count


def _is_visible(val, row_i, col_i, row, col):
    if not col[row_i] == row[col_i] == val:
        raise ValueError(val, row_i, col_i, row, col)

    # edges
    if row_i == 0 or row_i == len(col)-1: # upper/lower edge
        return True
    if col_i == 0 or col_i == len(row)-1:
        return True # edges

    if max(col[:row_i]) < val or max(col[row_i+1:]) < val:
        return True

    if max(row[:col_i]) < val or max(row[col_i+1:]) < val:
        return True

    return False

def _read_data(fin):
    with open(fin, "r") as file:
        data = [line.strip() for line in file.readlines()]

    return np.array([[int(char) for char in line] for line in data])

if __name__ == "__main__":
    main()