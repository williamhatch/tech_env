#!/usr/bin/env ruby
# encoding: utf-8

# Script to run the Sinatra API server

require 'fileutils'

# ANSI color codes
COLORS = {
  green: "\033[32m",
  yellow: "\033[33m",
  red: "\033[31m",
  blue: "\033[34m",
  cyan: "\033[36m",
  magenta: "\033[35m",
  reset: "\033[0m"
}

# Colorize text
def colorize(text, color)
  "#{COLORS[color]}#{text}#{COLORS[:reset]}"
end

# Print header
puts colorize("\n" + "=" * 50, :cyan)
puts colorize("STARTING API SERVER".center(50), :cyan)
puts colorize("=" * 50 + "\n", :cyan)

# Change to project root directory
root_dir = File.expand_path('..', File.dirname(__FILE__))
Dir.chdir(root_dir)

# Create db directory if it doesn't exist
FileUtils.mkdir_p('db')

# Create public directory if it doesn't exist
FileUtils.mkdir_p('public')

# Create views directory if it doesn't exist
FileUtils.mkdir_p('views')

# Check if database migrations exist
if Dir.glob('db/migrate/*.rb').empty?
  puts colorize("No migrations found. Make sure to run migrations before starting the server.", :yellow)
  puts colorize("Run: bundle exec rake db:migrate", :blue)
end

# Run the server
puts colorize("Starting Sinatra server at http://localhost:4567", :green)
puts colorize("Press Ctrl+C to stop the server", :yellow)
puts

# Start the server
exec "bundle exec ruby app.rb -o 0.0.0.0"
