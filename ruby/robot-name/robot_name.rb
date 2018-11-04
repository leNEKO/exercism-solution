# Robot: build robot
class Robot
  attr_reader :name

  def reset
    @name = NameGenerator.next
  end
  alias initialize reset

  # no need for this with this implementation
  def self.forget; end
end

# uniq name generator
module NameGenerator
  def self.reset
    @pool = [*'AA000'..'ZZ999'].shuffle.freeze
    @cursor = -1
  end

  # init the factory
  reset

  def self.next
    @cursor = (@cursor + 1) % @pool.length
    @pool[@cursor]
  end
end
