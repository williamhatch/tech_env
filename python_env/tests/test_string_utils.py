#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
测试字符串工具模块
"""

import unittest
from src.string_utils import StringUtils


class TestStringUtils(unittest.TestCase):
    """
    测试StringUtils类的功能
    """

    def test_reverse_string(self):
        """
        测试字符串反转方法
        """
        # 测试普通字符串
        self.assertEqual(StringUtils.reverse_string("hello"), "olleh")
        
        # 测试空字符串
        self.assertEqual(StringUtils.reverse_string(""), "")
        
        # 测试包含空格的字符串
        self.assertEqual(StringUtils.reverse_string("hello world"), "dlrow olleh")
        
        # 测试包含特殊字符的字符串
        self.assertEqual(StringUtils.reverse_string("hello!@#"), "#@!olleh")
        
        # 测试包含中文的字符串
        self.assertEqual(StringUtils.reverse_string("你好世界"), "界世好你")
    
    def test_is_palindrome(self):
        """
        测试回文检测方法
        """
        # 测试普通回文
        self.assertTrue(StringUtils.is_palindrome("level"))
        self.assertTrue(StringUtils.is_palindrome("radar"))
        
        # 测试非回文
        self.assertFalse(StringUtils.is_palindrome("hello"))
        self.assertFalse(StringUtils.is_palindrome("world"))
        
        # 测试空字符串（空字符串视为回文）
        self.assertTrue(StringUtils.is_palindrome(""))
        
        # 测试带有空格和标点的回文
        self.assertTrue(StringUtils.is_palindrome("A man, a plan, a canal: Panama"))
        self.assertTrue(StringUtils.is_palindrome("Race car"))
        
        # 测试带有大小写混合的回文
        self.assertTrue(StringUtils.is_palindrome("Able was I ere I saw Elba"))
        
        # 测试带有数字的回文
        self.assertTrue(StringUtils.is_palindrome("12321"))
        self.assertFalse(StringUtils.is_palindrome("12345"))
        
        # 测试中文回文
        self.assertTrue(StringUtils.is_palindrome("上海自来水来自海上"))


if __name__ == '__main__':
    unittest.main()
