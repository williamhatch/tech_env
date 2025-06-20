#!/usr/bin/env ruby
# encoding: utf-8
#
# Script for automatically generating test templates

require 'fileutils'

# ANSI color codes
class String
  def colorize(color_code)
    "\e[#{color_code}m#{self}\e[0m"
  end

  def green
    colorize(32)
  end

  def yellow
    colorize(33)
  end

  def blue
    colorize(34)
  end

  def magenta
    colorize(35)
  end

  def cyan
    colorize(36)
  end
end

def generate_test_template(class_name)
  puts "\n#{'='*50}".cyan
  puts "#{'GENERATE TEST'.center(50)}".cyan
  puts "#{'='*50}\n".cyan
  
  puts "Generating test template for class #{class_name}...".green
  
  # Change to project root directory
  project_root = File.expand_path('..', File.dirname(__FILE__))
  Dir.chdir(project_root)
  
  # Determine paths for source and test files
  file_name = class_name.gsub(/([A-Z])/) { "_#{$1.downcase}" }.sub(/^_/, '')
  source_file = File.join('lib', "#{file_name}.rb")
  test_file = File.join('test', "test_#{file_name}.rb")
  
  # Check if test file already exists
  if File.exist?(test_file)
    print "Test file #{test_file} already exists. Overwrite? (y/n): ".yellow
    choice = gets.strip.downcase
    return false unless choice == 'y'
  end
  
  # If source file doesn't exist, create an example source file
  unless File.exist?(source_file)
    # Ensure lib directory exists
    FileUtils.mkdir_p(File.dirname(source_file))
    
    # Create example source file
    File.open(source_file, 'w') do |f|
      f.puts <<~RUBY
        # #{class_name} class
        #
        # This is an example class for demonstrating test generation
        class #{class_name}
          # Initialize method
          def initialize
            @value = 0
          end
          
          # Set value
          # @param value [Numeric] Value to set
          # @return [Numeric] Value after setting
          def set_value(value)
            @value = value
          end
          
          # Get value
          # @return [Numeric] Current value
          def get_value
            @value
          end
          
          # Increment value
          # @param amount [Numeric] Amount to increment
          # @return [Numeric] Value after incrementing
          def increment(amount = 1)
            @value += amount
          end
          
          # Decrement value
          # @param amount [Numeric] Amount to decrement
          # @return [Numeric] Value after decrementing
          def decrement(amount = 1)
            @value -= amount
          end
        end
      RUBY
    end
    puts "Created example source file: #{source_file}".blue
  end
  
  # Analyze source file to get method list
  methods = []
  if File.exist?(source_file)
    File.readlines(source_file).each do |line|
      if line =~ /^\s*def\s+([a-zA-Z0-9_]+)(\(.*\))?/
        methods << $1
      end
    end
  end
  
  # If no methods found, add some default methods
  if methods.empty?
    methods = ['initialize', 'set_value', 'get_value', 'increment', 'decrement']
  end
  
  # Ensure test directory exists
  FileUtils.mkdir_p(File.dirname(test_file))
  
  # Create test file
  File.open(test_file, 'w') do |f|
    f.puts <<~RUBY
      require_relative 'test_helper'
      require '#{file_name}'
      
      # Tests for the #{class_name} class
      class Test#{class_name} < Minitest::Test
        # Setup before each test method
        def setup
          @instance = #{class_name}.new
        end
        
        # Cleanup after each test method
        def teardown
          # Perform cleanup work here
        end
    RUBY
    
    # Generate test methods for each method
    methods.each do |method|
      next if method == 'initialize'
      
      f.puts <<~RUBY
        
        # Test the #{method} method
        def test_#{method}
          # TODO: Implement test cases
          assert(true)  # Replace with actual tests
        end
      RUBY
    end
    
    f.puts "end"
  end
  
  puts "Generated test file: #{test_file}".green
  true
end

def create_example_class
  # Create an example class for demonstration
  generate_test_template('Calculator')
end

if __FILE__ == $PROGRAM_NAME
  # If no class name provided, show usage instructions
  if ARGV.empty?
    puts "Usage: ruby generate_test.rb <class_name>".yellow
    puts "Example: ruby generate_test.rb Calculator".blue
    puts "\nCreating example class...".magenta
    create_example_class
    exit 1
  end
  
  # Generate test template
  class_name = ARGV[0]
  success = generate_test_template(class_name)
  
  if success
    puts "\nSuccessfully generated test template for class #{class_name}".green
  else
    puts "\nFailed to generate test template for class #{class_name}".red
    exit 1
  end
end
