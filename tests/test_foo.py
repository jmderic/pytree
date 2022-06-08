# test_foo.py
from pathlib import PurePath
from unittest import mock
import pytest
from pytest_mock import MockerFixture
from _pytest.capture import capsys

from pytree.lib.tree.__main__ import walk_and_print

# from pytest import capsy
def foo():
    print("lol")

# @mock.patch('builtins.print')
def test_foo(mocker: MockerFixture, capsys) -> None:
    foo()
    captured,_ = capsys.readouterr()
    # print.assert_called()
    assert(captured=="lol\n")


def test_walk_and_print(capsys) -> None:
    from pytree.lib.tree import __main__.walk_and_print as wp
    wp('tests', print_files=True)
