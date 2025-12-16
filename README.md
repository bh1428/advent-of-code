# [Advent of code][advent_of_code]

Solutions for the [Advent of Code][advent_of_code] puzzles.

Code is formatted using [ruff][ruff]. In some code *ruff* is temporarily disabled using `# fmt: off` and `# fmt: on`.

Code is spell checked using the [Code Spell Checker][vsc_code_spell_checker] ([CSpell][cspell]). Where spelling errors are expected (i.e. puzzle input) its temporarily disabled using `# cSpell: disable` and `# cSpell: enable`.

- [2025](#2025)
- [Performance optimization](#performance-optimization)
  - [`pyinstrument`](#pyinstrument)
  - [`line_profiler`](#line_profiler)
  - [cProfile](#cprofile)
  - [`dis` module](#dis-module)

## 2025

- [Day 1: Secret Entrance][aoc2025_01]
- [Day 2: Gift Shop][aoc2025_02]
- [Day 3: Lobby][aoc2025_03]
- [Day 4: Printing Department][aoc2025_04]
- [Day 5: Cafeteria][aoc2025_05]
- [Day 6: Trash Compactor][aoc2025_06]
- [Day 7: Laboratories][aoc2025_07]

## Performance optimization

You can use a profiler to find the slowest parts of your solution. Some available options are:

1. [`pyinstrument`][pyinstrument]: focus on the slowest parts
2. [`line_profiler`][line_profiler]: line-by-line profiling of functions
3. [`cProfile`][cprofile]: standard profiler included with Python

As an alternative, use the [`dis`][dis_module] module to disassemble a function to [bytecode][bytecode].

### `pyinstrument`

The [`pyinstrument`][pyinstrument] profiler focuses on the slowest parts of your code. Use it like this (open `report.html` for the results):

```bash
pyinstrument -o report.html -r html my_program.py
```

### `line_profiler`

[`line_profiler`][line_profiler] is a module for doing line-by-line profiling of functions. To profile a python script:

- In the relevant file(s), `import line_profiler` and decorate function(s) you want to profile with `@line_profiler.profile`.
- Set the environment variable `LINE_PROFILE=1` and run the script:
  - Windows Powershell: `$Env:LINE_PROFILE=1; python my_program.py`
  - Windows CMD: `SET LINE_PROFILE=1 && python my_program.py`
  - Linux Bash: `LINE_PROFILE=1 python3 my_program.py`
- When the script ends a summary of profile results and files is written to disk while instructions for inspecting details are written to stdout.

### cProfile

[`cProfile`][cprofile] is a profiler included with Python. The profiler gives the total running time, tells the function call frequency and much more data. To visualize the data you can use [`snakeviz`][snakeviz]:

```bash
python -m cProfile -o out.profile my_program.py arg1 arg2
snakeviz out.profile
```

### `dis` module

The [`dis`][dis_module] module supports the analysis of CPython [bytecode][bytecode] by disassembling it. While it's typically not the first tool you would turn to, it becomes valuable when a profiler indicates that something is running slowly and you want to find out more details.

Use it like this:

```python
import dis

def some_function():
    print("Hello World!")

dis.dis(some_function)
```

Which will then print:

```text
  4           RESUME                   0

  5           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST               1 ('Hello World!')
              CALL                     1
              POP_TOP
              RETURN_CONST             0 (None)
```

Refer to the [Python Bytecode Instructions][python_bytecode_instructions] documentation when you really want to know what's happening. However, you will already get a good impression by simply scanning the disassembled bytecode.

[advent_of_code]: https://adventofcode.com/
[aoc2025_01]: ./2025/aoc2025_day01_secret_entrance.py
[aoc2025_02]: ./2025/aoc2025_day02_gift_shop.py
[aoc2025_03]: ./2025/aoc2025_day03_lobby.py
[aoc2025_04]: ./2025/aoc2025_day04_printing_department.py
[aoc2025_05]: ./2025/aoc2025_day05_cafeteria.py
[aoc2025_06]: ./2025/aoc2025_day06_trash_compactor.py
[aoc2025_07]: ./2025/aoc2025_day07_laboratories.py
[bytecode]: https://docs.python.org/3/glossary.html#term-bytecode
[cprofile]: https://docs.python.org/3/library/profile.html#module-cProfile
[cspell]: https://cspell.org/
[dis_module]: https://docs.python.org/3/library/dis.html
[line_profiler]: https://pypi.org/project/line_profiler/
[pyinstrument]: https://pypi.org/project/pyinstrument/
[python_bytecode_instructions]: https://docs.python.org/3/library/dis.html#python-bytecode-instructions
[ruff]: https://pypi.org/project/ruff/
[snakeviz]: https://pypi.org/project/snakeviz/
[vsc_code_spell_checker]: https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker
