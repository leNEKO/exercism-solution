# robot name format (AA000)
CONFIG = {
  alphas: {
    symbols: ('A'..'Z').to_a,
    size: 2
  },
  digits: {
    symbols: ('0'..'9').to_a,
    size: 3
  }
}.freeze

# max robots
MAX = CONFIG
      .map { |_k, val| val[:symbols].length**val[:size] }
      .inject(:*)

# LPRNG (Lame Pseudo Random Number Generator) :|
class LPRNG
  attr_reader :step, :current

  def initialize
    # random start position
    @current = rand(MAX)

    # random step
    primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
              41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    steps = (1..100).select { |i| primes.include?(MAX % (MAX / i)) }
    @step = MAX / steps.sample
  end

  def next
    value = @current
    @current = (@current + @step) % MAX
    value
  end
end

# custom base and symbols integer converter
class IntegerConverter
  def initialize(conf)
    @symbols, @size = conf.map { |_, v| v }
    @len = @symbols.length
  end

  # recursive decimal integer to custom base and symbols integer
  def convert(integer)
    q, r = integer.divmod(@len)
    (integer.zero? && '') ||
      convert(q) + @symbols[r]
  end

  # right padded custom integer
  def padded(integer)
    convert(integer).rjust(@size, @symbols[0])
  end
end

# convert an integer to the robot name format
class NameGenerator
  def initialize
    @alpha_convert, @digit_convert = CONFIG.map do |_, conf|
      IntegerConverter.new(conf)
    end
    @split = CONFIG[:digits][:symbols].length**CONFIG[:digits][:size]
  end

  def get(integer)
    alpha, digit = integer.divmod(@split)
    [
      @alpha_convert.padded(alpha),
      @digit_convert.padded(digit)
    ].join
  end
end

# generators
RNG = LPRNG.new
NAMEGEN = NameGenerator.new

# here is my robot
class Robot
  attr_reader :name

  def set_name
    @name = NAMEGEN.get(RNG.next)
  end
  alias reset set_name
  alias initialize set_name

  # no need for this with this implementation
  def self.forget; end
end
