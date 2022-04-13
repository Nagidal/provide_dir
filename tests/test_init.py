#!/usr/bin/env python


from remove_directory import rmdir
import os
from pathlib import Path
from provide_dir import provide_dir
from provide_dir import core_provide_dir


test_dir = Path(os.getenv("temp")) / "pytest_provide_dir"


def test_provide_dir(capsys):
    if test_dir.exists():
        rmdir(test_dir)
    provide_dir(test_dir)
    assert test_dir.is_dir()
    assert test_dir.exists()
    rmdir(test_dir)
    assert not test_dir.exists()


def test_provide_dir_with_sink(capsys):
    if test_dir.exists():
        rmdir(test_dir)
    provide_dir(test_dir, print)
    captured = capsys.readouterr()
    assert "was created" in captured.out
    assert test_dir.is_dir()
    assert test_dir.exists()
    provide_dir(test_dir, print)
    captured = capsys.readouterr()
    assert "already exists" in captured.out
    assert test_dir.is_dir()
    assert test_dir.exists()
    rmdir(test_dir)
    assert not test_dir.exists()


def test_core_provide_dir():
    if test_dir.exists():
        rmdir(test_dir)
    was_created = core_provide_dir(test_dir)
    assert was_created
    assert test_dir.is_dir()
    assert test_dir.exists()
    rmdir(test_dir)
    assert not test_dir.exists()
