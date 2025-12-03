"""Advent of Code - utilities"""

import pathlib
import time
import traceback
from typing import Callable, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


class InputFileNotFoundException(Exception):
    """Input file not found"""


def get_puzzle_input_filename() -> pathlib.Path:
    """Generate a filename where the puzzle input is expected.

    The method searches for a name on the caller stack assuming:
     - calling script is in a subdir of the parent of this file
     - input file is in the folder '../data' relative to calling script
     - input file has the same (base)name as the caller but with extension '.txt'

    Raises:
        InputFileNotFoundException: when no existing file was found

    Returns:
        Path: content puzzle input file
    """
    aoc_base_dir = str(pathlib.Path("__file__").resolve().parent)  # resolve() makes drive letter uppercase (on Windows)
    for stack_frame in traceback.extract_stack():
        filename = pathlib.Path(stack_frame.filename).resolve()  # again resolve() for drive letter
        if str(filename).startswith(aoc_base_dir):
            input_file = filename.parent.parent / "data" / filename.with_suffix(".txt").name
            if input_file.exists():
                return input_file
    raise InputFileNotFoundException("could not find name of puzzle input file")


def puzzle_input_as_list(ignore_empty_lines: bool = True) -> list[str]:
    """Read puzzle input file (optionally) suppress empty lines and return as list.

    Args:
        ignore_empty_lines (bool, optional): suppress empty lines (default: True).

    Yields:
        list[str]: list of puzzle input file lines
    """
    puzzle_input: list[str] = []
    with open(get_puzzle_input_filename(), encoding="utf-8") as fh_in:
        for line in fh_in:
            line = line.strip()
            if ignore_empty_lines and not line:
                continue
            puzzle_input.append(line)
    return puzzle_input


def puzzle_input_as_str() -> str:
    """Get the puzzle input as a string.

    Returns:
        str: content puzzle input file
    """
    return get_puzzle_input_filename().read_text(encoding="utf-8")


def measure_duration(func: Callable[P, R]) -> Callable[P, R]:
    """Decorator to measure the duration of a function call."""

    def wrap_func(*args: P.args, **kwargs: P.kwargs) -> R:
        t1 = time.perf_counter()
        result = func(*args, **kwargs)
        t2 = time.perf_counter()
        print(f"{func.__name__}(): {(t2 - t1):.4f}s")
        return result

    return wrap_func
