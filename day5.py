"""Advent of Code 2022 - Day 5"""

from pathlib import Path
import pandas as pd
import re

def main():
    fin = "input/5.txt"

    print(f"Day 5, part 1: {_solve(fin, '9000')}")
    print(f"Day 5, part 2: {_solve(fin, '9001')}")

def _solve(fin, crane_version):
    stacks, instructions, num_stacks = _read_data(fin)
    parsed_stacks = _parse_stacks(stacks, num_stacks)
    
    for instruction in instructions:
        parsed_stacks = _move(parsed_stacks, instruction, crane_version)

    return _get_top_of_each_stack(parsed_stacks)


def _get_top_of_each_stack(stacks):
    return "".join([value[-1] for value in stacks.values()])

def _move(stacks, instruction, crane_version):
    """Take the stacks, do the move, return the updated stacks"""

    amount, source, target = _parse_instruction(instruction)

    if crane_version == "9000":
        for i in range(amount):
            stacks[target].append(stacks[source].pop())
        return stacks
    if crane_version == "9001":
        lifted_cargo = []
        for i in range(amount):
            lifted_cargo.append(stacks[source].pop())
        stacks[target] += reversed(lifted_cargo)
        return stacks
    
    raise ValueError("Unknown crane version %s", crane_version)


def _move_9001(stacks, instruction):
    """Take the stacks, do the move, return the updated stacks"""

    amount, source, target = _parse_instruction(instruction)


    return stacks

def _parse_instruction(instruction):
    """move 1 from 2 to 3 -> (1, 2, 3)"""
    result = re.findall(r"\d+", instruction)
    return (int(result[0]), result[1], result[2])

def _read_data(fin):
    with open(fin, "r") as file:
        lines = [line.strip("\n") for line in file.readlines()]  # preserve spaces

    stacks = []
    instructions = []
    num_stacks_line_id = None

    for i, line in enumerate(lines):
        if "[" in line:
            stacks.append(line)
            continue
        if "move" in line:
            if num_stacks_line_id is None:
                num_stacks_line_id = i-2
            instructions.append(line)

    num_stacks = len(lines[num_stacks_line_id].strip().split())

    return stacks, instructions, num_stacks

def _parse_stacks(stacks, num_stacks):
    """Get the raw stacks, turn them into dict"""

    named_stacks = {str(stack_id+1):stack_id for stack_id in range(num_stacks)}
    parsed_stacks = {named_stack: [] for named_stack in named_stacks}
    stack_positions = [pos for pos in range(1, num_stacks*4, 4)]

    # go upwards
    for line in reversed(stacks):
        for named_stack, stack_position in zip(named_stacks, stack_positions):
            if line[stack_position] != " ":
                parsed_stacks[named_stack].append(line[stack_position])

    return parsed_stacks

if __name__ == "__main__":
    main()
