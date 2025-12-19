#!/usr/bin/env python3
"""Advent of Code 2025 - Day 6: Trash Compactor (https://adventofcode.com/2025/day/6)"""

import math
from dataclasses import dataclass
from typing import Callable, Iterable

import pytest

from aoc import puzzle_input_as_list


@dataclass
class Example:
    worksheet: list[str]
    grand_total: int


WORKSHEET = [
    "123 328  51 64 ",
    " 45 64  387 23 ",
    "  6 98  215 314",
    "*   +   *   +  ",
]

EXAMPLES_PART_1 = [Example(WORKSHEET, 4277556)]

EXAMPLES_PART_2 = [Example(WORKSHEET, 3263827)]


OPERATIONS: dict[str, Callable[[Iterable[int]], int]] = {
    "+": sum,
    "*": math.prod,
}


def part_1(worksheet: list[str]) -> int:
    rows = list(row.split() for row in worksheet)
    grand_total = 0
    for operation, numbers in zip(rows[-1], zip(*rows[:-1])):
        grand_total += OPERATIONS[operation](map(int, numbers))
    return grand_total


@pytest.mark.parametrize("example", EXAMPLES_PART_1)
def test_part_1(example: Example) -> None:
    assert part_1(example.worksheet) == example.grand_total


def part_2(worksheet: list[str]) -> int:
    rows = list(row.split() for row in worksheet)
    widths = [max(len(s) for s in problem) for problem in zip(*rows)]
    idx = 0
    grand_total = 0
    for operation, width in zip(rows[-1], widths):
        problem_numbers_by_row = [row[idx : idx + width] for row in worksheet[:-1]]
        numbers = [int("".join(col)) for col in zip(*problem_numbers_by_row)]
        grand_total += OPERATIONS[operation](numbers)
        idx += width + 1
    return grand_total


@pytest.mark.parametrize("example", EXAMPLES_PART_2)
def test_part_2(example: Example) -> None:
    assert part_2(example.worksheet) == example.grand_total


def main():
    print("Solution:")
    print(f"- Part 1: {part_1(puzzle_input_as_list())}")  # 3785892992137
    print(f"- Part 2: {part_2(puzzle_input_as_list())}")  # 7669802156452


if __name__ == "__main__":
    pytest.main(["-vv", __file__])
    main()
