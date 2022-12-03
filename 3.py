"""Advent of Code 2022 - Day 3"""

import string


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

        _duplicate_character = find_duplicates_in_strings(self._content["compartments"][0]["items"], self._content["compartments"][1]["items"])
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

def find_duplicates_in_strings(s1, s2):
    """Given two string, find duplicate characters, return as string"""

    duplicates = ""
    for char in s1:
        if char in s2 and char not in duplicates:
            duplicates += char

    return duplicates

def _find_priority_for_item(item):
    """Translate character to priority"""

    #Lowercase item types a through z have priorities 1 through 26.
    #Uppercase item types A through Z have priorities 27 through 52.

    return string.ascii_letters.index(item) + 1

def _pack_rucksacks(fin):
    with open(fin, "r") as file:
        lines = file.readlines()
    return [Rucksack(contents.strip()) for contents in lines]



def tests_part1():

    rucksacks = _pack_rucksacks("3_tests.txt")

    assert rucksacks[0].all_items == "vJrwpWtwJgWrhcsFMMfFFhFp", rucksacks[0].all_items
    assert rucksacks[0].content["compartments"][0]["items"] == "vJrwpWtwJgWr", rucksacks[0].items["compartments"][0]["items"]
    assert rucksacks[0].content["compartments"][1]["items"] == "hcsFMMfFFhFp", rucksacks[0].items["compartments"][1]["items"]

    assert rucksacks[1].content["compartments"][0]["items"] == "jqHRNqRjqzjGDLGL", rucksacks[0].items["compartments"][0]["items"]
    assert rucksacks[1].content["compartments"][1]["items"] == "rsFMfFZSrLrFZsSL", rucksacks[0].items["compartments"][1]["items"]

    assert find_duplicates_in_strings("jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL") == "L"

    assert find_duplicates_in_strings("abc", "axx") == "a"
    assert find_duplicates_in_strings("abc", "abc") == "abc"
    assert find_duplicates_in_strings("abc", "xyz") == ""
    assert find_duplicates_in_strings("Abc", "aBC") == ""
    assert find_duplicates_in_strings("Abc", "Aaa") == "A"

    assert rucksacks[0].content["duplicates"] == {"char": "p", "priority": 16}
    assert rucksacks[1].content["duplicates"] == {"char": "L", "priority": 38}
    assert rucksacks[2].content["duplicates"] == {"char": "P", "priority": 42}
    assert rucksacks[3].content["duplicates"] == {"char": "v", "priority": 22}
    assert rucksacks[4].content["duplicates"] == {"char": "t", "priority": 20}
    assert rucksacks[5].content["duplicates"] == {"char": "s", "priority": 19}

    assert _sum_of_priorities(rucksacks=rucksacks) == 157

    print("✅")


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
    return "".join(set.intersection(*map(set,strings)))

def _find_badge_for_group(group):
    return _find_common_string_across_strings([rucksack.all_items for rucksack in group])


def tests_part2():

    assert _find_common_string_across_strings(["abc", "ABc", "Abc"]) == "c"

    _testgroup0_items = ["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg"]
    assert _find_common_string_across_strings(_testgroup0_items) == "r"

    _testgroup1_items = ["wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "ttgJtRGJQctTZtZT", "CrZsJsPPZsGzwwsLwLmpwMDw"]
    assert _find_common_string_across_strings(_testgroup1_items) == "Z"

    rucksacks = _pack_rucksacks("3_tests.txt")

    groups = _find_groups(rucksacks)
    _all_items_group0 = [x.all_items for x in groups[0]]
    _all_items_group1 = [x.all_items for x in groups[1]]

    assert _all_items_group0 == _testgroup0_items, _all_items_group0
    assert _all_items_group1 == _testgroup1_items, _all_items_group1

    for i, group in enumerate(groups):
        assert len(group) == 3, f"Length of group {i} was {len(group)}"

    assert _find_badge_for_group(groups[0]) == "r", _find_badge_for_group(groups[0])
    assert _find_badge_for_group(groups[1]) == "Z", _find_badge_for_group(groups[1])
  
    badges = [_find_badge_for_group(group) for group in groups]
    assert badges == ["r", "Z"], badges

    assert sum([_find_priority_for_item(char) for char in badges]) == 70
    assert _sum_of_priorities(items=badges) == 70

    print("✅")

def main():
    rucksacks = _pack_rucksacks("3a.txt")
    print(f"Part 1, sum of priorities: {_sum_of_priorities(rucksacks=rucksacks)}")

    groups = _find_groups(rucksacks)
    badges = [_find_badge_for_group(group) for group in groups]
    print(f"Part 2, sum of priorities: {_sum_of_priorities(items=badges)}")

if __name__ == "__main__":
    tests_part1()
    tests_part2()
    main()