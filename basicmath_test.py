import unittest
from basicmath import div, plus, sum

class TestBasicMath(unittest.TestCase):

    def test_div(self):
        result = div(6, 3)
        self.assertEqual(result, 2)

    def test_plus(self):
        result = plus(1, 5)
        self.assertEqual(result, 6)

    def sum(self):
        sample_data = [1,2,3,4]
        result = sum(sample_data)
        self.assertEqual(result, 10)
