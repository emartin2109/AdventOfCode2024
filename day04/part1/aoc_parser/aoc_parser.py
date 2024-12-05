"""module used to parse the inputs of the current aoc day
"""

import re

from .config import Config

class AOCInput:
    """Class used to return daily AOC input in different formats
    """

    @staticmethod
    def get_content(strip : bool = False) -> str:
        """Return the content of the daily input file as a single string
        """
        with open(Config.INPUT_PATH, encoding="utf-8") as current_day_file:
            return current_day_file.read().strip() if strip else current_day_file.read()

    @staticmethod
    def split_input(patern: str, strip : bool = False) -> list[str]:
        """Return all str separated by the given patern in the daily input file as a list of strings
        """
        return AOCInput.get_content(strip).split(patern)

    @staticmethod
    def get_all_words() -> list[str]:
        """Return all words in the daily input file as a list of strings
        """
        return re.findall(r'\b\w+\b', AOCInput.get_content(), flags=re.UNICODE)

    @staticmethod
    def get_all_lines_and_words() -> list[list[str]]:
        """Return all lines and words in the daily input file
        as a list of lists of strings representing: lines[words[char]]
        """
        result: list[list[str]] = []
        lines : list[str] = AOCInput.split_input("\n")
        for line in lines:
            result.append(re.findall(r'\b\w+\b', line, flags=re.UNICODE))
        return result


class AOCParser:
    """Class for parsing input files for aoc day
    This class provide diverse methods for parsing input files
    """

    @staticmethod
    def matrix_to_list(list_of_list: list[list]) -> list:
        """Return a single list from a list of lists
        """
        return [item for sublist in list_of_list for item in sublist]

    @staticmethod
    def apply_regex_to_list(regex_method, regex: str, inputs: list[str],
                            additional_parameters: list = None) -> list:
        """Apply regex to each input in a list and return a list of lists
        """
        result : list[list[str]] = []
        for current_input in inputs:
            if additional_parameters is None:
                result.append(regex_method(regex, current_input))
            else:
                result.append(regex_method(regex, current_input, *additional_parameters))
        return result

    @staticmethod
    def find_paterns_in_grid(cursor_instructions: list[tuple[int, int]], regex_methods: list[str],
                             grid: list[list]) -> list[dict]:
        """Find all occurrences of a patern in a grid
        """
        result = []
        grid_height = len(grid)

        if grid_height == 0:
            return result

        grid_width = len(grid[0])

        for y, _ in enumerate(grid):
            for x, _ in enumerate(grid[y]):
                patern_found = True
                patern = []

                for cursor_instruction, regex_method in zip(cursor_instructions, regex_methods):
                    if y + cursor_instruction[0] < 0 or y + cursor_instruction[0] >= grid_height or x + cursor_instruction[1] < 0 or x + cursor_instruction[1] >= grid_width:
                        patern_found = False
                        break

                    regex_match = re.search(regex_method, grid[y + cursor_instruction[0]][x + cursor_instruction[1]:])

                    if regex_match is None:
                        patern_found = False
                        break

                    patern.append(regex_match.group())

                if patern_found:
                    result.append({"location": (y, x), "patern": patern})

        return result
