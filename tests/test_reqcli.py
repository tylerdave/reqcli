#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_reqcli
----------------------------------

Tests for `reqcli` module.
"""

import requests
import unittest
from click.testing import CliRunner
try:
    import mock
except ImportError:
    from unittest import mock

import reqcli.cli

class MockResponse(requests.Response):

    def __init__(self, status_code=None, content=None, headers=None):
        super(MockResponse, self).__init__()
        if status_code is not None:
            self.status_code = status_code
        if content is not None:
            self._content = str.encode(content)
        if headers is not None:
            self.headers = headers

hello_world_response = MockResponse(
        status_code=200,
        content='Hello, world!',
        headers={'Reqcli-Example':'Example Value'})

class TestReqcli(unittest.TestCase):

    def setUp(self):
        self.url = 'http://www.example.com/testing'
        self.runner = CliRunner()

    @mock.patch('requests.get',
            mock.Mock(return_value=hello_world_response))
    def test_basic_invocation(self):
        result = self.runner.invoke(reqcli.cli.cli, [self.url])
        assert result.output == "Hello, world!\n"
        assert result.exit_code == 0

    @mock.patch('requests.get',
            mock.Mock(return_value=hello_world_response))
    def test_showing_status(self):
        result = self.runner.invoke(reqcli.cli.cli, [self.url, '--show-status'])
        assert "Status: 200\n" in result.output
        assert result.exit_code == 0

    @mock.patch('requests.get',
            mock.Mock(return_value=hello_world_response))
    def test_showing_headers(self):
        result = self.runner.invoke(reqcli.cli.cli, [self.url, '--show-headers'])
        assert "Reqcli-Example: Example Value" in result.output
        assert result.exit_code == 0


    def tearDown(self):
        pass
