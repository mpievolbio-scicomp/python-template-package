#!/usr/bin/env python
"""Tests for `template` package."""

import pytest
from click.testing import CliRunner

from template import cli



def test_equal(response):
    """Test equality."""

    received = 1
    expected = 1

    assert received == expected


def test_lists_equal():
    """ Test that two lists are equal."""

    received = ["ACTG"]
    expected = ["ACTG"]
    assert received == expected
    
def test_cli():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'python-template-package' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
