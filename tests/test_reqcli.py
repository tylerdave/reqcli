#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_reqcli
----------------------------------

Tests for `reqcli` module.
"""

import unittest
from click.testing import CliRunner

import reqcli.cli


class TestReqcli(unittest.TestCase):

    def setUp(self):
        self.url = 'http://www.example.com/'
        self.runner = CliRunner()

    def test_basic_invocation(self):
        result = self.runner.invoke(reqcli.cli.cli, [self.url])
        assert result.exit_code == 0
        # FIXME: mock out requests and assert based on mock response
        # assert result.output == "Hello, world!\n"

    def tearDown(self):
        pass
