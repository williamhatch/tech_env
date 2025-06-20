# StringUtils class
#
# A utility class for string operations
class StringUtils
  # Reverse a string
  # @param input_str [String] Input string
  # @return [String] Reversed string
  def self.reverse_string(input_str)
    input_str.reverse
  end
  
  # Check if a string is a palindrome
  # Ignores case, spaces, and punctuation
  # @param input_str [String] Input string
  # @return [Boolean] True if the string is a palindrome, false otherwise
  def self.is_palindrome(input_str)
    # Remove all non-alphanumeric characters and convert to lowercase
    cleaned_str = input_str.gsub(/[^a-zA-Z0-9]/, '').downcase
    
    # Check if the cleaned string is a palindrome
    cleaned_str == cleaned_str.reverse
  end
end
