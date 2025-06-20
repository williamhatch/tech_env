require_relative 'test_helper'
require 'calculator'

# Calculator 类的测试
class TestCalculator < Minitest::Test
  # 在每个测试方法执行前设置
  def setup
    @calc = Calculator.new
  end
  
  # 在每个测试方法执行后清理
  def teardown
    # 在这里进行清理工作
  end
  
  # 测试 add 方法
  def test_add
    assert_equal(3, @calc.add(1, 2))
    assert_equal(0, @calc.add(-1, 1))
    assert_equal(-2, @calc.add(-1, -1))
  end
  
  # 测试 subtract 方法
  def test_subtract
    assert_equal(1, @calc.subtract(3, 2))
    assert_equal(0, @calc.subtract(1, 1))
    assert_equal(0, @calc.subtract(-1, -1))
  end
  
  # 测试 multiply 方法
  def test_multiply
    assert_equal(6, @calc.multiply(2, 3))
    assert_equal(0, @calc.multiply(0, 5))
    assert_equal(-6, @calc.multiply(-2, 3))
  end
  
  # 测试 divide 方法
  def test_divide
    assert_equal(2, @calc.divide(6, 3))
    assert_equal(2.5, @calc.divide(5, 2))
    assert_equal(-2, @calc.divide(-6, 3))
    
    # 测试除以零的异常
    assert_raises(ZeroDivisionError) do
      @calc.divide(5, 0)
    end
  end
end
