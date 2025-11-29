"""Advent of Code - utilities"""

import traceback
from pathlib import Path
from typing import Any, Generator


class InputFileNotFoundException(Exception):
    """Input file not found"""


def read_input_file_as_str() -> str:
    """Get the content of the puzzle input file.

    The method searching for a name on the caller stack assuming:
     - calling script is in a subdir of the parent of this file
     - input file is in the folder '../data' relative to calling script
     - input file has the same (base)name as the caller but with extension '.txt'

    Raises:
        InputFileNotFoundException: when no existing file was found

    Returns:
        Path: content puzzle input file
    """
    aoc_base_dir = str(Path("__file__").resolve().parent)  # resolve() makes drive letter uppercase (on Windows)
    for stack_frame in traceback.extract_stack():
        filename = Path(stack_frame.filename).resolve()  # again resolve() for drive letter
        if str(filename).startswith(aoc_base_dir):
            input_file = filename.parent.parent / "data" / filename.with_suffix(".txt").name
            if input_file.exists():
                return input_file.read_text(encoding="utf-8")
    raise InputFileNotFoundException("could not find name of puzzle input file")


def read_input_file_as_lines(ignore_empty_lines: bool = True) -> Generator[str]:
    """Read puzzle input file line by line and (optionally) suppress empty lines.

    Args:
        ignore_empty_lines (bool, optional): suppress empty lines (default: True).

    Yields:
        Generator[str]: line of the puzzle input file
    """
    for line in read_input_file_as_str().splitlines():
        line = line.strip()
        if ignore_empty_lines and not line:
            continue
        yield line


def list_to_generator(input_list: list[Any]) -> Generator[Any]:
    """Convert a list to a generator"""
    yield from input_list
