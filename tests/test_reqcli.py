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

    def test_something(self):
        assert(reqcli.hello_world())
        pass

    def tearDown(self):
        pass
