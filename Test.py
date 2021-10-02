"""
Date:10/02/2021
@author: Emay Pandarakutty
email: epandar@stevens.edu

Test for the main file.
"""
import unittest
from Main import get_repos, get_commits, main

user_id = 'Emay-Pandarakutty'
invalid_user_id = 'Pandarakutty'

class Test_Main(unittest.TestCase):
    def test_get_repos_valid(self):
        self.assertEqual(get_repos(user_id), ['HW04', 'ssw555b_team7', 'SSW567-HW00', 'Triangle567'])

    def test_get_repos_invalid(self):
        self.assertEqual(get_repos(invalid_user_id), 'repo url error')

    def test_get_commits_valid(self):
        self.assertEqual(get_commits(user_id, 'ssw555b_team7'), 'Repo: ssw555b_team7  Number of commits: 30')
        self.assertEqual(get_commits(user_id, 'SSW567-HW00'), 'Repo: SSW567-HW00  Number of commits: 5')

    def test_get_commits_invalid(self):
        self.assertEqual(get_commits(user_id, 'SSW567-HW05'), 'commit url error')

    def test_main(self):
        self.assertEqual(main(user_id), None)


if __name__ == '__main__':
    unittest.main()
