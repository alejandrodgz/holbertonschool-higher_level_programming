#test for base

import unittest
from models import rectangle
from models import square
from models import base

class Testbase(unittest.TestCase):
    def test_idbase(self):
         self.assertTrue(base.Base(999), self.id == 999)
        