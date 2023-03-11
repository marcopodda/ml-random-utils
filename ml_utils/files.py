"""Utilities to handle files."""

from pathlib import Path


def read_lines(path: str | Path, encoding: str | None = "utf-8") -> list[str]:
    """
    Reads file lines by stripping out breaklines and trailing empty lines.

    Arguments:
        path: the path to open as a file.
        encoding: the desired encoding

    Returns:
        lines: a list with one element for each file line.
    """
    with open(path, "r", encoding=encoding) as file:
        lines = [line.rstrip() for line in file.readlines()]

    # get rid of trailing empty lines if any
    if lines[-1] == "":
        lines = lines[:-1]

    return lines
