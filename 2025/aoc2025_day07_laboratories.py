#!/usr/bin/env python3
"""Advent of Code 2025 - Day 7: Laboratories (https://adventofcode.com/2025/day/7)"""

from dataclasses import dataclass

import pytest

from aoc import puzzle_input_as_list


@dataclass
class Example:
    diagram: list[str]
    answer: int


DIAGRAM = [
    ".......S.......",
    "...............",
    ".......^.......",
    "...............",
    "......^.^......",
    "...............",
    ".....^.^.^.....",
    "...............",
    "....^.^...^....",
    "...............",
    "...^.^...^.^...",
    "...............",
    "..^...^.....^..",
    "...............",
    ".^.^.^.^.^...^.",
    "...............",
]


EXAMPLES_PART_1 = [Example(DIAGRAM, 21)]

EXAMPLES_PART_2 = [Example(DIAGRAM, 40)]


def part_1(diagram: list[str]) -> int:
    splits = 0
    current_beams: set[int] = {diagram[0].find("S")}
    for line in diagram[1:]:
        new_beams: set[int] = set()
        splitters = [index for index, char in enumerate(line) if char == "^"]
        for beam in current_beams:
            if beam in splitters:
                new_beams.update([beam - 1, beam + 1])
                splits += 1
            else:
                new_beams.add(beam)
        current_beams = new_beams
    return splits


@pytest.mark.parametrize("example", EXAMPLES_PART_1)
def test_part_1(example: Example) -> None:
    assert part_1(example.diagram) == example.answer


def part_2(diagram: list[str]) -> int:
    data = [1 for _ in diagram[0]]
    for row in diagram[::-1]:
        new_data: list[int] = []
        for i, c in enumerate(row):
            match c:
                case "S":
                    return data[i]
                case "^":
                    new_data.append(data[i - 1] + data[i + 1])
                case _:
                    new_data.append(data[i])
        data = new_data
    return -1


@pytest.mark.parametrize("example", EXAMPLES_PART_2)
def test_part_2(example: Example) -> None:
    assert part_2(example.diagram) == example.answer


def main():
    print("Solution:")
    print(f"- Part 1: {part_1(puzzle_input_as_list())}")  # 1658
    print(f"- Part 2: {part_2(puzzle_input_as_list())}")  # 53916299384254


if __name__ == "__main__":
    pytest.main(["-vv", __file__])
    main()
