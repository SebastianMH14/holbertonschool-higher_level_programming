#!/usr/bin/python3
"""Unittest for max_integer([..])"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """class for test max integer"""
    def test_listmax(self):
        self.assertEqual(max_integer([1, 2, 10000]), 10000)
        self.assertEqual(max_integer([2]), 2)
        self.assertEqual(max_integer([-30, -10, -40]), -10)
        self.assertIsNone(max_integer([]))
        self.assertEqual(max_integer([30, 10, 20]), 30)
