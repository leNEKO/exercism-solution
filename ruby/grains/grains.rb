# Grains : Calculate the number of grains of wheat on a chessboard
# given that the number on each square doubles
module Grains
  MAX = 64

  def self.square(integer)
    unless integer.between?(1, MAX)
      throw ArgumentError.new("1 <= integer <= #{MAX}")
    end

    2**(integer - 1)
  end

  def self.total
    (2**MAX) - 1
  end

end
