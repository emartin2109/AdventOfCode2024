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
    def reduce_list_of_list(list_of_list: list[list]) -> list:
        """Return a single list from a list of lists
        """
        return [item for sublist in list_of_list for item in sublist]

    @staticmethod
    def apply_regex_to_list(regex_method, inputs: list[str], regex: str) -> list:
        """Apply regex to each input in a list and return a list of lists
        """
        result : list[list[str]] = []
        for current_input in inputs:
            result.append(regex_method(regex, current_input))
        return result
