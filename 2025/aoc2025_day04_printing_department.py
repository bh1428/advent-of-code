#!/usr/bin/env python3
"""Advent of Code 2025 - Day 4: Printing Department (https://adventofcode.com/2025/day/4)"""

from dataclasses import dataclass
from functools import cache

import pytest

from aoc import puzzle_input_as_list


@dataclass
class Example:
    paper_roll_grid: list[str]
    rolls: int


EXAMPLES_PART_1 = [
    Example(
        [
            "..@@.@@@@.",
            "@@@.@.@.@@",
            "@@@@@.@.@@",
            "@.@@@@..@.",
            "@@.@@@@.@@",
            ".@@@@@@@.@",
            ".@.@.@.@@@",
            "@.@@@.@@@@",
            ".@@@@@@@@.",
            "@.@.@@@.@.",
        ],
        13,
    )
]

EXAMPLES_PART_2 = [
    Example(
        [
            "..@@.@@@@.",
            "@@@.@.@.@@",
            "@@@@@.@.@@",
            "@.@@@@..@.",
            "@@.@@@@.@@",
            ".@@@@@@@.@",
            ".@.@.@.@@@",
            "@.@@@.@@@@",
            ".@@@@@@@@.",
            "@.@.@@@.@.",
        ],
        43,
    )
]


@dataclass
class Neighbor:
    row: int
    col: int
    max_row: int
    max_col: int
    neighbors: list[tuple[int, int]]


NEIGHBOR_EXAMPLES = [
    Neighbor(0, 0, 10, 10, [(0, 1), (1, 0), (1, 1)]),
    Neighbor(5, 0, 10, 10, [(4, 0), (4, 1), (5, 1), (6, 0), (6, 1)]),
    Neighbor(0, 5, 10, 10, [(0, 4), (0, 6), (1, 4), (1, 5), (1, 6)]),
    Neighbor(0, 10, 10, 10, [(0, 9), (1, 9), (1, 10)]),
    Neighbor(10, 10, 10, 10, [(9, 9), (9, 10), (10, 9)]),
    Neighbor(5, 5, 10, 10, [(4, 4), (4, 5), (4, 6), (5, 4), (5, 6), (6, 4), (6, 5), (6, 6)]),
]


@cache
def neighbors(row: int, col: int, max_row: int, max_col: int) -> list[tuple[int, int]]:
    # fmt: off
    candidates = [
        (row-1, col-1), (row-1, col), (row-1, col+1),
        (row,   col-1),               (row,   col+1 ),
        (row+1, col-1), (row+1, col), (row+1, col+1),
    ]
    # fmt: on
    return [(x, y) for x, y in candidates if (0 <= x <= max_row) and (0 <= y <= max_col)]


@pytest.mark.parametrize("neighbor", NEIGHBOR_EXAMPLES)
def test_neighbors(neighbor: Neighbor) -> None:
    assert neighbors(neighbor.row, neighbor.col, neighbor.max_row, neighbor.max_col) == neighbor.neighbors


def parse_grid(paper_grid: list[str]) -> list[list[int]]:
    return [[1 if cell == "@" else 0 for cell in row] for row in paper_grid]


def part_1(paper_roll_grid: list[str]) -> int:
    grid = parse_grid(paper_roll_grid)
    max_row, max_col = len(grid) - 1, len(grid[0]) - 1
    reachable_rolls = 0
    for row in range(max_row + 1):
        for col in range(max_col + 1):
            if grid[row][col] == 1:
                adjacent_rolls = sum(grid[r][c] for r, c in neighbors(row, col, max_row, max_col))
                if adjacent_rolls < 4:
                    reachable_rolls += 1
    return reachable_rolls


@pytest.mark.parametrize("example", EXAMPLES_PART_1)
def test_part_1(example: Example) -> None:
    assert part_1(example.paper_roll_grid) == example.rolls


def part_2(paper_roll_grid: list[str]) -> int:
    grid = parse_grid(paper_roll_grid)
    max_row, max_col = len(grid) - 1, len(grid[0]) - 1
    rolls_removed = 0
    while True:
        rolls_to_remove: set[tuple[int, int]] = set()
        # find rolls that can be removed
        for row in range(max_row + 1):
            for col in range(max_col + 1):
                if grid[row][col] == 1:
                    adjacent_rolls = sum(grid[r][c] for r, c in neighbors(row, col, max_row, max_col))
                    if adjacent_rolls < 4:
                        rolls_to_remove.add((row, col))
        # remove rolls
        if not rolls_to_remove:
            break
        rolls_removed += len(rolls_to_remove)
        for row, col in rolls_to_remove:
            grid[row][col] = 0
    return rolls_removed


@pytest.mark.parametrize("example", EXAMPLES_PART_2)
def test_part_2(example: Example) -> None:
    assert part_2(example.paper_roll_grid) == example.rolls


def main():
    print("Solution:")
    print(f"- Part 1: {part_1(puzzle_input_as_list())}")  # 1344
    print(f"- Part 2: {part_2(puzzle_input_as_list())}")  # 8112


if __name__ == "__main__":
    pytest.main(["-vv", __file__])
    main()
