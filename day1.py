"""Advent of Code 2022 - day 1"""

def main():
    fin = "input/1.txt"

    answer_1a = sum_of_calories(fin, 1)
    print(f"Day 1, part 1: {answer_1a}")

    answer_1b = sum_of_calories(fin, 3)
    print(f"Day 1, part 2: {answer_1b}")

def sum_of_calories(fin, i):
    with open(fin, "r") as file:
        input_data = file.readlines()
    
    return sum(sorted([sum([int(xxx) for xxx in xx]) for xx in [x.split() for x in " ".join([xx.strip() for xx in input_data]).split("  ")]], reverse=True)[:i])


if __name__ == "__main__":
    main()