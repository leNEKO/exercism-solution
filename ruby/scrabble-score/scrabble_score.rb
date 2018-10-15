class Scrabble
  # easy to maintain score configuration
  SCORE = {
    'AEIOULNRST' => 1,
    'DG' => 2,
    'BCMP' => 3,
    'FHVWY' => 4,
    'K' => 5,
    'JX' => 8,
    'QZ' => 10
  }.freeze

  attr_reader :word, :score_map

  # easy to maintain -> easy to use with reduce
  def init_score_map
    score_map = {}
    SCORE.each do |key, value|
      key.split('').each { |char| score_map[char] = value }
    end
    score_map.freeze
  end

  def initialize(word)
    @score_map = init_score_map
    @word = word.nil? ? '' : word.scan(/\w/).join.upcase
  end

  def score
    word.split('').reduce(0) { |sum, char| sum + score_map[char] }
  end

  # shortcut
  def self.score(word)
    new(word).score
  end
end
