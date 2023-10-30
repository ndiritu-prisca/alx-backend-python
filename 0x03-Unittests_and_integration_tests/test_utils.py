#!/usr/bin/env python3
"""Module for TestAccessNestedMap"""

from parameterized import parameterized
from utils import access_nested_map, get_json
from unittest.mock import patch, Mock

import unittest
import requests


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

    @parameterized.expand([
        ({}, ("a"), "'a'"),
        ({"a": 1}, ("a", "b"), "'b'"),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_msg):
        """A method to test access_nested_map_exception"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), expected_msg)


class TestGetJson(unittest.TestCase):
    """A class that tests GETJSON"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """Method that tests get_json"""
        with patch('requests.get') as mock:
            mock.return_value.json.return_value = test_payload
            self.assertEqual(get_json(url=test_url), test_payload)
