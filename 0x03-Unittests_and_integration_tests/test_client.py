#!/usr/bin/env python3
"""Test module for client.py"""

from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import patch, PropertyMock

import unittest


class TestGithubOrgClient(unittest.TestCase):
    """Class that tests GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock):
        """Method to test org"""
        test_instance = GithubOrgClient(org_name)
        test_instance.org()
        mock.assert_called_once_with(f'https://api.github.com/orgs/{org_name}')

    def test_public_repos_url(self):
        """Method to test _public_repos_url"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock:
            payload = {"repos_url": "Test"}
            mock.return_value = payload
            test_instance = GithubOrgClient('xyz')
            result = test_instance._public_repos_url
            self.assertEqual(result, payload["repos_url"])
