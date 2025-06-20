#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
字符串工具模块
"""

import re


class StringUtils:
    """
    提供字符串处理的工具类
    """

    @staticmethod
    def reverse_string(input_str):
        """
        反转字符串
        
        Args:
            input_str (str): 输入字符串
            
        Returns:
            str: 反转后的字符串
        """
        return input_str[::-1]
        
    @staticmethod
    def is_palindrome(input_str):
        """
        判断字符串是否为回文
        忽略大小写、空格和标点符号
        
        Args:
            input_str (str): 输入字符串
            
        Returns:
            bool: 如果是回文返回True，否则返回False
        """
        # 移除所有非字母数字字符并转为小写
        cleaned_str = re.sub(r'[^a-zA-Z0-9]', '', input_str).lower()
        
        # 判断清理后的字符串是否为回文
        return cleaned_str == cleaned_str[::-1]
