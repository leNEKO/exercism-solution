require_relative 'lib_lameprng'
require_relative 'lib_integerconverter'

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

# here is my robot
class Robot
  attr_reader :name

  def reset
    @name = NameGenerator.get
  end
  alias initialize reset

  def self.forget; end
end

# Generate name for robots
# TODO: make this really dynamical instead of fixed alpha, digit.
module NameGenerator
  # Pseudo random number generator
  def self.reset
    # possible robot names
    limit = CONFIG
            .map { |_k, val| val[:symbols].length**val[:size] }
            .inject(:*)


    @rng = LamePrng.new(limit)

    @alpha_convert, @digit_convert = CONFIG.map do |_, conf|
      IntegerConverter.new(conf)
    end
    @split = CONFIG[:digits][:symbols].length**CONFIG[:digits][:size]
  end

  # init
  reset

  def self.get
    integer = @rng.next
    alpha, digit = integer.divmod(@split)
    [
      @alpha_convert.padded(alpha),
      @digit_convert.padded(digit)
    ].join
  end
end


if $PROGRAM_NAME == __FILE__
  10.times do
    puts Robot.new.name
  end
end