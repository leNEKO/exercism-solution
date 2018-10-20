module Isogram
  def self.isogram?(input)
    chars = input.downcase.scan(/\w/)
    chars == chars.uniq
  end

  def self.isogram_len?(input)
    chars = input.downcase.scan(/\w/)
    chars.length == chars.uniq.length
  end
end

# some benchmarking
require 'benchmark'
input = 'abcdefghijklmnopqrstuvwxyz'
n = 10_000
Benchmark.bmbm do |x|
  x.report("isogram?") { n.times { Isogram.isogram?(input) } }
  x.report("isogram_len?") { n.times { Isogram.isogram_len?(input) } }
end
