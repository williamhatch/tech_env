#!/usr/bin/env ruby
# encoding: utf-8
#
# 自动生成测试模板的脚本

require 'fileutils'

def generate_test_template(class_name)
  puts "为类 #{class_name} 生成测试模板..."
  
  # 切换到项目根目录
  project_root = File.expand_path('..', File.dirname(__FILE__))
  Dir.chdir(project_root)
  
  # 确定源文件和测试文件的路径
  file_name = class_name.gsub(/([A-Z])/) { "_#{$1.downcase}" }.sub(/^_/, '')
  source_file = File.join('lib', "#{file_name}.rb")
  test_file = File.join('test', "test_#{file_name}.rb")
  
  # 检查测试文件是否已存在
  if File.exist?(test_file)
    print "测试文件 #{test_file} 已存在。是否覆盖? (y/n): "
    choice = gets.strip.downcase
    return false unless choice == 'y'
  end
  
  # 如果源文件不存在，创建一个示例源文件
  unless File.exist?(source_file)
    # 确保lib目录存在
    FileUtils.mkdir_p(File.dirname(source_file))
    
    # 创建示例源文件
    File.open(source_file, 'w') do |f|
      f.puts <<~RUBY
        # #{class_name} 类
        #
        # 这是一个示例类，用于演示测试生成
        class #{class_name}
          # 初始化方法
          def initialize
            @value = 0
          end
          
          # 设置值
          # @param value [Numeric] 要设置的值
          # @return [Numeric] 设置后的值
          def set_value(value)
            @value = value
          end
          
          # 获取值
          # @return [Numeric] 当前值
          def get_value
            @value
          end
          
          # 增加值
          # @param amount [Numeric] 要增加的数量
          # @return [Numeric] 增加后的值
          def increment(amount = 1)
            @value += amount
          end
          
          # 减少值
          # @param amount [Numeric] 要减少的数量
          # @return [Numeric] 减少后的值
          def decrement(amount = 1)
            @value -= amount
          end
        end
      RUBY
    end
    puts "创建示例源文件: #{source_file}"
  end
  
  # 分析源文件以获取方法列表
  methods = []
  if File.exist?(source_file)
    File.readlines(source_file).each do |line|
      if line =~ /^\s*def\s+([a-zA-Z0-9_]+)(\(.*\))?/
        methods << $1
      end
    end
  end
  
  # 如果没有找到方法，添加一些默认方法
  if methods.empty?
    methods = ['initialize', 'set_value', 'get_value', 'increment', 'decrement']
  end
  
  # 确保test目录存在
  FileUtils.mkdir_p(File.dirname(test_file))
  
  # 创建测试文件
  File.open(test_file, 'w') do |f|
    f.puts <<~RUBY
      require_relative 'test_helper'
      require '#{file_name}'
      
      # #{class_name} 类的测试
      class Test#{class_name} < Minitest::Test
        # 在每个测试方法执行前设置
        def setup
          @instance = #{class_name}.new
        end
        
        # 在每个测试方法执行后清理
        def teardown
          # 在这里进行清理工作
        end
    RUBY
    
    # 为每个方法生成测试方法
    methods.each do |method|
      next if method == 'initialize'
      
      f.puts <<~RUBY
        
        # 测试 #{method} 方法
        def test_#{method}
          # TODO: 实现测试用例
          assert(true)  # 替换为实际测试
        end
      RUBY
    end
    
    f.puts "end"
  end
  
  puts "已生成测试文件: #{test_file}"
  true
end

def create_example_class
  # 创建一个示例类，用于演示
  generate_test_template('Calculator')
end

if __FILE__ == $PROGRAM_NAME
  # 如果没有提供类名，显示使用说明
  if ARGV.empty?
    puts "使用方法: ruby generate_test.rb <class_name>"
    puts "示例: ruby generate_test.rb Calculator"
    puts "\n创建示例类..."
    create_example_class
    exit 1
  end
  
  # 生成测试模板
  class_name = ARGV[0]
  success = generate_test_template(class_name)
  
  if success
    puts "已成功为类 #{class_name} 生成测试模板"
  else
    puts "为类 #{class_name} 生成测试模板失败"
    exit 1
  end
end
