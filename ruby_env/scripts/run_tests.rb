#!/usr/bin/env ruby
# encoding: utf-8
#
# Automated script for running unit tests

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

def run_tests(coverage = true)
  puts "\n#{'='*50}".cyan
  puts "#{'RUN TESTS'.center(50)}".cyan
  puts "#{'='*50}\n".cyan
  
  puts "Running tests...".green
  
  # Change to project root directory
  Dir.chdir(File.expand_path('..', File.dirname(__FILE__)))
  
  # Set environment variable to enable coverage reporting
  if coverage
    ENV['COVERAGE'] = 'true'
    puts "Coverage reporting: #{'ENABLED'.green}"
  else
    ENV.delete('COVERAGE')
    puts "Coverage reporting: #{'DISABLED'.yellow}"
  end
  
  puts "\nExecuting test suite...".blue
  
  # Run all tests
  result = system('ruby -I lib:test test/test_helper.rb')
  
  # Show coverage report location if enabled
  if coverage && result
    puts "\n#{'='*50}".cyan
    puts "#{'COVERAGE REPORT'.center(50)}".cyan
    puts "#{'='*50}".cyan
    
    coverage_dir = File.join(Dir.pwd, 'coverage')
    if Dir.exist?(coverage_dir)
      index_file = File.join(coverage_dir, 'index.html')
      if File.exist?(index_file)
        puts "\nCoverage report generated at: #{'coverage/index.html'.green}"
        puts "Open with: #{'open coverage/index.html'.blue}\n"
      else
        puts "\nCoverage directory exists but no index.html found.".yellow
      end
    else
      puts "\nNo coverage directory found. Make sure SimpleCov is configured correctly.".yellow
    end
  end
  
  return result
end

if __FILE__ == $PROGRAM_NAME
  # Parse command line arguments
  coverage = true
  coverage = false if ARGV.include?('--no-coverage')
  
  # Run tests
  exit_code = run_tests(coverage) ? 0 : 1
  exit(exit_code)
end
