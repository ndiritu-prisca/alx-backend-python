#!/usr/bin/env python3
"""Test module for client.py"""

from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import patch, Mock

import unittest


class TestGithubOrgClient(unittest.TestCase):
    """Class that tests GithubOrgClient"""

    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock):
        """Method to test org"""
        test_instance = GithubOrgClient(org_name)
        test_instance.org()
        mock.assert_called_once_with(f'https://api.github.com/orgs/{org_name}')
