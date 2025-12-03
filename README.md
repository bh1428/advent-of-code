# [Advent of code](https://adventofcode.com/)

Solutions for the [Advent of Code](https://adventofcode.com/) puzzles.

Code is formatted using [ruff](https://pypi.org/project/ruff/). In some code *ruff* is temporarily disabled using `# fmt: off` and `# fmt: on`.

Code is spell checked using the [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker) ([CSpell](https://cspell.org/)). Where spelling errors are expected (i.e. puzzle input) its temporarily disabled using `# cSpell: disable` and `# cSpell: enable`.

- [2025](#2025)
- [Profiling](#profiling)
  - [`pyinstrument`](#pyinstrument)
  - [`line_profiler`](#line_profiler)
  - [cProfile](#cprofile)

## 2025

- [Day 1: Secret Entrance](./2025/src/aoc2025_day01_secret_entrance.py)
- [Day 2: Gift Shop](./2025/src/aoc2025_day02_gift_shop.py)
- [Day 3: Lobby](./2025/src/aoc2025_day03_lobby.py)

## Profiling

Use a profiler to find the slowest parts of your solution. Some available options are:

1. [`pyinstrument`](https://pypi.org/project/pyinstrument/): focus on the slowest parts
2. [`line_profiler`](https://pypi.org/project/line_profiler/): line-by-line profiling of functions
3. [`cProfile`](https://docs.python.org/3/library/profile.html#module-cProfile): standard profiler included with Python

### `pyinstrument`

The [`pyinstrument`](https://pypi.org/project/pyinstrument/) profiler focuses on the slowest parts of your code. Use it like this (open `report.html` for the results):

```bash
pyinstrument -o report.html -r html my_program.py
```

### `line_profiler`

[`line_profiler`](https://pypi.org/project/line_profiler/) is a module for doing line-by-line profiling of functions. To profile a python script:

- In the relevant file(s), `import line_profiler` and decorate function(s) you want to profile with `@line_profiler.profile`.
- Set the environment variable `LINE_PROFILE=1` and run the script:
  - Windows Powershell: `$Env:LINE_PROFILE=1; python my_program.py`
  - Windows CMD: `SET LINE_PROFILE=1 && python my_program.py`
  - Linux Bash: `LINE_PROFILE=1 python3 my_program.py`
- When the script ends a summary of profile results and files is written to disk while instructions for inspecting details are written to stdout.

### cProfile

[`cProfile`](https://docs.python.org/3/library/profile.html#module-cProfile) is a profiler included with Python. The profiler gives the total running time, tells the function call frequency and much more data. To visualize the data you can use [`snakeviz`](https://pypi.org/project/snakeviz/):

```bash
python -m cProfile -o out.profile my_program.py arg1 arg2
snakeviz out.profile
```
