# Calculate the Hamming difference between two DNA strands
class Hamming
  def self.compute(old_strand, new_strand)
    validate(old_strand, new_strand)

    old_strand
      .chars
      .zip(new_strand.chars)
      .count { |oc, nc| oc != nc }
  end

  def self.validate(old_strand, new_strand)
    return if old_strand.size == new_strand.size

    raise ArgumentError, 'Must be same size'
  end
end
