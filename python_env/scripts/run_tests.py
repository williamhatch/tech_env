#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
运行单元测试的自动化脚本
"""

import os
import sys
import subprocess


def run_tests(coverage=True):
    """
    运行测试并可选地生成覆盖率报告
    
    Args:
        coverage: 是否生成覆盖率报告
    """
    print("正在运行测试...")
    
    cmd = ["pytest", "-v"]
    if coverage:
        cmd.extend(["--cov=src", "--cov-report", "term"])
    
    result = subprocess.run(cmd)
    return result.returncode


if __name__ == "__main__":
    # 切换到项目根目录
    os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    
    # 解析命令行参数
    coverage = True
    if len(sys.argv) > 1 and sys.argv[1] == "--no-coverage":
        coverage = False
    
    # 运行测试
    exit_code = run_tests(coverage)
    sys.exit(exit_code)
