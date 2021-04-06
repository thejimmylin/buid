import unittest
from .buid import BUID


class TestStringMethods(unittest.TestCase):

    def test_is_instance(self):
        b = BUID()
        self.assertIsInstance(b, BUID)

    def test_invalid_input(self):
        with self.assertRaises(AssertionError):
            BUID('aaaa-bbbb-cccc-dddd', format='CVCV-CVCV-CVCV-CVCV')


if __name__ == '__main__':
    unittest.main()
