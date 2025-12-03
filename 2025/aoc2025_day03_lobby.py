#!/usr/bin/env python3
"""Advent of Code 2025 - Day 3: Lobby (https://adventofcode.com/2025/day/3)"""

from dataclasses import dataclass

import pytest

from aoc import puzzle_input_as_list


@dataclass
class Example:
    banks: list[str]
    joltage: int


EXAMPLES_PART_1 = [
    Example(["987654321111111"], 98),
    Example(["811111111111119"], 89),
    Example(["234234234234278"], 78),
    Example(["818181911112111"], 92),
    Example(
        [
            "987654321111111",
            "811111111111119",
            "234234234234278",
            "818181911112111",
        ],
        98 + 89 + 78 + 92,
    ),
]

EXAMPLES_PART_2 = [
    Example(["987654321111111"], 987654321111),
    Example(["811111111111119"], 811111111119),
    Example(["234234234234278"], 434234234278),
    Example(["818181911112111"], 888911112111),
    Example(
        [
            "987654321111111",
            "811111111111119",
            "234234234234278",
            "818181911112111",
        ],
        987654321111 + 811111111119 + 434234234278 + 888911112111,
    ),
]


def part_1(banks: list[str]) -> int:
    joltage = 0
    for bank in banks:
        max_battery_left = max(bank[:-1])
        position = bank.find(max_battery_left)
        max_battery_right = max(bank[position + 1 :])
        joltage += int(max_battery_left + max_battery_right)
    return joltage


@pytest.mark.parametrize("example", EXAMPLES_PART_1)
def test_part_1(example: Example) -> None:
    assert part_1(example.banks) == example.joltage


def part_2(banks: list[str], batteries_to_keep: int = 12) -> int:
    joltage = 0
    for bank in banks:
        start = 0
        bank_joltage = ""
        batteries_to_find = batteries_to_keep
        bank = f"{bank}0"  # avoid issue with bank[?:-0] (:-0 does not work)
        while batteries_to_find > 0:
            max_battery = max(bank[start:-batteries_to_find])
            position = bank[start:-batteries_to_find].find(max_battery) + start
            bank_joltage += bank[position]
            start = position + 1
            batteries_to_find -= 1
        joltage += int(bank_joltage)
    return joltage


@pytest.mark.parametrize("example", EXAMPLES_PART_2)
def test_part_2(example: Example) -> None:
    assert part_2(example.banks) == example.joltage


def main():
    print("Solution:")
    print(f"- Part 1: {part_1(puzzle_input_as_list())}")  # 17193
    print(f"- Part 2: {part_2(puzzle_input_as_list())}")  # 171297349921310


if __name__ == "__main__":
    pytest.main(["-vv", "-s", __file__])
    main()
