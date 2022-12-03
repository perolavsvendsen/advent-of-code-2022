from day3 import Rucksack, _pack_rucksacks, _find_badge_for_group, _find_common_string_across_strings, _find_groups, _find_priority_for_item, _sum_of_priorities

with open("testdata/3.txt") as file:
    TESTDATA = file.read().split()

rucksacks = _pack_rucksacks("testdata/3.txt")

def test_rucksacks():

    assert rucksacks[0].all_items == "vJrwpWtwJgWrhcsFMMfFFhFp", rucksacks[0].all_items
    assert rucksacks[0].content["compartments"][0]["items"] == "vJrwpWtwJgWr", rucksacks[0].items["compartments"][0]["items"]
    assert rucksacks[0].content["compartments"][1]["items"] == "hcsFMMfFFhFp", rucksacks[0].items["compartments"][1]["items"]

    assert rucksacks[1].content["compartments"][0]["items"] == "jqHRNqRjqzjGDLGL", rucksacks[0].items["compartments"][0]["items"]
    assert rucksacks[1].content["compartments"][1]["items"] == "rsFMfFZSrLrFZsSL", rucksacks[0].items["compartments"][1]["items"]

    assert rucksacks[0].content["duplicates"] == {"char": "p", "priority": 16}
    assert rucksacks[1].content["duplicates"] == {"char": "L", "priority": 38}
    assert rucksacks[2].content["duplicates"] == {"char": "P", "priority": 42}
    assert rucksacks[3].content["duplicates"] == {"char": "v", "priority": 22}
    assert rucksacks[4].content["duplicates"] == {"char": "t", "priority": 20}
    assert rucksacks[5].content["duplicates"] == {"char": "s", "priority": 19}


def test_find_common_strings_across_strings():

    assert _find_common_string_across_strings(["jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL"]) == "L"
    assert _find_common_string_across_strings(["abc", "axx"]) == "a"
    assert _find_common_string_across_strings(["abc", "abc"]) == "abc"
    assert _find_common_string_across_strings(["abc", "xyz"]) == ""
    assert _find_common_string_across_strings(["Abc", "aBC"]) == ""
    assert _find_common_string_across_strings(["Abc", "Aaa"]) == "A"
    assert _find_common_string_across_strings(["abc", "ABc", "Abc"]) == "c"

    _testgroup0_items = TESTDATA[0:3]
    assert TESTDATA[0:3] == ["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg"]
    assert _find_common_string_across_strings(_testgroup0_items) == "r"

    _testgroup1_items = TESTDATA[3:6]
    assert _testgroup1_items == ["wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "ttgJtRGJQctTZtZT", "CrZsJsPPZsGzwwsLwLmpwMDw"]
    assert _find_common_string_across_strings(_testgroup1_items) == "Z"


def test_sum_of_priorities():
    assert _sum_of_priorities(rucksacks=rucksacks) == 157


def test_find_groups():
    groups = _find_groups(rucksacks)

    _all_items_group0 = [x.all_items for x in groups[0]]
    _all_items_group1 = [x.all_items for x in groups[1]]

    _testgroup0_items = TESTDATA[0:3]
    assert _all_items_group0 == _testgroup0_items, _all_items_group0
    _testgroup1_items = TESTDATA[3:6]
    assert _all_items_group1 == _testgroup1_items, _all_items_group1

    for i, group in enumerate(groups):
        assert len(group) == 3, f"Length of group {i} was {len(group)}"

def test_find_badge_for_group():
    groups = _find_groups(rucksacks)

    assert _find_badge_for_group(groups[0]) == "r", _find_badge_for_group(groups[0])
    assert _find_badge_for_group(groups[1]) == "Z", _find_badge_for_group(groups[1])
  
    badges = [_find_badge_for_group(group) for group in groups]
    assert badges == ["r", "Z"], badges

    assert sum([_find_priority_for_item(char) for char in badges]) == 70
    assert _sum_of_priorities(items=badges) == 70

