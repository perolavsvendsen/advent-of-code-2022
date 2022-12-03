from day1 import sum_of_calories

fin = "testdata/1.txt"

def test_sum_of_calories():

    assert sum_of_calories(fin, 1) == 24000, sum_of_calories(fin, 1)
    assert sum_of_calories(fin, 3) == 45000, sum_of_calories(fin, 3)
