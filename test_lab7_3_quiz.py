import unittest
import time
from lab7_3_quiz import TotalExecutionTime

class TestTotalExecutionTime(unittest.TestCase):

    @TotalExecutionTime
    def dummy_function(self, sleep_time):
        """Prosta funkcja do testowania, która czeka przez określony czas."""
        time.sleep(sleep_time)
        return sleep_time

    def test_multiple_executions(self):
        """Test sprawdzający sumę czasów z wielokrotnych wywołań funkcji."""
        total_sleep_time = 0
        for i in range(0, 3):
            self.dummy_function(i)
            total_sleep_time += i
        measured_time = self.dummy_function.get_total_execution_time()
        self.assertTrue(measured_time >= total_sleep_time)

if __name__ == '__main__':
    unittest.main()
