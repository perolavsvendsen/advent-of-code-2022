"""Advent of Code 2022 - day 1"""

def main():
    fin = "1a.txt"

    answer_1a = sum_of_calories(fin, 1)
    print(f"1a: {answer_1a}")

    answer_1b = sum_of_calories(fin, 3)
    print(f"1b: {answer_1b}")

def sum_of_calories(fin, i):
    with open(fin, "r") as file:
        input_data = file.readlines()
    
    return sum(sorted([sum([int(xxx) for xxx in xx]) for xx in [x.split() for x in " ".join([xx.strip() for xx in input_data]).split("  ")]], reverse=True)[:i])

def tests():
    fin = "1a_tests.txt"

    assert sum_of_calories(fin, 1) == 24000, sum_of_calories(fin, 1)
    assert sum_of_calories(fin, 3) == 45000, sum_of_calories(fin, 3)

    print("✅")


if __name__ == "__main__":
    tests()
    main()


#1a: 73211
#1b: 213958