"""The solution for the aoc day
"""

import re

from aoc_parser import AOCInput, AOCParser

def get_parsed_input():
    """Return the parsed input of the current aoc day
    """
    input_lines = AOCInput.split_input("\n")
    input_nbrs = AOCParser.apply_regex_to_list(re.findall, input_lines, r"-?[0-9]+")
    parsed_input_nbrs = AOCParser.reduce_list_of_list(input_nbrs)
    return parsed_input_nbrs

def solve(parsed_input):
    """Solve the problem of the day with the given parsed input
    return the found solution
    """
    result = 0

    list1 = []
    list2 = []

    for i, curr_nbr in enumerate(parsed_input):
        if i % 2:
            list1.append(int(curr_nbr))
        else:
            list2.append(int(curr_nbr))

    for list1_nbr in list1:
        result += list1_nbr * list2.count(list1_nbr)

    return result

if __name__ == '__main__':
    print(solve(get_parsed_input()))
