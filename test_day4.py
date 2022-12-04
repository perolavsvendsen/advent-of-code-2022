from day4 import _read_data, _lists_fully_contains, _pair_to_list, _pair_fully_contains, _count_fully_contained, _pairs_overlap, _lists_overlap, _count_overlaps


def test_lists_fully_contains():
    assert _lists_fully_contains([1,2,3,4,5], [2,3,4])
    assert _lists_fully_contains([1,2,3,4,5], [3])
    assert _lists_fully_contains([1,2,3,4,5], [4,5])

def test_pair_to_list():
    assert _pair_to_list("1-5") == [1,2,3,4,5]
    assert _pair_to_list("1-1") == [1]
    assert _pair_to_list("6-7") == [6,7]

def test_pair_fully_contains():
    assert _pair_fully_contains("1-5", "2-4")
    assert _pair_fully_contains("2-8", "3-7")
    assert _pair_fully_contains("6-6", "4-6")
    assert not _pair_fully_contains("1-2", "3-5")
    assert not _pair_fully_contains("1-1", "5-5")

def test_count_fully_contains():
    TESTDATA = _read_data("testdata/4.txt")
    assert _count_fully_contained(TESTDATA) == 2

def test_lists_overlap():
    assert _lists_overlap([5,6,7], [7,8,9])
    assert _lists_overlap([2,3,4,5,6,7,8], [3,4,5,6,7])
    assert _lists_overlap([6], [4,5,6])
    assert _lists_overlap([2,3,4,5,6], [4,5,6,7,8])
    assert not _lists_overlap([2,3], [4,5])

def test_pairs_overlap():
    assert _pairs_overlap("5-7,7-9")
    assert _pairs_overlap("2-8,3-7")
    assert _pairs_overlap("6-6,4-6")
    assert _pairs_overlap("2-6,4-8")

def test_count_overlaps():
    TESTDATA = _read_data("testdata/4.txt")
    assert _count_overlaps(TESTDATA) == 4
