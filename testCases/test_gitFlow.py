import pytest
import unittest
from Git_API.GitAPI import Gitflow

class Git(unittest.TestCase):


    def test_git(self):
        g = Gitflow()
        g.get_user()
        g.post_create_repos()
        g.put_main_branch()
        g.createBranch_Post()
        g.createFileInBranch()
        g.pull_request()
        g.updateFileinBranch()
