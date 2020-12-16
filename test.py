# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 21:11:39 2020

@author: rodzina
"""

import unittest

from program import conflict, dtime

M1ST = dtime("8:15am")
M1ET = dtime("8:25am")
M2ST = dtime("7:15am")
M2ET = dtime("9:25am")
M3ST = dtime("7:00am")
M3ET = dtime("8:20am")
M4ST = dtime("6:00am")
M4ET = dtime("7:00am")

class TestConflict(unittest.TestCase):
    """Unit test class"""
    def test_conflict11(self):
        """
        Test meeting m1 conflicts with itself
        """
        result = conflict(M1ST, M1ET, M1ST, M1ET)
        self.assertTrue(result)

    def test_conflict12(self):
        """
        Test meeting m1 conflicts with m2
        """
        result = conflict(M1ST, M1ET, M2ST, M2ET)
        self.assertTrue(result)

    def test_conflict21(self):
        """
        Test as 12 but switch meetings
        """
        result = conflict(M2ST, M2ET, M1ST, M1ET)
        self.assertTrue(result)

    def test_conflict31(self):
        """
        Test meeting m3 conflicts with m1
        """
        result = conflict(M3ST, M3ET, M1ST, M1ET)
        self.assertTrue(result)

    def test_conflict13(self):
        """
        Test as31 but switch meetings
        """
        result = conflict(M1ST, M1ET, M3ST, M3ET)
        self.assertTrue(result)

    def test_conflict42(self):
        """
        Test no conflict
        """
        result = conflict(M4ST, M4ET, M2ST, M2ET)
        self.assertFalse(result)

    def test_conflict24(self):
        """
        Test as above but switch meetings
        """
        result = conflict(M2ST, M2ET, M4ST, M4ET)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
