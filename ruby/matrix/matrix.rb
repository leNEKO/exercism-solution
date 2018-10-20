class Matrix
  attr_reader :rows, :columns

  def initialize(str)
    @rows = str.split(/\n/).collect do |line|
      line.scan(/\d+/).map(&:to_i)
    end
    @columns = rows.transpose
  end
end
