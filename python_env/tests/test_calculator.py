#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
测试计算器模块
"""

import unittest
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):
    """
    测试计算器类的功能
    """

    def setUp(self):
        """
        每个测试方法执行前的设置
        """
        self.calc = Calculator()

    def test_add(self):
        """
        测试加法方法
        """
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)

    def test_subtract(self):
        """
        测试减法方法
        """
        self.assertEqual(self.calc.subtract(3, 2), 1)
        self.assertEqual(self.calc.subtract(1, 1), 0)
        self.assertEqual(self.calc.subtract(-1, -1), 0)

    def test_multiply(self):
        """
        测试乘法方法
        """
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(-2, 3), -6)

    def test_divide(self):
        """
        测试除法方法
        """
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        
        # 测试除以零的异常
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(5, 0)


if __name__ == '__main__':
    unittest.main()
