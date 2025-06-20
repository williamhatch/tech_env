# Calculator class
#
# A calculator class that implements basic mathematical operations
class Calculator
  # Initialize method
  def initialize
    # No initialization needed at the moment
  end
  
  # Calculate the sum of two numbers
  # @param a [Numeric] First number
  # @param b [Numeric] Second number
  # @return [Numeric] Sum of the two numbers
  def add(a, b)
    a + b
  end
  
  # Calculate the difference between two numbers
  # @param a [Numeric] First number
  # @param b [Numeric] Second number
  # @return [Numeric] Difference between the two numbers
  def subtract(a, b)
    a - b
  end
  
  # Calculate the product of two numbers
  # @param a [Numeric] First number
  # @param b [Numeric] Second number
  # @return [Numeric] Product of the two numbers
  def multiply(a, b)
    a * b
  end
  
  # Calculate the quotient of two numbers
  # @param a [Numeric] First number
  # @param b [Numeric] Second number
  # @return [Float] Quotient of the two numbers (floating point result)
  # @raise [ZeroDivisionError] When the divisor is zero
  def divide(a, b)
    raise ZeroDivisionError, "Divisor cannot be zero" if b.zero?
    # Convert the result to a floating point number to ensure integer division also returns decimal results
    a.to_f / b
  end
end
