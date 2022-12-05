from day5 import _read_data, _parse_stacks, _parse_instruction, _move, _get_top_of_each_stack

TESTDATA = _read_data("testdata/5.txt")

def test_read_data():
    stacks, instructions, num_stacks = TESTDATA
    assert len(stacks) == 3
    assert len(instructions) == 4
    assert num_stacks == 3

def test_parse_stacks():
    stacks, _, num_stacks = TESTDATA
    parsed_stacks = _parse_stacks(stacks, num_stacks)

    assert parsed_stacks == {
        "1": ["Z", "N"],
        "2": ["M","C","D"],
        "3": ["P"],
    }

def test_parse_instruction():
    assert _parse_instruction("move 1 from 2 to 1") == (1,"2","1")

def test_move_9000():
    prior = {
        "1": ["Z", "N"],
        "2": ["M","C","D"],
        "3": ["P"],
    }

    posterior = _move(prior, "move 1 from 2 to 1", "9000")
    assert posterior == {
        "1": ["Z", "N", "D"],
        "2": ["M","C"],
        "3": ["P"],
    }


def test_move_9001_single_crate():
    prior = {
        "1": ["Z", "N"],
        "2": ["M","C","D"],
        "3": ["P"],
    }

    posterior = _move(prior, "move 1 from 2 to 1", "9001")
    assert posterior == {
        "1": ["Z", "N", "D"],
        "2": ["M","C"],
        "3": ["P"],
    }

def test_move_9001_multi_crate():
    prior = {
        "1": ["Z", "N"],
        "2": ["M","C","D"],
        "3": ["P"],
    }

    posterior = _move(prior, "move 2 from 2 to 1", "9001")
    assert posterior == {
        "1": ["Z", "N", "C", "D"],
        "2": ["M"],
        "3": ["P"],
    }    

def test_multiple_moves_9000():
    prior = {
        "1": ["Z", "N"],
        "2": ["M","C","D"],
        "3": ["P"],
    }

    stacks, instructions, num_stacks = TESTDATA
    parsed_stacks = _parse_stacks(stacks, num_stacks)
    for instruction in instructions:
        parsed_stacks = _move(parsed_stacks, instruction, "9000")

    assert parsed_stacks == {'1': ['C'], '2': ['M'], '3': ['P', 'D', 'N', 'Z']}


def test_multiple_moves_9001():
    prior = {
        "1": ["Z", "N"],
        "2": ["M","C","D"],
        "3": ["P"],
    }

    stacks, instructions, num_stacks = TESTDATA
    parsed_stacks = _parse_stacks(stacks, num_stacks)
    for instruction in instructions:
        parsed_stacks = _move(parsed_stacks, instruction, "9001")

    assert parsed_stacks == {'1': ['M'], '2': ['C'], '3': ['P', 'Z', 'N', 'D']}


def test_get_top_of_each_stack():
    stacks = {
        "1": ["Z", "N"],
        "2": ["M","C","D"],
        "3": ["P"],
    }

    assert _get_top_of_each_stack(stacks) == "NDP"

    stacks = {'1': ['C'], '2': ['M'], '3': ['P', 'D', 'N', 'Z']}

    assert _get_top_of_each_stack(stacks) == "CMZ"


def test_solution_9000():
    stacks, instructions, num_stacks = TESTDATA
    parsed_stacks = _parse_stacks(stacks, num_stacks)
    for instruction in instructions:
        stacks = _move(parsed_stacks, instruction, "9000")
    assert _get_top_of_each_stack(stacks) == "CMZ"

def test_solution_9001():
    stacks, instructions, num_stacks = TESTDATA
    parsed_stacks = _parse_stacks(stacks, num_stacks)
    for instruction in instructions:
        stacks = _move(parsed_stacks, instruction, "9001")
    assert _get_top_of_each_stack(stacks) == "MCD"