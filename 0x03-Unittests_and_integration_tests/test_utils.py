#!/usr/bin/env python3
"""Module for TestAccessNestedMap"""

from parameterized import parameterized
from utils import access_nested_map

import unittest


class TestAccessNestedMap(unittest.TestCase):
    """Class that tests AccessNestedMap"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ])
    def test_access_nested_map(self, nested_map, path, expected):
        """A method to test access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
