#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
自动生成测试模板的脚本
"""

import os
import sys
import inspect
import importlib
from pathlib import Path


def generate_test_template(module_name):
    """
    为指定模块生成测试模板
    
    Args:
        module_name: 模块名称，例如 'calculator' 或 'src.calculator'
    
    Returns:
        bool: 是否成功生成测试
    """
    try:
        # 如果没有提供完整路径，假设它在src目录中
        if '.' not in module_name:
            module_name = f"src.{module_name}"
        
        # 尝试导入模块
        module = importlib.import_module(module_name)
        
        # 获取模块中的所有类
        classes = inspect.getmembers(module, inspect.isclass)
        
        if not classes:
            print(f"警告: 在模块 {module_name} 中没有找到类")
            return False
        
        # 为每个类生成测试文件
        for class_name, class_obj in classes:
            # 跳过导入的类
            if class_obj.__module__ != module.__name__:
                continue
            
            # 确定测试文件路径
            test_file_name = f"test_{module_name.split('.')[-1]}_{class_name.lower()}.py"
            test_file_path = Path("tests") / test_file_name
            
            # 如果测试文件已存在，询问是否覆盖
            if test_file_path.exists():
                print(f"测试文件 {test_file_path} 已存在。")
                choice = input("是否覆盖? (y/n): ").strip().lower()
                if choice != 'y':
                    continue
            
            # 获取类的所有方法
            methods = inspect.getmembers(class_obj, inspect.isfunction)
            
            # 生成测试类内容
            test_content = [
                f"#!/usr/bin/env python",
                f"# -*- coding: utf-8 -*-",
                f"\"\"\"",
                f"测试 {module_name}.{class_name} 类",
                f"\"\"\"",
                f"",
                f"import unittest",
                f"from {module_name} import {class_name}",
                f"",
                f"",
                f"class Test{class_name}(unittest.TestCase):",
                f"    \"\"\"",
                f"    测试 {class_name} 类的功能",
                f"    \"\"\"",
                f"",
                f"    def setUp(self):",
                f"        \"\"\"",
                f"        每个测试方法执行前的设置",
                f"        \"\"\"",
                f"        self.instance = {class_name}()",
                f"",
            ]
            
            # 为每个方法生成测试方法
            for method_name, method_obj in methods:
                # 跳过私有方法和特殊方法
                if method_name.startswith('_'):
                    continue
                
                test_content.extend([
                    f"    def test_{method_name}(self):",
                    f"        \"\"\"",
                    f"        测试 {method_name} 方法",
                    f"        \"\"\"",
                    f"        # TODO: 实现测试用例",
                    f"        self.assertTrue(True)  # 替换为实际测试",
                    f"",
                ])
            
            # 添加main函数
            test_content.extend([
                f"",
                f"if __name__ == '__main__':",
                f"    unittest.main()",
            ])
            
            # 写入测试文件
            with open(test_file_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(test_content))
            
            print(f"已生成测试文件: {test_file_path}")
        
        return True
    
    except ImportError:
        print(f"错误: 无法导入模块 {module_name}")
        print("请确保模块存在并且可以被导入")
        return False
    
    except Exception as e:
        print(f"生成测试模板时发生错误: {e}")
        return False


def create_example_module():
    """
    创建示例模块，用于演示
    """
    src_dir = Path("src")
    if not src_dir.exists():
        src_dir.mkdir(parents=True, exist_ok=True)
    
    # 创建__init__.py
    init_file = src_dir / "__init__.py"
    if not init_file.exists():
        init_file.touch()
    
    # 创建示例模块
    example_file = src_dir / "calculator.py"
    
    example_content = [
        "#!/usr/bin/env python",
        "# -*- coding: utf-8 -*-",
        "\"\"\"",
        "简单计算器模块示例",
        "\"\"\"",
        "",
        "",
        "class Calculator:",
        "    \"\"\"",
        "    实现基本数学运算的计算器类",
        "    \"\"\"",
        "",
        "    def add(self, a, b):",
        "        \"\"\"",
        "        计算两个数的和",
        "        ",
        "        Args:",
        "            a: 第一个数",
        "            b: 第二个数",
        "        ",
        "        Returns:",
        "            两个数的和",
        "        \"\"\"",
        "        return a + b",
        "",
        "    def subtract(self, a, b):",
        "        \"\"\"",
        "        计算两个数的差",
        "        ",
        "        Args:",
        "            a: 第一个数",
        "            b: 第二个数",
        "        ",
        "        Returns:",
        "            两个数的差",
        "        \"\"\"",
        "        return a - b",
        "",
        "    def multiply(self, a, b):",
        "        \"\"\"",
        "        计算两个数的乘积",
        "        ",
        "        Args:",
        "            a: 第一个数",
        "            b: 第二个数",
        "        ",
        "        Returns:",
        "            两个数的乘积",
        "        \"\"\"",
        "        return a * b",
        "",
        "    def divide(self, a, b):",
        "        \"\"\"",
        "        计算两个数的商",
        "        ",
        "        Args:",
        "            a: 第一个数",
        "            b: 第二个数",
        "        ",
        "        Returns:",
        "            两个数的商",
        "        ",
        "        Raises:",
        "            ZeroDivisionError: 当除数为零时抛出",
        "        \"\"\"",
        "        if b == 0:",
        "            raise ZeroDivisionError(\"除数不能为零\")",
        "        return a / b",
    ]
    
    with open(example_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(example_content))
    
    print(f"已创建示例模块: {example_file}")


if __name__ == "__main__":
    # 切换到项目根目录
    os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    
    # 如果没有提供模块名称，显示使用说明
    if len(sys.argv) < 2:
        print("使用方法: python generate_test.py <module_name>")
        print("示例: python generate_test.py calculator")
        print("\n创建示例模块...")
        create_example_module()
        sys.exit(1)
    
    # 生成测试模板
    module_name = sys.argv[1]
    success = generate_test_template(module_name)
    
    if success:
        print(f"已成功为模块 {module_name} 生成测试模板")
    else:
        print(f"为模块 {module_name} 生成测试模板失败")
