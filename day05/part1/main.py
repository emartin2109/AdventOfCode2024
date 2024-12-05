"""The solution for the aoc day
"""

import re

from aoc_parser import AOCInput, AOCParser

def get_parsed_input():
    """Return the parsed input of the current aoc day
    """
    parts = AOCInput.split_input("\n\n", strip=True)

    rules = AOCParser.apply_regex_to_list(re.findall, parts[0].split("\n"), r"\d+")
    pages = AOCParser.apply_regex_to_list(re.findall, parts[1].split("\n"), r"\d+")

    return rules, pages

def solve(parsed_input):
    """Solve the problem of the day with the given parsed input
    return the found solution
    """
    rules, pages = parsed_input
    result = 0

    for line in pages:
        valid = True

        for rule in rules:
            first_index = -1
            second_index = -1

            for i, _ in enumerate(line):
                if line[i] == rule[0]:
                    first_index = i
                if line[i] == rule[1]:
                    second_index = i

            if first_index != -1 and second_index != -1:
                if first_index > second_index:
                    valid = False
                    break

        if valid:
            result += int(line[int(len(line) / 2)])

    return result

if __name__ == '__main__':
    print(solve(get_parsed_input()))
