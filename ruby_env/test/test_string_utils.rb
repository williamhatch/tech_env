require_relative 'test_helper'
require 'string_utils'

# Tests for the StringUtils class
class TestStringUtils < Minitest::Test
  # Test the string reversal method
  def test_reverse_string
    # Test normal string
    assert_equal "olleh", StringUtils.reverse_string("hello")
    
    # Test empty string
    assert_equal "", StringUtils.reverse_string("")
    
    # Test string with spaces
    assert_equal "dlrow olleh", StringUtils.reverse_string("hello world")
    
    # Test string with special characters
    assert_equal "#@!olleh", StringUtils.reverse_string("hello!@#")
    
    # Test string with Chinese characters
    assert_equal "界世好你", StringUtils.reverse_string("你好世界")
  end
  
  # Test the palindrome detection method
  def test_is_palindrome
    # Test normal palindromes
    assert StringUtils.is_palindrome("level")
    assert StringUtils.is_palindrome("radar")
    
    # Test non-palindromes
    refute StringUtils.is_palindrome("hello")
    refute StringUtils.is_palindrome("world")
    
    # Test empty string (empty string is considered a palindrome)
    assert StringUtils.is_palindrome("")
    
    # Test palindromes with spaces and punctuation
    assert StringUtils.is_palindrome("A man, a plan, a canal: Panama")
    assert StringUtils.is_palindrome("Race car")
    
    # Test palindromes with mixed case
    assert StringUtils.is_palindrome("Able was I ere I saw Elba")
    
    # Test palindromes with numbers
    assert StringUtils.is_palindrome("12321")
    refute StringUtils.is_palindrome("12345")
    
    # Test Chinese palindrome
    assert StringUtils.is_palindrome("上海自来水来自海上")
  end
end
