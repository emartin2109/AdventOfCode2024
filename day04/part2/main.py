"""The solution for the aoc day
"""

from aoc_parser import AOCInput, AOCParser

patterns = [
    [
        r"^M.S",
        r"^.A.",
        r"^M.S"
    ],
    [
        r"^S.S",
        r"^.A.",
        r"^M.M"
    ],
    [
        r"^S.M",
        r"^.A.",
        r"^S.M"
    ],
    [
        r"^M.M",
        r"^.A.",
        r"^S.S"
    ]
]

def get_parsed_input():
    """Return the parsed input of the current aoc day
    """
    grid = AOCInput.split_input("\n")

    return grid

def solve(grid):
    """Solve the problem of the day with the given parsed input
    return the found solution
    """
    matches_nbr = 0

    for pattern in patterns:
        matches_nbr += len(AOCParser.find_paterns_in_grid([(0, 0), (1, 0), (2, 0), (3, 0)], pattern, grid))

    return matches_nbr

if __name__ == '__main__':
    print(solve(get_parsed_input()))
