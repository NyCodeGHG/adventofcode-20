from assertions import assert_equals
from input_reader import read_lines, read_split_lines
from printer import aoc_print

groups = read_split_lines("day06")

# Part one
total_sum = 0
for group in groups:
    votes = set()
    for single_person in group:
        for question in single_person:
            votes.add(question)

    total_sum += len(votes)

aoc_print(f"The count of 'yes' votes is {total_sum}.")
assert_equals(6714, total_sum)

# Part two
