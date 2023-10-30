#!/usr/bin/env python3
"""Test module for client.py"""

from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, PropertyMock
from fixtures import TEST_PAYLOAD

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

    @patch('client.get_json')
    def test_public_repos(self, json_mock):
        """Tests public_repos"""
        payload = [{"name": "URL1"}, {"name": "URL2"}]
        json_mock.return_value = payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as repo_mock:

            repo_mock.return_value = "Public_repo"
            test_instance = GithubOrgClient('xyz')
            result = test_instance.public_repos()

            public_repos = [i["name"] for i in payload]
            self.assertEqual(result, public_repos)

            repo_mock.assert_called_once()
            json_mock.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, key, expected):
        """Method to test has_license"""
        self.assertEqual(GithubOrgClient.has_license(repo, key), expected)

    @parameterized_class([
        ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
        TEST_PAYLOAD
    ])
    class TestIntegrationGithubOrgClient(unittest.TestCase):
        """Class test using integration"""
        @classmethod
        def setUpClass(cls):
            """Method for setting up the class"""
            cls.get_patcher = patch('client.requests.get')
            cls.mock_get = cls.get_patcher.start()

            cls.mock_get.side_effect = [payload for payload in cls.org_payload]

        @classmethod
        def tearDownClass(cls):
            """Method for tearing down the class"""
            cls.get_patcher.stop()

        def test_public_repos(self):
            """Method to test public_repos"""
            test_instance = GithubOrgClient("test")

            public_repos = test_instance.public_repos()
            self.assertEqual(public_repos, self.expected_repos)

        def test_public_repos_with_license(self):
            """Method to test public_repos_with_license"""
            test_instance = GithubOrgClient("test")

            apache2_repos = test_instance.public_repos(license="Apache-2.0")
            self.assertEqual(apache2_repos, self.apache2_repos)
