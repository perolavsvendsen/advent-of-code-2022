"""Advent of Code 2022 - Day 4"""

def main():
    data = _read_data("input/4.txt")
    print(f"Day 4, part 1: {_count_fully_contained(data)}")
    print(f"Day 4, part 2: {_count_overlaps(data)}")

# ================================
# Functions

def _read_data(fin):
    with open(fin) as file:
        data = file.read().split()
    return data

def _lists_fully_contains(list1, list2):
    """Return True if list 2 is fully contained by list 1"""
    return min(list1) <= min(list2) and max(list1) >= max(list2)

def _lists_overlap(list1, list2):
    """Return True if the lists overlap each other in any direction"""
    return min(list1) in list2 or min(list2) in list1 or max(list1) in list2 or max(list2) in list1

def _pair_to_list(pair):
    """Parse the pair, return a continuous list"""
    first, last = pair.split("-")
    return list(range(int(first), int(last)+1))

def _pair_fully_contains(pair1, pair2):
    """Turn pair into lists and check if fully contained in either direction"""
    return (
        _lists_fully_contains(_pair_to_list(pair1), _pair_to_list(pair2)) or
        _lists_fully_contains(_pair_to_list(pair2), _pair_to_list(pair1))
        )

def _count_fully_contained(pairs):
    """Return count of pairs where one is fully contained by the other."""
    return sum([_pair_fully_contains(*pair.split(",")) for pair in pairs])

def _pairs_overlap(pair):
    """Return True if pair overlap."""
    pair1, pair2 = pair.split(",")
    return _lists_overlap(_pair_to_list(pair1), _pair_to_list(pair2))

def _count_overlaps(pairs):
    """Return count of pairs that overlap."""
    return sum([_pairs_overlap(pair) for pair in pairs])


if __name__ == "__main__":
    main()