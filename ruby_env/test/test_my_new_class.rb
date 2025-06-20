require_relative 'test_helper'
require 'my_new_class'

# Tests for MyNewClass
class TestMyNewClass < Minitest::Test
  # Setup before each test method
  def setup
    @instance = MyNewClass.new
  end
  
  # Cleanup after each test method
  def teardown
    # Perform cleanup work here
  end

# Test set_value method
def test_set_value
  # TODO: Implement test case
  assert(true)  # Replace with actual test
end

# Test get_value method
def test_get_value
  # TODO: Implement test case
  assert(true)  # Replace with actual test
end

# Test increment method
def test_increment
  # TODO: Implement test case
  assert(true)  # Replace with actual test
end

# Test decrement method
def test_decrement
  # TODO: Implement test case
  assert(true)  # Replace with actual test
end
end
