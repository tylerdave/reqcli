#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_reqcli
----------------------------------

Tests for `reqcli` module.
"""

import unittest

import reqcli


class TestReqcli(unittest.TestCase):

    def setUp(self):
        pass

    def test_hello_world_runs(self):
        assert(reqcli.hello_world())

    def tearDown(self):
        pass
