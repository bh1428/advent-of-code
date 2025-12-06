"""Advent of Code - utilities"""

import time
import traceback
from pathlib import Path
from typing import Callable, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")

DEFAULT_DATA_DIR = "data"


class InputFileNotFoundException(Exception):
    """Input file not found"""


def get_puzzle_input_filename(data_dir: str | Path | None = None) -> Path:
    """Generate a filename where the puzzle input is expected.

    The file to be found is based on the name of the caller script (which is
    retrieved from the call stack). The puzzle input file must have the same
    name as the caller (but with .txt extension) and be located in a folder
    'data' below the project root folder. The folder structure below 'data'
    must be comparable to the location of the caller script, e.g.:
      project_root
       ├─► aoc
       │    └─► __init__.py        this file (__file__)
       ├─► parent_caller
       │    └─► caller.py          caller of this function
       └─► data                    data folder root
            └─► parent_caller      matches parent from caller
                 └─► caller.txt    puzzle input file, e.g. caller with .txt

    This example shows one level above the caller, but multiple levels are
    supported as well.

    Args:
        data_dir (str | Path | None, optional): base name of the data
            directory. Defaults to DEFAULT_DATA_DIR.

    Raises:
        InputFileNotFoundException: when no file was found

    Returns:
        Path: content puzzle input file
    """
    project_root = str(Path(__file__).resolve().parent.parent)
    data_dir = str(data_dir) if data_dir is not None else DEFAULT_DATA_DIR
    for stack_frame in traceback.extract_stack():
        filename = str(Path(stack_frame.filename).resolve())
        if filename.startswith(project_root):
            file_in_subtree = Path(filename[len(project_root) + 1 :])
            puzzle_input_file = Path(project_root) / data_dir / file_in_subtree.with_suffix(".txt")
            if puzzle_input_file.exists():
                return puzzle_input_file
    raise InputFileNotFoundException("could not find puzzle input file")


def puzzle_input_as_list(ignore_empty_lines: bool = True) -> list[str]:
    """Read puzzle input file, (optionally) suppress empty lines and return as list.

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
