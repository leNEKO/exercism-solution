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

# Here is my robot
class Robot
  attr_reader :name

  def initialize
    set_name
  end

  def reset
    set_name
  end

  def self.forget
    @name = nil
  end

  # build a name
  def set_name
    alpha_conf = CONFIG[:alphas]
    digit_conf = CONFIG[:digits]

    alpha, digit = RNG.next.divmod(
      digit_conf[:symbols].length**digit_conf[:size]
    )

    @name = [
      padded_base_n(alpha, alpha_conf),
      padded_base_n(digit, digit_conf)
    ].join
  end

  # decimal num into custom base integer
  def base_n(integer, symbols, symbols_length)
    (
      integer.zero? && symbols[0]
    ) ||
      base_n(integer / symbols_length, symbols, symbols_length) +
        symbols[integer % symbols_length]
  end

  # right padded custom integer
  def padded_base_n(integer, conf)
    symbols, size = conf.values_at(:symbols, :size)
    base_n(integer, symbols, symbols.length)[1, size]
      .rjust(size, symbols[0])
  end
end
