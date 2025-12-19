#!/usr/bin/env python3
"""Advent of Code 2025 - Day 8: Playground (https://adventofcode.com/2025/day/8)"""

import itertools
import math
from dataclasses import dataclass

import pytest

from aoc import puzzle_input_as_list


@dataclass
class Example:
    positions_list: list[str]
    answer: int


EXAMPLE_BOXES = [
    "162,817,812",
    "57,618,57",
    "906,360,560",
    "592,479,940",
    "352,342,300",
    "466,668,158",
    "542,29,236",
    "431,825,988",
    "739,650,466",
    "52,470,668",
    "216,146,977",
    "819,987,18",
    "117,168,530",
    "805,96,715",
    "346,949,466",
    "970,615,88",
    "941,993,340",
    "862,61,35",
    "984,92,344",
    "425,690,689",
]

EXAMPLES_PART_1 = [Example(EXAMPLE_BOXES, 40)]

EXAMPLES_PART_2 = [Example(EXAMPLE_BOXES, 25272)]


@dataclass
class Box:
    position: tuple[int, int, int]
    circuit: int


type BoxesType = list[Box]
type CircuitsType = dict[int, set[int]]


def parse_positions_list(positions_list: list[str]) -> tuple[BoxesType, CircuitsType]:
    boxes: BoxesType = []
    circuits: CircuitsType = {}
    for box_nr, row in enumerate(positions_list):
        x, y, z = map(int, row.split(","))
        boxes.append(Box((x, y, z), box_nr))
        circuits[box_nr] = set([box_nr])
    return boxes, circuits


def squared_euclidean_distance(b1: Box, b2: Box) -> int:
    # omit the SQRT (not needed for comparison)
    return (
        (b1.position[0] - b2.position[0]) ** 2
        + (b1.position[1] - b2.position[1]) ** 2
        + (b1.position[2] - b2.position[2]) ** 2
    )


def connect_circuits(boxes: BoxesType, circuits: CircuitsType, b1: Box, b2: Box) -> tuple[BoxesType, CircuitsType]:
    if b1.circuit != b2.circuit:
        new_circuit, old_circuit = b1.circuit, b2.circuit
        for box_nr in circuits[old_circuit]:
            boxes[box_nr].circuit = new_circuit
        circuits[new_circuit] |= circuits[old_circuit]
        del circuits[old_circuit]
    return boxes, circuits  # strictly not required (pass by reference), but let's make it obvious


def part_1(positions_list: list[str], number_connections: int) -> int:
    boxes, circuits = parse_positions_list(positions_list)
    distances = sorted([(squared_euclidean_distance(b1, b2), b1, b2) for b1, b2 in itertools.combinations(boxes, 2)])

    for _, b1, b2 in distances[:number_connections]:
        boxes, circuits = connect_circuits(boxes, circuits, b1, b2)

    three_largest_circuit_sizes = sorted([len(circuit) for circuit in circuits.values()], reverse=True)[:3]
    return math.prod(three_largest_circuit_sizes)


@pytest.mark.parametrize("example", EXAMPLES_PART_1)
def test_part_1(example: Example) -> None:
    assert part_1(example.positions_list, 10) == example.answer


def part_2(positions_list: list[str]) -> int:
    boxes, circuits = parse_positions_list(positions_list)
    distances = sorted([(squared_euclidean_distance(b1, b2), b1, b2) for b1, b2 in itertools.combinations(boxes, 2)])

    for _, b1, b2 in distances:
        boxes, circuits = connect_circuits(boxes, circuits, b1, b2)
        if len(circuits) == 1:
            return b1.position[0] * b2.position[0]

    return -1  # should never be reached, but make sure we always return an int


@pytest.mark.parametrize("example", EXAMPLES_PART_2)
def test_part_2(example: Example) -> None:
    assert part_2(example.positions_list) == example.answer


def main():
    print("Solution:")
    print(f"- Part 1: {part_1(puzzle_input_as_list(), 1000)}")  # 67488
    print(f"- Part 2: {part_2(puzzle_input_as_list())}")  # 3767453340


if __name__ == "__main__":
    pytest.main(["-vv", __file__])
    main()
