import unittest
from sqrt import lazy_sqrt, builtin_sqrt, newton_sqrt1


class SqrtTest(unittest.TestCase):
    """obligatory docstring"""
    def test_sqrt9(self):
        self.assertEqual(newton_sqrt1(9), 3)
    """Checks to see if the sqrt expression is almost equal to 1.414, but fails"""
    def test_sqrt2(self):
        self.assertAlmostEqual(newton_sqrt1(2), 1.4142)

if __name__ == '__main__':
    unittest.main()
