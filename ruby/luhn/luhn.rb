# Luhn: checksum
module Luhn
  def self.valid?(string)
    # check for invalid characters
    return false unless string.scan(/[^[:space:][:digit:]]/).empty?

    digits = string.scan(/[[:digit:]]/).reverse
    return false if digits.length < 2

    checksum = digits.map.with_index.sum do |item, index|
      value = item.to_i
      if index.odd?
        (value * 2).divmod(10).sum
      else
        value
      end
    end

    (checksum % 10).zero?
  end
end
