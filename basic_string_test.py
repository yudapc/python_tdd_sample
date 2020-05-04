import unittest
from basic_string import reverse

class TestBasicString(unittest.TestCase):

    def test_reverse(self):
        sample_string = "Aku adalah kamu"
        result = reverse(sample_string)
        self.assertEqual(result, "umak halada ukA")
