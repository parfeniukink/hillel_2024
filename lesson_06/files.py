from pathlib import Path
from typing import Generator, TextIO


def read_lines(filename: Path) -> Generator[str, None, None]:
    with open(file=filename) as file:
        # while line := file.readline():
        #     yield line
        while True:
            line = file.readline()
            yield line

            if not line:
                break


# Bad
def analyze_file(file: TextIO, pattern: str, strict: bool = False) -> int:
    lines: list[str] = file.readlines()
    # from pympler.asizeof import asizeof
    # print(asizeof(lines))
    # import sys
    # sys.getsizeof(lines)

    total = 0
    for line in lines:
        if strict is False:
            pattern, line = pattern.lower(), line.lower()

        if pattern in line:
            total += 1

    return total


# Good
def analyze_file_gen(
    filename: Path, pattern: str, strict: bool = False
) -> int:
    total = 0

    for line in read_lines(filename=filename):
        if strict is False:
            pattern, line = pattern.lower(), line.lower()

        if pattern in line:
            total += 1

    return total


def main():
    lesson_06_dir = Path(__file__).parent
    filename: Path = lesson_06_dir / "rockyou.txt"
    pattern: str = "apple"

    # with open(filename) as file:
    #     matches: int = analyze_file(file=file, pattern=pattern, strict=True)

    matches: int = analyze_file_gen(filename=filename, pattern=pattern)
    print(f"Analitics: matched {matches} lines")


if __name__ == "__main__":
    main()
else:
    raise SystemExit("This file is only can be executed")
