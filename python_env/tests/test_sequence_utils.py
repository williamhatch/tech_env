#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
测试序列处理工具模块
"""

import unittest
from src.sequence_utils import SequenceUtils


class TestSequenceUtils(unittest.TestCase):
    """
    测试SequenceUtils类的功能
    """

    def test_longest_common_subsequence(self):
        """
        测试最长公共子序列方法
        """
        # 测试基本情况
        self.assertEqual(SequenceUtils.longest_common_subsequence("abc", "ac"), "ac")
        self.assertEqual(SequenceUtils.longest_common_subsequence("abcde", "ace"), "ace")
        
        # 测试无公共子序列
        self.assertEqual(SequenceUtils.longest_common_subsequence("abc", "def"), "")
        
        # 测试空字符串
        self.assertEqual(SequenceUtils.longest_common_subsequence("", "abc"), "")
        self.assertEqual(SequenceUtils.longest_common_subsequence("abc", ""), "")
        self.assertEqual(SequenceUtils.longest_common_subsequence("", ""), "")
        
        # 测试相同字符串
        self.assertEqual(SequenceUtils.longest_common_subsequence("abcde", "abcde"), "abcde")
        
        # 测试包含重复字符的字符串
        self.assertEqual(SequenceUtils.longest_common_subsequence("aabcc", "abc"), "abc")
        
        # 测试较长的字符串
        self.assertEqual(
            SequenceUtils.longest_common_subsequence(
                "XMJYAUZ", "MZJAWXU"), "MJAU")
        
        # 测试中文字符串
        self.assertEqual(
            SequenceUtils.longest_common_subsequence(
                "我爱中国", "我是中国人"), "我中国")


if __name__ == '__main__':
    unittest.main()
