require 'prime'

# LehmerMcg : an implementation of a multiplicative  congruential generator
# https://en.wikipedia.org/wiki/Lehmer_random_number_generator
# translated to ruby from this lazyshuffledrange2 python implementation :
# http://www.christopia.net/blog/lazy-shuffled-list-generator
module LehmerMcg
  def self.generator(start, stop=nil, step=1)
    if stop.nil?
      stop = start
      start = 0
    end

    l = (stop - start) / step
    m = next_prime(l)
    a = rand(2...m)

    until primitive_root?(a, m)
      a = rand(2...m)
    end

    seed = rand(1...l)
    x = seed

    Enumerator.new do |g|
      loop do
        if x <= l
          g.yield (step * (x - 1) + start)
        end
        x = (a * x) % m
        if x == seed
          break
        end
      end
    end
  end

  def self.primitive_root?(a, n)
    phi = n-1

    phi.prime_division.flatten.each do |p|
      break unless p > 1 # 1
      if ((a**(phi / p)) % n) == 1
        return false
      end
    end
    true
  end

  def self.next_prime(integer)
    p = integer + 1
    if p <= 2
      return 2
    end

    p += 1 if (p % 2).zero?
    until p.prime?
      p += 2
    end
    p
  end
end

if $PROGRAM_NAME == __FILE__
  s = 10**9
  lmcg = LehmerMcg.generator(s)
  puts lmcg.take(s)
end
