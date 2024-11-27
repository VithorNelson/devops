import unittest
from helloworld import print_hello_devops

class TesteHelloDevOps(unittest.TestCase):
    def test_print_devops(self):
        self.assertEqual(print('Hello, DevOps'))