# will count words
class Phrase
  def initialize(str)
    # normalizing input
    # lowercase + remove quotes from quoted words
    @str = str.downcase.gsub(/['"](\w+)['"]/, '\1')
  end

  def word_count
    dict = Hash.new(0)
    @str.scan(/[\w']+/) { |w| dict[w] += 1 }
    dict
  end
end
