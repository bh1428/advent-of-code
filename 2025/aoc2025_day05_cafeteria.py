#!/usr/bin/env python3
"""Advent of Code 2025 - Day 5: Cafeteria (https://adventofcode.com/2025/day/5)"""

from dataclasses import dataclass

import pytest

from aoc import puzzle_input_as_list


@dataclass
class Example:
    database: list[str]
    fresh_ingredients: int


EXAMPLE_DATABASE = [
    "3-5",
    "10-14",
    "16-20",
    "12-18",
    "",
    "1",
    "5",
    "8",
    "11",
    "17",
    "32",
]

EXAMPLES_PART_1 = [Example(EXAMPLE_DATABASE, 3)]

EXAMPLES_PART_2 = [Example(EXAMPLE_DATABASE, 14)]

type RangeListType = list[tuple[int, int]]
type IngredientListType = list[int]


def parse_database(database: list[str]) -> tuple[RangeListType, IngredientListType]:
    ingredient_ranges: RangeListType = []
    ingredients: IngredientListType = []
    in_ranges = True
    for line in database:
        if not line:
            in_ranges = False
            continue
        if in_ranges:
            start, end = map(int, line.split("-"))
            ingredient_ranges.append((start, end))
        else:
            ingredients.append(int(line))
    return ingredient_ranges, ingredients


def part_1(database: list[str]) -> int:
    ingredient_ranges, ingredients = parse_database(database)
    fresh = 0
    for ingredient in ingredients:
        for start, end in ingredient_ranges:
            if start <= ingredient <= end:
                fresh += 1
                break
    return fresh


@pytest.mark.parametrize("example", EXAMPLES_PART_1)
def test_part_1(example: Example) -> None:
    assert part_1(example.database) == example.fresh_ingredients


def part_2(database: list[str]) -> int:
    ingredient_ranges, _ = parse_database(database)
    ranges: RangeListType = []
    while ingredient_ranges:
        start, end = ingredient_ranges.pop()
        new_ranges: RangeListType = []
        while ranges:
            known_start, known_end = ranges.pop()
            if (start > known_end) or (end < known_start):
                new_ranges.append((known_start, known_end))
            elif start < known_start <= end <= known_end:
                end = known_end
            elif start >= known_start:
                start = known_start
                end = max(end, known_end)
        new_ranges.append((start, end))
        ranges = new_ranges
    return sum(end - start + 1 for start, end in ranges)


@pytest.mark.parametrize("example", EXAMPLES_PART_2)
def test_part_2(example: Example) -> None:
    assert part_2(example.database) == example.fresh_ingredients


def main():
    print("Solution:")
    print(f"- Part 1: {part_1(puzzle_input_as_list(ignore_empty_lines=False))}")  # 885
    print(f"- Part 2: {part_2(puzzle_input_as_list(ignore_empty_lines=False))}")  # 348115621205535


if __name__ == "__main__":
    pytest.main(["-vv", __file__])
    main()
