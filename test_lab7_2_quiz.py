import unittest
from lab7_2_quiz import perfect_numbers

class TestPerfectNumbers(unittest.TestCase):
    def test_first_three_perfect_numbers(self):
        """Test if the generator correctly yields the first three perfect numbers."""
        gen = perfect_numbers()
        expected = [6, 28, 496]
        for e in expected:
            self.assertEqual(next(gen), e)


if __name__ == '__main__':
    unittest.main()
