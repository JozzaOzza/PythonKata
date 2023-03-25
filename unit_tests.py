import unittest
import kata_solutions as kata

class TestKataSolutions(unittest.TestCase):

    def test_simple_addition(self):
        self.assertEqual(5, kata.KataSolutions.simple_addition(2, 3))
        
if __name__ == '__main__':
    unittest.main()        