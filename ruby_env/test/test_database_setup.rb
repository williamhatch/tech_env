require 'sinatra/activerecord'
require 'fileutils'
require 'logger'

# Set test environment
ENV['RACK_ENV'] = 'test'

# Configure database connection for test environment
ActiveRecord::Base.establish_connection(
  adapter: 'sqlite3',
  database: ':memory:',
  timeout: 5000
)

# Create logger
log_dir = File.join(File.dirname(__FILE__), '..', 'log')
FileUtils.mkdir_p(log_dir)
logger = Logger.new(File.join(log_dir, 'test.log'))

# Define Item model if not already defined
unless defined?(Item)
  class Item < ActiveRecord::Base
    validates :name, presence: true
  end
end

# Create items table in memory
ActiveRecord::Schema.define do
  create_table :items, force: true do |t|
    t.string :name, null: false
    t.text :description
    t.boolean :active, default: true
    t.timestamps
  end
end

logger.info "Test database setup complete with in-memory SQLite database"
