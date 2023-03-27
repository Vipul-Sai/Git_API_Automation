import pytest
import unittest
from Git_API.GitAPI import Gitflow

class Git(unittest.TestCase):


    def test_git(self):
        g = Gitflow()
        g.user_login()
        g.create_repository()
        g.create_branch_main()
        g.create_branch()
        g.create_file_in_branch()
        g.pull_request()
        g.update_file_in_branch()
        g.rename_branch()
        g.delete_repo()
