"""Advent of Code 2022 - Day 3"""

import string


def main():
    rucksacks = _pack_rucksacks("input/3.txt")
    print(f"Day 3, part 1: {_sum_of_priorities(rucksacks=rucksacks)}")

    groups = _find_groups(rucksacks)
    badges = [_find_badge_for_group(group) for group in groups]
    print(f"Day 3, part 2: {_sum_of_priorities(items=badges)}")

class Rucksack:
    def __init__(self, items=None):
        """Initialize the Rucksack"""

        self._content = {}

        if items:
            self.put_content(items)

    def put_content(self, items:str):
        """Put content into the Rucksack"""

        self._content = {
            "compartments": [
                {"items": items[0:int(len(items)/2)]}, 
                {"items": items[int(len(items)/2):]},
            ],
            "total": {"items": items},
        }

        _duplicate_character = _find_common_string_across_strings(
            [self._content["compartments"][0]["items"], self._content["compartments"][1]["items"]]
            )
        if len(_duplicate_character) > 1:
            raise ValueError("More than one duplicate character")

        self._content["duplicates"] = {
            "char": _duplicate_character,
        }

        self._content["duplicates"]["priority"] = _find_priority_for_item(self._content["duplicates"]["char"])


    @property
    def content(self):
        return self._content

    @property
    def all_items(self):
        return self._content["total"]["items"]

def _find_priority_for_item(item):
    """Translate character to priority"""

    #Lowercase item types a through z have priorities 1 through 26.
    #Uppercase item types A through Z have priorities 27 through 52.

    return string.ascii_letters.index(item) + 1

def _pack_rucksacks(fin):
    """Initialize Rucksack instance for each given input."""

    with open(fin, "r") as file:
        lines = file.read().split()
    return [Rucksack(contents) for contents in lines]

def _sum_of_priorities(rucksacks=None, items=None):
    if rucksacks and items:
        raise ValueError("Rucksacks or items, not both")

    if rucksacks:
        return sum([r.content["duplicates"]["priority"] for r in rucksacks])

    if items:
        return sum([_find_priority_for_item(item) for item in items])

def _find_groups(rucksacks, groupsize=3):

    groups = []

    for i in range(0, len(rucksacks), groupsize):
        groups.append(rucksacks[i:i+groupsize])
        
    return groups

def _find_common_string_across_strings(strings):

    # catch when identical lists are given
    if len(set(strings)) == 1:
        return strings[0]

    return "".join(set.intersection(*map(set,strings)))

def _find_badge_for_group(group):
    return _find_common_string_across_strings([rucksack.all_items for rucksack in group])


if __name__ == "__main__":
    main()