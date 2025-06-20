#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
简单计算器模块示例
"""


class Calculator:
    """
    实现基本数学运算的计算器类
    """

    def add(self, a, b):
        """
        计算两个数的和
        
        Args:
            a: 第一个数
            b: 第二个数
        
        Returns:
            两个数的和
        """
        return a + b

    def subtract(self, a, b):
        """
        计算两个数的差
        
        Args:
            a: 第一个数
            b: 第二个数
        
        Returns:
            两个数的差
        """
        return a - b

    def multiply(self, a, b):
        """
        计算两个数的乘积
        
        Args:
            a: 第一个数
            b: 第二个数
        
        Returns:
            两个数的乘积
        """
        return a * b

    def divide(self, a, b):
        """
        计算两个数的商
        
        Args:
            a: 第一个数
            b: 第二个数
        
        Returns:
            两个数的商
        
        Raises:
            ZeroDivisionError: 当除数为零时抛出
        """
        if b == 0:
            raise ZeroDivisionError("除数不能为零")
        return a / b
