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

# LPRNG (Lame Pseudo Random Number Generator)
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

RNG = LPRNG.new

# convert an integer to the robot name format
class NameGenerator
  def self.get_name(integer)
    alpha_conf = CONFIG[:alphas]
    digit_conf = CONFIG[:digits]

    alpha, digit = integer.divmod(
      digit_conf[:symbols].length**digit_conf[:size]
    )

    [
      padded_base_n(alpha, alpha_conf),
      padded_base_n(digit, digit_conf)
    ].join
  end

  # recursive decimal integer to custom base and symbols integer
  def self.base_n(integer, symbols)
    q, r = integer.divmod(symbols.length)
    (
      integer.zero? && ''
    ) ||
      base_n(q, symbols) + symbols[r]
  end

  # right padded custom integer
  def self.padded_base_n(integer, conf)
    symbols, size = conf.values_at(:symbols, :size)
    base_n(integer, symbols).rjust(size, symbols[0])
  end
end

# here is my robot
class Robot
  attr_reader :name

  def set_name
    @name = NameGenerator.get_name(RNG.next)
  end
  alias reset set_name
  alias initialize set_name

  # no need of this with my implementation
  def self.forget; end
end
