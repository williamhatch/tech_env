require_relative 'test_helper'
require 'math_utils'

# Tests for the MathUtils class
class TestMathUtils < Minitest::Test
  # Test the Fibonacci sequence calculation method
  def test_fibonacci
    # Test basic cases
    assert_equal 0, MathUtils.fibonacci(0)
    assert_equal 1, MathUtils.fibonacci(1)
    assert_equal 1, MathUtils.fibonacci(2)
    assert_equal 2, MathUtils.fibonacci(3)
    assert_equal 3, MathUtils.fibonacci(4)
    assert_equal 5, MathUtils.fibonacci(5)
    assert_equal 8, MathUtils.fibonacci(6)
    
    # Test larger numbers
    assert_equal 55, MathUtils.fibonacci(10)
    assert_equal 6765, MathUtils.fibonacci(20)
  end
end
