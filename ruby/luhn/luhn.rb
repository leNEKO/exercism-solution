# Luhn: checksum
module Luhn
  def self.valid?(string)
    # validate characters
    return false if string.scan(/[^[:space:][:digit:]]/).any?

    digits = normalize(string)

    # validate length
    return false if digits.length < 2

    # validate cheksum
    (checksum(digits) % 10).zero?
  end

  def self.checksum(digits)
    digits.map.with_index.sum { |data| digit_value(*data) }
  end

  # compute digit value according to its index
  def self.digit_value(digit, index)
    index.odd? ? (digit * 2).divmod(10).sum : digit
  end

  # convert string to a reversed integers array
  def self.normalize(string)
    string.scan(/[[:digit:]]/).map(&:to_i).reverse
  end
end
