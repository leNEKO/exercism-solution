# custom base and symbols integer converter
class IntegerConverter
  def initialize(conf)
    @symbols, @size = conf.map { |_, v| v }
    @len = @symbols.length
  end

  # convert integer to custom symbols string
  def encode(integer)
    q, r = integer.divmod(@len)
    integer.zero? ? '' : encode(q) + @symbols[r]
  end

  # convert custom symbols string to integer
  def decode(string)
    string.reverse.chars.each_with_index.map do |char, k|
      @symbols.index(char) * @len**k
    end.sum
  end

  # right padded custom integer
  def padded(integer)
    encode(integer).rjust(@size, @symbols[0])
  end
end

if $PROGRAM_NAME == __FILE__
  ic = IntegerConverter.new(
    symbols: ('A'..'Z').to_a,
    size: 3
  )
  hw_int = ic.decode('HELLOWORLD')
  print hw_int, ' : ', ic.encode(hw_int)
end
