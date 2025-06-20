require_relative 'test_helper'
require 'calculator'

# Tests for the Calculator class
class TestCalculator < Minitest::Test
  # Setup before each test method
  def setup
    @calc = Calculator.new
  end
  
  # Cleanup after each test method
  def teardown
    # Perform cleanup work here
  end
  
  # Test the add method
  def test_add
    assert_equal(3, @calc.add(1, 2))
    assert_equal(0, @calc.add(-1, 1))
    assert_equal(-2, @calc.add(-1, -1))
  end
  
  # Test the subtract method
  def test_subtract
    assert_equal(1, @calc.subtract(3, 2))
    assert_equal(0, @calc.subtract(1, 1))
    assert_equal(0, @calc.subtract(-1, -1))
  end
  
  # Test the multiply method
  def test_multiply
    assert_equal(6, @calc.multiply(2, 3))
    assert_equal(0, @calc.multiply(0, 5))
    assert_equal(-6, @calc.multiply(-2, 3))
  end
  
  # Test the divide method
  def test_divide
    assert_equal(2, @calc.divide(6, 3))
    assert_equal(2.5, @calc.divide(5, 2))
    assert_equal(-2, @calc.divide(-6, 3))
    
    # Test division by zero exception
    assert_raises(ZeroDivisionError) do
      @calc.divide(5, 0)
    end
  end
end
