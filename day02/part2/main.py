"""The solution for the aoc day
"""

import re

from aoc_parser import AOCInput, AOCParser

def get_parsed_input():
    """Return the parsed input of the current aoc day
    """
    input_lines = AOCInput.split_input("\n")
    input_nbrs = AOCParser.apply_regex_to_list(re.findall, input_lines, r"\d+")
    return input_nbrs

def solve(parsed_input):
    """Solve the problem of the day with the given parsed input
    return the found solution
    """
    nbr_safe = 0
    for line in parsed_input:

        for i, _ in enumerate(line):
            safe = True
            increasing = True
            decreasing = True
            prev_nbr = None

            for j, nbr in enumerate(line):
                nbr = int(nbr)

                if j == i:
                    continue

                if prev_nbr is None:
                    prev_nbr = nbr
                    continue

                if nbr >= prev_nbr:
                    decreasing = False

                if nbr <= prev_nbr:
                    increasing = False

                if abs(nbr - prev_nbr) > 3:
                    increasing = False
                    decreasing = False

                if not increasing and not decreasing:
                    safe = False
                    break

                prev_nbr = nbr

            if safe:
                nbr_safe += 1
                break

    return nbr_safe


if __name__ == '__main__':
    print(solve(get_parsed_input()))
