"""The solution for the aoc day
"""

from aoc_parser import AOCInput, AOCParser

def get_parsed_input():
    """Return the parsed input of the current aoc day
    """
    return AOCInput.split_input("\n")

def solve(grid):
    """Solve the problem of the day with the given parsed input
    return the found solution
    """
    matches_nbr = 0

    pattern = [r"^X", r"^M", r"^A", r"^S"]

    matches_nbr += len(AOCParser.find_paterns_in_grid([(0, 0), (0, 1), (0, 2), (0, 3)], pattern, grid))
    matches_nbr += len(AOCParser.find_paterns_in_grid([(0, 0), (0, -1), (0, -2), (0, -3)], pattern, grid))
    matches_nbr += len(AOCParser.find_paterns_in_grid([(0, 0), (1, 0), (2, 0), (3, 0)], pattern, grid))
    matches_nbr += len(AOCParser.find_paterns_in_grid([(0, 0), (-1, 0), (-2, 0), (-3, 0)], pattern, grid))
    matches_nbr += len(AOCParser.find_paterns_in_grid([(0, 0), (1, 1), (2, 2), (3, 3)], pattern, grid))
    matches_nbr += len(AOCParser.find_paterns_in_grid([(0, 0), (-1, -1), (-2, -2), (-3, -3)], pattern, grid))
    matches_nbr += len(AOCParser.find_paterns_in_grid([(0, 0), (1, -1), (2, -2), (3, -3)], pattern, grid))
    matches_nbr += len(AOCParser.find_paterns_in_grid([(0, 0), (-1, 1), (-2, 2), (-3, 3)], pattern, grid))

    return matches_nbr

if __name__ == '__main__':
    print(solve(get_parsed_input()))
