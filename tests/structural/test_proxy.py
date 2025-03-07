import sys
import unittest
from io import StringIO

from patterns.structural.proxy import Proxy, client


class ProxyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Class scope setup."""
        cls.proxy = Proxy()

    def setUp(self):
        """Function/test case scope setup."""
        self.output = StringIO()
        self.saved_stdout = sys.stdout
        sys.stdout = self.output

    def tearDown(self):
        """Function/test case scope teardown."""
        self.output.close()
        sys.stdout = self.saved_stdout

    def test_do_the_job_for_admin_shall_pass(self):
        client(self.proxy, "admin")
        assert self.output.getvalue() == (
            "[log] Doing the job for admin is requested.\n"
            "I am doing the job for admin\n"
        )

    def test_do_the_job_for_anonymous_shall_reject(self):
        client(self.proxy, "anonymous")
        assert self.output.getvalue() == (
            "[log] Doing the job for anonymous is requested.\n"
            "[log] I can do the job just for `admins`.\n"
        )
