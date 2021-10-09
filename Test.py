"""
Date:10/09/2021
@author: Emay Pandarakutty
email: epandar@stevens.edu

Test for the main file.
"""
import unittest
from unittest import mock
from Main import get_repos, get_commits, main

user_id = 'Emay-Pandarakutty'
invalid_user_id = 'Pandarakutty'


class Test_Main(unittest.TestCase):
    # decorator mock
    @mock.patch('Main.get_repos', return_value=['HW04', 'ssw555b_team7', 'SSW567-HW00', 'Triangle567'])
    def test_get_repos_valid(self, mock_get_repos):
        self.assertEqual(get_repos(user_id), ['HW04', 'ssw555b_team7', 'SSW567-HW00', 'Triangle567'])

    @mock.patch('Main.get_repos', return_value=r'repo url error')
    def test_get_repos_invalid(self, mock_get_repos):
        self.assertEqual(get_repos(invalid_user_id), 'repo url error')

    @mock.patch('Main.get_commits', return_value='Repo: ssw555b_team7  Number of commits: 30')
    def test_get_commits_valid(self, mock_get_commit):
        self.assertEqual(get_commits(user_id, 'ssw555b_team7'), 'Repo: ssw555b_team7  Number of commits: 30')
        # context Manger mock
        with mock.patch('Main.get_commits', return_value=r'Repo: SSW567-HW00  Number of commits: 5'):
            self.assertEqual(get_commits(user_id, 'SSW567-HW00'), 'Repo: SSW567-HW00  Number of commits: 5')

    # context Manger mock
    def test_get_commits_invalid(self):
        with mock.patch('Main.get_commits', return_value=r'commit url error'):
            self.assertEqual(get_commits(user_id, 'SSW567-HW05'), 'commit url error')

    # decorator mock
    @mock.patch('Main.main', return_value=None)
    def test_main(self, mock_main):
        self.assertEqual(main(user_id), None)


if __name__ == '__main__':
    unittest.main()
