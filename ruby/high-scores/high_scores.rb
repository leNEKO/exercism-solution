class HighScores
  attr_reader :scores

  def initialize(scores)
    @scores = scores
  end

  def latest
    scores.last
  end

  def highest
    scores.max
  end

  def top
    scores.max(3)
  end

  def report
    diff = highest - latest
    [
      "Your latest score was #{latest}.",
      if diff.zero?
        "That's your personal best!"
      else
        "That's #{diff} short of your personal best!"
      end
    ].join(' ')
  end
end
