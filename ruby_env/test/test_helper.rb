require 'minitest/autorun'

# 如果启用了覆盖率报告，则加载simplecov
if ENV['COVERAGE']
  require 'simplecov'
  SimpleCov.start do
    add_filter '/test/'
  end
end

# 加载所有测试文件
Dir.glob(File.join(File.dirname(__FILE__), 'test_*.rb')).each do |file|
  require file
end
