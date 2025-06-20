# Python 技术面试环境

这个环境为您提供了使用Python进行技术面试的完整设置，包括自动化测试和监视工具。

## 环境设置

1. 安装依赖：
```bash
pip install -r requirements.txt
```

2. 项目结构：
   - `src/`: 放置您的源代码
   - `tests/`: 放置测试用例
   - `scripts/`: 自动化脚本

## 使用自动化脚本

### 运行测试
```bash
python scripts/run_tests.py
```

### 监视文件变化并自动运行测试
```bash
python scripts/watch_tests.py
```

### 生成测试模板
```bash
python scripts/generate_test.py <module_name>
```

## 技术面试提示

1. 使用TDD（测试驱动开发）方法
2. 先编写测试用例，再实现功能
3. 保持代码简洁清晰
4. 注意边界条件和异常处理
