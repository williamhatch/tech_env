#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
序列处理工具模块
"""


class SequenceUtils:
    """
    提供序列处理的工具类
    """

    @staticmethod
    def longest_common_subsequence(str1, str2):
        """
        计算两个字符串的最长公共子序列
        
        Args:
            str1 (str): 第一个字符串
            str2 (str): 第二个字符串
            
        Returns:
            str: 最长公共子序列
        """
        # 获取两个字符串的长度
        m, n = len(str1), len(str2)
        
        # 创建一个二维数组来存储子问题的解
        # dp[i][j] 表示 str1[0...i-1] 和 str2[0...j-1] 的最长公共子序列长度
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # 填充 dp 数组
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    # 如果当前字符相同，则最长公共子序列长度加1
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # 否则，取两种可能情况的最大值
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # 重建最长公共子序列
        lcs = []
        i, j = m, n
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                # 当前字符是LCS的一部分
                lcs.append(str1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                # 向上移动
                i -= 1
            else:
                # 向左移动
                j -= 1
        
        # 因为我们是从后向前构建的，所以需要反转
        return ''.join(reversed(lcs))
