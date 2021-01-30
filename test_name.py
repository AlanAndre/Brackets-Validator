import unittest
from main import is_matched


class Test(unittest.TestCase):
    def test_balanced(self):
        self.assertTrue(is_matched('[]'))
        self.assertTrue(is_matched('[]{{}}'))
        self.assertTrue(is_matched('[]{{{}}}'))
        self.assertTrue(is_matched('[]{{{[]}}}'))
        self.assertTrue(is_matched('[](){{{[]}}}'))

    def test_unbalanced(self):
        self.assertFalse(is_matched(')'))
        self.assertFalse(is_matched(']'))
        self.assertFalse(is_matched('}'))
        self.assertFalse(is_matched('[)'))
        self.assertFalse(is_matched('[]()()(()'))
        self.assertFalse(is_matched('[]()()((())'))
        self.assertFalse(is_matched('[]()()(((()))'))
        self.assertFalse(is_matched('[]()()(((([])))'))


if __name__ == '__main__':
    unittest.main()
