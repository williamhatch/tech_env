require 'minitest/autorun'
require 'minitest/reporters'

# Enable code coverage if COVERAGE env var is set
if ENV['COVERAGE']
  require 'simplecov'
  SimpleCov.start do
    add_filter '/test/'
    add_group 'Library', 'lib'
    add_group 'Web App', 'app.rb'
  end
  puts "\nCode coverage enabled. Report will be generated to coverage/index.html"
end

# Add lib directory to the load path
$LOAD_PATH.unshift(File.expand_path('../lib', File.dirname(__FILE__)))

# Load test database setup
require_relative 'test_database_setup'

# Custom reporter for Minitest with colorized output
class ColorizedReporter < Minitest::Reporters::DefaultReporter
  def initialize(options = {})
    super(options.merge(color: true))
  end
  
  def record_pass(test)
    super
  end
  
  def record_skip(test)
    super
  end
  
  def record_failure(test)
    super
  end
  
  def record_error(test)
    super
  end
  
  # Override the result method to customize the output
  def report
    super
    
    # Format the results with colors
    puts "\n"
    puts "#{colored_for("#{count} runs", :green)}, #{colored_for("#{assertions} assertions", :green)}, " +
         "#{failures > 0 ? colored_for("#{failures} failures", :yellow) : colored_for("#{failures} failures", :green)}, " +
         "#{errors > 0 ? colored_for("#{errors} errors", :red) : colored_for("#{errors} errors", :green)}, " +
         "#{skips > 0 ? colored_for("#{skips} skips", :yellow) : colored_for("#{skips} skips", :green)}"
  end
end

# Register our custom reporter
Minitest::Reporters.use! [ColorizedReporter.new]

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
