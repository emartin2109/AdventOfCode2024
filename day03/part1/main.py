"""The solution for the aoc day
"""

import re

from aoc_parser import AOCInput

def get_parsed_input():
    """Return the parsed input of the current aoc day
    """
    input_content = AOCInput.get_content()
    instructions = re.findall(r"mul\((\d+),(\d+)\)", input_content)

    return instructions

def solve(instructions):
    """Solve the problem of the day with the given parsed input
    return the found solution
    """
    result = 0

    for nbrs in instructions:
        result += int(nbrs[0]) * int(nbrs[1])

    return result

if __name__ == '__main__':
    print(solve(get_parsed_input()))
