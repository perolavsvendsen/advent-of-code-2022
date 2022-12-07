from day7 import _parse_structure, _read_data, _find_dirs_below_size, _sum_of_dirs_below_threshold, Filesystem, _find_dirs_above_size, _find_smallest_dir

TESTDATA = _read_data("testdata/7.txt")
THRESHOLD_PART1 = 100000
REQUIRED_PART2 = 30000000
TOTAL_SIZE_PART2 = 70000000

def test_parse_structure():
    root = _parse_structure(TESTDATA)
    assert root.size == 48381165, root.size

def test_find_dirs_below_size():
    root = _parse_structure(TESTDATA)
    qualified_dirs = _find_dirs_below_size(root, THRESHOLD_PART1)
    assert [d.name for d in qualified_dirs] == ["a", "e"]

def test_find_dirs_above_size():
    root = _parse_structure(TESTDATA)
    qualified_dirs = _find_dirs_above_size(root, 8381165)  # part 2
    assert [d.name for d in qualified_dirs] == ["/", "d"]

def test_sum_of_dirs_below_threshold():
    root = _parse_structure(TESTDATA)
    assert _sum_of_dirs_below_threshold(root, THRESHOLD_PART1) == 95437

def test_filesystem():
    filesystem = Filesystem(_parse_structure(TESTDATA), TOTAL_SIZE_PART2)
    assert filesystem.total_size == TOTAL_SIZE_PART2
    assert filesystem.used == 48381165
    assert filesystem.unused == 21618835
    assert REQUIRED_PART2 - filesystem.unused == 8381165
    assert filesystem.get_space_delta(REQUIRED_PART2) == 8381165

    assert filesystem.find_smallest_dir_to_delete(REQUIRED_PART2).name == "d"
    assert filesystem.find_smallest_dir_to_delete(REQUIRED_PART2).size == 24933642


def test_find_smallest():
    root = _parse_structure(TESTDATA)
    qualified_dirs = _find_dirs_above_size(root, 8381165)
    smallest = _find_smallest_dir(qualified_dirs)
    assert smallest.name == "d"
    assert smallest.size == 24933642