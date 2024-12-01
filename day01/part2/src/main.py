"""The solution for the aoc day
"""

import re

from aoc_parser import AOCInput

def cast_list(test_list: list, data_type):
    """Cast a list of strings to a list of specified data type
    """
    return list(map(data_type, test_list))

def get_parsed_input():
    """Return the parsed input of the current aoc day
    """
    input_str = AOCInput.get_content()

    list1 = sorted(cast_list(re.findall(r"[0-9]+ +", input_str), int))
    list2 = sorted(cast_list(re.findall(r" +[0-9]+", input_str), int))

    return list1, list2

def solve(lists):
    """Solve the problem of the day with the given parsed input
    return the found solution
    """
    result = 0

    for list1_nbr in lists[0]:
        result += list1_nbr * lists[1].count(list1_nbr)

    return result

if __name__ == '__main__':
    print(solve(get_parsed_input()))
