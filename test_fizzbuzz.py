import unittest
from fizzbuzz import FizzBuzz


class TestFizzBuzz(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(FizzBuzz.of(1), '1')

    def test_div_3(self):
        self.assertEqual(FizzBuzz.of(3), 'Fizz')

    def test_div_5(self):
        self.assertEqual(FizzBuzz.of(5), 'Buzz')

    def test_div_3_5(self):
        self.assertEqual(FizzBuzz.of(15), 'FizzBuzz')


if __name__ == '__main__':
    unittest.main()
