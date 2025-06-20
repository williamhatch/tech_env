# MyNewClass
#
# This is an example class for demonstrating test generation
class MyNewClass
  # Initialize method
  def initialize
    @value = 0
  end
  
  # Set value
  # @param value [Numeric] The value to set
  # @return [Numeric] The value after setting
  def set_value(value)
    @value = value
  end
  
  # Get value
  # @return [Numeric] The current value
  def get_value
    @value
  end
  
  # Increment value
  # @param amount [Numeric] The amount to increment by
  # @return [Numeric] The value after incrementing
  def increment(amount = 1)
    @value += amount
  end
  
  # Decrement value
  # @param amount [Numeric] The amount to decrement by
  # @return [Numeric] The value after decrementing
  def decrement(amount = 1)
    @value -= amount
  end
end
