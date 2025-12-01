#!/usr/bin/env python3
"""Advent of Code 2025 - Day 1: Secret Entrance (https://adventofcode.com/2025/day/1)"""

from dataclasses import dataclass

import pytest

from aoc import PuzzleInputType, puzzle_input_as_list

START_POSITION = 50
DIAL_SIZE = 100


@dataclass
class Example:
    rotations: list[str]
    answer: int


EXAMPLES_PART_1 = [
    Example(["L25"], 0),
    Example(["R25"], 0),
    Example(["L50"], 1),
    Example(["R50"], 1),
    Example(["L75"], 0),
    Example(["R75"], 0),
    Example(["L150"], 1),
    Example(["R150"], 1),
    Example(["L175"], 0),
    Example(["R175"], 0),
    Example(["L275"], 0),
    Example(["R275"], 0),
    Example(["L68"], 0),
    Example(["L68", "L30"], 0),
    Example(["L68", "L30", "R48"], 1),
    Example(["L68", "L30", "R48", "L5"], 1),
    Example(["L68", "L30", "R48", "L5", "R60"], 1),
    Example(["L68", "L30", "R48", "L5", "R60", "L55"], 2),
    Example(["L68", "L30", "R48", "L5", "R60", "L55", "L1"], 2),
    Example(["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99"], 3),
    Example(["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14"], 3),
    Example(["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"], 3),
]

EXAMPLES_PART_2 = [
    Example(["L25"], 0),
    Example(["R25"], 0),
    Example(["L50"], 1),
    Example(["R50"], 1),
    Example(["L75"], 1),
    Example(["R75"], 1),
    Example(["L150"], 2),
    Example(["R150"], 2),
    Example(["L175"], 2),
    Example(["R175"], 2),
    Example(["L275"], 3),
    Example(["R275"], 3),
    Example(["L68"], 1),
    Example(["L68", "L30"], 1),
    Example(["L68", "L30", "R48"], 2),
    Example(["L68", "L30", "R48", "L5"], 2),
    Example(["L68", "L30", "R48", "L5", "R60"], 3),
    Example(["L68", "L30", "R48", "L5", "R60", "L55"], 4),
    Example(["L68", "L30", "R48", "L5", "R60", "L55", "L1"], 4),
    Example(["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99"], 5),
    Example(["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14"], 5),
    Example(["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"], 6),
]


def parse_rotation(rotation):
    direction, clicks = rotation[0], int(rotation[1:])
    if direction == "L":
        return -clicks
    return clicks


def part_1(rotations: PuzzleInputType) -> int:
    position = START_POSITION
    times_landed_on_zero = 0
    for rotation in rotations:
        clicks = parse_rotation(rotation)
        position = (position + clicks) % DIAL_SIZE
        if position == 0:
            times_landed_on_zero += 1
    return times_landed_on_zero


@pytest.mark.parametrize("example", EXAMPLES_PART_1)
def test_part_1(example: Example) -> None:
    assert part_1(example.rotations) == example.answer


def part_2(rotations: PuzzleInputType) -> int:
    position = START_POSITION
    landing_on_or_passing_zero = 0
    for rotation in rotations:
        clicks = parse_rotation(rotation)
        rounds, new_position = divmod(position + clicks, DIAL_SIZE)
        landing_on_or_passing_zero += abs(rounds)
        if clicks < 0:
            if position == 0:
                landing_on_or_passing_zero -= 1
            if new_position == 0:
                landing_on_or_passing_zero += 1
        position = new_position
    return landing_on_or_passing_zero


@pytest.mark.parametrize("example", EXAMPLES_PART_2)
def test_part_2(example: Example) -> None:
    assert part_2(example.rotations) == example.answer


def main():
    print("Solution:")
    print(f"- Part 1: {part_1(puzzle_input_as_list())}")  # 1059
    print(f"- Part 2: {part_2(puzzle_input_as_list())}")  # 6305


if __name__ == "__main__":
    pytest.main(["-vv", __file__])
    main()
