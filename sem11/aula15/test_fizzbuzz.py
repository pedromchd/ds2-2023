import unittest
from fizzbuzz import robot

class FizzBuzzTest(unittest.TestCase):
    def test_say_1_when_1(self):
        self.assertEqual(robot(1), '1')

    def test_say_2_when_2(self):
        self.assertEqual(robot(2), '2')

    def test_say_4_when_4(self):
        self.assertEqual(robot(4), '4')

    def test_say_fizz_when_3(self):
        self.assertEqual(robot(3), 'Fizz')

    def test_say_fizz_when_6(self):
        self.assertEqual(robot(6), 'Fizz')

    def test_say_fizz_when_9(self):
        self.assertEqual(robot(9), 'Fizz')

    def test_say_buzz_when_5(self):
        self.assertEqual(robot(5), 'Buzz')

    def test_say_buzz_when_10(self):
        self.assertEqual(robot(10), 'Buzz')

    def test_say_buzz_when_20(self):
        self.assertEqual(robot(20), 'Buzz')

    def test_say_fizzbuzz_when_5(self):
        self.assertEqual(robot(15), 'FizzBuzz')

    def test_say_fizzbuzz_when_10(self):
        self.assertEqual(robot(30), 'FizzBuzz')

    def test_say_fizzbuzz_when_20(self):
        self.assertEqual(robot(45), 'FizzBuzz')
