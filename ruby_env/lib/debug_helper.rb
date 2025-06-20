#!/usr/bin/env ruby
# encoding: utf-8
#
# Ruby Environment Debugging Helper
# Provides various debugging tools and helper functions to assist with rapid code debugging

# ANSI color codes
module ColorHelper
  def colorize(text, color_code)
    "\e[#{color_code}m#{text}\e[0m"
  end

  def green(text)
    colorize(text, 32)
  end

  def yellow(text)
    colorize(text, 33)
  end

  def red(text)
    colorize(text, 31)
  end

  def blue(text)
    colorize(text, 34)
  end

  def cyan(text)
    colorize(text, 36)
  end

  def magenta(text)
    colorize(text, 35)
  end
end

# Debug helper module
module DebugHelper
  extend ColorHelper

  # Insert a breakpoint in the code
  # Usage:
  # require_relative 'lib/debug_helper'
  # include DebugHelper
  #
  # def some_method
  #   x = 10
  #   y = 20
  #   debug_break  # Code execution will pause here
  #   z = x + y
  # end
  def debug_break
    begin
      require 'pry'
      binding.pry
    rescue LoadError
      begin
        require 'byebug'
        byebug
      rescue LoadError
        puts red("Unable to load debugger. Please install pry or byebug:")
        puts yellow("gem install pry")
        puts yellow("gem install byebug")
      end
    end
  end

  # Print variable information
  # Usage:
  # require_relative 'lib/debug_helper'
  # include DebugHelper
  #
  # x = [1, 2, 3]
  # print_var(x, "x")
  def print_var(var, name = nil)
    # Try to get variable name (if not provided)
    if name.nil?
      caller_line = caller.first
      if caller_line =~ /`([^']*)'/ 
        method_name = $1
        if method_name =~ /print_var\((.*)\)/
          name = $1.strip
        end
      end
    end

    var_type = var.class.name
    puts blue("Variable #{name} (#{var_type}):")
    puts green("Value: #{var.inspect}")
    
    # If it's a container type, print more information
    if var.respond_to?(:length)
      puts cyan("Length: #{var.length}")
    end
    
    # If it's a hash, print keys
    if var.is_a?(Hash)
      puts magenta("Keys: #{var.keys}")
    end
  end

  # Trace method execution
  # Usage:
  # require_relative 'lib/debug_helper'
  # include DebugHelper
  #
  # trace_method :calculate_sum do |a, b|
  #   result = a + b
  #   return result
  # end
  def trace_method(method_name, &block)
    puts cyan("===== Start tracing method: #{method_name} =====")
    
    # Get method parameters
    params = block.parameters.map { |_, name| name }
    puts blue("Parameters: #{params}")
    
    # Execute method and record results
    start_time = Time.now
    result = block.call
    end_time = Time.now
    
    puts green("Return value: #{result.inspect}")
    puts yellow("Execution time: #{(end_time - start_time) * 1000} milliseconds")
    puts cyan("===== Method tracing complete =====")
    
    result
  end

  # Print debugging environment information
  # Usage:
  # require_relative 'lib/debug_helper'
  # include DebugHelper
  #
  # debug_info
  def debug_info
    puts cyan("\n===== Debugging Environment Info =====")
    puts green("Ruby version: #{RUBY_VERSION}")
    puts green("Working directory: #{Dir.pwd}")
    
    # Check if debugging tools are installed
    debug_tools = {
      'pry' => false,
      'byebug' => false,
      'pry-byebug' => false
    }
    
    begin
      require 'pry'
      debug_tools['pry'] = true
    rescue LoadError
    end
    
    begin
      require 'byebug'
      debug_tools['byebug'] = true
    rescue LoadError
    end
    
    begin
      require 'pry-byebug'
      debug_tools['pry-byebug'] = true
    rescue LoadError
    end
    
    puts blue("\nAvailable debugging tools:")
    debug_tools.each do |tool, available|
      status = available ? green("Installed") : red("Not installed")
      puts "- #{tool}: #{status}"
    end
    
    puts yellow("\nDebugging commands:")
    puts "- debug_break: Insert breakpoint"
    puts "- print_var(var): Print variable information"
    puts "- trace_method(:method_name) { |params| ... }: Trace method execution"
    puts cyan("======================\n")
  end
end

# If this file is run directly, show usage examples
if __FILE__ == $PROGRAM_NAME
  include DebugHelper
  include ColorHelper
  
  debug_info
  puts magenta("\nExample usage:")
  puts %{
require_relative 'lib/debug_helper'
include DebugHelper

# Print debugging environment info
debug_info

# Using breakpoints
def example_method
  x = [1, 2, 3]
  debug_break  # Code execution will pause here
  y = x.sum
  return y
end

# Trace method execution
trace_method(:calculate_sum) do |a, b|
  result = a + b
  return result
end

# Print variable information
data = {"name" => "test", "value" => 42}
print_var(data, "data")
  }
end
