# Calculate the Hamming difference between two DNA strands
class Hamming
  def self.compute(old_strand, new_strand)
    # error handling
    raise ArgumentError, 'Must be same length' unless (
      old_strand.chars.count == new_strand.chars.count
    )
    # count diff.
    old_strand.chars.zip(new_strand.chars).reject { |oc, nc| oc == nc }.count
  end
end
