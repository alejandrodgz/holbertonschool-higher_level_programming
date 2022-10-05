#!/usr/bin/python3
'''this is a test for function max_integer in
module 6-max_integer with unittest'''

import unittest
max_integer =__import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    
    def test_max(self):
        '''test when the list have integers'''

        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)

        '''test when len of list = 0'''

        self.assertAlmostEqual(max_integer(), None)