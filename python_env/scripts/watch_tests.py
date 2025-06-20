#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
监视文件变化并自动运行测试的脚本
"""

import os
import sys
import time
import subprocess
from pathlib import Path


def run_pytest_watch():
    """
    使用pytest-watch监视文件变化并自动运行测试
    """
    print("启动测试监视器...")
    print("监视src和tests目录中的文件变化...")
    print("按Ctrl+C退出")
    
    # 使用pytest-watch运行测试
    cmd = ["ptw", "--clear", "--runner", "pytest -v", "src", "tests"]
    subprocess.run(cmd)


def check_directories():
    """
    检查必要的目录是否存在，如果不存在则创建
    """
    project_root = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    src_dir = project_root / "src"
    tests_dir = project_root / "tests"
    
    # 确保src目录存在
    if not src_dir.exists():
        print(f"创建源代码目录: {src_dir}")
        src_dir.mkdir(parents=True, exist_ok=True)
        
        # 创建__init__.py文件以使其成为包
        init_file = src_dir / "__init__.py"
        if not init_file.exists():
            init_file.touch()
    
    # 确保tests目录存在
    if not tests_dir.exists():
        print(f"创建测试目录: {tests_dir}")
        tests_dir.mkdir(parents=True, exist_ok=True)
        
        # 创建__init__.py文件以使其成为包
        init_file = tests_dir / "__init__.py"
        if not init_file.exists():
            init_file.touch()


if __name__ == "__main__":
    # 切换到项目根目录
    os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    
    # 检查并创建必要的目录
    check_directories()
    
    # 运行测试监视器
    run_pytest_watch()
