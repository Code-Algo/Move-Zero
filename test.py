from unittest import TestCase, main
from operationmovezero import MoveZero, end_zed

class MoveZeroTestCase(TestCase):
    def test_1_array_1(self):
        self.assertEqual(end_zed.move_zero([0, 1, 0, 3, 12]), [1, 3, 12, 0, 0])

    def test_2_array_2(self):
        self.assertEqual(end_zed.move_zero([1, 7, 0, 0, 8, 0, 10, 12, 0, 4]), [1, 7, 8, 10, 12, 4, 0, 0, 0, 0])
    
    def test_3_array_3(self):
        self.assertEqual(end_zed.move_zero([0,0,0,0,0,0,0,0,0]), [0,0,0,0,0,0,0,0,0])