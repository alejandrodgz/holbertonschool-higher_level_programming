#!/usr/bin/python3
'''this is a test for function max_integer in
module 6-max_integer with unittest'''

import unittest
max_integer =__import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    
    def test_max(self):
        '''test when the list have integers and max at the end'''

        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)

        '''test when len of list = 0'''

        self.assertAlmostEqual(max_integer(), None)

        '''test when the list have integers and max at the start'''

        self.assertAlmostEqual(max_integer([4, 2, 3, 1]), 4)

        '''test when the list have integers and max at the middle'''

        self.assertAlmostEqual(max_integer([4, 2, 5, 1, 3]), 5)

        '''test when the list have integers and one negative number'''

        self.assertAlmostEqual(max_integer([4, -2, 5, 1, 3]), 5)

        '''test when the list just have one number'''

        self.assertAlmostEqual(max_integer([5]), 5)

        '''test when the list just have one number'''

        self.assertAlmostEqual(max_integer([-4, -2, -5, -1, -3]), -1)