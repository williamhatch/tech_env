#!/usr/bin/env ruby
# encoding: utf-8
#
# 监视文件变化并自动运行测试的脚本

require 'fileutils'

def check_directories
  # 确保必要的目录存在
  project_root = File.expand_path('..', File.dirname(__FILE__))
  lib_dir = File.join(project_root, 'lib')
  test_dir = File.join(project_root, 'test')
  
  # 创建lib目录（如果不存在）
  unless Dir.exist?(lib_dir)
    puts "创建源代码目录: #{lib_dir}"
    FileUtils.mkdir_p(lib_dir)
  end
  
  # 创建test目录（如果不存在）
  unless Dir.exist?(test_dir)
    puts "创建测试目录: #{test_dir}"
    FileUtils.mkdir_p(test_dir)
    
    # 创建test_helper.rb
    test_helper_path = File.join(test_dir, 'test_helper.rb')
    unless File.exist?(test_helper_path)
      File.open(test_helper_path, 'w') do |f|
        f.puts <<~RUBY
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
        RUBY
      end
      puts "创建测试助手文件: #{test_helper_path}"
    end
  end
end

def run_guard
  puts "启动测试监视器..."
  puts "监视lib和test目录中的文件变化..."
  puts "按Ctrl+C退出"
  
  # 创建Guardfile（如果不存在）
  project_root = File.expand_path('..', File.dirname(__FILE__))
  guardfile_path = File.join(project_root, 'Guardfile')
  
  unless File.exist?(guardfile_path)
    File.open(guardfile_path, 'w') do |f|
      f.puts <<~GUARD
        # 监视Ruby文件的变化
        guard :minitest do
          # 监视lib目录中的所有.rb文件
          watch(%r{^lib/(.+)\.rb$}) { |m| "test/test_\#{m[1]}.rb" }
          
          # 监视test目录中的所有测试文件
          watch(%r{^test/test_(.+)\.rb$})
          
          # 监视test_helper.rb
          watch(%r{^test/test_helper\.rb$}) { 'test' }
        end
      GUARD
    end
    puts "创建Guard配置文件: #{guardfile_path}"
  end
  
  # 运行Guard
  system('bundle exec guard')
end

if __FILE__ == $PROGRAM_NAME
  # 切换到项目根目录
  Dir.chdir(File.expand_path('..', File.dirname(__FILE__)))
  
  # 检查并创建必要的目录
  check_directories
  
  # 运行测试监视器
  run_guard
end
