# easy to maintain -> easy to use with function
def init_score_map(score)
  score_map = {}
  score.each do |key, value|
    key.scan(/\w/).each { |char| score_map[char] = value }
  end
  score_map.freeze
end

# easy to maintain score configuration
SCORE = init_score_map(
  'AEIOULNRST' => 1,
  'DG' => 2,
  'BCMP' => 3,
  'FHVWY' => 4,
  'K' => 5,
  'JX' => 8,
  'QZ' => 10
)

class Scrabble
  attr_reader :chars

  def initialize(word)
    @chars = word.to_s.upcase.scan(/\w/)
  end

  def score
    chars.sum { |char| SCORE[char] }
  end

  def self.score(word)
    new(word).score
  end
end
