"""The solution for the aoc day
"""

import re

from aoc_parser import AOCInput, AOCParser


def get_parsed_input():
    """Return the parsed input of the current aoc day
    """
    input_lines = AOCInput.split_input("\n")
    input_nbrs = AOCParser.apply_regex_to_list(re.findall, r"\d", input_lines)
    return input_nbrs

def take_path(grid, start_pos, prev_nbr):
    """Return the positions reached by taking a path in the grid
    """
    if not 0 <= start_pos[0] < len(grid) or not 0 <= start_pos[1] < len(grid[start_pos[0]]) or \
        int(grid[start_pos[0]][start_pos[1]]) != prev_nbr + 1:
        return 0

    if int(grid[start_pos[0]][start_pos[1]]) == 9:
        return 1

    result = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for direction in directions:
        result += take_path(grid, (start_pos[0] + direction[0], start_pos[1] + direction[1]), int(grid[start_pos[0]][start_pos[1]]))

    return result

def solve(grid):
    """Solve the problem of the day with the given parsed input
    return the found solution
    """
    result = 0

    for i, line in enumerate(grid):
        for j, _ in enumerate(line):
            result += take_path(get_parsed_input(), (i, j), -1)

    return result

if __name__ == '__main__':
    print(solve(get_parsed_input()))
