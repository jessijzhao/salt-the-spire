"""
Author: jessijzhao
Date: June 17, 2022

Test decoding and encoding save files for Slay the Spire.
"""

from typing import Callable

import pytest

from salt_the_spire import decode, encode


@pytest.mark.parametrize(
    "in_file, out_file, function",
    [
        ("tests/decoded.txt", "tests/encoded.txt", encode),
        ("tests/encoded.txt", "tests/decoded.txt", decode),
    ],
)
def test_salting(in_file: str, out_file: str, function: Callable) -> None:
    """Tests encoding/decoding a file."""

    with open(in_file, "rb") as in_file, open(out_file, "rb") as out_file:
        assert function(in_file.read()) == out_file.read()

        # decoding and encoding in any order should result in the original text
        assert encode(decode(in_file.read())) == in_file.read()
        assert decode(encode(in_file.read())) == in_file.read()
