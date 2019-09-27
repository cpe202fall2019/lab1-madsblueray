import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
    def test_max_list_iter1(self):
        self.assertEqual(max_list_iter([1,1,1,1,1,1,1]), 1)
    def test_max_list_iter2(self):
        self.assertEqual(max_list_iter([]), None)
    def test_max_list_iter3(self):
        self.assertEqual(max_list_iter([2,1,1,1,1,1,1]), 2)
    def test_max_list_iter4(self):
        self.assertEqual(max_list_iter([1,2,3,3,1,1,5]), 5)

    def test_reverse_rec(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(tlist)
    def test_reverse_rec1(self):
        self.assertEqual(reverse_rec([]), None)
    def test_reverse_rec2(self):
        self.assertEqual(reverse_rec([2,2,2,3,2]), [2,3,2,2,2])

    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )
    def test_bin_search1(self):
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            bin_search(0, 0, 1, tlist)
    def test_bin_search2(self):
        self.assertEqual(bin_search(1, 0, 2, []), None)
    def test_bin_search3(self):
        l = [1,2,3]
        self.assertEqual(bin_search(2, 0, len(l)-1, l), 1)
    def test_bin_search3(self):
        l = [1,2,3,4,5,7]
        self.assertEqual(bin_search(5, 0, len(l)-1, l), 4)

if __name__ == "__main__":
        unittest.main()

    
