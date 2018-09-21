# Squares: with the math tricks
class Squares
  def initialize(int)
    @int = int
  end

  def square_of_sum
    # ((N * (N + 1)) / 2) ^ 2
    ((@int * (@int + 1)) / 2)**2
  end

  def sum_of_squares
    # (N * (N + 1) * (2N + 1)) / 6
    (@int * (@int + 1) * (2 * @int + 1)) / 6
  end

  def difference
    square_of_sum - sum_of_squares
  end
end
