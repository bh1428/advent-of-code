#!/usr/bin/env python3
"""Advent of Code 2025 - Day 2: Gift Shop (https://adventofcode.com/2025/day/2)"""

from dataclasses import dataclass
from functools import lru_cache

import pytest

from aoc import puzzle_input_as_str


@dataclass
class Example:
    ranges: str
    sum_invalid_ids: int


EXAMPLES_PART_1 = [
    Example("11-22", 11 + 22),
    Example("95-115", 99),
    Example("998-1012", 1010),
    Example("1188511880-1188511890", 1188511885),
    Example("222220-222224", 222222),
    Example("1698522-1698528", 0),
    Example("446443-446449", 446446),
    Example("38593856-38593862", 38593859),
    Example("565653-565659", 0),
    Example("824824821-824824827", 0),
    Example("2121212118-2121212124", 0),
    Example(
        (
            "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,"
            "1698522-1698528,446443-446449,38593856-38593862,565653-565659,"
            "824824821-824824827,2121212118-2121212124"
        ),
        1227775554,
    ),
]

EXAMPLES_PART_2 = [
    Example("11-22", 11 + 22),
    Example("95-115", 99 + 111),
    Example("998-1012", 999 + 1010),
    Example("1188511880-1188511890", 1188511885),
    Example("222220-222224", 222222),
    Example("1698522-1698528", 0),
    Example("446443-446449", 446446),
    Example("38593856-38593862", 38593859),
    Example("565653-565659", 565656),
    Example("824824821-824824827", 824824824),
    Example("2121212118-2121212124", 2121212121),
    Example(
        (
            "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,"
            "1698522-1698528,446443-446449,38593856-38593862,565653-565659,"
            "824824821-824824827,2121212118-2121212124"
        ),
        4174379265,
    ),
]


@dataclass
class CheckPattern:
    str_len: int
    expected_pattern_lengths: list[int]


CHECK_PATTERNS = [
    CheckPattern(1, []),
    CheckPattern(2, [1]),
    CheckPattern(3, [1]),
    CheckPattern(4, [1, 2]),
    CheckPattern(5, [1]),
    CheckPattern(6, [1, 2, 3]),
    CheckPattern(7, [1]),
    CheckPattern(8, [1, 2, 4]),
    CheckPattern(9, [1, 3]),
    CheckPattern(10, [1, 2, 5]),
]


def parse_ranges(ranges: str) -> list[tuple[int, int]]:
    return [(int(start), int(end)) for start, end in (r.split("-") for r in ranges.split(","))]


def part_1(ranges: str) -> int:
    sum_invalid_ids = 0
    for start, end in parse_ranges(ranges):
        for product_id in range(start, end + 1):
            str_id = str(product_id)
            str_id_half_pos = len(str_id) // 2
            if str_id[str_id_half_pos:] == str_id[:str_id_half_pos]:
                sum_invalid_ids += product_id
    return sum_invalid_ids


@pytest.mark.parametrize("example", EXAMPLES_PART_1)
def test_part_1(example: Example) -> None:
    assert part_1(example.ranges) == example.sum_invalid_ids


@lru_cache
def lengths_to_be_checked(len_str: int) -> list[int]:
    return [i for i in range(1, len_str) if len_str % i == 0]


@pytest.mark.parametrize("check_pattern", CHECK_PATTERNS)
def test_lengths_to_be_checked(check_pattern: CheckPattern) -> None:
    assert lengths_to_be_checked(check_pattern.str_len) == check_pattern.expected_pattern_lengths


def part_2(ranges: str) -> int:
    sum_invalid_ids = 0
    for start, end in parse_ranges(ranges):
        for product_id in range(start, end + 1):
            str_id = str(product_id)
            len_str_id = len(str_id)
            for pattern_length in lengths_to_be_checked(len_str_id):
                pieces = {str_id[i : i + pattern_length] for i in range(0, len_str_id, pattern_length)}
                if len(pieces) == 1:
                    sum_invalid_ids += product_id
                    break
    return sum_invalid_ids


@pytest.mark.parametrize("example", EXAMPLES_PART_2)
def test_part_2(example: Example) -> None:
    assert part_2(example.ranges) == example.sum_invalid_ids


def main():
    print("Solution:")
    print(f"- Part 1: {part_1(puzzle_input_as_str())}")  # 12599655151
    print(f"- Part 2: {part_2(puzzle_input_as_str())}")  # 20942028255


if __name__ == "__main__":
    pytest.main(["-vv", __file__])
    main()
