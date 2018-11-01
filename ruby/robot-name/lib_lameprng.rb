require 'prime'

# LPRNG (Lame Pseudo Random Number Generator) :|
class LamePrng
  attr_reader :step, :current, :limit

  def initialize(limit)
    raise ArgumentError, 'Error: limit <= 100' unless limit > 100

    @limit = limit
    # random start position
    @current = rand(limit)

    # random step
    primes = Prime.take(20)[1...-1]
    steps = (1..100).select { |i| primes.include?(limit % (limit / i)) }
    @step = limit / steps.sample
  end

  def next
    value = current
    @current = (current + step) % limit
    value
  end
end

if $PROGRAM_NAME == __FILE__
  l = 101
  rng = LamePrng.new(l)
  l.times do |_|
    puts rng.next
  end
end
