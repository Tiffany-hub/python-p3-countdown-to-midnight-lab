import io
import sys
import time
import unittest
from countdown import countdown, countdown_with_sleep

class TestCountdown(unittest.TestCase):

    def test_counts_down_prints_happy_new_year(self):
        '''counts down from number and prints "HAPPY NEW YEAR!"'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        countdown(5)
        sys.stdout = sys.__stdout__
        expected_output = "5 SECOND(S)!\n4 SECOND(S)!\n3 SECOND(S)!\n2 SECOND(S)!\n1 SECOND(S)!\nHAPPY NEW YEAR!"
        self.assertEqual(captured_out.getvalue().strip(), expected_output)

    def test_counts_down_prints_happy_new_year_with_sleep(self):
        '''counts down from number and prints "HAPPY NEW YEAR!" with sleep'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        countdown_with_sleep(5)
        sys.stdout = sys.__stdout__
        expected_output = "5 SECOND(S)!\n4 SECOND(S)!\n3 SECOND(S)!\n2 SECOND(S)!\n1 SECOND(S)!\nHAPPY NEW YEAR!"
        self.assertEqual(captured_out.getvalue().strip(), expected_output)

if __name__ == '__main__':
    unittest.main()
