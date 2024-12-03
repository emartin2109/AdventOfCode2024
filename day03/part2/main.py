"""The solution for the aoc day
"""

import re

from aoc_parser import AOCInput

def get_parsed_input():
    """Return the parsed input of the current aoc day
    """
    input_content = AOCInput.get_content()
    instructions = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", input_content)

    return instructions

def solve(instructions):
    """Solve the problem of the day with the given parsed input
    return the found solution
    """
    result = 0
    activated = True

    for instruction in instructions:
        if len(re.findall(r"do\(\)", instruction)) > 0:
            activated = True

        elif len(re.findall(r"don't\(\)", instruction)) > 0:
            activated = False

        elif len(re.findall(r"mul\(\d+,\d+\)", instruction)) > 0 and activated:
            nbrs = list(map(int, re.findall(r"\d+", instruction)))
            result += nbrs[0] * nbrs[1]

    return result

if __name__ == '__main__':
    print(solve(get_parsed_input()))