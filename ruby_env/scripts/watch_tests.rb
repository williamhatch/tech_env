#!/usr/bin/env ruby
# encoding: utf-8
#
# Script to watch file changes and automatically run tests

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

def check_directories
  # Ensure necessary directories exist
  project_root = File.expand_path('..', File.dirname(__FILE__))
  lib_dir = File.join(project_root, 'lib')
  test_dir = File.join(project_root, 'test')
  
  # Create lib directory if it doesn't exist
  unless Dir.exist?(lib_dir)
    puts "Creating source code directory: #{lib_dir}".yellow
    FileUtils.mkdir_p(lib_dir)
  end
  
  # Create test directory if it doesn't exist
  unless Dir.exist?(test_dir)
    puts "Creating test directory: #{test_dir}".yellow
    FileUtils.mkdir_p(test_dir)
    
    # Create test_helper.rb
    test_helper_path = File.join(test_dir, 'test_helper.rb')
    unless File.exist?(test_helper_path)
      File.open(test_helper_path, 'w') do |f|
        f.puts <<~RUBY
          require 'minitest/autorun'
          
          # Add lib directory to the load path
          $LOAD_PATH.unshift(File.expand_path('../lib', File.dirname(__FILE__)))
          
          # Load simplecov if coverage reporting is enabled
          if ENV['COVERAGE']
            require 'simplecov'
            SimpleCov.start do
              add_filter '/test/'
            end
          end
          
          # Load all test files
          Dir.glob(File.join(File.dirname(__FILE__), 'test_*.rb')).each do |file|
            require file
          end
        RUBY
      end
      puts "Created test helper file: #{test_helper_path}".green
    end
  end
end

def run_guard
  puts "\n#{'='*50}".cyan
  puts "#{'WATCH TESTS'.center(50)}".cyan
  puts "#{'='*50}\n".cyan
  
  puts "Starting test watcher...".green
  puts "Watching files in lib/ and test/ directories...".blue
  puts "Press Ctrl+C to exit".yellow
  
  # Create Guardfile if it doesn't exist
  project_root = File.expand_path('..', File.dirname(__FILE__))
  guardfile_path = File.join(project_root, 'Guardfile')
  
  unless File.exist?(guardfile_path)
    File.open(guardfile_path, 'w') do |f|
      f.puts <<~GUARD
        # Watch for changes in Ruby files
        guard :minitest do
          # Watch all .rb files in the lib directory
          watch(%r{^lib/(.+)\.rb$}) { |m| "test/test_\#{m[1]}.rb" }
          
          # Watch all test files in the test directory
          watch(%r{^test/test_(.+)\.rb$})
          
          # Watch test_helper.rb
          watch(%r{^test/test_helper\.rb$}) { 'test' }
        end
      GUARD
    end
    puts "Created Guard configuration file: #{guardfile_path}".green
  end
  
  # Set environment variable to enable coverage reporting
  ENV['COVERAGE'] = 'true'
  puts "Coverage reporting: #{'ENABLED'.green}"
  
  # Display coverage report info
  puts "\n#{'COVERAGE REPORT INFO'.center(50)}".cyan
  puts "Coverage report will be generated at: #{'coverage/index.html'.green}"
  puts "After tests run, open with: #{'open coverage/index.html'.blue}\n"
  
  # Run Guard
  system('bundle exec guard')
end

if __FILE__ == $PROGRAM_NAME
  # Change to project root directory
  Dir.chdir(File.expand_path('..', File.dirname(__FILE__)))
  
  # Check and create necessary directories
  check_directories
  
  # Run the test watcher
  run_guard
end
