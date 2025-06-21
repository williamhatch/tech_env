# Python 和 Ruby 调试指南

本文档提供了在开发环境中调试 Python 和 Ruby 代码的详细步骤和方法。我们将介绍多种调试技术，从简单的打印调试到使用专业的调试工具。

## 目录

- [Python 调试指南](#python-调试指南)
  - [基础调试技术](#python-基础调试技术)
  - [使用内置调试辅助模块](#python-使用内置调试辅助模块)
  - [使用 pdb/ipdb 调试器](#使用-pdbipdb-调试器)
  - [使用 PySnooper 进行无侵入式调试](#使用-pysnooper-进行无侵入式调试)
  - [使用 VS Code 进行图形界面调试](#python-使用-vs-code-进行图形界面调试)
- [Ruby 调试指南](#ruby-调试指南)
  - [基础调试技术](#ruby-基础调试技术)
  - [使用内置调试辅助模块](#ruby-使用内置调试辅助模块)
  - [使用 pry 和 byebug 调试器](#使用-pry-和-byebug-调试器)
  - [使用 VS Code 进行图形界面调试](#ruby-使用-vs-code-进行图形界面调试)

## Python 调试指南

### Python 基础调试技术

#### 1. 使用 print 语句

最简单的调试方法是使用 `print` 语句输出变量值：

```python
def calculate_sum(a, b):
    print(f"a = {a}, b = {b}")
    result = a + b
    print(f"结果: {result}")
    return result
```

#### 2. 使用 logging 模块

比 print 更灵活的方法是使用 Python 的 `logging` 模块：

```python
import logging
logging.basicConfig(level=logging.DEBUG)

def calculate_sum(a, b):
    logging.debug(f"a = {a}, b = {b}")
    result = a + b
    logging.info(f"计算结果: {result}")
    return result
```

### Python 使用内置调试辅助模块

我们的环境提供了一个专门的调试辅助模块，位于 `scripts/debug_helper.py`，包含多种实用的调试功能：

#### 1. 导入调试辅助模块

```python
from scripts.debug_helper import debug_break, trace_function, print_var, debug_info
```

#### 2. 查看调试环境信息

```python
# 打印当前环境的调试工具信息
debug_info()
```

#### 3. 在代码中插入断点

```python
def example_function():
    x = [1, 2, 3]
    debug_break()  # 代码会在这里暂停执行
    y = sum(x)
    return y
```

#### 4. 跟踪函数执行

使用装饰器跟踪函数执行过程中的变量变化：

```python
@trace_function
def calculate_sum(a, b):
    result = a + b
    return result
```

#### 5. 打印变量详细信息

```python
data = {"name": "测试", "value": 42, "items": [1, 2, 3]}
print_var(data, "data")  # 会显示变量类型、值、长度等信息
```

### 使用 pdb/ipdb 调试器

pdb 是 Python 的内置调试器，ipdb 是其增强版本，提供了语法高亮和tab补全等功能。

#### 1. 安装 ipdb

```bash
pip install ipdb
```

#### 2. 在代码中插入断点

```python
import ipdb

def problematic_function():
    x = 10
    y = 0
    ipdb.set_trace()  # 代码会在这里暂停执行
    result = x / y  # 这里会出现除零错误
    return result
```

#### 3. 常用调试命令

- `n` (next): 执行当前行，并移动到下一行
- `s` (step): 单步执行，如果当前行调用了函数则进入函数内部
- `c` (continue): 继续执行直到下一个断点
- `q` (quit): 退出调试器
- `p 变量名`: 打印变量值
- `pp 变量名`: 格式化打印变量值
- `l` (list): 显示当前行周围的代码
- `w` (where): 打印当前的调用栈

### 使用 PySnooper 进行无侵入式调试

PySnooper 是一个非常方便的调试工具，它可以记录函数执行过程中的变量变化。

#### 1. 安装 PySnooper

```bash
pip install pysnooper
```

#### 2. 使用 PySnooper 跟踪函数执行

```python
import pysnooper

@pysnooper.snoop()
def calculate_division(a, b):
    result = a / b
    return result

calculate_division(10, 2)  # 会输出函数执行的每一步和变量变化
```

#### 3. 保存调试日志到文件

```python
@pysnooper.snoop('/tmp/debug_log.log')
def complex_function():
    # 函数代码
    pass
```

### Python 使用 VS Code 进行图形界面调试

VS Code 提供了强大的图形界面调试功能，特别适合复杂项目的调试。

#### 1. 配置 VS Code

1. 安装 Python 扩展：在 VS Code 扩展市场搜索并安装 "Python" 扩展
2. 创建 `.vscode/launch.json` 文件：

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: 当前文件",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal"
        }
    ]
}
```

#### 2. 设置断点

1. 在代码行号左侧点击设置断点（会出现红色圆点）
2. 或在代码中添加 `breakpoint()` 语句（Python 3.7+）

#### 3. 开始调试

1. 打开要调试的 Python 文件
2. 按 F5 键或点击调试面板中的开始按钮
3. 程序会在断点处暂停执行

#### 4. 调试控制

- 继续执行 (F5)
- 单步跳过 (F10)
- 单步进入 (F11)
- 单步跳出 (Shift+F11)
- 重启 (Ctrl+Shift+F5)
- 停止 (Shift+F5)

## Ruby 调试指南

### Ruby 基础调试技术

#### 1. 使用 puts 语句

最简单的调试方法是使用 `puts` 语句输出变量值：

```ruby
def calculate_sum(a, b)
  puts "a = #{a}, b = #{b}"
  result = a + b
  puts "结果: #{result}"
  result
end
```

#### 2. 使用 pp 方法

对于复杂的数据结构，可以使用 `pp`（pretty print）方法：

```ruby
require 'pp'

def inspect_data(data)
  pp data  # 格式化打印数据
  # 处理数据...
end
```

### Ruby 使用内置调试辅助模块

我们的环境提供了一个专门的调试辅助模块，位于 `lib/debug_helper.rb`，包含多种实用的调试功能：

#### 1. 导入调试辅助模块

```ruby
require_relative 'lib/debug_helper'
include DebugHelper
```

#### 2. 查看调试环境信息

```ruby
# 打印当前环境的调试工具信息
debug_info
```

#### 3. 在代码中插入断点

```ruby
def example_method
  x = [1, 2, 3]
  debug_break  # 代码会在这里暂停执行
  y = x.sum
  return y
end
```

#### 4. 跟踪方法执行

```ruby
trace_method(:calculate_sum) do |a, b|
  result = a + b
  return result
end
```

#### 5. 打印变量详细信息

```ruby
data = {"name" => "测试", "value" => 42, "items" => [1, 2, 3]}
print_var(data, "data")  # 会显示变量类型、值、长度等信息
```

### 使用 pry 和 byebug 调试器

pry 是 Ruby 的交互式调试器，byebug 是另一个强大的调试器，两者可以结合使用。

#### 1. 安装调试器

在 Gemfile 中添加：

```ruby
gem 'pry'
gem 'byebug'
gem 'pry-byebug'  # 整合 pry 和 byebug
```

然后运行：

```bash
bundle install
```

#### 2. 在代码中插入断点

```ruby
require 'pry'

def problematic_method
  x = 10
  y = 0
  binding.pry  # 代码会在这里暂停执行
  result = x / y  # 这里会出现除零错误
  result
end
```

或使用 byebug：

```ruby
require 'byebug'

def problematic_method
  x = 10
  y = 0
  byebug  # 代码会在这里暂停执行
  result = x / y  # 这里会出现除零错误
  result
end
```

#### 3. 常用调试命令

Pry 命令：
- `next` 或 `n`: 执行当前行并移动到下一行
- `step` 或 `s`: 单步执行，如果当前行调用了方法则进入方法内部
- `continue` 或 `c`: 继续执行直到下一个断点
- `exit` 或 `quit`: 退出调试器
- `whereami`: 显示当前位置的代码
- `help`: 显示帮助信息

Byebug 命令：
- `next` 或 `n`: 执行当前行并移动到下一行
- `step` 或 `s`: 单步执行，进入方法内部
- `continue` 或 `c`: 继续执行
- `quit` 或 `q`: 退出调试器
- `display 变量名`: 每次停止时显示变量值
- `undisplay`: 取消变量显示

### Ruby 使用 VS Code 进行图形界面调试

VS Code 也支持 Ruby 的图形界面调试。

#### 1. 配置 VS Code

1. 安装 Ruby 扩展：在 VS Code 扩展市场搜索并安装 "Ruby" 扩展
2. 安装必要的 gem：

```ruby
gem 'ruby-debug-ide'
gem 'debase'
```

3. 创建 `.vscode/launch.json` 文件：

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Debug Ruby",
            "type": "Ruby",
            "request": "launch",
            "program": "${file}",
            "useBundler": true
        }
    ]
}
```

#### 2. 设置断点

1. 在代码行号左侧点击设置断点（会出现红色圆点）

#### 3. 开始调试

1. 打开要调试的 Ruby 文件
2. 按 F5 键或点击调试面板中的开始按钮
3. 程序会在断点处暂停执行

#### 4. 调试控制

- 继续执行 (F5)
- 单步跳过 (F10)
- 单步进入 (F11)
- 单步跳出 (Shift+F11)
- 重启 (Ctrl+Shift+F5)
- 停止 (Shift+F5)

## 调试最佳实践

1. **从简单开始**：先使用简单的 print/puts 语句，如果问题仍然存在，再使用更高级的调试工具
2. **隔离问题**：尝试创建一个最小的示例来复现问题
3. **检查数据类型**：很多错误是由于数据类型不匹配导致的
4. **使用版本控制**：在进行大的调试更改前，确保代码已提交到版本控制系统
5. **记录调试过程**：记录你尝试过的方法和发现的问题，有助于避免重复工作
6. **使用断言**：在代码中添加断言来验证假设
7. **检查边界条件**：特别注意边界条件，如空值、零值、极大值等

## 常见问题排查

### Python 常见问题

1. **ImportError/ModuleNotFoundError**：检查模块路径和 PYTHONPATH 环境变量
2. **IndentationError**：检查代码缩进，Python 对缩进非常敏感
3. **TypeError**：检查变量类型，特别是在函数调用时
4. **IndexError/KeyError**：检查列表索引或字典键是否存在
5. **AttributeError**：检查对象是否有该属性或方法

### Ruby 常见问题

1. **NameError**：检查变量或常量是否已定义
2. **NoMethodError**：检查对象是否有该方法
3. **ArgumentError**：检查方法调用的参数数量是否正确
4. **TypeError**：检查变量类型是否符合预期
5. **LoadError**：检查 require 的文件路径是否正确

## 结论

调试是编程过程中不可避免的一部分。通过掌握本文档中介绍的各种调试技术和工具，你可以更高效地定位和解决代码中的问题。记住，最好的调试策略是结合使用多种方法，从简单到复杂，逐步缩小问题范围。