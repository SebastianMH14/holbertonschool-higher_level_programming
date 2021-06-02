#!/usr/bin/python3
"""a class MyInt that
inherits from int:"""


class MyInt(int):
    """clase heredada de int"""

    def __ne__(self, x):
        """compare ne"""
        return True

    def __eq__(self, x):
        """compare eq"""
        return False
