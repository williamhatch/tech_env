# MathUtils class
#
# A utility class for mathematical calculations
class MathUtils
  # Calculate the nth number in the Fibonacci sequence
  # Uses dynamic programming to avoid performance issues with recursion
  # @param n [Integer] Position (0-indexed)
  # @return [Integer] The nth number in the Fibonacci sequence
  def self.fibonacci(n)
    return 0 if n == 0
    return 1 if n == 1
    
    # Use dynamic programming to avoid redundant calculations
    fib = [0, 1]
    (2..n).each do |i|
      fib[i] = fib[i-1] + fib[i-2]
    end
    
    fib[n]
  end
end
