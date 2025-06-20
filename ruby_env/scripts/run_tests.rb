#!/usr/bin/env ruby
# encoding: utf-8
#
# 运行单元测试的自动化脚本

require 'fileutils'

def run_tests(coverage = true)
  puts "正在运行测试..."
  
  # 切换到项目根目录
  Dir.chdir(File.expand_path('..', File.dirname(__FILE__)))
  
  # 设置环境变量以启用覆盖率报告
  if coverage
    ENV['COVERAGE'] = 'true'
  else
    ENV.delete('COVERAGE')
  end
  
  # 运行所有测试
  system('ruby -I lib:test test/test_helper.rb')
end

if __FILE__ == $PROGRAM_NAME
  # 解析命令行参数
  coverage = true
  coverage = false if ARGV.include?('--no-coverage')
  
  # 运行测试
  exit_code = run_tests(coverage) ? 0 : 1
  exit(exit_code)
end
