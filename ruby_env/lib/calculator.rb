# Calculator 类
#
# 实现基本数学运算的计算器类
class Calculator
  # 初始化方法
  def initialize
    # 暂无需初始化任何内容
  end
  
  # 计算两个数的和
  # @param a [Numeric] 第一个数
  # @param b [Numeric] 第二个数
  # @return [Numeric] 两个数的和
  def add(a, b)
    a + b
  end
  
  # 计算两个数的差
  # @param a [Numeric] 第一个数
  # @param b [Numeric] 第二个数
  # @return [Numeric] 两个数的差
  def subtract(a, b)
    a - b
  end
  
  # 计算两个数的乘积
  # @param a [Numeric] 第一个数
  # @param b [Numeric] 第二个数
  # @return [Numeric] 两个数的乘积
  def multiply(a, b)
    a * b
  end
  
  # 计算两个数的商
  # @param a [Numeric] 第一个数
  # @param b [Numeric] 第二个数
  # @return [Numeric] 两个数的商
  # @raise [ZeroDivisionError] 当除数为零时抛出
  def divide(a, b)
    raise ZeroDivisionError, "除数不能为零" if b.zero?
    a / b
  end
end
