#!/usr/bin/env python3
"""
    this is a test case that
    parameterizes a unit test
"""

from utils import access_nested_map
from unittest import TestCase
from parameterized import parameterized


class TestAccessNestedMap(TestCase):
    """ class that holds the test """

    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ tests that the method returns what is supposed """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)
